# 스파크에서 정렬 관련 내용 정리

#### 주의사항
- 정렬시 필드명만 넘겨주면 limit과 연계되지 않음
- 반드시 필드명을 키로 지정해서 이후에도 사용 가능하도록 해야함
```scala
val sorted = res.orderBy(col("score").desc).limit  // 동작
val sorted = res.orderBy("score").limit            // 미동작
val sorted = res.orderBy(desc("score")).limit      // 미동작
val sorted = res.orderBy(res("score").desc).limit  // 확인필요
val sorted = res.orderBy($"score".desc).limit      // 확인필요
```
