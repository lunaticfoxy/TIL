"""
주소: https://leetcode.com/problems/string-matching-in-an-array/submissions/

내용
- 문자열의 배열이 주어진다
- 문자열중 다른 문자열의 부분 문자열인 문자열을 모두 찾아서 리턴하라

샘플
Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []


풀이방법
- 단순 구현
- 배열을 돌면서 해당 값을 부분 문자열로 가지는 배열의 원소가 2개 이상인지 체크
  - 1개는 자기 자신이므로
"""
object Solution {
    def stringMatching(words: Array[String]): List[String] = {
        words.filter(x => words.filter(y => y.contains(x)).size >= 2).toList
    }
}
