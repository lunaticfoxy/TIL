### 직접 Dataframe 만드는 법

#### 망할 스파크는 직접 Dataframe 만드는것도 어렵게 되어있습니다
- Seq 데이터를 2중 Seq로 구성
- spark.sparkContext.parallelize 함수를 이용하여 spark에서 사용 가능한 형태로 만든다
- Dataframe의 스키마를 StructType으로 지정한다
  - 내부에 StructField의 시퀀스로 컬럼명을 지정해준다
  - 이때 컬렘명의 Seq와 map을 사용하면 편리
- spark.createDataFrame 함수를 사용하여 rows와 schema를 Dataframe으로 합친다

```scala
val rawRows = Seq("data1", "data2", "data3", "data4")

val doubleSeq = Seq(rawRows)

val rows = spark.sparkContext.parallelize(doubleSeq)

val schema = StructType(Seq("col1", "col2", "col3", "col4")
                        .map(col => StructField(col, StringType, nullable = false)))

val df = spark.createDataFrame(rows, schema)
```
