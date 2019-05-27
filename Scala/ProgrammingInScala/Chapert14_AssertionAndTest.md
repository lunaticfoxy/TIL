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
                            // 만족함ㄴㄷ
  } ensuring (w <= _.width) // 리턴값 _ 의 원소 width가 w <= _.width 를 만족하ㅎ
  } ensuring (w <= _.width) // 리턴값 _ 의 원소 width가 w <= _.width 를 만족하는가?
}
```

- JVM에서 명령형 옵션을 켜서
