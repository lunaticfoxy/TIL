"""
주소: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de

내용
- N개의 0 또는 1이 주어지는데 B개의 값이 출력되지 않는다
- 값이 출력되지 않는 부분은 매번 동일하다
- F번의 기회를 줄테니 몇번째 값이 출력되지 않고있는지 맞춰라
- Interactive 문제
  - 내가 출력 신호를 보내면 실제 출력값이 변경되어서 나옴
  - 이를 다시 읽어서 테스트 하는 방식

샘플
Input
3
5 2 4
=> 유저 출력: 01101    # 테스트 시작
111
=> 유저 출력: 00110
010
=> 유저 출력: 01010
100
=> 유저 출력: 11010
100
=> 유저 출력: 0 3     # 정답 제출
1                    # 맞음
2 1 1
=> 유저 출력: 01      # 테스트 시작
1
=> 유저 출력: 1       # 정답 제출
0                    # 틀림

Output


풀이방법
- 해당 문제는 맞았는지 확인되지 않음
  - 샘플은 다 통과하였으나 Interactive 문제라... 제출 방법을 모르겠음...
- 앞에서부터 하나씩 1 인 값과 0인값을 채워나간다고 생각하면 된다
- 먼저 N개의 위치를 모두 확인 불가(-1)로 지정
- 이후 루프를 돌면서 탐색
  - 테스트 할 값 결정
    - 확인 불가한 위치에 순차적으로 0 1 0 1 형태로 출력 => -1 -1 -1 0 -1 이라면 => 0 1 0 0 1 형태
    - 0 (확실히 출력되는 위치) 또는 1 (확실히 출력안되는 위치)이 들어간 지점은 0 출력
  - 이후 출력해서 결과값을 받아오고
  - 출력한 값 (Before) 과 실제나온 값 (After)과 동일한 길이로 각 위치의 값이 뒤로 몇개 남았는지를 배열에 같이 넣는다
    - 1 1 0 0 0 1 0 일경우 => (1,3) (1,2) (0,4) (0,3) (0,2) (1,1), (0,1)
  - 이후 Before의 index를 0으로 두고 After를 앞에서부터 하나씩 스캔한다
    - Before[index] 위치가 확실히 출력 안되는 위치라면 index를 1 증가시키고 After의 위치는 그대로 둔다
    - Before[index] 위치가 확실히 출력 되는 위치라면 index를 1 증가시키고 After의 위치도 하나 이동한다
    - Before[index] 위치가 알수 없는 상태라면
      - 둘이 출력된 값, 남아있는 값이 모두 같으면 현재 위치를 확실히 출력되는 위치(1) 로 표시하고 Before와 After 모두 다음으로 넘어간다
      - 출력된 값만 같으면 Before의 상태를 그대로 두고 Before와 After 모두 다음 값으로 넘어간다
      - 둘이 출력된 값이 다르면 Before의 위치를 확실히 출력 안되는 위치(0) 로 표시하고 Before만 다음으로 넘어간다
    - 이 스캔을 모든 After에 대해 진행한다
- 위 루프를 모든 값이 결정할때까지 돌면 되겠지...


적용 가능 분야
- 매 단계를 돌면서 기존 추론된 정보를 다시 활용한다는 개념
  - 어떻게보면 부스팅이랑 비슷하기도 함...
"""
def getWorks(works, before, after):
    beforeStack = []
    afterStack = []
    bzCnt = 0
    boCnt = 0
    azCnt = 0
    aoCnt = 0
    
    for i in range(len(before)):
        if before[i]==0:
            bzCnt += 1
        else:
            boCnt += 1
    
    for i in range(len(after)):
        if after[i]==0:
            azCnt += 1
        else:
            aoCnt += 1
    
    for i in range(len(before)):
        if before[i]==0:
            beforeStack.append([0, bzCnt])
            bzCnt -= 1
        else:
            beforeStack.append([1, boCnt])
            boCnt -= 1

    for i in range(len(after)):
        if after[i]==0:
            afterStack.append([0, azCnt])
            azCnt -= 1
        else:
            afterStack.append([1, aoCnt])
            aoCnt -= 1
    
    bIdx = 0
    
    #print(beforeStack)
    #print(afterStack)
    for i in range(len(afterStack)):
        while bIdx<len(works):
            #print(str(afterStack[i]) + " => " + str(beforeStack[bIdx]))
            if works[bIdx]==0:
                bIdx +=1
            elif works[bIdx]==1:
                bIdx +=1
                break
            else:
                if afterStack[i][0]==beforeStack[bIdx][0]:
                    if afterStack[i][1]==beforeStack[bIdx][1]:
                        works[bIdx] = 1
                    bIdx += 1
                    break
                else:
                    works[bIdx] = 0
                    bIdx += 1
    
    while bIdx<len(works):
        works[bIdx] = 0
    
    return works

def makeTestSet(works):
    testSet = []
    isOne = True
    
    for i in range(len(works)):
        if works[i]==-1:
            if isOne:
                testSet.append(1)
                isOne = False
            else:
                testSet.append(0)
                isOne = True
        else:
            testSet.append(0)
    
    return testSet

"""
def test(before):
    return [before[1],before[2],before[4]]
print("start")
works = [-1,-1,-1,-1,-1]
for _ in range(10):
    before = makeTestSet(works)
    after = test(before)
    works = getWorks(works, before, after)
    print(before)
    print(after)
    print(works)
    print("-----------------")
"""
import sys
T = int(input())

for t in range(T):
    n, b, f = [int(item) for item in input().split()]
    dummy = "".join(["0" for _ in range(n)])
    works = [-1 for _ in range(n)]

    for _ in range(f):
        if -1 in works:
            before = makeTestSet(works)
            before_str = [str(item) for item in before]
            print("".join(before_str))
            sys.stdout.flush()
            after = [int(item) for item in list(input())]
            works = getWorks(works, before, after)
        else:
            print(dummy)
            sys.stdout.flush()
            after = [int(item) for item in list(input())]
    
    answer = []

    for i in range(len(works)):
        if works[i]==0:
            answer.append(i)
    
    answer_str = [str(item) for item in answer]
    print(" ".join(answer_str))
    sys.stdout.flush()
    verdict = int(input())
exit(0)
