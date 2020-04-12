"""
주소: https://www.hackerrank.com/challenges/angry-children/problem
(주소 잘못된거 아님... 주소가 이상한 이름인데 max min 문제 맞음)

내용
- 배열이 주어지고 이중에 k개의 숫자를 뽑아 subarray를 만든다
  - 연속되지 않아도 된다
- 이때 subarray 내의 최대값과 최소값의 차이가 최소인 경우의 차이값을 구하라

샘플
Sample Input 0
7
3
10
100
300
200
1000
20
30

Sample Output 0
20

Sample Input 1
10
4
1
2
3
4
10
20
30
40
100
200

Sample Output 1
3

Sample Input 2
5
2
1
2
1
2
1

Sample Output 2
0


풀이방법
- 복잡해보이지만 사실 윈도우 문제
- 정렬한다음 subarray를 윈도우 단위로 나누어서 맨 뒤 값과 맨 앞 값의 차이를 계속 계산한다
- 그리고 가장 작은 차이값을 리턴

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    min_val = arr[-1]
    for i in range(len(arr)-k+1):
        tmp = arr[i+k-1]-arr[i]
        if tmp < min_val:
            min_val = tmp
    
    return min_val



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
