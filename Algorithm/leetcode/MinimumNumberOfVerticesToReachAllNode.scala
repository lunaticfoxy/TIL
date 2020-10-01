/*
주소: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

내용
- 단방향 그래프가 주어진다
- 이 그래프에서 모든 노드를 탐색할 수 있는 최소한의 시작 지점을 구하라

예시
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.


풀이방법
- 모든 노드의 탐색이 가능하려면 자기를 가리키는 엣지가 없는 노드도 탐색 가능해야 한다
- 이 노드들만 탐색하면 나머지는 어떻게든 연결될 것이다
*/

object Solution {
    def findSmallestSetOfVertices(n: Int, edges: List[List[Int]]): List[Int] = {
        val noAns = edges.map{x =>
            x(1)
        }.toSet
        
        (0 until n).toSet.diff(noAns).toList
    }
}
