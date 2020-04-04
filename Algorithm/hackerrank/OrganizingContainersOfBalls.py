"""
주소: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

내용
- n개의 컨테이너가 있고 n개의 종류의 공이 있다
- x번 공은 x번 컨테이너에 담고 싶다
- 컨테이너 사이의 공 교환은 1:1로만 가능하다
- 컨테이너마다 포함된 종류별 공들의 개수가 주어질 때 모든 공을 각 컨테이너에 담을수 있는지 여부를 리턴하라

예제
Sample Input 1
2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0

Sample Output 1
Impossible
Possible

Sample Input 2
2
2
999336263 998799923
998799923 999763019
4
997612619 934920795 998879231 999926463
960369681 997828120 999792735 979622676
999013654 998634077 997988323 958769423
997409523 999301350 940952923 993020546

Sample Output 2
Possible
Possible


풀이방법
- 어차피 교환은 1:1이니깐 x번 컨테이너 밖에 있는 x번 공의 수와 x번 컨테이너에 들어있는 다른 공의 수가 같으면 교환이 가능하다
- 이때, 꼭 x번 컨테이너가 아니라도 다른 임의의 컨테이너에 들어있는 다른 공의 수와 x번 컨테이너 밖 x번 공의 수가 같아도 된다
- 왜냐하면 일단 한 컨테이너로 공을 몰아 넣는 작업만 수행 끝나면 컨테이너끼리 교환해버리면 되니깐
- 따라서 모든 컨테이너별 공의 합, 공끼리의 합을 계산한다음 둘이 패턴이 같으면 교환 가능하다
- 이때 순서를 고려하지 않기 위해 정렬하고 비교한다
  - 꼭 정렬 아니고 딕셔너리로도 해결 가능한데 당장은 귀찮으니 나중에 고칠거다


"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    ball_nums = []
    cont_nums = []

    for i in range(len(container)):
        ball_nums.append(0)
        cont_nums.append(0)
        for j in range(len(container)):
            ball_nums[i] += container[i][j]
            cont_nums[i] += container[j][i]
    
    ball_nums = sorted(ball_nums)
    cont_nums = sorted(cont_nums)

    for i in range(len(ball_nums)):
        if not cont_nums[i]==ball_nums[i]:
            return "Impossible"

    return "Possible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
