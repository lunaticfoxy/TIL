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

      
