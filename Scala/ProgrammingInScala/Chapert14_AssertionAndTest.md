#### 개요
- 스칼라에서 단언문(asssertion)과 테스트를 작성하기 위한 방법 명세


#### 14.1 단언문 (assertion)
- 스칼라에서 assert 를 발생시키기 위한 방법
- 조건을 충족하지 않는 경우 AssertionError 발생
- assert 함수를 통해 정의
  - 기본 형태: assert(조건)
  - 인자를 2개 받을수도 있음
    - assert(조건, 설명객체) 형태로 전달
    - AssertionError에서 설명객체.toString 의 내용을 포함하여 리턴
  - Predef 싱글톤 객체 내에 포함되어 있어 모든 스칼라 파일에서 자동 임포트

- 단언문 예시
```scala
// 10.14에 있는 Element클래스
// 한줄에 한 String을 가지고 있고, 이 String의 각각 원소는 행렬의 column을 의미
// 한 String은 행렬의 row을 의미하며 String의 배열인 contents를 가지고 있는 객체
// ex) abc
//     def
// 형태는 contents = ["abc", "def"] 로 표현

abstract class Element {
  def contents: Array[String]
  
  def width: Int = contents(0).length
  def height: Int contents.length
  
  ...
  def above(that: Element): Element = { // 새로 row를 추가하는 함수 - 길이가 맞지 않으면 짧은쪽의 양쪽에 패딩을 줘서 맞춤 
    val this1 = this widen that.width // 위쪽 값의 길이를 조절
    var that1 = that widen this.width // 새로 추가할 값의 길이를 조절
    assert(this1.width == that1.width) // 두 값의 길이가 다르면 에러
    elem(this1.contents ++ that1.contents) // 합쳐진 객체 리턴
  }
  
  private def widen(w: Int): Element = { // 새로 row를 추가할때 좌우 길이를 맞춰주는 함수
    if (w <= width) // 늘려줄 길이보다 크면 그냥 리턴
      this
    else {
      val left = elem(' ', (w - width) / 2, height) // 왼쪽 패딩 계산
      val right = elem(' ', w - width - left.width, height) // 오른쪽 패딩 계산
      left beside this beside right // (왼쪽패딩)(값)(오른쪽패딩) 형태로 이어붙임
    }
  }
  ...
```

- ensuring을 사용해서 좀 더 간결하게 구성 가능
  - 리턴값의 조건을 확인하는 방법
  - 조건이 false면 AssertionError 발생
  - ensuring은 전달받은 값을 그대로 리턴
```scala
private def widen(w: Int): Element = {
  if (w <= width)
    this
  else {
    val left = elem(' ', (w - width) / 2, height)
    val right = elem(' ', w - width - left.width, height)
    left beside this beside right
  } ensuring (w <= _.width) // 리턴값 _ 의 원소 width가 w <= _.width 를 만족하는가?
                            // 만족한다면 _ 리턴, 아니면 에러 발생
}
```

- JVM에서 명령형 옵션 통해 assertion과 ensuring On-Off 가능


#### 14.2 스칼라에서 테스트하기
- 스칼라테스트 (ScalaTest)
  - 가장 유연한(?) 스칼라 테스트 프레임워크
  - 쉽게 커스터마이즈 가능 (= 어떠한 테스트 스타일로도 사용가능)

- 스칼라테스트를 통한 테스트
  - 스위트 (Suite): 테스트 집합
    - Suite는 트레이트이며 테스트를 실행하기 위한 생명주기 (life cycle) 메소드들을 선언
    - 테스트 방식에 따라 이 메소드들이 오버라이드 됨
  - Suite의 확장 및 오버라이드를 위해 스타일 트레이트 (style trait) 지원
  - 특별한 테스트 요구를 해결하기 위해(?) 생명 주기 메소드를 오버라이드 하는 믹스인 트레이트 (mixin trait) 지원
    - 이후 별도 설명은 없는데 여러 트레이트를 연속해서 정의할 수 있게 하는게 믹스인 이니 테스트의 조합이 가능하다는 것으로 이해

- 예시) FunSuite
  - Fun: function의 약자
  - 내부에 test 함수 사전 정의
    - 첫번째 괄호 인자: 테스트 이름
    - 두번째 괄호 인자: by name-parameter 형태의 테스트 로직
  - 실행시 execute 함수 실행
```
import org.scalatest.FunSuite
import Element.elem   // 위에서 언급된 객체

class ElementSuite extends FunSuite {
  test("elem result should have passed width") {
    val ele = elem('x', 2, 3) // x를 가로 2개짜리 3줄로 채우겠다는 이야기
    assert(ele.width == 2)
  }
}

(new ElementSuite).execute()
```

#### 14.3 충분한 정보를 제공하는 실패 보고
- 14.2의 테스트에서 단언문 실패시 파일 이름, 실패한 단언문의 줄 번호, 추가 정보가 담긴 오류메시지가 오류 보고에 포함되어야 함
- DiagrammedAssertions를 통해 assert에서 발생한 오류메시지의 다이어그램 확인 가능
  - 책에 이렇게만 나와있는데 import DiagrammedAssertions._ 를 통해 사용 가능함
- assertResult: 단순 값이 가대하는 값인지 확인하고 싶을때 사용할 수 있는 테스트  
  - 첫번째 함수 인자: 기대하는 값 {1}
  - 두번째 함수 인자: 확인할 값 {2}
  - 실패시 "Expected {1}, but got {2}" 라는 에러 메시지 출력
- 발생할 
  - 실패시 "Expected {1}, but got {2}" 라는 에러 메시지 출력

```scala
import DiagrammedAssertions._

assert(List(1, 2, 3).contains(4))

org.scalatest.exceptions.TestFailedException:
assert(List(1, 2, 3).contains(4))
        |   |  |  |     |     |
        |   1  2  3   false   4
       List(1, 2, 3)


assertResult(2) {  // ele.width == 2 인지 확인하고자 한다
  ele.width
}                  // ele.width = 3 이라면 "Expected 2, but got 3" 에러 메시지 발생
```


