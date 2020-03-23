"""
주소: https://www.hackerrank.com/challenges/drawing-book/problem

내용
- 첫장이 0-1 페이지로 구성된 책이 있다
- 이 책의 페이지수와 찾으려고 하는 페이지가 주어진다
- 책을 맨 앞에서 뒤로 넘기거나, 맨 뒤에서 앞으로 넘겨서 찾으려고 하는 페이지까지 도달하는데 걸리는 페이지 넘김 횟수를 구하라

예제
Sample Input 0
6
2

Sample Output 0
1

Sample Input 1
5
4

Sample Output 1
0


풀이방법
- 단순 구현이니 생략
"""
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n%2==0:
        n += 1

    cnt_f = int(p/2)
    cnt_b = int((n-p)/2)

    return min(cnt_f, cnt_b)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
