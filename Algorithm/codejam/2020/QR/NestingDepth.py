"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

내용
- 9이하의 digit 으로 이루어진 문자열 배열이 들어온다
- 각 숫자가 자기 자신 만큼의 괄호 depth 에 들어가는 최소의 문자열로 바꾸어라

샘플
Input
4
0000
101
111000
1

Output
Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)

풀이방법
- 단순 구현문제
"""
def solution(s):
    depth = 0

    res = ""
    for c in s:
        cur_num = int(c)
        while cur_num > depth:
            res += "("
            depth += 1
        
        while cur_num < depth:
            res += ")"
            depth -= 1
        
        res += c
    
    while depth > 0:
        res += ")"
        depth -= 1
    
    return res

T = int(input())

for t in range(T):
    res = solution(input().replace("\n",""))
    print("Case #" + str(t+1) + ": " + res)
