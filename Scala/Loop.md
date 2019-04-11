#### Scala에서의 반복문 관련된 내용 정리

##### 기본적인 내용
- 단순 연산을 위한 반복과 결과값을 사용하기 위한 반복이 나뉘어 있음
  - 단순 연산: while, for, foreach 등
  - 결과값 활용: map, filter 등
- break 없음
  - 조건문을 잘 만들어서 회피하길 바란다고 함...
  - 물론 continue도 없음
- Array, List, Seq등 여러 값을 저장하는 시퀀셜 자료구조에 자체 포함된 연산들이 많음
  - foreach, map, filter, flatmap 등도 예시
  
##### while 문
- 지원은 한다
  - 하지만 권장하진 않는다
  - 이론상 모든 while문은 for문으로 대체할 수 있으므로 가급적이면 for 사용할 것
- 다른 언어와 거의 동일
- 리턴값 없음

##### for 문
- 적극 권장한다
- 사용법은 기본적으로 for(각각변수명 <- 전체변수명) 이다
```scala
for(eachItem <- allItems)
    println(eachItem)
```
- 조건에 filter를 넣을 수 있음
  - 해당 조건에 맞는 값만 본문으로 들어감
  - 반복 요소 뒤에 if를 넣어 사용
```scala
for(eachItem <- allItems if eachItem > 10)
    println(eachItem)
```
- 리턴값은 없다고 보는게 무방

##### foreach 문
- 시퀀셜 자료구조에서 연산만을 수행할때 권장
- 리턴값이 없음
- 변수.foreach(x => 본문) 형태로 사용
```scala
(0 to 10).foreach(x => println(x))
```

##### map, filter + a
- 시퀀셜한 자료구조에서 연산 결과를 다시 시퀀셜한 자료구조로 저장하고자 할때 사용
- 리턴값도 시퀀셜한 자료구조
- 사실상 함수임
  - foreach와 사용법 동일
  - 변수.map(x => 본문), 변수.filter(x => 본문) 형태로 사용
- map은 각각 연산 결과를 쭉 이어붙여서 저장
- filter는 조건에 맞는 값만 저장
```scala
val temp1 = Array(1, 2, 3, 4).map(x => x * 2) // temp1에 Array(2, 4, 6, 8) 저장
val temp2 = Array(1, 2, 3, 4).filter(x => x % 2 == 0) // temp2에 Array(2, 4) 저장
```
  
##### flatmap
- 조금 특이한애라 따로 작성
- 기본은 map과 동일하지만 map내의 리턴이 시퀀셜한 자료구조일 경우에도 이를 flat 하게 펴줌
```scala
val temp1 = Array(Array(1, 2), Array(3, 4)).map(x => x) // temp1에 Array(Array(1, 2), Array(3, 4)) 저장
val temp2 = Array(Array(1, 2), Array(3, 4)).flatmap(x => x) // temp2에 Array(1, 2, 3, 4) 저장
```
