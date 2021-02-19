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


def BSTIter(start: Long): Map[Long, (List[Long], Long)] = {
    val queue = new scala.collection.mutable.Queue[(Long, List[Long], Long)]()
    val path: scala.collection.mutable.Map[Long, (List[Long], Long)] = scala.collection.mutable.Map[Long, (List[Long], Long)]()
    val visited: scala.collection.mutable.Set[Long] = scala.collection.mutable.Set[Long]()

    queue.enqueue((start, List[Long](), 0L))
    visited += start

    while(queue.nonEmpty) {
      val (curId, curPath, curDist) = queue.dequeue()
      val newPath = curPath ++ List(curId)
      path.put(curId, (newPath, curDist))

      if(vertexMap.contains(curId)) {
        vertexMap(curId).foreach{x =>
          if(!visited.contains(x._1)) {
            queue.enqueue((x._1, newPath, curDist + 1))
            visited += x._1
          }
        }
      }
    }

    path.toMap
  }
