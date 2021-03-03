  def dotProductMatInt(a: collection.mutable.Map[Int, collection.mutable.Map[Int, Int]], b: collection.mutable.Map[Int, collection.mutable.Map[Int, Int]]): collection.mutable.Map[Int, collection.mutable.Map[Int, Int]] = {
    val transB = collection.mutable.Map[Int, collection.mutable.Map[Int, Int]]()

    b.foreach{x =>
      x._2.foreach{y =>
        if(transB.contains(y._1))
          transB(y._1)(x._1) = y._2
        else
          transB(y._1) = collection.mutable.Map[Int, Int](x._1 -> y._2)
      }
    }

    //println(transB)

    val resMap = collection.mutable.Map[Int, collection.mutable.Map[Int, Int]]()
    a.foreach{x =>
      transB.foreach{y =>
        val curVal = x._2.map(v => y._2.getOrElse(v._1, 0) * v._2).sum

        if(resMap.contains(x._1))
          resMap(x._1)(y._1) = curVal
        else
          resMap(x._1) = collection.mutable.Map[Int, Int](y._1 -> curVal)
      }
    }

    resMap
  }
