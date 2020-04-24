"""
주소: https://leetcode.com/problems/find-all-good-strings/

내용
- 같은 길이의 문자열 2개와 evil 문자열이 주어진다
  - 2번 문자열은 항상 1번 문자열보다 사전순으로 크다
- evil 문자열을 substring으로 포함하지 않는 문자열을 good string 이라 부른다
- 1번 문자열과 2번 문자열 사이에 있는 문자열 중 good string의 개수를 리턴하라
  - 1번 문자열, 2번 문자열도 포함한다
  
  
샘플
Example 1:
Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 

Example 2:
Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

Example 3:
Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2

풀이방법
- 재귀 시도
  - scala로 먼저 시도시 재귀에서 타임리밋 발생
  - 파이썬으로 시도시에도 재귀 맥시멈 발생
  - 재귀는 현실적으로 불가능해보임
- 반복 시도
  - 얘도 타임리밋 발생
  - 아무래도 모든 경우의수 따지면 안되는것으로 보임
- 예측 시도
  - 생각해보면 예측이 가능
  - [aaaa, cccc] 사이에 ee 가 나타나는 경우는
    - aaee, abee, ..., azee, aeea, aeeb, ... ,aeez, baee, bbee, bcee, ..., cbee
    - 요걸 체크하는 로직만 만들면 될듯함

"""
# 재귀로 구성한 코드
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def findGoodStringsRecur(s1: str, s2: str, evil: str, retVal: int) -> int:
            def findNextString(s: str) -> str:
                if len(s) == 0:
                    return []
                
                if s[-1] == "z":
                    return findNextString(s[:len(s)-1]) + "a"
                else:
                    newS = s[:len(s)-1] + str(chr(ord(s[-1])+1))
                    return newS
            

            if s1 == s2:
                if evil in s1:
                    return retVal
                else:
                    return retVal + 1
            
            if evil in s1:
                return findGoodStringsRecur(findNextString(s1), s2, evil, retVal)
            else:
                return findGoodStringsRecur(findNextString(s1), s2, evil, retVal + 1)
    
        
        return findGoodStringsRecur(s1, s2, evil, 0)


# 반복문으로 시도
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def findNextString(s: str) -> str:
            if len(s) == 0:
                return s
                
            sList = list(s)
                
            for i in range(1, len(s)+1):
                if sList[-i] == "z":
                    sList[-i] = "a"
                else:
                    sList[-i] = str(chr(ord(sList[-i]) + 1))
                    break
                
            return "".join(sList)
        
        cnt = 0
        
        if not evil in s1:
            cnt += 1
            
        while s1 != s2:
            s1 = findNextString(s1)
            if not evil in s1:
                cnt += 1
            
        return cnt

      
### 예측으로 푸는중
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        
        def findGoodStringUpper(s1:str, evil:str) -> int:
            all_str = 26**len(s1)
            evil_str = 26**(len(s1) - len(evil))
            
            
            
            return all_str - evil_str
        
        if evil in s1:
            add = 1
        else:
            add = 0
        
        return findGoodStringUpper(s2) - findGoodStringUpper(s1) + add
    
