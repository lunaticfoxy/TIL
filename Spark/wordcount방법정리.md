### 데이터 타입에 따른 word count 방법 정리

#### RDD
```scala
rdd.flatMap(line => line.split(" "))
    .map(word => (word, 1))
    .reduceByKey(_ + _)
    .foreach(tuple => println(tuple._1, tuple._2)
```

#### DataFrame
```scala
df.map{x => (x, 1)}
  .toDF("word", "count")
  .groupBy("word")
  .count()
  .foreach{x =>
     println(x.getAs[String]("word"), x.getAs[Int]("count")) // count가 long일수도 있음 확인하지 않음
  }
```

#### Collection
```scala
data.map(x => (x, 1))
    .groupBy(_._1)
    .mapValues(_.size)
    .foreach(tuple => println(tuple._1, tuple._2)
```
