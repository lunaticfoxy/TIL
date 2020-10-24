"""
주소: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

내용
- 최대 괄호 깊이 탐색

예제
Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Example 3:
Input: s = "1+(2*3)/(2-1)"
Output: 1

Example 4:
Input: s = "1"
Output: 0


풀이방법
- 스택을 활용한 단순 구현

"""
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth : int = 0
        stack: list[str] = []
            
        for c in s:
            if c == "(":
                stack.append(c)
                max_depth = max(len(stack), max_depth)
            elif c == ")":
                stack.pop()
        
        return max_depth
