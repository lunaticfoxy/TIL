"""
주소: https://leetcode.com/problems/consecutive-characters/

내용
- 문자열 내에서 연속적으로 같은 문자가 나오는 최대 길이를 구하라

샘플
Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

풀이방법
- 단순 구현
"""
object Solution {
    def maxPower(s: String): Int = {
        
        def recurFunc(s: Array[Char], last: Char, curCnt: Int, maxCnt: Int): Int = {
            if(s.size == 0)
                maxCnt
            else {
                if(last == s(0))
                    recurFunc(s.drop(1), s(0), curCnt + 1, Math.max(curCnt + 1, maxCnt))
                else
                    recurFunc(s.drop(1), s(0), 1, maxCnt)
            }
        }
        
        if(s == "")
            0
        else
            recurFunc(s.toCharArray.drop(1), s.toCharArray.apply(0), 1, 1)
    }
}
