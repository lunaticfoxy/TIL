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

#### 동작원리
- case class를 하나의 트리로 관리됨
  - toString, hashCode, equals 같은 경우 객체의 함수가 아닌 트리 구조 내에 포함된 값을 기반으로 연산
    - 따라서 case class끼리 값 equals 비교가능
  - copy 메소드도 동작
  
  
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
  - 사용법
    - match { case (조건) => 내부 } 형태
    - 조건에 _ 를 넣으면 default
      - 각 case에서 Match 에러가 발생시 다음으로 넘어가는 형태이니 default 케이스가 없으면 다른 조건에 매치되지 않을떼 에러 발생
    - _ 는 와일드카드 패턴으로 값이 사용되지 않으니 무시해도 좋다 (쓰레기값이 들어가도 좋다)를 표시하기 위해서도 사용
  - 가능한 패턴
    - _ : default 패턴, 어떤 값에도 매칭됨
    - 값: 값과 동일할 경우 매칭됨
    - 시퀀스: 시퀀스의 일부만 매칭 가능
    - 생성자: 생성자 처리 과정에서 에러가 발생하지 않으면 매칭
    - 튜플: 원소가 모두 일치되면 매칭
    - 타입 지정 패턴: 위 패턴들을 타입을 지정해서 매칭 가능
      - 스칼라에서의 타입 검사가 복잡하니 이렇게 돌려서 쉽게 활용 가능
    - 변수 바인딩 패턴: 패턴 매칭 후 다시 패턴을 매칭한다?? => 이거 나중에 자세히 볼것
  - 패턴가드
    - 패턴 직후에 if로 시작하는 부분
      - 패턴에 가드가 있으면 가드가 true일 경우에만 매치에 성공
    - 패턴이 맞아야할뿐만 아니라 조건까지 일치해야 할 경우에 사용
    - 패턴에 조건문을 추가하는 거라 생각하면 됨
    
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

- 봉인된 클래스
  - 비슷한 패턴 매칭이 일어날 경우 다른 파일에서 비슷한 이름을 가지는 케이스 클래스가 생길 수 있음
  - 꼬일 경우를 없애려고 sealed class를 지정
    - sealed class는 해당 파일 내에서만 사용됨
    - 다른 파일에선 동일한 이름으로 다른 클래스를 만들어도 OK
 
