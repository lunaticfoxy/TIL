def calcRatio(arr: Array[(Int, Int)], lastSum: Int, allSum: Int, arrRes: Array[(Int, Int, Int, Double)]): Array[(Int, Int, Int, Double)]= {
  if(arr == null || arr.isEmpty)
    arrRes
  else
    calcRatio(arr.drop(1), lastSum + arr(0)._2, allSum, arrRes ++ Array((arr(0)._1, arr(0)._2, lastSum + arr(0)._2, (arrRes.last._3 + arr(0)._1).toDouble / allSum.toDouble)))
}
