####개요
- 스칼라에는 내장된 제어 추상화가 많지 않음
- 다만 자신만의 고유한 제어 추상화 작성 가능

####학습 내용
- 함수값을 활용한 흐름 제어 추상화
- 커링 (currying)
- 이름에 의한 호출 파라미터 (by-name parameter)


####1. 코드 중복 줄이기
- 함수에는 호출에 따라 달라지는 비 공통 부분, 모든 호출에서 사용되는 공통 부분이 존재
- 비 공통 부분을 별도의 함수값으로 전달하여 코드 중복 제거 가능
  - 단순히 함수를 파라미터로 넘겨서 호출한다는 이야기
- 함수를 인자로 받는 함수를 "고차 함수(higher-order function)" 라 부름
- 주의사항
  - scala는 메소드의 이름을 함수 내로 전달하는 것을 허용하지 않음 (????)
  - 하지만 메소드가 할당된 함수값은 전달할 수 있음 (????)
  - 개념적인 내용이고, 실제 코드상에서는 함수의 입출력 타입만 지정해주면 동작하는 것으로 보임...
  - 코드가 컴파일되어 객체로 변환될 수 있어야 전달 가능하다는 의미로 해석함
    - 부가 설명에 "동적 언어"에서는 메소드 이름을 전달할수 있다는 이야기가 있으니 맞을듯함 
  - 샘플코드 - 조건에 맞는 파일명 탐색

```scala
object FileMatcherBefore {                                         // 중복 제거 전 객체
    private def filesHere = (new Java.io.File(".")).listFiles      // 파일 리스트 가져옴
 
 
    def filesEnding(query: String) = {                             // 파일명이 query로 끝나는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getame.endsWith(query))
            yield file
    }
 
 
    def filesContaining(query: String) = {                         // 파일명에 query가 들어가는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getame.contains(query))
            yield file
    }
 
    def filesRegex(query: String) = {                              // 파일명에 regular expression query와 매칭되는 파일들만 리턴 (여기서는 지연 리턴)
        for (file <- filesHere; if file.getame.matches(query))
            yield file
    }
}
 
 
object FileMatcherAfter {                                          // 중복 제거 후 객체
    private def filesHere = (new Java.io.File(".")).listFiles      // 파일 리스트 가져옴
 
    def filesMatching(matcher: String => Boolean) = {                         // 파일명이 matcher에 합당하는 파일들만 리턴
        for (file <- filesHere; if matcher(file.getName))
            yield file
    }
 
 
    def filesEnding(query: String) = filesMatching(_.endsWith(query))           // 파일의 끝이 query인지 체크하는 클로저 리턴 (클로저의 입력은 파일 이름)
    def filesContaining(query: String) = filesMatching(_.contains(query))       // 파일에 query가 들어가있는지 체크하는 클로저 리턴
    def filesRegex(query: String) = filesMatching(_.matches(query))             // 파일이름이 query regular expression 에 매칭되는지 체크하는 클로저 리턴
}
```

- 위의 FileMatcherAfter를 자바에서 구현하려면? (스칼라의 1급 계층함수가 자바에는 없으므로)
  - String을 인자로 받아서 Boolean을 반환하는 메소드를 포함한 인터페이스 작성
  - 작성된 인터페이스를 구현한 익명 내부 클래스 (anonymous inner class)의 인스턴스를 생성해서, filesMatching에 전달
  - (사실 자바에 람다 표현식이 들어가면서 쉬워졌다 한다...)

####2. 클라이언트 코드 단순하게 만들기
- 서버-클라이언트 구조에서 API에 고차 함수를 포함시키면 클라이언트 코드를 간결하게 구성할 수 있음
- 스칼라 컬렉션 타입의 특별 루프 메소드가 실제 구현된 예시들
- 단순화된 코드 예시
```scala
def containsNeg(nums: List[Int]):Boolean = {                          // nums 리스트 내부에 음수가 존재하는지 체크
    var exists = false
    for (num <- nums)
        if (num < 0)
            exists = true
    exists
}
 
def containsOdd(nums: List[Int]): Boolean = {                         // nums 리스트 내부에 홀수가 존재하는지 체크
    var exists = false
    for (num <- nums)
        if (num % 2 == 1)
            exists = true
    exists
}

 
def containsNegSimple(nums: List[Int]):Boolean = nums.exists(_ < 0)        // containsNeg와 동일한 함수
def containsOddSimple(nums: List[Int]):Boolean = nums.exists(_ % 2 == 1)   // containsOdd와 동일한 함수
```

####3. 커링 (currying)
- 함수형 언어에서 자주 사용되는 기법
- 인자 목록을 여러개 가지고 있음
  - 인자 목록 개수만큼 중첩된 함수가 존재하고, 인자를 모두 입력하여 호출시 이를 모두 호출하는 형태
  - 따라서 일부 인자만 채워주면 나머지 인자를 채울 수 있는 함수가 리턴
- 이전에 나왔던 클로저를 리턴하는 함수를 좀 더 구조적으로 구성할 수 있게 해주는거라 생각하면 됨
- 샘플 코드
```scala
def plainOldSum(x: Int, y: Int) = x + y        // 일반적인 형태의 덧셈 함수
val res1 = plandOldSum(1, 2)
 
 
def curriedSum(x: Int)(y: Int) = x + y         // 커링을 사용한 덧셈 함수
val res2 = curriedSum(1)(2)
 
 
def first(x: Int) = (y: Int) => x + y          // 클로저를 사용한 덧셈 함수
val second = first(1)
val res3 = second(2)
 
 
val onePlus = curriedSum(1) _                  // 커링을 사용하면 클로저를 사용해서 동작하는 것과 동일하게 사용할 수 있음
val res4 = onePlus(2)                          // 실제 내부적으로는 클로저를 사용하는 동작과 동일한 바이트코드가 생성됨
```

####4. 새로운 제어 구조 작성
- 제어 구조 변경
  - 1급 계층 하수를 통해 제어 구조를 고도화 할 수 있음
  - 샘플코드
```scala
def twice(op: Double => Double, x: Double) = op(op(x))     // x에다가 op를 두번 연산하고 결과값을 리턴해주는 함수
val res = twice(_ + 1, 5)                                  // res에는 7이 저장됨
```

- 빌려주기 패턴 (loan pattern)
  - 함수 내로 자원을 빌려주고 이를 내부에서 처리하는 로직
  - 샘플코드
```scala
def withPrintWriter(file: File, op: PrintWriter => Unit) = {         // 결과를 저장할 파일과, writer에서 호출할 함수 형태를 전달해줌
    val writer = new PrintWriter(file)
    try {
        op(writer)
    } finally {
        writer.close()
    }
}
 
 
withPrintWriter(new File("date.txt"), w => w.println(new java.util.Date))
 
/*
위의 코드를 실행하면 date.txt 에 println(new java.util.Date) 의 결과가 저장됨 (현재 날짜 시간 저장)
동작 과정은
val op = (w: PrintWriter): Unit = w.println(new java.util.Date)
를 생성하고 이걸 인자로 넘겨줌
그리고 내부에서 op의 파라미터라 writer를 넘겨줘서 실제로 생행되는건 writer.println(new java.util.Date) 임
 
여기서 withPrintWriter가 파일을 닫고있음
따라서 외부에서는 withPrintWriter 한테 File 자원을 빌려주고 닫는건 신경쓰지 않아도 됨
*/
```

- 그리고 scala에서는 파라미터가 1개일경우 소괄호를 중괄호로 대체할 수 있음
  - 내장 제어 구문인것처럼 함수 사용 가능
  - 샘플코드
```scala
def withPrintWriter(file: File)(op: PrintWriter => Unit) = {         // 위와 동일하지만 커링 사용
    val writer = new PrintWriter(file)
    try {
        op(writer)
    } finally {
        writer.close()
    }
}
 
val file = new File("date.txt")
withPrintWriter(file) {
    writer => writer.println(new java.util.Date)                     // 요렇게 중괄호를 사용해서 내장 구문인것처럼 쓸 수 있음. 뭐가 좋은진 모르겠음
}
```

####5. 이름에 의한 호출 파라미터 (by-name parameter) 작성
- call by name과 같은 방식
- 입력 인자를 넣어주지 않고 함수의 출력값만 지정해주면 됨
- 반드시 함수 값이 들어가야 함
- 내부에서 값 변경시 외부에서 반영
  - val이라 파라미터 자체를 바꾸는건 안되지만 객체를 넘겨주고 객체 내부에 var이 있으면 그 값 변경 가능
  - 뭐 사실 이건 다른데서도 동일하니 패스
- call by reference랑 뭐가 다른가?
  - 함수를 넘겨줄때 차이
  - call by reference는 연산이 일어나고 그 결과를 전달함
  - by-name parameter에서는 lazy evaluation이 일어남 => 내부 파라미터에 해당 연산이 그대로 동일하게 전달
    - 예를들어 파라미터를 출력하는 함수가 있다면 해당 함수 내에서 차이는
    - ex) callByRef( 5 > 3 ) => println( true )
    - ex) callByName( 5 > 3 ) => println( 5 > 3 )
- 선언 방법
  - 함수 전달 형태에 대해 입력값 부분을 비우고 출력값만 넣음
  - ()도 생략
- 샘플코드
```scala
var assertOn = True
 
 
def byNameAsssert(predicate: => Boolean) = {        // by-name parameter를 사용
    if (assertOn && !predicate)
        throw new AssertionError
}
 
 
def boolAsssert(predicate: Boolean) = {             // 단순히 파라미터를 전달 - 동일하게 동작하나 lazy evaluation이 동작하지 않음
    if (assertOn && !predicate)
        throw new AssertionError
}
 
 
byNameAsssert(5 > 3)             // 정상 동작
boolAsssert(5 > 3)               // 정상 동작
byNameAsssert(x / 0 == 0)        // division by zero 발생
boolAsssert(5 > 3)               // division by zero 발생
 
 
assertOn = False
byNameAsssert(x / 0 == 0)        // 정상동작 (x / 0 연산이 일어나지 않은채로 전달)
boolAsssert(5 > 3)               // division by zero 발생
```
