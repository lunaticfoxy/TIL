"""
주소: https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

내용
- 도시간 연결 상태를 나타낸 양방향 그래프가 주어진다
  - 이 그래프는 트리로 전환 가능하다 (=사이클이 존재하지 않는다)
- 도시간 거리가 1, 2, ..., n-1 이 되는 sub graph의 개수를 각각 구하라

예제
Example 1:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:
Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:
Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]


풀이방법
- 모든 경우의수를 고려
- 각 노드에서 시작하면서 옆 노드를 하나씩 추가하고, 이때 포함된 노드간의 최대 거리를 계산
- 단, 중복 제거 및 가지치기를 위해 frozenset을 활용하여 현재 포함된 노드를 저장
- 저장된 노드가 그대로 다시 나타날경우 재귀 종료

"""
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        dist_map = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        found = [set([]) for _ in range(n)]
        ebn = [set([]) for _ in range(n+1)]
        
        for edge in edges:
            ebn[edge[0]].add(edge[1])
            ebn[edge[1]].add(edge[0])
            dist_map[edge[0]][edge[1]] = 1
            dist_map[edge[1]][edge[0]] = 1
            
        for i in range(n+1):
            dist_map[i][i] = 0
        
        
        def search(dist: int, nodes: frozenset):
            if dist >= 1:
                if nodes in found[dist]:
                    return
                else:
                    found[dist].add(nodes)
            
            for con_node in nodes:
                for new_node in ebn[con_node]:
                    if not new_node in nodes:
                        new_nodes = set([new_node])

                        max_dist = -1
                        max_dist_nodes = []
                        for node in nodes:
                            new_nodes.add(node)
                            dist_map[node][new_node] = dist_map[node][con_node] + 1
                            dist_map[new_node][node] = dist_map[node][con_node] + 1
                            
                            if dist_map[node][con_node] > max_dist:
                                max_dist = dist_map[node][con_node]
                                max_dist_nodes = [node]
                            elif dist_map[node][con_node] == max_dist:
                                max_dist_nodes.append(node)
                        
                        if max_dist == dist:
                            for node in max_dist_nodes:
                                search(dist + 1, frozenset(new_nodes))
                        else:
                            search(dist, frozenset(new_nodes))
                        
        
        for i in range(1, n+1):
            search(0, frozenset([i]))
            #print(found[2])
        
        
        return [len(found[i]) for i in range(1, n)]
            
