"""
주소: https://leetcode.com/problems/maximum-number-of-balloon

내용
- 영소문자로 이루어진 문자열이 주어진다
- 이 문자열을 재조합해서 balloon이란 문자열이 몇번 나타날 수 있는지 카운트 하라

예시
Example 1
Input: text = "nlaebolko"
Output: 1

Example 2
Input: text = "loonbalxballpoon"
Output: 2

Example 3
Input: text = "leetcode"
Output: 0

풀이방법
- 단순히 생각해서 balloon에 들어가는 문자중 등장 횟수가 가장 적은만큼이 만들수 있는 횟수가 됨
- 주의해야 할 점은 l과 o가 2번씩 나오니 얘들은 2 나눈 값으로 처리해줘야 함
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCnt = dict()
        
        for c in text:
            if not c in charCnt:
                charCnt[c] = 1
            else:
                charCnt[c] += 1
        
        maxCnt = len(text)
        
        for c in "ban":
            if not c in charCnt:
                return 0
            else:
                maxCnt = min(maxCnt, charCnt[c])
        
        for c in "lo":
            if not c in charCnt:
                return 0
            else:
                maxCnt = min(maxCnt, int(charCnt[c]/2))
        
        return maxCnt
