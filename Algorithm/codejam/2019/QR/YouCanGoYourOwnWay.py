"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

내용
- 어떤 장애물이 하나도 없는 NxN 미로가 있다
- 이 미로에서 이미 나간 경로가 있을때 그 경로랑 하나도 안겹치게 이동하고 싶다.
- 이때 이동은 오른쪽(E), 아래(R) 만 가능하다

샘플
Input
2
2
SE
5
EESSSESE

Output
Case #1: ES
Case #2: SEEESSES

풀이방법
- 기존 경로가 주어지면 E와 S를 반대로만 가면 된다...
- 솔직히 왜냈는지 날 모르겠다...

적용 가능 분야
- ...

"""
T = int(input())

for i in range(T):
    N = int(input())
    P = input()
    
    resStr = ""
    for c in P:
        if c=="E":
            resStr += "S"
        else:
            resStr += "E"
    print("Case #" + str(i+1) + ": " + resStr)
