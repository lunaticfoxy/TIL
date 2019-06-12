"""
주소: https://leetcode.com/problems/occurrences-after-bigram/

내용
- 문장과 두개의 단어 first, second가 주어진다
- 문장 내에서 [first second third] 형태로 나타나는 모든 third를 구하라
  - 중복이 허용된다

샘플
Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


풀이방법
- 단순 매칭 구현문제

"""
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        splited = text.split()
        
        for i in range(len(splited)-2):
            if splited[i]==first and splited[i+1]==second:
                res.append(splited[i+2])
        
        return res
