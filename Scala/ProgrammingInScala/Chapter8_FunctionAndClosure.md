1. 메소드
- 메소드: 객체의 멤버인 함수
- 메소드는 함수의 부분집합
 
2. 지역함수
- 블록 내에서만 존재하는 함수
- 블록 밖에서 사용 불가능
- 지역 함수는 블록 내 변수 사용 가능

3. 1급 계층 함수
- 1급 계층 함수란?
 - 함수를 지정된 변수에 할당 가능
 - 함수를 인자로 사용 가능
 - 타 함수 내에서 함수 반환 가능
 - 대략 함수를 다른 변수와 동일하게 사용할수 있는지로 구분
- 스칼라는 1급 계층 함수 지원
 - 타 언어와 비교해보면 C에서는 함수 내에서 새로운 함수를 만들고 이걸 리턴하는게 불가능하므로 1급 계층이 아님 (2급)
- 함수 리터럴
 - 별도의 이름 없이 표기되는 함수
 - 물론 변수에 할당해서 이름을 지정해줄수도 있음
 - foreach나 filter와 같은 메소드에서 사용하면 용이
 - 첨언 - 타 언어의 람다 함수와 동일하다고 생각하면 될듯 함
- 샘플 코드
```scala
var increase = (x: Int) => x + 1 // (x: Int) => x + 1 부분이 함수 리터럴이며, 이를 increase라는 변수에 할당하는 형태
 

val res = increase(10)   // res에는 11이 들어감
increase = (x: Int) => {
    println("We")
    println("are")
    println("here!")
    x+2                  // 함수 리터럴도 마지막 줄의 연산 결과를 리턴
}
 
 
val res2 = increase(10)  // res2에는 12가 들어감
 
 
val someNumbers = List(-11, -10, -5, 0, 5, 10)
someNumbers.foreach((x: Int) => println(x))     // 모든 값 출력
someNumbers.filter((x: Int) => x > 0)           // List(5, 10) 반환 
```

- 타입이 확실할경우 생략 가능
- 타입을 생략하면서 괄호도 생략 가능

```scala
someNumbers.filter((x: Int) => x > 0)
someNumbers.filter(x => x > 0)         // 위와 동일한 코드
```

4. 위치 표시자 문법
- 리터럴을 더 간단하게 만들기 위해 _ 를 파라미터의 위치 표시자로 사용 가능
- _ 를 채워 넣어야 할 빈칸 이라 생각하면 이해하기 쉬움
 - _ 가 1개이면 빈칸이 1개이므로 인자 1개
 - _ 가 2개이면 빈칸이 2개이므로 인자 2개
 - _ 가 n개이면 빈칸이 n개이므로 인자 n개
- 타입이 확실하지 않아 지정해야 할때는 (_: Type) 형태로 타입 명시
- 샘플 코드
```scala
someNumbers.filter(x => x > 0)
someNumbers.filter(_ > 0)       // 위와 동일한 코드
 
val f = _ + _                  // 타입을 추론할수 없어 에러 발생
val f = (_: Int) + (_: Int)    // 타입을 명시해서 사용 가능
val res = f(5, 10)             // res에 15 저장
```


5. 부분 적용한 함수
- 함수의 인자값으로도 _ 를 넘길수 있음
 - 괄호 없이 쓸수도 있음 다만 공백 필수
 - 이는 부분 적용 함수라 생각하면 됨
- 부분 적용 함수
 - 함수에 필요한 인자를 전부 적용하지 않은 표현식
 - 인자 대신에 _ 를 넣어 인자를 넣을수 있는 함수를 리턴함
 - 일부 인자만 _ 로 대체하는 것도 가능
 - 내부 동작
  - 실제로는 apply 라는 메소드를 생성하고, 리턴되는 객체의 apply 메소드에 인자를 집어넣는 형태로 동작
  - apply 메소드 안에서 전체 함수를 호출
  - 따라서 부분함수.apply() 는 부분함수() 와 동일
 - 만약 함수의 역할이 확실히 지정되어있는 foreach, filter등의 인자로는 _ 마저 생략 가능함
- 샘플코드
```scala
someNumbers.foreach(println _)       // 요런 형태로 인자를 _ 로 생략 가능
 
 
def sum(a: Int, b: Int, c: Int) = a + b + c  // 전체 sum 함수
 
 
val a = sum _
val res1 = a(1, 2, 3)            // res1에 6 저장
val res2 = a.apply(1, 2, 3)      // res2에도 6 저장 (위와 동일한 함수 호출하는 것임)
 
 
val b = sum(1, _: Int, 3)
val res3 = b(2)                  // res3에 6 저장
val res4 = b(5)                  // res4에 9 저장
 
 
someNumbers.foreach(x => println(x))
someNumbers.foreach(println _ )
someNumbers.foreach(println)           // 이 3개 코드는 모두 동일한 코드임 (foreach 내부에는 인자가 하나씩 내부 함수로 들어간다는게 확실하므로 _ 까지 생략)
```


6. 클로저
- 함수 내에서 외부 변수를 사용 가능
- 그렇다면 그 변수의 값이 변한다면? 어떻게될까
- 클로저
 - 함수 리터럴에 외부 변수가 들어가 있을때 런타임에 생기는 함수 값
 - 외부 변수가 없는 함수는 컴파일 타임에 바로 닫힌 함수 (closed term)이 될 수 있음
 - 하지만 외부 변수가 있는 함수는 런타임까지 가야 해당 변수를 추적할수 있음 (open term)
 - 따라서 추적하다가 함수가 정의되는 순간 변수의 바인딩을 포획해서 함수로 사용함 => 따라서 open term을 closed term으로 닫는 역할을 하므로 클로저 라고 부름 (closure)
- 클로저가 생성된 뒤에도 변수의 값이 아닌 변수의 바인딩 자체를 포획하므로 값을 바꾸면 바꾼 값에 동적으로 반응함
- 함수 내부에서 외부 변수의 값을 바꾸면 함수 밖에서도 변화가 일어남
- 만약 클로저가 참조될수 있는 변수가 여러개라면? (동일한 이름의 변수가 동적으로 생성될때)
 - 클로저가 생성되는 시점에 참조 가능한 변수를 사용
 - 이후에 해당 이름이 다른 변수로 가더라도 기존 변수를 계속 참조
- 샘플 코드
```scala
var more = 1
val addMore = (x: Int) => x + more   // addMore는 클로저
val res1 = addMore(10)               // res1에 10 저장
 
 
more = 9999
val res2 = addMore(10)               // res2에 10009 저장 (more의 변화가 반영됨)
 
 
val someNumbers = List(-11, -10, -5, 0, 5, 10)
var sum = 0
someNumbers.foreach(sum += _)
val res3 = sum                        // res3에 -11 저장 (foreach 안에서 매 아이템마다 클로저가 생성되고, 이 클로저가 호출될때마다 sum에 값을 더하고 반영됨)
 
 
def makeIncreaser(more: Int) = (x: Int) => x + more    // makeIncreaser는 입력받는 값만큼을 더해주는 클로저 생성 (more가 매번 동적 생성됨)
val inc1 = makeIncreaser(1)
val inc9999 = makeIncreaser(9999)
val res4 = inc1(10)                                    // res4에 11 저장 (inc1 생성 시점에 생성된 more에는 1 저장)
val res5 = inc9999(10)                                 // res5에 10009 저장 (inc9999 생성 시점에 생성된 more에는 9999 저장)
```

7. 특별한 종류의 함수 호출
- 반복 파라미터
 - 함수의 마지막 파라미터에 *를 붙여서 반복 가능하다고 표시 가능
 - 이를 반복 파라미터라 부름
 - 반복 파라미터는 사실 배열임. 호출할때 배열 형태로 넣어줄 필요가 없을뿐
  - 하지만 배열을 직접 인자로 넣어주면 컴파일 에러 발생
  - 혹시 배열 원소를 넣어주고 싶다면 (배열명):  _* 형태로 호출하면 내부 값을 풀어서 전달할 수 있음
- 이름붙인 인자
 - 인자 호출시 이름을 넣고 = 로 값을 대입하면 위치에 상관 없이 값 삽입 가능
 - 위치 기반 인자와 함께 사용 가능
 - 이름붙인 인자 형태로 호출하는 경우는 대부분 디폴트 인자를 주고 사용
- 디폴트 인자 값
 - 인자에 = 를 통해 디폴트 값 줄 수 있음 
- 샘플 코드
```scala
def echo(args: String*) = for (arg <- args) println(arg)     // args에 *를 붙여 반복 파라미터로 설정
echo()                                          // 출력 없음
echo("one")                                     // one 출력
echo("hello", "world")                          // hello\nworld! 출력
 
 
val arr = Array("What`s", "up", "doc?")
echo(arr)                                       // 에러 발생 - 내부적으로는 배열로 관리하지만 실제 배열을 넘겨주면 안됨
echo(arr: _*)                                   // 정상 동작 - 내부적으로 인자를 풀어서 전달해줌
 
 
def speed(distance: Float, time: Float): Float = distance / time
val res1 = speed(100, 10)                       // res1에 10 저장
val res2 = speed(time = 10, distance = 100)     // res2에도 10 저장
 
 
def printTime(out: java.io.PrintStream = Console.out, divisor:Int = 1) = out.println("time = " + System.currentTimeMills()/divisor)
printTime()                                     // console에 현재 시간 출력
printTime(Console.err)                          // 시스템 에러 로그에 현재 시간 출력
printTime(divisor = 1000)                       // console에 현재 시간/1000 출력
printTime(out = Console.err, divisor = 1000)    // 시스템 에러 로그에 현재 시간/1000 출력
```


8. 꼬리재귀
- 꼬리재귀란?
 - 함수의 맨 마지막에 자기 자신을 호출해서 리턴하는 동작"만" 있는 재귀
 - 두 함수가 상호 재귀한다면? => 꼬리재귀 아님
 - 재귀값+1 을 리턴한다면? => 꼬리재귀 아님
- 일반 재귀에 비해 어떤점이 다른가?
 - 함수 스택을 추가 생성하지 않음 => 앞으로 안쓸걸 확실하게 알고 있으니
 - 현재 스택에서 위치만 시작 지점으로 이동
 - 따라서 반복문과 성능 차이 없음!
- 컴파일 타임에 반복문과 동일한 자바 바이트 코드로 변환됨
- 스택 트레이스 시에 꼬리재귀 최적화 때문에 찝찝하다면 컴파일 시 -g:notailcalls 옵션을 줘서 최적화 안할수 있음
- 자기 자신이라도 다른 이름으로 할당된 함수를 호출한다면 꼬리 재귀가 일어나지 않음
- 샘플 코드
```scala
def approximate(guess: Double): Double = {
    if (isGoodEnough(guess)) guess
    else approximate(improve(guess))                    // 리턴값이 자기 자신의 호출이므로 꼬리재귀
}
 
 
def approximateLoop(initialGuess: Double): Double = {   // 이 두 함수의 자바 바이트코드는 동일함
    var guess = initialGuess
    while (!isGoodEnough(guess))
        guess = improve(guess)
    guess
}
 
 
 
 
def foo(x: Int): Int = {
    if (x % 2 == 1) foo(x / 2)
    else 1 + foo(x / 2)                                  // 리턴값에 자기 자신의 호출 이후 연산해야 하는 값이 있으므로 꼬리재귀 아님
}
 
 
def boom(x: Int): Int = {
    if (x == 0) throw new Exception("boom!")
    else boom(x - 1) + 1                                 // 리턴값에 자기 자신의 호출 이후 1을 더하므로 꼬리재귀 아님
}
 
 
def bang(x: Int): Int = {
    if (x == 0) throw new Exception("bang!")
    else bang(x - 1)                                      // 리턴값에 자기 자신의 호출 밖에 없으므로 꼬리재귀임
}
 
 
 
 
def isEven(x: Int): Boolean = if (x == 0) true else isOdd(x - 1)       // 상호 재귀는 꼬리재귀가 될 수 없음
def isOdd(x: Int): Boolean = if (x == 0) false else isEven(x - 1) 
 
 
 
 
val funValue = nestedFun _
def nestedFun(x: Int): Unit = {
    if (x != 0) { println(x); funValue(x - 1) }           // funValue가 가리키는 함수는 nestedFun이지만 외부로 할당되었으므로 꼬리재귀 불가능
}
```
