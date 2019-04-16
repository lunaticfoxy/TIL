#### Shapless

##### 개요
- 타 언어의 Template과 유사
- 한 함수에서 20개까지 사용 가능

##### 사용법
- 함수에서의 사용법
  - def fName[T](arrVal:Array[T], oneVal:T) 형태로 사용
```scala
def maxVal[T](arr:Array[T]):T = {
    var maxValue:T = 0
    for(x <= arr) {
        if(x > maxValue)
            maxValue = x
    }
    maxValue
}
```
- 여러개가 쓰고 싶으면?
  - def fName[T1, T2, T3, T4, T5](val1:T1, val2:T2, arrVal3:T3, mapVal4:Map[T4]=>T5)
  - T, T1, T2, ... , T19까지 사전 정의되어 있음
