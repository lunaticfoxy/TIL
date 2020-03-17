"""
주소: https://www.hackerrank.com/challenges/larrys-array/problem

내용
- 1부터 순차 증가하는 값들이 무작위로 배치된 배열이 주어진다
- 해당 배열의 원소는 3개 단위로 회전이 가능하다
- 해당 배열이 회전을 통해 오름차순으로 정렬이 가능한지 여부를 리턴하라

샘플
Sample Input
3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4

Sample Output
YES
YES
NO


풀이방법
- 배열의 길이가 2일때는 무조건 성공
- 배열의 길이가 3일때는 조건에 따라 성공
- 배열의 길이가 3보다 클때는 가장 큰 값을 맨 뒤로 보낸뒤 나머지 값들만 가지고 재귀 수행

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    if len(A)<3:
        return "YES"
    elif len(A)==3:
        if A[0]==1:
            if A[1]==2:
                return "YES"
            else:
                return "NO"
        elif A[0]==2:
            if A[1]==3:
                return "YES"
            else:
                return "NO"
        else:
            if A[1]==1:
                return "YES"
            else:
                return "NO"
    else:
        cur_loc = len(A)-1
        for i in range(len(A)-1):
            if A[i]==len(A):
                cur_loc = i
                break
        
        while cur_loc+2 < len(A):
            temp = A[cur_loc]
            A[cur_loc] = A[cur_loc+1]
            A[cur_loc+1] = A[cur_loc+2]
            A[cur_loc+2] = temp
            cur_loc = cur_loc + 2
        
        if cur_loc+1 < len(A):
            temp = A[cur_loc + 1]
            A[cur_loc + 1] = A[cur_loc]
            A[cur_loc] = A[cur_loc - 1]
            A[cur_loc - 1] = temp
            cur_loc = cur_loc + 1
        
        return larrysArray(A[:len(A)-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
