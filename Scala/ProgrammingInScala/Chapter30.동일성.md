

#### 30.1 스칼라에서의 동일성
- Java
  - ==
    - 값에 대해서는 값 일치 여부
    - 객체에 대해서는 주소 일치 여부
  - equals
    - 객체에 대해서 주소 일치 여부
- Scala
  - ==
    - 값에 대해서는 값 일치 여부
    - 객체에 대해서는 객체의 equals 함수 호출
  - equals
    - 자동으로는 주소 일치 여부 (=eq 함수)
    - 오버라이드 해서 값 일치 여부로 체크 가능
    

#### 30.2 동일성 비교 메소드 참조
- equals 재정의시
  - Any에 포함된 equals를 재정의 해야한다
  - 해당 객체에 equals를 부르는게 아니라
  - 잘못된 예시
```scala
class Point(val x: Int, val y: Int) { 
  //잘못된 equals정의
  def equals(other: Point): Boolean =
    this.x == other.x && this.y == other.y
}

val p1, p2 = new Point(1, 2)
val q = new Point(2, 3)
p1 equals p2 // true
p1 equals q // false
 
 
//맞는것 같지만, 컬렉션에 넣으면 문제가 생긴다
import scala.collection.mutable
val coll = mutable.HashSet(p1)
coll contains p2 // false!

val p2a: Any = p2  // Point 타입말고 Any타입으로 만들어보자
p1 equals p2a // false
```
  - Point에 equals를 추가한거라 collection의 contains 메소드 호출시 동일한 객체로 인식되지 않음
  
  - 제대로 된 방법
```scala
override def equals(other: Any) = other match {
  case that: Point => this.x = that.x && this.y == that.y
  case _ => false
}
```
    - Any로 받아서 재정의한다

- hashCode 재정의 필요
  - HashSet에 넣을때 hashCode를 통해 해싱하는데 이걸 재정의 안하면 원하는대로 동작하지 않을 수 있음
```scala
class Point(val x: Int, val y:Int) {
   override def hashCode = (x, y).## 
   override def equals(other: Any) = other match {
      case that: Point => this.x == that.x && this.y == that.y  
      case _ => false
     }
} //## 메소드는 기본 타입의 값, 참조 타입의 값, 그리고 null 값에 작용하는 해시 코드를 계산하는 것을 짧게 쓴 것.
```
  - 이때 해싱되는 값은 var이 면 안됨 (변경 가능하면 안됨)
```scala
class Point(var x: Int, var y:Int) {
   override def hashCode = (x, y).##
   override def equals(other: Any) = other match {
      case that: Point => this.x == that.x && this.y == that.y
      case _ => false
   }
}
 
 
val p = new Point(1,2)
val coll = collection.mutable.HashSet(p)
coll pcontains p // true
 
p.x += 1
coll contains p // false (1)
coll.iterator contains p // true (2)
```

- 대칭성 고려
  - a equals b 의 결과와 b equals a 의 결과가 같아야한다
  - 서브 클래스에서 생길 수 있는 문제
```scala
object Color extends Enumeration {
  val Red, Orange, Yellow, Green, Blue, Indigo, Violet = Value
}
 
class ColoredPoint(x: Int, y: Int, val color: Color.Value)
    extends Point(x, y) {
    override def equals(other: Any) = other match{
       case that: ColoredPoint =>
        this.color == that.color && super.equals(that)
    case _ => false
   }
} //대칭성 깨짐
 
val p = new Point(1,2)
val cp = new ColoredPoint(1, 2, Color.Red)
 
p equals cp // true
cp equals p // false -> ColoredPoint에 있는 메소드를 사용하기 때문
 
//대칭성이 깨지면 다음과 같은 일이 일어날 수 있다.
collection.mutable.HashSet[Point](p) contains cp // true
collection.mutable.HashSet[Point](cp) contains p // false
```
- 해결방법
  - 완벽한 해결책은 없고 상황에 따라서 일부를 포기해야함
  - 느슨한 equals로 해결
    - 양쪽 모두 true
```scala
class ColoredPoint(x: Int, y: Int, val color: Color.Value)
     extends Point(x, y) {
   override def equals(other: Any) = other match {
     case that: ColoredPoint =>
       (this.color == that.color) && super.equals(that)
     case that: Point =>
       that equals this
     case _ => false
   }
} //추이성 깨짐
 
 
val redp = new ColoredPoint(1, 2, Color.Red)
val bluep = new ColoredPoint(1, 2, Color.Blue)
redp == p // true
p == bluep // true
redp == bluep // false. transitive 깨짐
```
  - 엄격한 equals로 해결
    - 클래스까지 동일한지
    - 양쪽 모두 false
```scala

//어쩔수 없다.. 클래스가 다른 객체는 아예 다른 것으로 간주..
 
class Point(val x: Int, val y: Int) {
   override def hashCode = (x,y).##
   override def equals(Other: Any) = other match {
     case that: Point =>
       this.x == that.x && this.y == that.y &&
       this.getClass == that.getClass
    case _ => false
  }
}
 
 
class ColoredPoint(x: Int, y: Int, val color: Color.Value)
    extends Point(x, y) {
    override def equals(other: Any) = other match{
       case that: ColoredPoint =>
        this.color == that.color && super.equals(that)
    case _ => false
   }
} //대칭성 깨졌던 그 버전
 
 
// 이러면 아래도 안된다
val pAnon = new Point(1, 1) { override val y = 2}
pAnon == p //false
// java.lang.Class 객체가 다르다. p는 Point지만 pAnon은 Point를 상속한 이름 없는 클래스.
```

  - 엄격한 equals에서 pAnon은 동일하게 체크하고 싶을 경우
    - canEqual 사용

```scala
class Point(val x: Int, val y: Int) {
   override def hashCode = (x,y).##
   override def equals(Other: Any) = other match {
     case that: Point =>
      (that canEqual this) &&
      (this.x == that.x) && (this.y == that.y)
     case _ => false }
    
   def canEqual(other: Any) = other.isInstanceOf[Point]
}
canEqual을 호출하는 서브클래스 equals 메소드
class ColoredPoint(x: Int, y: Int, val color: Color.Value)
     extends Point(x, y) { //대칭성 깨짐
   override def hashCode = (super.hashCode, color).##
   override def equals(other: Any) = other match{
     case that: ColoredPoint =>
       (that canEqual this) &&
       super.equals(that) && this.color == that.color
     case _ => false
  }
 override def canEqual(other: Any) =
       other.isInstanceOf[ColoredPoint]
}
 
 
val p = new Point(1,2)
val cp = new ColoredPoint(1,2, Color.Indigo)
val pAnon = new Point(1, 1) { override val y = 2}
val coll = List(p)
coll contains p //true  
coll contains cp//false.. 원했던 바이다. ColoredPoint 는 canEqual을 오버라이드 함.
coll contains pAnon//true  pAnon이 참조하는 이름 없는 서브클래스는 canEqual을 오버라이드하지 않기 때문에 Point의 인스턴스와 같을

```

#### 30.3 파라미터화 한 타입의 동일성
```scala
//이진 트리
trait Tree[+T] {
   def elem: T
   def left: Tree[T]
   def right: Tree[T]
}
 
 
object EmptyTree extends Tree[Nothing] {
   def elem =
      throw new NoSuchElementException("EmptyTree.elem")
   def left=
      throw new NoSuchElementException("EmptyTree.left")
   def right=
      throw new NoSuchElementException("EmptyTree.right")
}
 
class Branch[+T] (
   val elem: T,
   val left: Tree[T],
   val right: Tree[T]
) extends Tree[T]
```

- Branch에 equals 추가 하려면?
  - Tree는 trait고 EmptyTree는 오브젝트이므로 패스
```scala
class Branch[+T] (
   val elem: T,
   val left: Tree[T]
   val right: Tree[T]
) extends Tree[T] {
   override def equals(other: Any) = other match {
      case that: Brach[T] => this.elem == that.elem &&
                             this.left == that.left&&
                             this.right== that.right&&
      case _ => false
   }
}
 
//하지만 컴파일하려 하면 경고가 나옴...
// 검사할 수 있는 것은 other 가 참조하는 게 Branch(의 일종)인가 하는 것 뿐. 트리의 원소타입이 T인지는 검사할수 X
 
val b1 = new Branch[List[String]](Nil, EmptyTree, EmptyTree)
val b2 = new Branch[List[Int]](Nil, EmptyTree, EmptyTree)
b1 == b2 // true. Branch의 원소타입을 검사하지 않기 때문.
 
// unchecked경고 싫으면 T -> t 로 바꿉시다. 15장에서 배웠듯 패턴에서 소문자로 시작하는 타입 파라미터는 알려지지 않은 타입을 표현.
 
case that: Branch[t] => ... // t 말고 _ 써도 같다.
 
// 아래는 올바른 구현
// - 아예 타입 체크를 피하는 방법
// - 와일드 카드 타입을 넣어 모든 타입에 대해 통과 가능하도록 한다
class Branch[+T] (
   val elem: T,
   val left: Tree[T]
   val right: Tree[T]
) extends Tree[T] {
   override def equals(other: Any) = other match {
      case that: Brach[_] => this.elem == that.elem &&
                             this.left == that.left&&
                             this.right== that.right&&
      case _ => false
   }
  def canEqual(other: Any) = other.isInstanceOf[Branch[_]]
  // _ 는 뭘까? Branch[_]는 타입패턴이 아님. 와일드카드 타입 -> 자세한건 다음장에..
  override def hashCode: Int = (elem, left, right).##
}
```

#### 3.4 equals와 hashCode 요리법
- equals
  - 1.equals를 final이 아닌 클래스에서 override한다면, canEqual 메소드를 만들어야 한다.
  - 2.canEqual 메소드는 인자 객체가 현재 클래스라면 true, 아니면 false를 반환해야 한다.
  - 3.equals 메소드 정의에서 전달받는 파라미터의 타입은 반드시 Any여야 한다.
  - 4.equals 메소드의 본문을 match 표현식을 하나 사용해 작성하라.
  - 5.match식은 두 가지 경우를 처리해야 한다. 첫 번째 대안 부분에서는 equals 메소드 정의가 있는 클래스 타입과 같은 타입 패턴을 설정해야 한다.
  - 6
    - 6-1.case의 본문에 객체들이 같기 위해 만족해야 하는 조건을 논리적 곱(&&) 을 사용하여 작성하라.
    - 6-2.오버라이드 하는 equals가 AnyRef에서 온 것이 아니면 super.equals(that) 를 넣어라.
    - 6-3.equals를 재정의한 것을 다시 오버라이드하는 경우, super.equals 호출하지 않으면 꼭 canEqual호출을 해야만 한다.
  - 7.match문의 두번째 case에는 와일드 카드 패턴을 사용해 false를 반환하라.
- hashCode
  - 1.equals 메소드에서 동일성 계산에 사용했던 모든 필드를 포함한 튜플을 만들어라. 그리고 그 튜플에 대해 ##를 호출
    - 예: override def hashCode: Int = (a, b, c, d, e).##
  - 2.equals 메소드가 super.equals(that) 호출한다면, hashCode도 super.hashCode 호출
    - 예: override def hashCode: Int = (super.hashCode, number, denom).##
  - 3.필드 중 하나가 컬렉션이면, 그 필드의 해시 코드를 컬렉션에 들어있는 모든 원소를 기반으로 계산할 수도 있다. Vector, List, Set, Map, 튜플이라면 그냥 hashCode 호출로 충분. Array는 각 원소를 일반 객체의 개별 필드와 마찬가지로 다뤄야 함.
  - 4.hashCode 계산이 프로그램 성능에 악영향을 미친다면 hashCode 캐시를 고려하라. 예: override val hashCode: Int = (numer, denom).##
