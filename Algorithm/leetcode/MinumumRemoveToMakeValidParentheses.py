"""
주소: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

내용
- ( 와 )이 0개 이상 포함된 문자열이 주어진다
- 이 문자열에서 최소한의 문자를 삭제하여 ( 와 ) 의 쌍이 맞는 문자열을 만들어라

예시
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


풀이방법
- 다음 두 규칙만 만족하면 된다
  - 문자열을 하나씩 탐색하면서 쌍이 맞지 않는 닫힌 지점 삭제
  - 모든 문자열 탐색 후 남은 열린 지점 삭제
- 위 규칙만 만족하면 단순 구현문제

"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        delList = []
        
        stack = []
        
        for i, c in enumerate(s):
            if c=="(":
                stack.append(i)
            elif c==")":
                if len(stack)==0:
                    delList.append(i)
                else:
                    stack.pop()
        
        for item in stack:
            delList.append(item)
        
        delList = set(delList)
        
        res = ""
        for i, c in enumerate(s):
            if not i in delList:
                res += c
        
        return res
            
            
                
