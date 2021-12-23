"""
주소: https://leetcode.com/problems/largest-substring-between-two-equal-characters/

내용
- 소문자 알파벳으로 이루어진 문자열이 주어진다
- 이 문자열 내에 같은 문자 사이의 가장 큰 거리를 구하라


예제
Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Example 4:
Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".


풀이방법
- 단순 구현
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c_first = dict()
        max_length = -1
        
        for i, c in enumerate(s):
            if c in c_first:
                cur_length = (i - c_first[c] - 1)
                max_length = max(cur_length, max_length)
            else:   
                c_first[c] = i
                
        return max_length
