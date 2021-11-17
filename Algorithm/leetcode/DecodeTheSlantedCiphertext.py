"""
주소: https://leetcode.com/problems/decode-the-slanted-ciphertext/

내용
- 어떤 문장을 2차원 배열로 암호화한뒤 한 문장으로 다시 이어놓았다
- 암호화는 [n, m] 번째의 다음 문자가 [n+1, m+1] 에 존재하는 식으로 구성했다
- 암호화된 문장과 2차원 배열의 길이가 주어질 때 원문을 구하라
- 단, 맨 마지막에 이어지는 공백은 없다고 가정한다

예제
Example 1:
Input: encodedText = "ch   ie   pr", rows = 3
Output: "cipher"
Explanation: This is the same example described in the problem description.


Example 2:
Input: encodedText = "iveo    eed   l te   olc", rows = 4
Output: "i love leetcode"
Explanation: The figure above denotes the matrix that was used to encode originalText. 
The blue arrows show how we can find originalText from encodedText.


Example 3:
Input: encodedText = "coding", rows = 1
Output: "coding"
Explanation: Since there is only 1 row, both originalText and encodedText are the same.


Example 4:
Input: encodedText = " b  ac", rows = 2
Output: " abc"
Explanation: originalText cannot have trailing spaces, but it may be preceded by one or more spaces.

풀이방법
- 단순 구현
- 마지막 패딩을 제거하기 위해 empty_start 변수를 추가하여 연속되는 공백 탐색

"""
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        lineLen = int(len(encodedText) / rows)
        
        res = ""
        empty_start = -1
        for i in range(lineLen):
            for j in range(rows):
                if i + j*lineLen + j < len(encodedText):
                    cur = encodedText[i + j*lineLen + j]
                    #print(str(i + j*lineLen + j) + " : " + cur)
                    res += cur
                    if cur == " ":
                        if empty_start == -1:
                            empty_start = len(res) - 1
                    else:
                        empty_start = -1
                    #print("empty_start: " + str(empty_start))

        if empty_start == -1:
            return res
        else:
            return res[:empty_start]
                
