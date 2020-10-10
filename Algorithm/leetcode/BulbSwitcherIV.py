"""
주소: https://leetcode.com/problems/bulb-switcher-iv/

내용
- 0과 1로 이루어진 문자열이 있다
- 이 문자열의 한 지점부터 이후 모두를 flip 할 수 있다
- 시작이 0000...00 이라 할때 주어진 문자열을 만들기 위한 최소한의 flip 횟수를 구하라

예제
Example 1:
Input: target = "10111"
Output: 3
Explanation: Initial configuration "00000".
flip from the third bulb:  "00000" -> "00111"
flip from the first bulb:  "00111" -> "11000"
flip from the second bulb:  "11000" -> "10111"
We need at least 3 flip operations to form target.

Example 2:
Input: target = "101"
Output: 3
Explanation: "000" -> "111" -> "100" -> "101".

Example 3:
Input: target = "00000"
Output: 0

Example 4:
Input: target = "001011101"
Output: 5


풀이방법
- 앞에서부터 하나씩 순회하며 값이 바뀌는 지점을 센다
- 이때 초기값은 0이라 가정하고 센다
"""
class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        last = "0"
        for t in target:
            if t != last:
                cnt += 1
                last = t
        
        return cnt
