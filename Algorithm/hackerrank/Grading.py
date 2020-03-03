"""
주소: https://www.hackerrank.com/challenges/grading/problem

내용
- 점수를 3점 이내로 올렸을때 5의 배수가 되는 아이들의 점수를 5점 단위로 맞춰주고싶다
- 단 올림해서 40점이 안되는 아이들은 미달이므로 무시한다

샘플
Sample Input 0
4
73
67
38
33

Sample Output 0
75
67
40
33


풀이방법
- 생략
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res = []

    for grade in grades:
        if grade < 38:
            res.append(grade)
        else:
            if grade%5<=2:
                res.append(grade)
            else:
                res.append(grade + 5 - grade%5)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
