"""
주소: https://www.hackerrank.com/challenges/kangaroo/problem

내용
- 캥거루 두마리가 뛰어가는데 시작점과 한번에 뛰는 점프거리가 주어진다
- 두 캥거루가 같은 시간에 같은 장소에 있을수 있는지 여부를 구하라

샘플
Sample Input 0
0 3 4 2

Sample Output 0
YES

Sample Input 1
0 2 5 3

Sample Output 1
NO


풀이방법
- 단순 시뮬레이션 문제
- 엣지케이스 걸러내는거만 생각하면 됨
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    elif v1 == v2:
        return  "NO"
    elif v1 > v2:
        if x1 > x2:
            return "NO"
        else:
            case = 0
    else:
        if x2 > x1:
            return "NO"
        else:
            case = 1

    while True:
        x1 += v1
        x2 += v2

        if x1==x2:
            return "YES"
        else:
            if case == 0:
                if x1 > x2:
                    return "NO"
            else:
                if x2 < x1:
                    return "NO"

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
