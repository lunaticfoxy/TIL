"""
주소: https://leetcode.com/problems/rotting-oranges/

내용
- 오렌지가 grid에 담겨있는데 썩은건 2, 신선한건 1, 빈칸은 0이다
- 썩은 오렌지는 상하좌우로 1분마다 전염된다.
- 몇분뒤에 모든 오렌지가 썩는가? (썩지 않으면 -1)

샘플
Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

풀이방법
- 단순하다 매 분마다 시뮬레이션 수행
- 단 그리드 전체를 볼필요는 없고 fresh한 리스트만 저장해놓고 이것들의 상하좌우 확인
- 그리고 새로운 fresh 리스트와 grid를 만들어서 반복
- 새로운 fresh 리스트와 기존 fresh 리스트의 크기가 같으면 갱신이 안되는 것이므로 -1 리턴


적용가능분야
- 당장 적용할수있는덴 없어보임
- 다만 시뮬레이션 자체는 많이 사용되니 기본기 연습 정도로...

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        freshes = []
        
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item==1:
                    freshes.append([i,j])
        
        
        def checkRotten(grid, roc):
            if roc[0]>0 and grid[roc[0]-1][roc[1]]==2:
                return True
            
            if roc[1]<(len(grid[0])-1) and grid[roc[0]][roc[1]+1]==2:
                return True
            
            if roc[0]<(len(grid)-1) and grid[roc[0]+1][roc[1]]==2:
                return True
            
            if roc[1]>0 and grid[roc[0]][roc[1]-1]==2:
                return True
            
            return False
                    
        
        while len(freshes)>0:
            newFreshes = []
            newGrid = []
            
            for gridLine in grid:
                newGrid.append(list(gridLine))
            
            for fresh in freshes:
                if checkRotten(grid, fresh):
                    newGrid[fresh[0]][fresh[1]] = 2
                else:
                    newFreshes.append(fresh)
            
            if len(newFreshes)==len(freshes):
                return -1
            
            count += 1
            freshes = newFreshes
            grid = newGrid
        
        return count
                
