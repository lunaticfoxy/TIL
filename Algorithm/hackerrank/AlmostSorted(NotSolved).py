"""
주소: https://www.hackerrank.com/challenges/almost-sorted/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    first = []
    end = []
    last = -1

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            if len(first)==0:
                first.append(i)
                first.append(i+1)
            elif first[1]==i:
                first[1]=i+1
            elif len(end)==0:
                if first[1]-first[0]>1:
                    print("no")
                    return
                else:
                    end.append(i)
                    end.append(i+1)
            elif end[1]==i:
                end[1] = i+1
            else:
                print("no")
                return
    
    print("yes")
    if len(end)>0:
        if end[0]

        print("swap " + str(first[0]+1) + " " + str(end[0]+1))
    elif first[1]-first[0]==1:
        print("swap " + str(first[0]+1) + " " + str(first[1]+1))
    else:
        print("reverse " + str(first[0]+1) + " " + str(first[1]+1))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
