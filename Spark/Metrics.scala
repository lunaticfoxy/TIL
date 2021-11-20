
object Metrics {
  case class result_(label: Double, precision: Double, recall: Double, Fmeasure: Double)

  case class result(conf_matrix: org.apache.spark.mllib.linalg.Matrix, total: Int, accuracy: Double, resultArray: Array[result_]) {
    override def toString(): String = {
      var strB = new StringBuilder
      strB.append("total : " + total + "\n")
      strB.append("accuracy : " + accuracy + "\n")
      strB.append("conf matrix : \n" + conf_matrix + "\n")
      strB.append(resultArray.mkString(","))
      strB.toString
    }
  }

  case class resultForDf(confMat: Map[(String, String), Long], total: Long, accuracy: Double) {
    override def toString(): String = {
      val strB = new StringBuilder
      strB.append("total : " + total + "\n")
      strB.append("accuracy : " + accuracy + "\n")
      strB.append("conf matrix : \n" + confMat + "\n\n")

      val labels = confMat.keys.map(_._1).toArray.sorted

      val labelString = " \t" + labels.mkString("\t")
      strB.append(labelString + "\n")
      strB.append("-" * (labelString.size * 2) + "\n")

      labels.foreach{l =>
        strB.append(l + " |\t")
        labels.foreach { p =>
          strB.append(confMat(l, p).toString + "\t")
        }
        strB.append("\n")
      }

      strB.toString
    }
  }

  def getMultiClsResultDf(df: DataFrame, predField: String, actualField: String): resultForDf = {
    val total = df.count()
    val accuracy = df.filter(x => x.getAs[Double](predField) == x.getAs[Double](actualField)).count().toDouble / df.count()
    val confMat: Map[(String, String), Long] = df.groupBy(actualField, predField).count().collect().map{x =>
      val actual = x.getAs[Double](actualField)
      val pred = x.getAs[Double](predField)
      val cnt = x.getAs[Long]("count")
      (actual.toString, pred.toString) -> cnt
    }.toMap

    val clsResultDf = new resultForDf(confMat, total, accuracy)

    clsResultDf
  }

  def getMultiClsResult(PredsAndValue: RDD[(Double, Double)]): result = {
    import org.apache.spark.mllib.evaluation.MulticlassMetrics
    val metric = new MulticlassMetrics(PredsAndValue)
    val accuracy = PredsAndValue.filter(x => x._1 == x._2).count().toDouble / PredsAndValue.count()
    val clsResult = new result(metric.confusionMatrix, PredsAndValue.count().asInstanceOf[Int], accuracy, metric.labels.map {
      e => new result_(e, metric.precision(e), metric.recall(e), metric.fMeasure(e))
    })
    clsResult
  }
}
