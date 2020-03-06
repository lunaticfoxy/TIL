"""
주소: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

내용
- 리더보드가 주어지고 앨리스가 계속 점수를 낸다
- 이때 각 점수를 낼때마다 앨리스의 리더보드 내 위치를 출력하ㅏ

샘플
Sample Input 1
7
100 100 50 40 40 20 10
4
5 25 50 120

Sample Output 1
6
4
2
1

Sample Input 2
6
100 90 90 80 75 60
5
50 65 77 90 102

Sample Output 2
6
5
4
2
1


풀이방법
- 문제 자체는 단순
- 함정 존재
  - 리더보드에서 중복 점수가 있을경우 같은 순위, 다음은 + n이 아니라 +1이다
  - 중복 제거 한번 필요
- 탐색 시간
  - 단순 앞에서부터 찾으면 쉽지만 타임리밋에 걸린다
  - 바이너리 서치를 변형해서 탐색한다
  - 기본적으론 바이너리 서치와 같지만 정확히 같은게 아니라 들어갈 위치를 찾는것
  - 따라서 mid의 앞뒤를 체크해서 종료 여부를 탐색한다

"""
#!/bin/python3

import math
import os
import random
import re
import sys

def binSearch(arr, item, end):
    start = 0
    #print("item: " + str(item))

    while start <= end:
        mid = int((start + end)/2)
        #print("start: " + str(start) + ", mid: "  + str(mid) + ", end: " + str(end))
        
        if arr[mid] == item:
            #print("mid")
            return mid
        elif arr[mid] > item:
            if mid < len(arr)-1 and arr[mid+1] <= item:
                #print("mid+1")
                return mid+1
            else:
                start = mid+1
        else:
            if mid > 0:
                if arr[mid-1] > item:
                    #print("mid-1 (mid)")
                    return mid
                elif arr[mid-1] == mid:
                    #print("mid-1")
                    return mid-1
                else:
                    end = mid - 1
            else:
                end = mid-1
    return -1


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores_check = []

    for score in scores:
        if len(scores_check)==0:
            scores_check.append(score)
        elif scores_check[-1] != score:
            scores_check.append(score)

    #print(scores_check)

    res = []
    alice_max = 0
    alice_max_idx = len(scores_check)

    for alice_each in alice:
        current_idx = -1
        if alice_max >= alice_each:
            res.append(alice_max_idx + 1)
        elif alice_each>scores_check[0]:
            res.append(1)
            alice_max = alice_each
            alice_max_idx = 0
        else:
            alice_max = alice_each

            current_idx = binSearch(scores_check, alice_each, alice_max_idx-1)
            #print(current_idx)

            if current_idx == -1:
                current_idx = alice_max_idx
            else:
                alice_max_idx = current_idx

            res.append(current_idx + 1)
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
