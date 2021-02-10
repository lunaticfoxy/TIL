def sumTwoMaps(a: Map[Long, Long], b: Map[Long, Long]): Map[Long, Long] = {
  a ++ b.map{ case (k: Long,v: Long) => 
    k -> (v + a.getOrElse(k,0L))
  }
}
  
def sumTwoSparseMat(a: Map[Long, Map[Long, Long]], b: Map[Long, Map[Long, Long]]): Map[Long, Map[Long, Long]] = {
  val modB = b.map{ case (k1: Long, m: Map[Long, Long]) =>
    val aMap = a.getOrElse(k1, Map[Long, Long]())
    k1 -> sumTwoMaps(m, aMap)
  }

  a ++ modB
}
