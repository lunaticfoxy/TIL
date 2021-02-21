/*
주소: https://leetcode.com/problems/wildcard-matching/

내용
- 정규표현식 매칭의 축약버전
- 영어 소문자로 이루어진 문자열이 들어옴
- 이를 영어 소문자, ?, * 가 포함된 표현식으로 매칭하려 함
  - 영어 소문자는 동일한 문자 1개 매칭
  - ?는 1개의 문자 매칭
  - *는 0개 이상의 문자 매칭
- 매칭이 가능한지 여부를 리턴

예제
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false


풀이 방법
- DFS 탐색이라 생각하면 됨
  - 영어 소문자나 ?가 매칭되면 둘다 다음으로 이동
  - *가 매칭되면
    - 둘다 다음으로 이동
    - 문자열만 다음으로 이동
    - 표현식만 다음으로 이동
- 재귀와 스택으로 해결
  - 단 이미 방문한 케이스을 다시 방문하지 않도록 visited 체크 필요

*/

object Solution {
  def isMatch(s: String, p: String): Boolean = {
    val visited = scala.collection.mutable.Set[(Int, Int)]()

    def isMatchRecur(sIdx: Int, pIdx: Int): Boolean = {
      if(visited.contains(sIdx, pIdx))
        false
      else {
        visited.add((sIdx, pIdx))

        if (sIdx == s.length) {
          if (pIdx == p.length)
            true
          else if (p(pIdx).toString == "*")
            isMatchRecur(sIdx, pIdx + 1)
          else
            false
        }
        else if (pIdx == p.length)
          false
        else {
          if (p(pIdx).toString == "?")
            isMatchRecur(sIdx + 1, pIdx + 1)
          else if (p(pIdx).toString == "*")
            isMatchRecur(sIdx + 1, pIdx + 1) || isMatchRecur(sIdx + 1, pIdx) || isMatchRecur(sIdx, pIdx + 1)
          else if (p(pIdx) == s(sIdx))
            isMatchRecur(sIdx + 1, pIdx + 1)
          else
            false
        }
      }
    }

    isMatchRecur(0, 0)
  }
  
  def isMatchStack(s: String, p: String): Boolean = {
    val stack = scala.collection.mutable.Stack[(Int, Int)]()
    var isTrue = false

    val visited = scala.collection.mutable.Set[(Int, Int)]((0, 0))

    stack.push((0, 0))

    while(stack.nonEmpty) {
      //println(stack.take(5))
      val cur = stack.pop()
      val curSIdx = cur._1
      val curPIdx = cur._2

        if(curSIdx == s.length) {
          if(curPIdx == p.length) {
            isTrue = true
            stack.popAll()
          }
          else if(p(curPIdx).toString == "*") {
            if(!visited.contains((curSIdx, curPIdx + 1))) {
              visited.add((curSIdx, curPIdx + 1))
              stack.push((curSIdx, curPIdx + 1))
            }
          }

        }
        else if(curPIdx < p.length) {
          if(p(curPIdx).toString == "?") {
            if(!visited.contains((curSIdx + 1, curPIdx + 1))) {
              visited.add((curSIdx + 1, curPIdx + 1))
              stack.push((curSIdx + 1, curPIdx + 1))
            }
          }
          else if(p(curPIdx).toString == "*") {
            if(!visited.contains((curSIdx + 1, curPIdx + 1))) {
              visited.add((curSIdx + 1, curPIdx + 1))
              stack.push((curSIdx + 1, curPIdx + 1))
            }

            if(!visited.contains((curSIdx + 1, curPIdx))) {
              visited.add((curSIdx + 1, curPIdx))
              stack.push((curSIdx + 1, curPIdx))
            }

            if(!visited.contains((curSIdx, curPIdx + 1))) {
              visited.add((curSIdx, curPIdx + 1))
              stack.push((curSIdx, curPIdx + 1))
            }
          }
          else if(p(curPIdx) == s(curSIdx)) {
            if(!visited.contains((curSIdx + 1, curPIdx + 1))) {
              visited.add((curSIdx + 1, curPIdx + 1))
              stack.push((curSIdx + 1, curPIdx + 1))
            }
          }

        }

    }

    isTrue
  }
}

