"""
주소: https://leetcode.com/problems/max-area-of-island/

내용
- 바다는 0, 육지는 1로 표시된 지도가 주어진다
- 이 지도에서 가로-세로로 이어진 육지의 최대 넓이를 구하라

샘플
Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.


풀이방법
- flood fill 문제의 확장형
- 푸는 방법은 동일하다 stack에 쌓아서 너비우선탐색
- 단 시작 지점을 순환하면서 찾고 이미 탐색한 지점은 시작지점이 되지 않도록 체크하는 내용 필요

"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def findArea(i, j):
            #print(str(i) + "," + str(j))
            area = 0
            visit[i][j] = True
            stack = [[i, j]]
            
            while len(stack)>0:
                #print(stack)
                area += 1
                cur = stack.pop()
                
                if cur[0]>0 and (grid[cur[0]-1][cur[1]]==1) and (not visit[cur[0]-1][cur[1]]):
                    #print("#1")
                    visit[cur[0]-1][cur[1]] = True
                    stack.append([cur[0]-1, cur[1]])
                
                if cur[0]<len(grid)-1 and (grid[cur[0]+1][cur[1]]==1) and (not visit[cur[0]+1][cur[1]]):
                    #print("#2")
                    visit[cur[0]+1][cur[1]] = True
                    stack.append([cur[0]+1, cur[1]])
                    
                if cur[1]>0 and (grid[cur[0]][cur[1]-1]==1) and (not visit[cur[0]][cur[1]-1]):
                    #print("#3")
                    visit[cur[0]][cur[1]-1] = True
                    stack.append([cur[0], cur[1]-1])
                
                if cur[1]<len(grid[0])-1 and (grid[cur[0]][cur[1]+1]==1) and (not visit[cur[0]][cur[1]+1]):
                    #print("#4")
                    #print(grid[cur[0]][cur[1]+1])
                    visit[cur[0]][cur[1]+1] = True
                    stack.append([cur[0], cur[1]+1])
                        
            #print(area)
            return area
            
        
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visit[i][j]:
                    area = findArea(i, j)
                    if area>res:
                        res = area
        
        return res
