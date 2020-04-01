"""
주소: https://www.hackerrank.com/challenges/migratory-birds/problem

내용
- 가장 많이 나타난 새 종류를 출력하라
- 나타난 횟수가 같으면 번호가 작은 새를 출력하라

풀이방법
- 워밍업 문제

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds_cnt = dict()

    for bird in arr:
        if bird in birds_cnt:
            birds_cnt[bird] += 1
        else:
            birds_cnt[bird] = 1
    
    max_cnt = 0
    max_type = -1
    for bird in birds_cnt:
        if birds_cnt[bird]>max_cnt:
            max_cnt = birds_cnt[bird]
            max_type = bird
        elif birds_cnt[bird]==max_cnt and max_type>bird:
            max_type = bird
            
    
    return max_type



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
