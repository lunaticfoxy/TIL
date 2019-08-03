"""
주소: https://leetcode.com/problems/longest-common-subsequence/

내용
- 두 문자열 사이의 최대 커먼 서브시퀀스를 찾아라

샘플
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3 
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

풀이방법
- 행렬을 만들어 비교한다
  - 에딧 디스턴스 구하는것과 비슷하게

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            a = text2
            b = text1
        else:
            a = text1
            b = text2
        
        mat = [[0 for _ in range(len(a)+1)]]
        
        for i in range(1, len(b)+1):
            mat.append([0])
            for j in range(1, len(a)+1):
                if a[j-1]==b[i-1]:
                    mat[-1].append(max(mat[-2][j-1]+1, mat[-2][j], mat[-1][j-1]))
                else:
                    mat[-1].append(max(mat[-2][j], mat[-1][j-1]))
        
        return mat[-1][-1]
