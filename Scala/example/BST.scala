def BSTRecur(vertexMap: Map[VertexId, Array[(VertexId, Long)]], visited: Set[VertexId], queue: Array[(VertexId, Array[VertexId])], path: Map[VertexId, Array[VertexId]]): Map[VertexId, Array[VertexId]] = {
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
