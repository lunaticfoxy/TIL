/*
주소: https://leetcode.com/problems/happy-number/

내용
- 자기 자신의 각 자리수의 제곱의 합을 모두 더하는 과정을 반복해서 한 숫자가 반복되는 경우를 Happy Number라 한다
- 어떤 숫자가 Happy Number 인지 여부를 리턴하라

예제
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false


풀이방법
- 단순 구현
- 종료 조건은 0, 1로만 둠
- 이전 결과를 저장하여 루프가 생기면 false 리턴
*/
object Solution {
  def isHappy(n: Int): Boolean = {
    def isHappyRecur(n: Int, visited: Set[Int]): Boolean = {
      if(visited.contains(n))
        false
      else {
        if(n == 1 || n == 0)
          true
        else {

          val newN = n.toString.map {x =>
            val d =  x.toString.toInt
            d * d
          }.sum

          isHappyRecur(newN, visited ++ Set[Int](n))
        }
      }
    }

    isHappyRecur(n, Set[Int]())
  }
}
