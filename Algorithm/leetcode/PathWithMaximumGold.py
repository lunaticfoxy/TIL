"""
주소 : https://leetcode.com/problems/path-with-maximum-gold/

내용
- 직사각형 지도가 주어지고 각 위치에는 보물의 가치가 적혀있다
- 가치가 0인 지역은 지날수 없고, 이미 방문한 지점은 돌아갈 수 없을때 보물을 주울수 있는 최대의 가치를 찾아라
- 시작점과 끝점은 아무데나 상관없다

예제
Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

풀이방법
- DFS에 대한 구현문제
- 단 시작점을 모든 경우에 대해 수행하는데 이부분에서 중복이 발생하지 않도록 처리하면 빨라질 수 있을것으로 보인다

"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, cur, visited):
            i = int(cur / len(grid[0]))
            j = cur % len(grid[0])
            
            if grid[i][j] == 0:
                return 0
            
            nextD = []
            
            if i>0 and grid[i-1][j]!=0:
                u = cur - len(grid[0])
                if u not in visited:
                    nextD.append(u)
            
            if i<len(grid)-1 and grid[i+1][j]!=0:
                d = cur + len(grid[0])
                if d not in visited:
                    nextD.append(d)
            
            if j>0 and grid[i][j-1]!=0:
                l = cur - 1
                if l not in visited:
                    nextD.append(l)
            
            if j<len(grid[0])-1 and grid[i][j+1]!=0:
                r = cur + 1
                if r not in visited:
                    nextD.append(r)
            
            reses = [0]
            for dst in nextD:
                newVisited = set(visited)
                newVisited.add(dst)
                reses.append(dfs(grid, dst, newVisited))
            
            return max(reses) + grid[i][j]
    
        maxRes = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    temp = dfs(grid, i*len(grid[0])+j, set([i*len(grid[0])+j]))
                    if temp > maxRes:
                        maxRes = temp
        
        return maxRes
            
