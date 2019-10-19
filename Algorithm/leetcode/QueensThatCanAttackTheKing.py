"""
주소: https://leetcode.com/problems/queens-that-can-attack-the-king/

내용
- 8x8 체스판 안에 킹 하나와 퀸 여러개가 주어진다
- 킹을 공격할 수 있는 퀸의 리스트를 리턴하라

예제
Example 1:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

풀이방법
- 단순 구현문제이므로 생략
"""
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        cands = [-1 for _ in range(8)]
        
        for i, queen in enumerate(queens):
            diff = [king[0] - queen[0], king[1] - queen[1]]
            
            if diff[0]==0:
                if diff[1] > 0:
                    if cands[0]==-1 or queens[cands[0]][1]<queen[1]:
                        cands[0] = i
                else:
                    if cands[1]==-1 or queens[cands[1]][1]>queen[1]:
                        cands[1] = i
            elif diff[1]==0:
                if diff[0] > 0:
                    if cands[2]==-1 or queens[cands[2]][0]<queen[0]:
                        cands[2] = i
                else:
                    if cands[3]==-1 or queens[cands[3]][0]>queen[0]:
                        cands[3] = i
            elif diff[0]==diff[1]:
                if diff[0] > 0:
                    if cands[4]==-1 or queens[cands[4]][1]<queen[1]:
                        cands[4] = i
                else:
                    if cands[5]==-1 or queens[cands[5]][1]>queen[1]:
                        cands[5] = i
            elif diff[0]==-diff[1]:
                if diff[0] > 0:
                    if cands[6]==-1 or queens[cands[6]][1]>queen[1]:
                        cands[6] = i
                else:
                    if cands[7]==-1 or queens[cands[7]][1]<queen[1]:
                        cands[7] = i
        
        res = []
        for i in cands:
            if i!=-1:
                res.append(queens[i])
                    
        return res
