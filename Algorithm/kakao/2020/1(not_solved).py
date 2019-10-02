"""
주소: https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3#

설명
- 문자열을 압축하려 한다
- 이때 동일한 문자집합의 반복 횟수를 기준으로 압축하며 동일한 길이로만 자른다고 가정한다
- 압축시 (반복수)(문자) 형태로 압축되며, 반복수가 1일 경우 기록하지 않는다
  - 2bc4abc => bcbcababababc
  - a2ba => abba
- 맨 앞에서부터 동일한 간격으로 자르며 건너뛰는 문자는 없다
- 동일한 간격으로 자른 뒤 맨 뒤에 남은 문자열은 이어 붙여준다

풀이방법
- 단순 구현문제이므로 패스
- 아마 중간에 경계케이스가 꼬인듯한데 체크해봐야함

"""

def solution(s):
    answer = len(s)
    
    for i in range(1, int(len(s)/2)+1):
        idx = 0
        last = None
        lastCnt = 0
        tempAnswer = 0
        
        while idx+i <= len(s):
            """
            print("-----")
            print(s[idx:idx+i])
            print(last)
            print(lastCnt)
            print(tempAnswer)
            """
            
            if s[idx:idx+i] == last:
                lastCnt += 1
            else:
                if lastCnt == 1:
                    tempAnswer += i
                elif lastCnt > 1:
                    tempAnswer += (i+1)
                lastCnt = 1
                last = s[idx:idx+i]
            idx += i
        
        if lastCnt == 0:
            tempAnswer += i
        elif lastCnt == 1:
            tempAnswer += i
        elif lastCnt > 1:
            tempAnswer += (i+1)
        
        tempAnswer += (len(s)-idx)
        
        if answer==0 or tempAnswer < answer:
            answer = tempAnswer
        
        #print("tempAnswer: " + str(tempAnswer) + " ==================")
        
    return answer
