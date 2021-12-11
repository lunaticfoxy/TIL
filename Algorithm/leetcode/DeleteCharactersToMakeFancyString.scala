/*
주소: https://leetcode.com/problems/delete-characters-to-make-fancy-string/

내용
- 같은 문자가 연속해서 3개 이상 반복되지않는 문자열을 fancy string이라 한다
- 3개이상 연속해서 반복되는 문자를 지워 fancy string을 만들어라 

예제
Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".



풀이방법
- 단순 구현
- 단, 재귀로 했더니 메모리 리밋이 나서 수정필요
  - 꼬리재귀가 안먹히는것으로 보임
*/
object Solution {
    def makeFancyString(s: String): String = {
        
        def recurFunc(cArr: Array[Char], res: String, lastChar: Char, cnt: Int): String = {
            if(cArr.isEmpty)
                res
            else {
                if(cArr.head == lastChar) {
                    if(cnt >= 2)
                        recurFunc(cArr.drop(1), res, lastChar, cnt)
                    else
                        recurFunc(cArr.drop(1), res + cArr(0).toString, lastChar, cnt + 1)
                }
                else
                    recurFunc(cArr.drop(1), res + cArr(0).toString, cArr(0), 1)
            }
        }
        
        recurFunc(s.toArray, "", " ".charAt(0), 0)
    }
}
