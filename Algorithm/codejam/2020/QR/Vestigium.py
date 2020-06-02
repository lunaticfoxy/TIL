"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

내용
- 가로 세로 길이가 같은 행렬이 주어진다
- 이 행렬의 대각선 합, 중복되는 원소를 가진 row의 수, 중복되는 원소를 가진 col의 수를 각각 계산하라

샘플
Input
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

Output
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2

  
풀이방법
- 단순 구현 문제
"""
from collections import Counter

def solution(mat):
    sum_val = sum([mat[i][i] for i in range(len(mat))])
    row_val = len([x for x in [len([v for v in Counter(mat[i]).values() if v > 1]) for i in range(len(mat))] if x > 0])
    col_val = len([x for x in [len([v for v in Counter([mat[j][i] for j in range(len(mat))]).values() if v > 1]) for i in range(len(mat))] if x > 0])

    return sum_val, row_val, col_val

T = int(input())

for t in range(T):
    N = int(input())
    mat = [[int(x) for x in input().split()] for _ in range(N)]

    sum_val, row_val, col_val = solution(mat)

    print("Case #" + str(t+1) + ": " + str(sum_val) + " " + str(row_val) + " " + str(col_val))
    
