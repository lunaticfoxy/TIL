"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

내용
- Jamie와 Cameron이 일을 나눠서 하려 한다
- 일들의 시작, 종료 시간이 주어질때 각각의 일을 누가 해야하는지를 J, C로 표시하여 문자열로 반환하라
- 한명은 동시에 한가지 일만 할수있다
- 일을 할 수 없는 경우에는 IMPOSSIBLE을 출력하라

샘플
Input
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

Output
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC


풀이방법
- 처음엔 힙까지 써가면서 복잡하게 했는데 필요 없음
- 그냥 제이미랑 카메룬이 한명씩 이전일 끝났는지 체크
- 중요한점은 리턴할때 시간 순이 아니라 일 순으로 리턴해야 함
"""
def solution(schedules):
    times = []
    res = ""

    schedules = sorted(schedules, key = lambda x: x[1][0]*10000 + x[1][1])

    C = [0, 0]
    J = [0, 0]

    for sc in schedules:
        if C[1] <= sc[1][0]:
            sc[2] = "C"
            C = sc[1]
        elif J[1] <= sc[1][0]:
            sc[2] = "J"
            J = sc[1]
        else:
            return "IMPOSSIBLE"

    schedules = sorted(schedules, key = lambda x: x[0])
    res = "".join([x[2] for x in schedules])

    return res


T = int(input())

for t in range(T):
    N = int(input())
    schedules = [[i, [int(x) for x in input().split()], ""] for i in range(N)]
    res = solution(schedules)
    print("Case #" + str(t+1) + ": " + res)
