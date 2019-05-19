"""
주소: https://leetcode.com/problems/champagne-tower/

내용
- 맨 위에는 잔 1개, 그 밑에는 잔 2개, 3개, ..., 100개 까지 쌓여진 탑이 있다.
- 위에서부터 샴페인을 부으면 반씩 나눠서 아래로 계속 흘러간다
- 샴페인을 부은 양과 잔의 좌표가 주어졌을때 해닽 잔에 차있는 샴페인의 양을 구해라


샘플
Example 1:
Input: poured = 1, query_glass = 1, query_row = 1
Output: 0.0
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_glass = 1, query_row = 1
Output: 0.5
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.


풀이방법
- 이전
  - 아직 못푼 문제... 분명 간단해보이는데 정작 구현하려니깐 어떤식으로 해야될지 모르겠네...
  - 일단 제일 단순하게 재귀로...
  - 단순히 한 잔마다 2개씩 나눠지는 형태로 계산함
- 수정
  - 위 방법을 그대로 다이나믹으로 변경
  - 단 기존에는 dfs였다면 이번에는 bfs로 한 단계씩 각 유리잔에 들어갈 값을 계산하는 형태로 함
  - 위에서 잔에 붓고 남은걸 다시 아래 레이어에 반씩 넘겨주는 형태
  - 풀리긴 했는데... 속도가 매우 느림... 타임리밋 아슬아슬하게 걸린 느낌?
  - 추후 개선해봐야함

"""
from collections import deque 

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0 for _ in range(i+1)] for i in range(100)]
        
        """
        def fillTower(poured, row, glass):
            tower[row][glass] += poured
            
            remained = 0.0
            if tower[row][glass]>1.0:
                remained = tower[row][glass] - 1.0
                tower[row][glass] = 1.0
            
            #print("----" + str(poured) + "," + str(row) + "," + str(glass) + "---")
            #print(tower[:4])
            
            if remained>0:
                fillTower(remained/2.0, row+1, glass)
                fillTower(remained/2.0, row+1, glass+1)
            
        fillTower(poured, 0, 0)
        """
        
        eachPoured = [poured]
        for i in range(100):
            newEach = [0.0 for _ in range(i+2)]
            cnt = 0
            for j in range(i+1):
                tower[i][j] += eachPoured[j]
                
                if tower[i][j]>1.0:
                    remained = tower[i][j] - 1.0
                    tower[i][j] = 1.0
                    newEach[j] += remained/2.0
                    newEach[j+1] += remained/2.0
                    cnt += 1
            
            if cnt==0:
                break
                
            eachPoured = newEach
        
        return tower[query_row][query_glass]
