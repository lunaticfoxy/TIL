"""
주소: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

내용
- a = 0, b = 1, c = 2, ... 식으로 문자가 숫자로 치환된다
- 단어 3개가 주어지고 이를 숫자로 변환한다
- 이때 firstWord 의 변환 숫자와 secondWord의 변환 숫자의 합이 targetWord의 변환 숫자와 같은지 여부를 리턴하라


예제
Example 1:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.


풀이방법
- 단순구현

"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a_ord = ord('a')
        
        def toInt(word):
            res = 0
            for c in word:
                res = res*10 + (ord(c) - a_ord)
            return res
        
        
        first_int = toInt(firstWord)
        second_int = toInt(secondWord)
        target_int = toInt(targetWord)
        
        return (first_int + second_int) == target_int
