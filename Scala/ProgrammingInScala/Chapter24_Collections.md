### 24장 컬렉션 자세히 들여다보기


#### 스칼라 컬렉션의 기본 특징
- 사용하기 쉬움
  - 20 ~ 50개의 메소드로 거의 모든 컬렉션 문제 해결 가능
- 간결함
  - 하나 이상의 루프를 한 단어로 대체 가능
    - 함수적 연산에 용이
    - 조합 쉬움
  - 대수식과 유사한 형태로 표현
- 안전함
  - 정적 타입 검사를 하므로 컴파일 타임에 대부분의 실수 확인 가능
  - 컬렉션 단위 연산이 정적 타입 체크를 하므로 가능한 방식
- 빠름
  - 튜닝과 최적화가 잘 되어 있음
  - 병렬화에 용이
- 보편적: 같은 컬렉션은 같은 연산을 제공


#### 24.1 변경 가능, 변경 불가능 컬렉션
- 변경 가능 컬렉션
  - 메모리상에서 변경하거나 확장 가능
  - 원소의 추가, 변경, 삭제 가능
  - scala.collection.mutable 패키지 내 존재
- 변경 불가능 컬렉션
  - 변경 불가능
  - 원소의 변경도 불가능
  - 함수가 존재는 하나 실제로는 새로운 컬렉션이 생성되는 것
  - scala.collection.immutable 패키지 내 존재
  - 기본적으로 사용되는 모든 컬렉션은 변경 불가능이라고 생각하면 됨
- scala.collecion 패키지에 존재하는 컬렉션들은 구현에 따라 변경 가능, 변경 불가능 상태로 사용 가능

#### 24.2 컬렉션 일관성
- 컬렉션 계층도 (최하위는 생략)
  - Traversable
    - Iterable
      - Seq
        - IndexedSeq
        - LinearSeq
        - Buffer
      - Set
        - SortedSet
        - HashSet
        - LinkedHashSet
        - BitSet
        - EmptySet
      - Map
        - SortedMap
        - HashMap
        - LinkedHashMap
        - EmptyMap

- 모든 컬렉션은 동일한 문법으로 생성할 수 있음
- 컬렉션 변환을 제외한 모든 API의 리턴은 구체적인 개별 클래스를 반환함
  - List에서 map 호출시 List 리턴
  - Set에서 map 호출시 Set 리턴
- 대부분의 컬렉션은 루트 (구현에 따른 변화 가능), 변경 불가능, 변경 가능 버전이 존재
  - 단 Buffer 만 변경 가능한 컬렉션만 존재

#### 24.3 Traversable 트레이트
- 추상 멤버 함수 foreach가 존재하는 트레이트
  - 모든 컬렉션의 기반
  - def foreach[U](f:Elem => U) 형태로 구헝
  - 해당 클래스를 상속받으면 새로운 컬렉션 생성 가능
- 컬렉션 단위 이외의 연산
  - 크기 연산: 컬렉션의 크기 리턴
  - 원소를 가져오는 연산
    - 순서가 있는 컬렉션과 순서가 없는 클렉션으로 나뉨
    - 순서가 있으면 항상 같은 순서로 원소 리턴 (ex LinkedHashSet)
    - 순서가 없으면 원소 리턴 순서가 보장되지 않음 (ex HashSet)

#### 24.4 Iterable 트레이트
- iterator를 가지고 있는 트레이트
  - 기존 정의된 모든 컬렉션은 Iterable 트레이트를 상속받았다고 생각하면 된다
- Traversable에서 상속받은 foreach에 iterator를 넣어 구현
  - 가장 기본적인 구현은 다음 형태로 되어있음
```scala
def foreach[U](f: Elem => U): Unit = {
  val it = iterator
  while (it.hasNext) f(it.next())
}
```
  - 사실 대부분의 서브클래스는 이걸 다시 오버라이딩 해서 효율적으로 만들어 사용
- grouped와 sliding을 사용해서 iterator를 직접 가져올수도 있음
  - grouped
    - 0번 인덱스부터 n개의 원소를 가진 iterator를 가져옴
    - next 호출시 n번째, 2*n번째 인덱스가 시작인 iterator로 넘어감
  - sliding
    - 0번 인덱스부터 n개의 원소를 가진 iterator를 가져옴
    - next 호출시 1번째, 2번째 인덱스가 시작인 iterator로 넘어감
 ```scala
val xs = List(1, 2, 3, 4, 5)

val git = xs grouped 3
val res1 = git.next()  // res1 = List(1, 2, 3)
val res2 = git.next()  // res2 = List(4, 5)

val sit = xs sliding 3
val res3 = sit.next()  // res3 = List(1, 2, 3)
val res4 = sit.next()  // res4 = List(2, 3, 4)
val res5 = sit.next()  // res5 = List(3, 4, 5)
```

##### Trabersable 과 Iterable이 각각 존재하는 이유
- iterator는 반드시 next()를 호출해서 다음 원소를 리턴해야 함
  - 다음 원소를 리턴하지 않고 연산만 해도 될때는 속도에 불리
- Trabersable의 foreach를 효율적으로 구현해서 속도를 올리는 경우가 다수 존재
  - 예시: 리프 노드에만 값을 저장하는 이진 트리를 탐색하는 경우
```scala
sealed abstract class Tree
case class Branch(left: Tree, right: Tree) extends Tree
case class Node(elem: Int) extends Tree


/*
foreach로 구현시 일반적으로 생각하는 재귀 형태로 구현됨
*/
sealed abstract class Tree extends Traversable[Int] {
  def foreach[U](f: Int => U) = this match {
    case Node(elem) => f(elem)
    case Branch(l, r) => l.foreach(f); r.foreach(f)
  }
}

/*
iterator로 구현시 Branch마다 자식 iterator 2개씩을 이어붙인 다음 리턴해줘야 하는 문제 발생
- 자식이 2개씩이라 이어 붙이는데 추가 연산이 든다고 생각하면 됨
*/
sealed abstract class Tree extends Iterable[Int] {
  def iterator: Iterator[Int] = this match {
    case Node(elem) => Iterator.single(elem)
    case Branch(l, r) => l.iterator ++ r.iterator
  }
}
```

- Iterable의 하위 분류
  - Seq, Set, Map 존재
  - 공통점: apply와 isDefinedAt 메소드 제공
  - 차이점
    - Seq의 apply는 위치 인덱스로 사용됨 => Seq(1,2,3)(1) == 2 
    - Set의 apply는 원소가 있는지 검사 => Set(1,2,3)(1) == true, Set()(1) == false
    - Map의 apply는 키로 값 선택 => Map('a'->1, 'b'->10)('b') == 10

#### 24.5 시퀀스 트레이트: Seq, IndexedSeq, LinearSeq
- 길이가 정해져있고, 각 원소의 위치가 0부터 시작하는 인덱스를 지닌 iterable 객체
- Seq[T]의 apply는 Int 타입 인덱스를 입력받아 해당 위치의 T 타입 원소 리턴
- 하위 트레이트
  - LinearSeq
    - head, tail 연산이 효율적
    - List나 Stream에 사용
  - IndexedSeq
    - apply, length, update 연산이 효율적
    - Array나 ArrayBuf에 사용
  - Vector는 양쪽 다 구현되어있다고 보면 된다
- Buffer
  - 기존 원소의 변경 허용, 원소 삽입 및 제거 지원, 맨 뒤에 원소 추가 가능한 특이한 형태
  - List를 기반으로 구현되어 있는 ListBuffer, Array를 기반으로 구현되어 있는 ArrayBuffer 존재
  - 최종 결과가 List로 나타날지, Array로 나타날지에 짜라 골라서 쓰면됨
    - 뭘 쓰던 구현은 되는데 성능에 차이


#### 24.6 집합
- 원소 중복을 허용하지 않는 Iterable
- contains라는 함수 존재
  - 원소의 존재 여부 확인
  - apply 함수 내에서 contains 호출
```scala
val fruit = Set("apple", "orange", "peach", "banana")

fruit("peach") // true
fruit("potato") // false
```
- 집합 연산이 사용 가능하며 연산자로도 호출 가능
  - intersect => &
  - union => |
    - ++ 연산과 사실상 결과는 같음
    - 단, ++ 연산은 Traversable을 상속받은 모든 컬렉션, | 연산은 Set 끼리 사용 가능
  - diff => &~
- 원소 변경 연산
  - +, ++, -, --
    - 각각 원소의 추가, 삭제를 의미
    - 연산자 1개일경우 집합과 원소의 연산
    - 연산자 2개 중첩시 집합 단위 연산
    - 단, 매번 새로운 집합이 생기는 형태
  - +=, -=
    - 변경 가능한 Set에서 효율적인 연산을 수행하기 위해 사용
    - 기존 Set에 원소를 넣고 빼는 연산
    - 새로운 집합 생기지 않음
      - 변경 불가능한 Set에서도 해당 연산자를 지원은 하나, + - 와 동일하게 동작
- 변경 가능 Set과 변경 불가능한 Set은 선언시 val로 저장하는지, var로 저장하는지와 관계없이 타입에 따라 동작
```scala
var s = Set(1, 2, 3)
s += 4; s -= 2 // scala.collection.immutable.Set[Int] = Set(1, 3, 4)

val s = collection.mutable.Set(1, 2, 3) // scala.collection.mutable.Set[Int] = Set(1, 2, 3)

s += 4 // Set(1, 4, 2, 3)
s -= 2 // Set(1, 4, 3)
```

#### 24.7 맵
- 키와 값이 쌍으로 이루어진 Iterable
- Map("x" -> 24) 는 Map(("x", 24)) 와 같음
- Map[T]의 get 연산은 키에 대한 값이 있을 경우 Some(값) 을 리턴, 없을경우 None 리턴
- Map[T]의 apply 연산은 get과 동일하지만 Some으로 감싸지 않고 값을 리턴
- Map도 += -= 같은 연산 지원
- 맵을 캐시로 사용하는 경우를 위해 getOrElseUpdate 함수가 내장되어 있음
```scala
def f(x: String) = {
  println("taking my time.")
  Thread.sleep(100)
  x.reverse
}

/*
f에 부수 효과가 없다면, 같은 인자로 다시 f를 호출하면 항상 같은 결과가 나온다.
f를 사용해 계산한 인자와 결과 값을 맵에 담아두고 f의 인자를 맵의 키에서 찾을 수 없을 경우에만 f를 호출
getOrElseUpdate 사용시 맵이 함수 f의 계산에 대해서 자동으로 캐시를 수행하여 값만 리턴
*/
 
val cache = collection.mutable.Map[String, String]()
def cachedF(s: String) = cache.getOrElseUpdate(s, f(s))    // 두 번째 인자는 이름에 의한 호출

val res1 = cachedF("abc")
taking my time. // 해당 문구 출력후 0.1초 대기 이후 res1에 "cba" 저장

val res2 = cachedF("abc") // 호출 즉시 res2에 "cba" 저장
```

#### 24.8 변경 불가능한 구체적인 컬렉션 클래스
- 리스트
- 스트림
  - 리스트와 유사하나 원소를 지연 계산
  - 들어오는 그대로 가지고 있다가 외부에서 요청시에만 연산 수행
- 벡터
- 변경 불가능한 stack (scala.collection.immutable.Stack)
  - push pop 모두 새로운 컬렉션을 생성
  - 사실상 사용할 이유가 없음
- 변경 불가능한 queue (scala.collection.immutable.Queue): stack과 동일
- 범위 (Range)
  - 간격이 일정한 정수를 순서대로 나열한 시퀀스
  - 1 to 3 => Range(1,2,3)
  - 5 to 14 by 3 => Range(5,8,11,14)
  - 1 until 3 => Range(1,2)
- 해시 트라이: 해싱을 위한 트라이 형태로 집합이나 맵등에서 인덱스를 효율적으로 탐색하기 위해 사용
- Red-Black Tree: TreeSet, TreeMap, SortedSet등에서 사용됨
- 변경 불가능한 비트 집합 (BitSet)
- ListMap
  - 맵의 원소가 리스트 형태로 이어져있음
  - 탐색시 리스트 탐색과 동일하게 탐색하며 키 체크
  - 맵의 첫번째 원소를 다른 원소보다 압도적으로 많이 이용시 유리

#### 24.9 변경 가능한 구체적인 컬렉션 클래스
- ArrayBuffer
- ListBuffer
- StringBuilder
- LinkedList
