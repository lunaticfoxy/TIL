"""
주소: https://www.hackerrank.com/challenges/3d-surface-area/problem

내용
- 직사각형 바닥내에 높이를 가지는 3차원 그래프의 높이가 주어진다
- 이 그래프는 3차원 히스토그램으로 형태이다
- 이 그래프의 표면적을 구하라

예제
Sample Input 0
1 1
1

Sample Output 0
6


Sample Input 1
3 3
1 3 4
2 2 3
1 2 4

Sample Output 1
60



풀이방법
- 바닥, 윗면
  - 둘 다 같은 값을 가짐
  - 전체 직사각형 넓이 - 0인 지점의 수
- 옆면
  - 각 칸마다 네 귀퉁이를 비교한다
  - 모서리일 경우: 높이
  - 모서리가 아니면서 옆 칸보다 높을 경우: 옆 칸과의 차이
  - 모서리가 아니면서 옆 칸보다 낮거나 같을 경우: 0


"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    z_cnt = 0
    surface = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==0:
                z_cnt += 1
                continue

            if i==0:
                surface += A[i][j]
            elif A[i][j] > A[i-1][j]:
                surface += A[i][j] - A[i-1][j]
                
            if j==0:
                surface += A[i][j]
            elif A[i][j] > A[i][j-1]:
                surface += A[i][j] - A[i][j-1]

            if i==len(A)-1:
                surface += A[i][j]
            elif A[i][j] > A[i+1][j]:
                surface += A[i][j] - A[i+1][j]
            
            if j==len(A[i])-1:
                surface += A[i][j]
            elif A[i][j] > A[i][j+1]:
                surface += A[i][j] - A[i][j+1]
    
    return surface + 2*(len(A)*len(A[0])-z_cnt)
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
