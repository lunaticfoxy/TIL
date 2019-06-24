#### Scala 문자열 관련 내용 정리

- 문자열 이어붙이기
  - + 연산으로 가능
  - 타 언어 타입도 자동으로 변환 (앞 변수가 문자열이어야됨)

```scala
val temp:Int = 44 
val res:String = "test" + " str " + 123 + " " + temp // res = "test str 123 44"
```

- 문자열 분할
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

- 문자열 내에 변수 삽입
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
