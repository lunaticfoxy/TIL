"""
주소: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

내용
- 8방향으로 연결된 매트릭스가 주어진다
- 가장 큰 1의 집합의 크기를 찾아라


풀이방법
- 단순 8방향 dfs 문제니 

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):

    max_cnt = 0
    width = 0
    height = len(matrix)
    if height>0:
        width = len(matrix[0])

    visited = set([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i*width + j in visited or matrix[i][j]==0:
                continue
            
            cnt = 1
            stack = [[i,j]]
            visited.add(i*width + j)

            while len(stack)>0:
                cur_i, cur_j = stack.pop()
                
                if cur_i>0:
                    if cur_j>0:
                        if not (cur_i-1)*width+(cur_j-1) in visited and matrix[cur_i-1][cur_j-1]==1:
                            stack.append([cur_i-1, cur_j-1])
                            visited.add((cur_i-1)*width+cur_j-1)
                            cnt += 1

                    if cur_j<width-1:
                        if not (cur_i-1)*width+(cur_j+1) in visited and matrix[cur_i-1][cur_j+1]==1:
                            stack.append([cur_i-1, cur_j+1])
                            visited.add((cur_i-1)*width+cur_j+1)
                            cnt += 1

                    if not (cur_i-1)*width+cur_j in visited and matrix[cur_i-1][cur_j]==1:
                        stack.append([cur_i-1, cur_j])
                        visited.add((cur_i-1)*width + cur_j)
                        cnt += 1
                
                if cur_i<height-1:
                    if cur_j>0:
                        if not (cur_i+1)*width+(cur_j-1) in visited and matrix[cur_i+1][cur_j-1]==1:
                            stack.append([cur_i+1, cur_j-1])
                            visited.add((cur_i+1)*width+cur_j-1)
                            cnt += 1

                    if cur_j<width-1:
                        if not (cur_i+1)*width+(cur_j+1) in visited and matrix[cur_i+1][cur_j+1]==1:
                            stack.append([cur_i+1, cur_j+1])
                            visited.add((cur_i+1)*width+cur_j+1)
                            cnt += 1

                    if not (cur_i+1)*width+cur_j in visited and matrix[cur_i+1][cur_j]==1:
                        stack.append([cur_i+1, cur_j])
                        visited.add((cur_i+1)*width + cur_j)
                        cnt += 1
                        

                if cur_j>0 and not cur_i*width+cur_j-1 in visited and matrix[cur_i][cur_j-1]==1:
                    stack.append([cur_i, cur_j-1])
                    visited.add(cur_i*width+cur_j-1)
                    cnt += 1

                if cur_j<width-1 and not cur_i*width+cur_j+1 in visited and matrix[cur_i][cur_j+1]==1:
                    stack.append([cur_i, cur_j+1])
                    visited.add(cur_i*width+cur_j+1)
                    cnt += 1

            if cnt>max_cnt:
                max_cnt = cnt;
    
    return max_cnt
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
