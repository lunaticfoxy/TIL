"""
주소: https://www.hackerrank.com/challenges/beautiful-path/problem

내용
- 내용

샘플



풀이방법


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
