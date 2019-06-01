"""
주소: https://leetcode.com/problems/unique-morse-code-words/

내용
- 문자 별로 모스코드가 주어진다
- 단어는 모스코드의 연결로 이루어진다
- 이때 여러 단어가 주어지고 나타나는 모스코드의 수를 구하라
  - 서로 다른 단어라도 같은 모스코드로 표현될 수 가능성 존재
  
샘플
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

풀이과정
- 구현문제니 패스
"""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        charAs = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        aOrd = ord('a')
        res = set([])
        for word in words:
            morseWord = ""
            for char in word:
                morseWord += charAs[ord(char) - aOrd]
            
            if not morseWord in res:
                res.add(morseWord)
            
        return len(res)
