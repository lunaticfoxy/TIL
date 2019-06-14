### Spark에서 IN, NOT IN 연산 수행


#### 쿼리를 이용한 방법
```sql
select *
from table
where key in (select key from key_table)

select *
from table
where key in (select key from except_table)
```
- 하이브 쿼리와 동일
- 잘 돌지 않는 경우 존재
  - 스파크 자체 조인이 아니므로 내부적으로 최적화 되지 않는 경우 존재
  - 모든 경우에 최적화가 일어나지 않는 경우는 아니지만 비추천


#### scala Seq 객체와 수행하는 방법
```scala
val keys:Seq[String] = Seq(...)
val excepts:Seq[String] = Seq(...)

val df = spark.sql("select * from table")
val df_key = df.filter(df("key").isIn(keys:_*))
val df_except = df.filter(!df("key").isIn(excepts:_*))
```
- spark df나 rdd를 collect 한 이후에도 사용 가능
  - 물론 메모리는 알아서...
- 현실적으로 하둡 자원을 가져와서 사용해야 하는 spark에서는 사용하기 어려움


#### spark Dataframe 끼리 수행하는 방법
```scala
val keysDf = spark.sql("select key from key_table")
val exceptsDf = spark.sql("select key from except_table")

val df = spark.sql("select * from table")
val df_key = df.join(keysDf.withColumn("isKey", lit(1)), df("key")===keysDf("key"), "left")  // left 조인으로 붙인 뒤 null이 아닌 값들이
              .filter(col("isKey").isNotNull)                                                // 양쪽에 모두 포함된 값

val df_except = df.join(keysDf.withColumn("isKey", lit(1)), df("key")===keysDf("key"), "left") // left 조인으로 붙인 뒤 null인 값들이
              .filter(col("isKey").isNull)                                                     // df에만 포함된 값
```
- 사실상 제일 필요한 기능이지만 스파크 자체 미지원
- 조인을 통해 꼼수를 써서 해결
- 원리
  - a에 있고 b에도 있는 데이터를 가져오려면 a에만 있는 데이터를 제거해야 함
  - a와 b를 LEFT 조인하면 a의 데이터는 그대로 남고 b의 데이터는 a에 있는 것만 붙으므로 이를 사용하자
  - b에 새로운 컬럼을 하나 넣어서 flag로 사용한다 (위에서는 isKey)
  - a를 기준으로 b와 LEFT 조인을 하면 a에만 있는 데이터는 isKey값이 NULL이 된다
  - 따라서 이후에 isKey값이 NULL인 데이터를 제거하면 a에만 있는 데이터가 제거됨 (in 조건)
    - 반대로 a에만 있는 데이터만 남기고 싶다면 isKey값이 NULL이 아닌것만 남기면 됨 (not in 조건)
