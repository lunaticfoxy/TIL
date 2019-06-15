"""
주소: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

내용
- 영소문자로 이루어진 문자열이 주어진다
- 이 문자열에서 연속되지 않아도 되는 substring을 만든다 (순서는 바꿀수 없다)
- 이때 모든 문자가 한번씩만 포함되면서 사전순으로 가장 앞에 오는 substring을 찾아라

샘플
Example 1:
Input: "cdadabcc"
Output: "adbc"

Example 2:
Input: "abcd"
Output: "abcd"

Example 3:
Input: "ecbacba"
Output: "eacb"

Example 4:
Input: "leetcode"
Output: "letcod"


풀이방법
- 기본적으로는 사전순이지만 예외적으로 해당 글자가 더 뒤에 나올수 없으면 그 자리에 놔둬야 한다
  - 따라서 해당 글자가 더 뒤에 나올 수 있는지 체크해야 한다
- 체크를 위해 글자별로 마지막 나타나는 지점을 저장한다
- 이후 문자열을 순회한다
  - 이미 들어있는 문자는 패스한다
  - 안들어 있는 문자는 해당 문자를 넣을 위치를 찾는다
    - 기존 문자들을 뒤에서부터 하나씩 체크하면서 새로 넣을 문자보다 큰거면 빼버린다
    - 단 기존 문자가 마지막 지점의 문자일경우는 빼지 않는다
  - 뺄 문자를 다 뺀 뒤에 새로운 문자를 넣는다

"""
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        charLast = dict()
        
        for i, c in enumerate(text):
            charLast[c] = i
        
        stack = []
        stack_set = set()
        
        for i, c in enumerate(text):
            if not c in stack_set:
                while len(stack)>0 and ord(stack[-1])>ord(c) and charLast[stack[-1]]>i:
                    stack_set.remove(stack.pop())
                stack.append(c)
                stack_set.add(c)
        
        return "".join(stack)
