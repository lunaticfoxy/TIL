### Scala의 Case Class에 대한 내용

#### 개요
- 뭐하는 앤가?
  - 연관된 데이터들의 불변성을 보장하기 위해 사용되는 클래스
    - 원하면 바꿀순 있음
  - 로직보다는 데이터 구조를 처리하기 위한 용도로 주로 사용
    - C의 Struct와 유사한 용도로 사용됨
- 어떤게 좋은가?
  - 초기화가 간단하다
  - 비교시 레퍼런스 대신 구조적 동일성을 비교한다
    - 다른 객체라도 데이터가 같으면 같다고 확인
    - 기존 class도 연산자 오버라이딩을 통해 가능하지만 기본적으로 지원함
  - 패턴 매칭 형태로 사용 가능
  - 초기화가 쉬움
  
#### 사용법
- 정의 및 초기화
  - 일반 class와 동일한 문법으로 정의
  - new 없이 할당
  - 생성자에 포함된 인자도 public (일반 class 는 private)
```scala
abstract class Notification
case class Email(sourceEmail : String, title : String, body : String) extends Notification
case class SMS(sourceNumber : String, message : String) extends Notification
case class VoiceRecording(contactName : String, link : String) extends Notification

val emailFromTodd = Email("todd@daum.net", "Greeting", "Hello world")

val title = emailFromTodd.title;
println(title)
```

- 데이터 불변성 보장
  - 생성자의 파라미터도 public이므로 직접 접근 가능
  - 외부에서는 데이터 변경 불가능
    - var여도 그런지는 확인해보자
  - copy를 통해 새로운 객체를 생성하면서 값 변경 가능
```scala
val editedEmail = emailFromTodd.copy(title = "Greeting!", body = "Hello world")
println(editedEmail.title)
```

- 구조적 동일성 체크
  - eques 메소드가 기본적으로 structural 동일성을 체크하도록 구현되어 있음
  - 자동으로 toString 메소드를 생성해줌
```scala
val firstSms = SMS("12345", "Hello")
val secondSms = SMS("12345", "Hello")

if (firstSms == secondSms)
println("They are equal.")
```

- 패턴 매칭
  - case class 자체가 패턴 매칭의 인자로 사용 가능
  - 설명이 조금 어려우니 예시로 대치하자
```scala
def showNotification(notification: Notification) : String = {
  notification match {
    case Email(email, title, _) =>
      "You got an email from " + email + " with title " + title
    case SMS(number, message) =>
      "You got an SMS from " + number + "! Message: " + message
    case VoiceRecording(name, link) =>
      "You received a Voice Recording from " + name + "! Click the link to hear it: " + link
  }
}
```
