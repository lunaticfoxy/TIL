"""
주소: https://www.hackerrank.com/challenges/mini-max-sum/problem

내용
- 5개의 숫자가 주어지는데
- 4개의 합이 최소, 최대가 되는 값을 출력하라

샘플
Sample Input
1 2 3 4 5

Sample Output
10 14


풀이방법
- 생략...

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_all = sum(arr)
    min_sum = sum_all - max(arr)
    max_sum = sum_all - min(arr)
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
