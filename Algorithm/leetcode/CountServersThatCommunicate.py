"""
주소: https://leetcode.com/problems/count-servers-that-communicate/

내용
- 서버들이 2차원 grid 형태의 망에 붙어있고, 한 서버는 자기와 직선으로 연결된 서버만 통신할 수 있다
- 서버끼리 중계가 가능할때 다른 서버와 통신이 가능한 서버의 수를 구하라

예제
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


풀이방법
- 단순 그래프에서 크기가 2 이상인 집합을 찾는 문제다
- 그래프로 만들어서 풀면 더 빠르겠지만 일단 메모리 덜쓰게 (귀찮아서)
- 한 집합을 포함하는 row와 col의 set으로 표현하고
- 집합끼리 전부 비교하며 겹쳐지는건 합친다
- 이후 집합 크기가 2 이상인거들의 크기를 합쳐서 리턴
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def compareTwoGrid(grid1, grid2):
            for r in grid1[0]:
                if r in grid2[0]:
                    return True
            
            for c in grid1[1]:
                if c in grid2[1]:
                    return True
            
            return False
        
        
        def reduceGrid(grids):
            if len(grids)<=1:
                return grids
            
            retry = True
            while retry:
                retry = False
                for i in range(0, len(grids)-1):
                    for j in range(i+1, len(grids)):
                        if compareTwoGrid(grids[i], grids[j]):
                            grids[i][0] = grids[i][0] | grids[j][0]
                            grids[i][1] = grids[i][1] | grids[j][1]
                            grids[i][2] += grids[j][2]
                            del grids[j]
                            retry = True
                            break
                    if retry:
                        break
            
            return grids
    
        grids = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    grids.append([set([i]), set([j]), 1])

        reduced = reduceGrid(grids)
        
        res = 0
        for each in reduced:
            print(each)
            if each[2]>1:
                res += each[2]
        
        return res
