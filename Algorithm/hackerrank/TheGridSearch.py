"""
주소: https://www.hackerrank.com/challenges/the-grid-search/problem

내용
- 숫자 행렬이 두개 주어진다
- 1번 행렬 안에 2번 행렬이 포함되어 있는지 여부를 체크하고 리턴하라

샘플
Sample Input
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99

Sample Output
YES
NO


풀이방법
- 일일히 매칭하면 귀찮으니... 잘 만들어두신 string의 find를 사용하자
- 1번 행렬을 앞에서부터 탐색하면서 2번 행렬의 첫줄이 포함되어 있는 열을 찾는다
- 발견하면 1번행렬의 다음 줄로 넘어가서 동일한 위치에 2번행렬의 다음 줄이 있는지 비교한다
- 모든 줄이 있다면 YES 리턴, 아니면 계속 진행한다
- 마지막까지 YES가 리턴되지 않았으면 NO를 리턴한다

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    strG = [''.join(g) for g in G]
    strP = [''.join(p) for p in P]

    for i in range(len(strG) - len(strP) + 1):
        loc = -1
        while True:
            loc = strG[i].find(strP[0], loc+1)
            #print(loc)
            if loc == -1:
                break

            failure = False
            for j in range(1, len(strP)):
                if strG[i+j].find(strP[j], loc)!=loc:
                    failure = True
                    break
                
            if not failure:
                return "YES"
    
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
