### Window와 관련된 내용을 정리

#### group 별 상위 row를 뽑는 방법
- group을 묶은뒤 Window에 row_count 함수를 적용한다
- 이후 expr 함수에서 row_count 가 일정 이하인 값을 리턴한다
  - 정렬시 오름차순이므로 내림차순 정렬이 필요하면 별도 세팅을 통해 내림차순으로 바꿔야 한다

```scala
val windowSpec = Window.partitionBy(to).orderBy(col("date_id").desc)
convDf.select(from, to, "date_id")
    .withColumn("row_number", row_number.over(windowSpec))
    .filter("row_number = 1")
    .select(from, to).distinct()
```
