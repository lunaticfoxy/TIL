"""
################# 타임 리밋에 걸린 문제 ###################

주소: https://leetcode.com/problems/shortest-path-in-binary-matrix/

내용
- 1, 0 으로 이루어진 매트릭스가 주어진다
- 이 매트릭스의 왼쪽 위에서 오른쪽 위까지 0인 값을 따라 이동하고자 한다
- 이동할수 있는 경로의 최단 거리를 구하라
  - 경로가 없을경우 -1을 출력하라


풀이방법
- 이 문제는 아직 타임리밋에 걸려서 해결해야 하는데... 당장 떠오르는 방법이 없어서 임시 저장용
- 일단 가장 단순한 방법은 그래프로 표현한 다음 다익스트라 알고리즘
- connection matrix가 주어졌다고 가정하고 다익스트라 알고리즘을 구현한다
  - 시작점 끝지점은 고정
  - bfs형태로 탐색하면서 거리가 갱신되는 지점을 계속 스택에 넣는 형태
- 그리고 connection matrix를 생성하는 코드를 삽입
  - 모두 False로 놓고 0인 지점에서 주변 8칸을 체크해서 해당하는 지점만 True로 바꾸는 방식
  - 모두 True로 놓고 1인 지점을 모두 False로 바꾸는 방식도 해봤으나 같은 결과
- 알고리즘 자체는 큰 문제가 없는듯 하다... 어디서 시간을 줄일수 있을까...
  - connection matrix를 만들지 않고 바로 grid를 탐색에 사용할 수 있긴 하겠지

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def dijikstra(con_mat):
            last = len(con_mat)-1
            dist = [9999 for _ in range(len(con_mat))]
            dist[0] = 1
            
            stack = [0]
            stack_set = set([0])
            
            while len(stack)>0:
                cur = stack.pop()
                stack_set.remove(cur)
                
                for i in range(len(con_mat)):
                    if i==cur:
                        continue
                        
                    if con_mat[cur][i] and dist[i]>(dist[cur]+1):
                        dist[i] = dist[cur]+1
                        
                        if i not in stack_set and i!=last:
                            stack.append(i)
                            stack_set.add(i)
                #print(dist)
            
            if dist[-1]==9999:
                return -1
            else:
                return dist[-1]
        
        def getIdx(i, j):
            return i*len(grid[0]) + j
        
        con_mat = [[False for _ in range(len(grid)*len(grid[0]))] for _ in range(len(grid)*len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    continue
                
                if i>0 and j>0 and grid[i-1][j-1]==0:
                    con_mat[getIdx(i, j)][getIdx(i-1, j-1)] = True
                    con_mat[getIdx(i-1, j-1)][getIdx(i, j)] = True
                    
                if i>0 and grid[i-1][j]==0:
                    con_mat[getIdx(i, j)][getIdx(i-1, j)] = True
                    con_mat[getIdx(i-1, j)][getIdx(i, j)] = True
                    
                if i>0 and j<len(grid[i])-1 and grid[i-1][j+1]==0:
                    con_mat[getIdx(i, j)][getIdx(i-1, j+1)] = True
                    con_mat[getIdx(i-1, j+1)][getIdx(i, j)] = True
                    
                if j>0 and grid[i][j-1]==0:
                    con_mat[getIdx(i, j)][getIdx(i, j-1)] = True
                    con_mat[getIdx(i, j-1)][getIdx(i, j)] = True
                    
                if j<len(grid[i])-1 and grid[i][j+1]==0:
                    con_mat[getIdx(i, j)][getIdx(i, j+1)] = True
                    con_mat[getIdx(i, j+1)][getIdx(i, j)] = True
                
                if i<len(grid)-1 and j>0 and grid[i+1][j-1]==0:
                    con_mat[getIdx(i, j)][getIdx(i+1, j-1)] = True
                    con_mat[getIdx(i+1, j-1)][getIdx(i, j)] = True
                    
                if i<len(grid)-1 and grid[i+1][j]==0:
                    con_mat[getIdx(i, j)][getIdx(i+1, j)] = True
                    con_mat[getIdx(i+1, j)][getIdx(i, j)] = True
                    
                if i<len(grid)-1 and j<len(grid[i])-1 and grid[i+1][j+1]==0:
                    con_mat[getIdx(i, j)][getIdx(i+1, j+1)] = True
                    con_mat[getIdx(i+1, j+1)][getIdx(i, j)] = True
        
        #print(con_mat)
        
        """
        con_mat = [[True for _ in range(len(grid)*len(grid[0]))] for _ in range(len(grid)*len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    continue
                
                idx = getIdx(i, j)
                for k in range(len(con_mat)):
                    con_mat[idx][k] = False
                    con_mat[k][idx] = False
        """
        
        return dijikstra(con_mat)
                
                
                
                
                
                
                
                
                
                
                
                
