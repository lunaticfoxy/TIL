"""
주소: https://www.hackerrank.com/challenges/electronics-shop/problem

내용
- 일정량의 돈을 들고 키보드와 usb 드라이브를 사려한다
- 키보드와 usb 드라이브를 하나씩 사려 할때 주어진 돈 내에서 가장 크게 쓸수 있는 돈을 구하라

샘플
Sample Input 0
10 2 3
3 1
5 2 8

Sample Output 0
9

Explanation 0
She can buy the  keyboard and the  USB drive for a total cost of .


Sample Input 1
5 1 1
4
5

Sample Output 1
-1

Explanation 1
There is no way to buy one keyboard and one USB drive because , so we print .


풀이방법
- 모든 경우의수를 구하면 O(n*m)
- 하지만 각자 소팅한뒤에 연산하면 O(n*log n + m*log m) 으로 줄일수 있다
- 먼저 각자 오름차순으로 정렬
- 이후 키보드 가격을 앞에서부터 하나씩 확인한다
- 그리고 이전 usb가격부터 하나씩 인덱스를 줄여가면서 키보드가격 + usb가격 <= 주어진돈 이 되는 최대의 usb가격을 찾는다
- 현재 키보드가격 + usb가격이 지금까지 계산한 값보다 커지면 저장한다

"""
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards = sorted(keyboards)
    drives = sorted(drives)

    max_money = -1
    j = len(drives)-1
    for i in range(len(keyboards)):
        remain = b - keyboards[i]
        
        while drives[j] > remain:
            j -= 1
            if j==-1:
                break
    
        if j==-1:
            break
        
        cur = drives[j]+keyboards[i]
        if max_money < cur:
            max_money = cur
    
    return max_money




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
