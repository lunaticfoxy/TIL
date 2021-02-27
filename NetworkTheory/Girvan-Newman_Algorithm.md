### 개요
- betweenness centrality를 이용한 네트워크내 커뮤니티 탐색 알고리즘

### 목적
- 네트워크 내에서 Modularity를 최대화 하는 커뮤니티 탐색

### 내용
- betweenness centrality (BC)
  - 특정 지점 k가 있을때 네트워크 내의 한 지점 i 부터 j까지 최단거리 상에 k가 몇번 나타나는지에 대한 값
  - 노드 기준이 될 수도 있고, 엣지 기준이 될 수도 있음
  - 거번-뉴먼 알고리즘에서는 엣지 기준을 기본으로 함
- 탐색 방법
  1. 모든 엣지에 대해서 BC를 계산
  2. 가장 높은 BC를 지닌 엣지를 제거
  3. Modularity 계산 후 기존 저장된 Modularity와 비교하여 높으면 현재 상태를 저장
  4. 2~3을 모든 엣지가 사라질때까지 반복
  5. Modularity가 최대인 지점이 가장 모듈화가 잘 된 커뮤니티

```scala
  def GirvanNewman(): Seq[NeighborGraph] = {

    var edgeCnt = vertexMap.map(_._2.keys.size).sum - 1

    val (src, dst, bc) = NeighborGraph.findMaxBetweennessCentrality(vertexMap)
    var foundMap = vertexMap
    var maxModularity: Double = 0.0
    var next = NeighborGraph.removeEdge(vertexMap, src, dst)

    while(edgeCnt > 0) {
      val modularity = NeighborGraph.getModularity(next)

      if(modularity > maxModularity) {
        maxModularity = modularity
        foundMap = next
      }
      else
        edgeCnt = 0

      val (src, dst, bc) = NeighborGraph.findMaxBetweennessCentrality(next)
      next = NeighborGraph.removeEdge(next, src, dst)
      edgeCnt -= 1
    }

    NeighborGraph.findCommunity(foundMap).map{comm =>
      val newVertMap = vertexMap.filter(x => comm.contains(x._1))
        .map(x => x._1 -> x._2.filter(y => comm.contains(y._1)))

      if(newVertMap.isEmpty)
        NeighborGraph(comm.map(x => (x, Map[Long, Long]())).toMap)
      else
        NeighborGraph(newVertMap)
    }
  }
```
