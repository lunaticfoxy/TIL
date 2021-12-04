
def overSampling(df: Dataframe, labelCol: String, overallRatio: Map[Double, Double], maxSample: Double = 30.0): Dataframe = {
  val maxRatio = overallRatio.values.max
  val weights = overallRatio.map{x => x._1 -> x._2 / maxRatio}.map { x =>
    (x._1, Math.min(1.0 / x._2, maxSample))
  }

  val sampleTb = "tb_example"
  spark.sql(s"DROP TABLE IF EXISTS ${sampleTb}")

  weights.foreach{w =>
    println(s"weight_val: ${w._1} - ${w._2}")
    val filtered = df.filter(s"${labelCol} = ${w._1}")

    println(s"sample repeat ${w._2.toInt} times")
    (0 until w._2.toInt).foreach{i =>
      filtered.write.mode("append").saveAsTable(sampleTb)
    }

    if(w._2.toInt != w._2) {
      println("sample remained")
      filtered.sample(w._2 - w._2.toInt.toDouble).write.mode("append").saveAsTable(sampleTb)
    }
  }
    
  spark.sql("SELECT * FROM ${sampleTb})
}
