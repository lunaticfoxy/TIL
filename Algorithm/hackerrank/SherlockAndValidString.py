"""
주소: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

내용
- 문자열 내의 모든 문자가 동일한 횟수로 나타나는 경우를 valid string 이라 한다
- 이때 문자열 내의 한개 문자를 삭제해서 valid string으로 만들수도 있다
- 문자열이 valid string인지 여부를 리턴하라

샘플
Sample Input 0
aabbcd

Sample Output 0
NO

Sample Input 1
aabbccddeefghi

Sample Output 1
NO

Explanation 1
Frequency counts for the letters are as follows:
{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}


Sample Input 2
abcdefghhgfedecba

Sample Output 2
YES


풀이방법
- 푸는 방법 자체는 단순
- 문자 개수를 카운트한뒤 카운트 한 값들이 몇개 그룹으로 나오는지 저장한다
- 1개 그룹이라면 바로 valid
- 3개 이상 그룹이라면 바로 invalid
- 2개 그룹이라면 다음 케이스를 체크한다
  - 첫번째 그룹의 카운트가 1이고 1개가 속한 경우 => 1개 문자를 삭제하여 그룹 하나 없앨 수 있음
  - 두번째 그룹의 카운트가 첫번째 그룹 + 1이고 1개가 속한경우 => 1개 문자를 삭제하여 두 그룹을 합칠 수 있음


"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if len(s)<=1:
        return "YES"

    chars = dict()
    charNums = dict()

    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    maxCnt = -1
    minCnt = len(s)
    for c in chars:
        if chars[c] in charNums:
            charNums[chars[c]].append(c)
        else:
            charNums[chars[c]] = [c]
        
        if maxCnt < chars[c]:
            maxCnt = chars[c]
        
        if minCnt > chars[c]:
            minCnt = chars[c]

    if len(charNums)>=3:
        return "NO"
    elif len(charNums)==2:
        if len(charNums[maxCnt])==1 and (maxCnt-1 in charNums):
            return "YES"
        elif len(charNums[minCnt])==1 and minCnt==1:
            return "YES"
        else:
            return "NO"
    else:
        return "YES"

    
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
