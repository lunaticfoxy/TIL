"""
주소: https://www.hackerrank.com/challenges/circular-array-rotation/problem

내용
- n개 길이의 어레이를 k만큼 왼쪽 회전시켰다
- q의 위치에 있는 값을 구하라

샘플
Sample Input 0
3 2 3
1 2 3
0
1
2

Sample Output 0
2
3
1


풀이
- 감 익히기용 생략

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    res = []
    k = k%len(a)
    for q in queries:
        res.append(a[q-k])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
