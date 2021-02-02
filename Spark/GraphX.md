# GraphX 에 관한 내용을 정리하는 문서



- outerJoinVertices[U, VD2](other: RDD[(VertexId, U)])(mapFunc: (VertexId, VD, Option[U]) => VD2): Graph[VD2, ED]
  - 개요: 그래프를 조인하면서 값을 변경하는 함수
  - 입력
    - other: 조인할 Vertex RDD
    - mapFunc: 조인 대상 함수
      - VertexID: 해당 Vertex의 식별값
      - VD: 기존 Vertex의 속성
      - Option[D]: 조인할 Vertex의 속성
  - 출력: 조정된 그래프

- subgraph(epred: EdgeTriplet[VD,ED] => Boolean = (x => true), vpred: (VertexId, VD) => Boolean = ((v, d) => true)): Graph[VD, ED]
  - 개요: 그래프에서 부분 집합을 탐색하는 함수
  - 입력
    - epred: 엣지 기준으로 부분집합을 탐색하는 함수
    - vpred: 버텍스 기준으로 부분집합을 탐색하는 함수

- mapVertices[VD2](map: (VertexId, VD) => VD2): Graph[VD2, ED]
  - 개요: 버텍스를 순회하며 map 연산을 수행하여 버텍스의 속성을 변경하고 이를 반영하여 새로운 그래프를 생성

- 위의 함수들 예제
  - validGraphTest를 돌면서 degree (외부로 나가는 엣지 수)가 0인 노드들을 제거한 새로운 그래프 생성
```scala
validGraphTest
  .outerJoinVertices(validGraphTest.degrees){(vid, oldAttr, outDegOpt) =>         // 자기 자신 버텍스의 degree와 조인
    outDegOpt match {                                                             // degree 값을 체크하여
      case Some(outDegOpt) => (oldAttr, outDegOpt)                                // degree 값이 있는 애들은 그대로 유지
      case None => (oldAttr, 0)                                                   // degree 값이 없는 애들은 0 을 넣어줌
    }
  }
  .subgraph(vpred = (vid, attr) => attr._2 > 0})                                  // 앞에서 넣은 degree가 0 보다 큰 애들만 남김
  .mapVertices((vid, attr) => attr._1)                                            // 추가된 degree 속성을 없애고 기존 속성만 남겨 새로운 그래프 생성
```
