"""
주소: https://leetcode.com/problems/valid-sudoku/

내용
- 주어진 스도쿠가 valid 한지 여부를 체크하라

예제
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

풀이방법
- 단순구현
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkCol(col):
            exist = set([])
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in exist:
                    return False
                else:
                    exist.add(board[i][col])
            return True
        
        def checkRow(row):
            exist = set([])
            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in exist:
                    return False
                else:
                    exist.add(board[row][i])
            return True
                    
        def checkRect(start_i, start_j):
            exist = set([])
            for i in range(start_i, start_i + 3):
                for j in range(start_j, start_j + 3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in exist:
                        return False
                    else:
                        exist.add(board[i][j])
            return True
        
        for i in range(9):
            if not checkCol(i):
                return False
            elif not checkRow(i):
                return False
        
        for i in range(3):
            for j in range(3):
                if not checkRect(i*3, j*3):
                    return False
        
        return True
