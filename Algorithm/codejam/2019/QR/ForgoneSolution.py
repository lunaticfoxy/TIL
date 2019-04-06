"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

설명
- 최소 1개의 자리가 4로 이루어진 숫자 N이 들어온다
- 이때 4를 포함하지 않고 합이 N이되는 자연수 A, B를 구하라

샘플
Input
3
4
940
4444

Output  
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777

풀이과정
- 일단 자연수니 모두 1 이상이어야 하므로 A를 1로 주고 시작
- 그리고 N에서는 1을 빼줘서 합을 일정하게 맞춰줌
- 이후 루프를 돌면서
  - N의 맨 아래자리가 4인지 체크하고 맞으면 A의 해당 자리에 1을 더해줌
  - 그리고 N에 10을 나눠주고 N>0 일때까지 루프를 반복
- 마지막에 A와 처음 나온 N을 어디 저장해놨다가 N-A를 해주면 결과 확인 가능

적용 가능한곳
- 어렵진 않지만 1을 빼주고 시작해야 된다는 점에서 엣지 케이스를 
"""
C = int(input())
    
for i in range(C):
    N = int(input())
    A = 1
    B = N
    N -= 1
    
    pad = 1
    while N>0:
        temp = 0
        if N%10==4:
            temp = 1
        
        A += pad*temp
        
        N = int(N/10)
        pad *= 10
    
    B -= A
    print("Case #" + str(i+1) + ": " + str(A) + " " + str(B))
