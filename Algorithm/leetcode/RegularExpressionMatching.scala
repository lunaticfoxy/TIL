/*
주소: https://leetcode.com/problems/regular-expression-matching/

내용
- RegularExpression 간소화 매칭
- 입력 문자는 알파벳 소문자로만 이루어짐
- 패턴 문자는 알파벳 소문자, . , * 로만 이루어짐
  - 패턴 문자에서 . 는 모든 값에 매칭
  - 패턴 문자에서 * 는 앞의 값을 0번 이상 반복
- 입력 문자가 패턴 문자로 처리 가능한지 여부를 


예제
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false


풀이 방법
- 경우의 수에 따라 재귀로 동작
- case 1. 패턴 문자가 비어있을 경우
  - 찾을 문자도 비어있으면 true, 아니면 false
- case 2. 패턴 문자가 있을 경우
  - case 2-1. 체크할 문자가 비어있을 경우
    - caes 2-1-1. 현재 패턴 문자에 *가 붙어 잇을 경우
      - 패턴을 2개 지우고 다음으로 이동
    - case 2-1-2. 현재 패턴 문자에 *가 붙어있지 않을 경우
      - false 리턴
  - case 2-2. 채크할 문자가 있을 경우
    - case 2-2-1. 현재 패턴 문자가 . 이거나 체크할 문자와 일치할 경우
      - case 2-2-1-2. 현재 패턴 문자에 * 가 붙어 있을 경우
        - 다음 세가지 방법으로 재귀를 돌려 하나라도 true 라면 true 리턴
        - 현재 문자와 현재 패턴문자 + * 까지 지우고 재귀 수행
        - 현재 문자는 두고 현재  + * 까지 지우고 재귀 수행

*/
object Solution {
    def isMatch(s: String, p: String): Boolean = {
    //println(s + " / " + p)
    if(p.isEmpty) {
        if(s.isEmpty)
          true
        else
          false
    }
    else{
      val curPattern = p(0).toString
      val curStar = if(p.length > 1 && p(1).toString == "*") true else false

      if(s.isEmpty) {
        if(curStar)
          isMatch(s, p.drop(2))
        else
          false
      }
      else {
        val curChar = s(0).toString

        if((curPattern == ".") || (curChar == curPattern)) {
          if(curStar)
            isMatch(s.drop(1), p.drop(2)) || isMatch(s.drop(1), p) || isMatch(s, p.drop(2))
          else
            isMatch(s.drop(1), p.drop(1))
        }
        else {
          if(curStar)
            isMatch(s, p.drop(2))
          else
            false
        }
      }
    }

  }
}
