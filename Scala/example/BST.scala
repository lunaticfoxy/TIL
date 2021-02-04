def BSTRecur(vertexMap: Map[Int, Array[(Long, Long)]], visited: Set[Int], queue: Array[(Int, Array[Int])], path: Map[Int, Array[Int]]): Map[Int, Array[Int]] = {
      if(queue.size == 0)
        path
      else {
        val curId = queue(0)._1
        val curPath = queue(0)._2

        val newVisit = vertexMap(curId).map(_._1).filter(!visited.contains(_))

        BSTRecur(vertexMap,
          visited ++ newVisit.toSet,
          queue.drop(1) ++ newVisit.map((_, curPath ++ Array(curId))),
          path ++ Map(curId -> (curPath ++ Array(curId)))
        )
      }
    }
