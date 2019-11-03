"""
주소: https://leetcode.com/problems/tree-diameter/

내용
- 무방향 그래프가 주어진다
- 그래프 내에서 두 노드 사이의 최대 거리를 구하라

예제
Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


풀이방법
- 통과 못한 문제임
- 분명 간단한 DFS 문제인데 타임리밋이 난다
  - 서브밋에서 걸린 케이스도 런하면 잘 돌아감...
- 스택 사용한것과 재귀 사용한 케이스 둘다
- 좀 더 최적화할 방안 찾아볼것
"""
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        conn = dict()
        
        for edge in edges:
            if edge[0] in conn:
                conn[edge[0]].add(edge[1])
            else:
                conn[edge[0]] = set([edge[1]])
            
            if edge[1] in conn:
                conn[edge[1]].add(edge[0])
            else:
                conn[edge[1]] = set([edge[0]])

        
        def dfs(conn, pr, nx, dist):
            if pr!=None and len(conn[nx])==1:
                return dist
            
            maxRes = dist
            for cand in conn[nx]:
                if cand!=pr:
                    tmp = dfs(conn, nx, cand, dist + 1)
                    if tmp>maxRes:
                        maxRes = tmp
            
            return maxRes
        
        
        maxDist = 0
        for node in conn:
            if len(conn[node])>=2:
                continue
            
            dist = dfs(conn, None, node, 0)
            
            if dist>maxDist:
                maxDist = dist
            
            """
            stack = [[node, 0]]
            visited = set([node])
            
            while len(stack)>0:
                cur, dist = stack.pop()
                
                if dist>maxDist:
                    maxDist = dist
                
                for cand in conn[cur]:
                    if not cand in visited:
                        stack.append([cand, dist + 1])
                        visited.add(cand)
            """
            
        return maxDist
