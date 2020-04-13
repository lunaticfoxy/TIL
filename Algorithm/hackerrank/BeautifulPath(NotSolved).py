"""
주소: https://www.hackerrank.com/challenges/beautiful-path/problem

내용
- 무방향 가중 엣지로 구성된 그래프가 주어진다
- A 부터 B 까지의 경로의 거리는 사이에 있는 엣지들의 OR 연산으로 계산된다
- 이때 주어진 A, B 사이의 최단 거리를 구하라

샘플
Sample Input
3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3

Sample Output
3


풀이방법
- 단순 다익스트라에 덧셈 대신 OR 연산으로 시도하였으나 실패
- 실패 이유
  - 2 | 5 가
  - (1 | 2) | 4 보다 작을수있다
  - OR 연산은 조합에 따라 결과가 다르게 나올수 있음...
- 그럼 어떻게? 모든 조합을 다 구해서 OR을 수행해야 하나?
- 혹은 비트 단위로 체크가 필요할까?

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPath function below.
def beautifulPath(n, edges, A, B):
    edge_map = dict()

    for edge in edges:
        edge[0] = int(edge[0])
        edge[1] = int(edge[1])
        edge[2] = int(edge[2])
        if not edge[0] in edge_map:
            edge_map[edge[0]] = dict()

        if not edge[1] in edge_map[edge[0]]:
            edge_map[edge[0]][edge[1]] = [edge[2]]
        else:
            edge_map[edge[0]][edge[1]].append(edge[2])
        
        if not edge[1] in edge_map:
            edge_map[edge[1]] = dict()
            
        if not edge[0] in edge_map[edge[1]]:
            edge_map[edge[1]][edge[0]] = [edge[2]]
        else:
            edge_map[edge[1]][edge[0]].append(edge[2])


    dist = [2048 for _ in range(n+1)]
    dist[A] = 0
    
    cands = set([A])

    while len(cands)>0:
        cur = cands.pop()

        if not cur in edge_map:
            continue

        for conn in edge_map[cur]:
            new_dists = [dist[cur]|each_pan for each_pan in edge_map[cur][conn]]
            new_dist = min(new_dists)
            if new_dist < dist[conn]:
                dist[conn] = new_dist
                if not conn in cands:
                    cands.add(conn)
    
    if dist[B]==2048:
        dist[B] = -1
    
    return dist[B]
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(input().rstrip().split())

    AB = input().split()

    A = int(AB[0])

    B = int(AB[1])

    result = beautifulPath(n, edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
