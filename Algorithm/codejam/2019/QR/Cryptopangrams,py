"""
#### 2개의 테스트 셋 중 1개만 정답처리 (나머지 1개는 TLE)

주소: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

내용
- 소수를 26개 알파벳 대문자와 1:1로 치환한 암호가 있다
  - 소수는 오름차순으로 알파벳과 매칭된다
    - a < b < c ... 란 이야기
  - 소수의 최대크기는 N이다
- 알파벳으로만 이루어진 문장은 다음 규칙으로 암호로 변환된다
  - 알파벳이 소수로 치환된다
  - n번째 알파벳 치환값*n+1번째 알파벳 치환값 을 계산한다
  - 위 결과값들을 리스트에 넣는다
    - [1번째*2번째, 2번째*3번째, 3번째*4번째, ...]
  - 문장은 최소 26글자이다 => 암호 리스트 길이는 최소 25
- 암호에서 원래 문자를 찾아내라

샘플
Input
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

Output
Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ


풀이
- 먼저 가능한 모든 소수 리스트를 만들어서 저장해둠
  - 이부분이 2차 테스트셋에서 통과 안됨
  - 리스트 크기가 작아서 or TLE이깐 다른 문제일지도
- 맨 처음 암호에서 소수의 곱을 찾아낸다
- 처음에 찾은 소수의 곱 원소중 두번째 암호와 나누어 떨어지는 값을 2번째로, 다른 값을 1번째로 가지는 변환 리스트를 만든다
- 나머지 리스트를 순회하며 변환 리스트의 마지막 값과 나눈 몫을 계산해서 새로 변환 리스트에 넣는다
- 나타나는 값 중 새로운게 있으면 별도 set에 저장한다
- 혹시 이상한 결과가 나오면 다시 처음으로 돌아가 소수의 곱을 찾는다
  - 이부분이 조금 잘못된것 같긴 함
  - 원래는 이상한 결과가 나올 수 없음
- set에 있는 값들을 오름차순으로 정렬하여 알파벳과 매칭시킨다
- 변환 리스트를 알파벳으로 치환한다

실제 적용할 수 있는 부분
- 소수를 미리 생성해서 저장해놓고 사용하는 DP개념
- 여기서 나타나는 변환 과정 자체를 Hashing에 사용해도 무방할듯
  - 두 리스트를 비교할때 연속되는 두 값이 같은지만 비교하려면 이러면 정보가 뭉개지면서 해결될수 있을듯
  - 예시
    - [5, 1, 3, 6, 8] => [5, 3, 18, 48]
    - [1, 3, 8, 5, 3, 6] => [3, 24, 40, 15, 18]
    - 두군데가 같다는걸 확인 가능하면서 원래 정보는 확인 불가능
"""
def F(t, N, L, codeList, primeSet):
    if L<=0:
        print("Case #" + str(t+1) + ": ")
        return
    
    for val in range(2, N+1):
        isDone = False
        if codeList[0]%val == 0 and val in primeSet and int(codeList[0]/val) in primeSet and int(codeList[0]/val) <= N:
            val1 = val
            val2 = int(codeList[0]/val)
            isDone = True
            plists = []
            last = -1
            
            if codeList[1]%val1==0:
                plists.append(val2)
                plists.append(val1)
            else:
                plists.append(val1)
                plists.append(val2)
            plistsSet = set(plists)

            last = plists[-1]
            for i in range(1, len(codeList)):
                newPrime = int(codeList[i]/last)
                
                if not newPrime in plistsSet:
                    plistsSet.add(newPrime)
                
                plists.append(newPrime)
                last = newPrime

                if last<2 or last>N or len(plistsSet)>26:
                    isDone = False
                    break
            if isDone:
                break
    
    if not isDone:
      a = 5/0      # 디버깅을 위해 강제 에러 발생시키는 부분

    sortedList = sorted(list(plistsSet))
    keyMap = dict()
    
    for i, prime in enumerate(sortedList):
        keyMap[prime] = chr(ord("A") + i)

    resStr = ""
    
    for pItem in plists:
        resStr += keyMap[pItem]
    
    print("Case #" + str(t+1) + ": " + resStr)

primes = [2, 3]

for i in range(5, 10001, 2):
    isPrime = True
    for j in range(2, i):
        if i%j==0:
            isPrime = False
            break
    if isPrime:
      primes.append(i)

primeSet = set(primes)

T = int(input())

for t in range(T):
    N, L = input().split()
    N, L = int(N), int(L)
    codeList = [int(item) for item in input().split()]
    F(t, N, L, codeList, primeSet)
