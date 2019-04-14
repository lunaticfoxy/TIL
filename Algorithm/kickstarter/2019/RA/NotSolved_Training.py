"""
주소: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6

내용
- N명의 학생이 주어지고 P명을 골라 팀을 짜야함
- 이때 P명의 학생이 모두 동일한 실력을 가지고 있어야 함
- 트레이너가 1 시간을 소모하면 학생 한명의 실력이 1 늘어남
- 팀을 구성하기 위해 트레이너가 써야하는 시간의 최소값을 구하라

샘플
Input
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7
 	
Output 
Case #1: 14
Case #2: 0
Case #3: 6


풀이과정
- 주의: 해당 문제는 테스트케이스 1번만 통과하고 2번에선 메모리 리밋 (1GB)를 넘은 상태임. 수정 필요
- 일단 직관적으로 생각나는데로 풀었는데 아마 diffs 저장하는 테이블 지우고 직접 계산하면 되지 않을까 예상
  - time complexity는 늘겠지만 실제 연산 시간은 큰 차이 없을것
  - 또는 지금은 학생의 차이를 저장하는데 그냥 답을 저장하면?
    - 아니다 이건 결국 시간 똑같음
- 먼저 학생 실력을 오름차순으로 정렬
- 팀 수가 P일때 diffs 2중 리스트를 만들어 diffs[p][i] 에는 i번째 학생과 p+i+1 번째 위치의 학생의 차이를 저장
- 이후 diffs 리스트를 계산식으로 참조하여 tempSum을 계산하고 제일 작은 값을 저장
  - tempSum = diff[0][2] + diff[1][1] + diff[2][0] 이런 형태
  
적용 가능 분야
- 차이가 가장 작은 부분집합을 찾는 문제
- 데이터가 정렬되어 있거나 정렬할 수 있을때 사용 가능
- 차이가 크게 벌어지는 구간을 찾아 집단을 나눌때 쓸 수 

"""
T = int(input())

for i in range(T):
    N, P = input().split()
    N, P = int(N), int(P)
    S = [int(item) for item in input().split()]
    
    S = sorted(S)
    
    diffs = []
    for p in range(P-1):
        diffs.append([])
    
    for j in range(len(S)-1):
        diffs[0].append(S[j+1] - S[j])
        
    for p in range(1, P-1):
        for j in range(len(diffs[p-1]) - 1):
            diffs[p].append(diffs[p-1][j] + diffs[0][j+p])

    minSum = 9999999999
    
    for j in range(N-P+1):
        tempSum = 0
        
        for p in range(P-1):
            #print("diffs[" + str(p) + "][" + str(j+P-2-p) + "]: " + str(diffs[p][j+P-2-p]))
            tempSum += diffs[p][j+P-2-p]
        
        #print("---" + str(tempSum))
        
        if tempSum < minSum:
            minSum = tempSum
    
    print("Case #" + str(i+1) + ": " + str(minSum))
