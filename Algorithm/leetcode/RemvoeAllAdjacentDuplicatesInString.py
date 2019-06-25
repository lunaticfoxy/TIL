"""
주소: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

내용
- 문자열이 주어지고 이중에 두개의 연속된 문자는 지울수 있다
- 위 과정을 반복해서 더이상 지울수 없는 문자열을 찾아라

샘플
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

풀이방법
- 연속된 문자를 지우니 스택에 쌓다가 연속된게 나오면 빼버리면 된다

"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        
        for c in S:
            if len(stack)>0 and stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
                
