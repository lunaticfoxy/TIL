### Spark에서 IN, NOT IN 연산 수행


#### 쿼리를 이용한 방법
- 하이브 쿼리와 동일
```sql
select *
from table
where key in (select key from key_table)

select *
from table
where key in (select key from except_table)
```


#### scala Seq 객체와 수행하는 방법
```scala
val keys:Seq[String] = Seq(...)
val excepts:Seq[String] = Seq(...)

val df = spark.sql("select * from table")
val df_key = df.filter(df("key").isIn(keys:_*))
val df_except = df.filter(!df("key").isIn(excepts:_*))
```


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
