#### 스칼라의 계층 구조
- 개요
  - 스칼라 클래스의 전반적인 계층 구조
  - 슈퍼 클래스 Any, 매 바닥의 Nothing, Null 등 존재


##### 11.1 스칼라의 클래스 계층구조
- 다음 계층 구조지님
  - Any: 모든 클래스의 슈퍼클래스
    - AnyVal: 모든 기본 정의 값 클래스의 슈퍼 클래스
      - Unit: 자바의 void와 유사
      - Boolean
      - Byte, Short: Byte는 Short로 변환 가능, Short는 Int로 변환 가능
      - Char: Char는 Int로 변환 가능
      - Int, Long, Float, Double: Int->Long->Float->Double로 변환 가능
    - AnyRef: AnyVal에 속하지 않는 모든 클래스의 슈퍼클래스
      - String
      - ScalaObject: String, 몇몇 자바클래스를 제외한 모든 AnyRef 하위 클래스의 슈퍼 클래스
        - Interable
          - Seq
            - List
        - ...
          - ...
            - ...
              - 모든 클래스
                - Null: AnyRef 클래스에 속한 모든 클래스으 서브 클래스
                  - Nothing: 모든 클래스의 서브 클래스
- 모든 클래스가 Any의 특성을 지님
  - ==, !=, equals 의 비교 연산자가 Any에 구현
    - == 와 != 는 finalㄹ 구현되어 있어 오버라이딩 불가능
    - 하지만 equals 를 오버라이딩 하여 == 연산자와 != 연산자의 동작을 변경시킬 수 있음
  - ##, hashCode, toString 또한 Any에 구성되어 있음
- AnyVal 클래스
  - 스칼라에서 기본으로 제공하느 모든 값의 슈퍼클래스
  - 원하면 AnyVal을 상속받아 추가 정의 가능
  - new를 사용해 인스턴스화 불가능
    - 모든 값 클래스 추상클래스이면서 final 클래스임
    - 추상클래스라 new가 불가능하면서 오버라이딩이 불가능
  - 일반적인 산술 연산자와 논리연산자를 기본을 제공
    - +, *, ||, && 등
  - 암시적 변환이 가능
    - 서로간의 상속관계는 없음
    - 암시적 변환 대상이 되는 클래스에 변환 코드가 존재
      - ex) Int 클래스의 min, max, abs, until, to 등은 사실 scala.runtime.RichInt 클래스에 들어있으며, RichInt 클래스 내부에 Int클래스의 암시적 변환 코드가 존재    
- AnyRef 클래스
  - 모든 참조 클래스 (reference class)의 슈퍼 클래스
  - java.lang.Object와 동격
    - 모든 자바 클래스는 AnyRef를 슈퍼 클래스로 삼음

##### 11.2 여러 기본 클래스를 어떻게 구현했는가?
- 스칼라는 자바와 동일한 방법으로 정수 저장
  - 32bit Word
  - 덧셈, 곱셈 등의 표준 연산은 자바 기본 연산자 사용
  - 다만 정수를 객체로 취급하기 위해서는 자바의 백업 클래스 사용
    - java.lang.Integer
    - 정수에서 toString 등의 함수를 호출할때마다 변환됨
  - 정리
    - 기본적으로는 자바의 정수와 동일하게 처리되지만 객체만의 특성이 필요한 함수 호출같은 부분이 필요한 경우에 java.lang.Integer로 변환되어 사용됨
    - 사용자가 쓰기에는 전부 객체라고 생각하고 쓸 수 있음
  - java의 자동 박싱 (auto-boxing)과 유사: 기본형 타입을 필요한 경우 자동으로 java.lang 패키지 내의 객체로 전환
- 자바랑 스칼라가 그럼 어떤면에서 다른가??
  - 자바에서 값 비교
```java
boolean isEqual(int x, int y) {
    return x == y;
}
System.out.println(isEqual(421, 421));    // true

boolean isEqual2(Integer x, Integer y) {
    return x == y;
}
System.out.println(isEqual2(421, 421));   // false
```
    - auto-boxing 전 결과와 boxing 후에 연산 결과가 다름
    - 값에 대해서는 실제 값 비교, 객체에 대해서는 주소 비교로 연산이 다르므로 발생하는 문제
  - 스칼라에서의 값 비교
```scala
def isEqual(x:Int, y:Int) = x == y
println(isEqual(421, 421))                // true

def isEqual2(x:Any, y:Any) = x == y
println(isEqual2(421, 421))               // true
```
    - 타입 표현과 무관하게 동작
    - 변환 과정에 자동으로 값을 비교하도록 동작
      - 그냥 기본 == 는 값을 비교한다고 생각해라...
    - 혹시 스칼라에서 참조 비교가 하고싶다면?
      - AnyRef 객체의 하위 메소드로 오버라이드가 불가능한 eq, ne 존재
        - eq: 참조 주소가 같은가?
        - ne: 참조 주소가 다른가?
    - 동일성에 대해서는 30장에서 자세히 다루니 여기선 패스

##### 11.3 바닥에 있는 타입
- scala.Null, scala.Nothing을 의미
- 일부 "특이한 경우"를 처리하기 위한 타입
- NULL 클래스
  - null 참조 타입
  - 참조 타입 (AnyRef)을 참조한 모든 클래스의 서브 클래스
    - 값 타입 (AnyVal) 과는 호환되지 않음
- Nothing 클래스
  - 모든 타입의 서브 타입
  - 값이 존재하지 않음
  - 비정상적인 종료 표시시 주로 사용
    - ex
```scala
def error(message:String):Nothing = throw new RuntimeException(message)
```
      - 값을 정상적으로 리턴하지 않는다는 의미
      - 정상적으로 리턴하지만 단순히 값을 사용하지 않을거란 의미의 Unit 과 차이
  - 모든 타입의 서브 타입이므로 모든 곳에서 사용할 수 있음
    - ex
```scala
def divide(x:Int, y:Int): Int = {
    if (y != 0) x / y
    else error("can`t divide by zero")
}
```
      - y == 0 일경우 error가 발생하고 Nothing 이 리턴되나 Nothing이 Int의 subtype이므로 타입 체크에 문제가 되지 않음

#### 11.4 자신만의 값 클래스 정의
- 원할경우 자신만의 값 클래스 정의 가능
  - 자동으로 박싱과 언박싱 일어남
  - 조건
    - 한개의 파라미터만 취할 것
    - def를 제외한 어떤 필드도 내부에 없을 것
      - 내부에 함수만 존재 가능
    - extends 불가능
    - equals, hashCode 재정의 불가능
- AnyVal 타입의 서브클래스로 선언하고, 파라미터 앞에 val 지정
```scala
class Dollars(val amount:Int) extends AnyVal {
    override def toString() = "$" + amount
}
```
- 한 가지 타입만 남용하는 것을 막기
  - 클래스 계층을 가장 잘 활용하기 위한 방법
  - 문제 영역에 잘 들어맞는 새로운 클래스를 정의해서 사용하라
    - 심지어 동일한 클래스를 다른 목적에 재활용 가능해도 가능한 새로 정의하라
    - 새로운 클래스 내에 메소드나 필드가 없어도 새로 정의하면 컴파일러가 최적화 하는데 도움을 줌 (= tiny type)
  - ex) HTML 코드
    - HTML은 문자열이므로 다음과 같이 정의 가능
```scala
def title(text:String, anchor:String, style:String): String = 
    s"<a id='$anchor'><h1 class='$style'>$text</h1></a>"
```
    - 문자열이 4개나 사용된 코드
      - 기술적으로는 "강하게 타입이 지정된 코드"
      - 하지만 다른 타입에 대한 문자열을 써도 컴파일러가 감지 불가능
```scala
title("chap:vcls", "bold", "Value Clases")   // <a id='bold'><h1 class='Vale Classes'>>chap:vcls</h1></a>
```
    - 작은 타입 (tiny type)을 정의하면 컴파일러가 더 많은 도움을 줄 수 있음
```scala
class Anchor(val value:String) extends AnyVal
class Style(val value:String) extends AnyVal
class Text(val value:String) extends AnyVal
class Html(val value:String) extends AnyVal

def title(text:Text, anchor:Anchor, style:Style):Html = {
    new Html(
        s"<a id='${anchor.value}'>" + 
            s"<h1 class='${style.value}'>" +
            text.value +
            "</h1>" +
        "</a>"
    )
}

title(new Text("Value Classes"), new Anchor("chap:vcls"), new Style("bold"))  // 정상 동작
title(new Anchor("chap:vcls"), new Style("bold"), new Text("Value Classes"))  // 오류 발생
```
