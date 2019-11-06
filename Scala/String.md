### Scala 문자열 관련 내용 정리

- 문자열 이어붙이기
  - + 연산으로 가능
  - 타 언어 타입도 자동으로 변환 (앞 변수가 문자열이어야됨)

```scala
val temp:Int = 44 
val res:String = "test" + " str " + 123 + " " + temp // res = "test str 123 44"
```

#### 문자열 분할
- split 함수로 가능
- 단 Regualr Expression사용
  - regex에 매칭되는 값을 기준으로 분할
  - metacharacter들을 분할값에 사용하고 싶으면 ₩₩를 앞에 붙일것
    - ₩ 하나만 붙이면 scala 자체의 escape문자로 취급
    - ₩₩ 를 붙여야 ₩ 를 문자열에 포함하게 되어서 사용 가능
    - ₩₩? ₩₩. 등
```scala
val url = "http://www.daum.net/test1/test2?val1=0&val2=1"
val splited = url.split("\\?")                                // Array("http://www.daum.net/test1/test2", "val1=0&val2=0")
val splited_again = splited(0).split("[\\.:,=/]")             // Array("http", "www", "daum", "net", "test1", "test2")
val filterArr:Array[String] = Array("http", "https", "", "www")
val res = splited_again.filter(!filterArr.contains(_))        // Array("daum", "net", "test1", "test2")
```

#### 문자열 내에 변수 삽입
- 덧셈 연산자 이용
  - 사용법: "앞 문자열" + 변수 + "뒷 문자열"
  - 원리: 변수.toString이 자동으로 호출되어 문자열의 합으로 변환됨
  - 장점: 쉽고 직관적
  - 단점: 긴 문자열의 경우 헷갈릴 가능성이 높음
- 변수 직접 지정
  - 사용법
    - s"문자열 안에 변수 ${value}를 넣기"
    - s"문자열 안에 변수 $value 를 넣기"
      - {}는 생략 가능하지만 그럴 경우 뒤에 공백이 나와야 함
      - 변수명과 섞이지 않게
  - 원리: 변수.toString을 자동으로 호출해서 해당 지점에 넣어줌
  - 장점: 생성된 문자열의 형태가 쉽게 확인 가능
  - 단점: 문자열 앞에 s를 붙여주어야 하며, 실수할경우 변수명이 그대로 출력될 실수를 할 가능성이 높음


#### Symbol
- 자바와 스칼라의 문자열 비교 차이
  - 자바에서는 == 연산시 객체의 동일성을 비교
    - 따라서 동일한 값을 지닌 문자열이 == 을 통과하지 못할 수 있음
    - 대신 equals 사용 필요
  - 스칼라에서는 == 연산시 객체의 값을 비교
    - 따라서 두 문자열이 같은지 비교가 가능
    - 하지만 eq 연산을 수행할 경우 서로 다른 객체이므로 통과하지 못함
      - 자바의 == 와 동일
- 해결을 위한 방법
  - intern() 함수 사용
    - String을 JVM의 String Pool에 들어있는 객체로 변환해준다
    - 동일한 값을 가진 두 문자열이 intern()을 호출하면 동일한 객체가 되서 == 와 eq 모두 통과 가능
  - Symbol 타입 사용
    - val test = '문자열 형태로 사용한다
    - eq 와 == 를 모두 통과할 수 있도록 별도로 지정해둔 타입
    - 비교시 이외에는 String과 동일한 타입으로 취급된다고 생각하면 편하다
```scala
val str1 = new String("String")
val str2 = new String("String")

println(str1 eq str2) // false

val str1 = new String("String").intern() // val str1 = "String"과 같다.
val str2 = new String("String").intern() // val str2 = "String"과 같다.

println(str1 eq str2) // true

val symbol1 = 'String
val symbol2 = 'String

println(symbol1 eq symbol2) // true
```
