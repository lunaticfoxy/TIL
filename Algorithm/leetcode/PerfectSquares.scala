/*
주소: https://leetcode.com/problems/perfect-squares/

내용
- 자연수가 주어진다
- 이 자연수를 다른 자연수의 제곱의 합으로 만들려 한다
- 사용해야 하는 자연수의 최소 갯수를 구하라

예제
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


풀이방법
- 단순 구현
- 재귀로 구현하되 dp로 가지치기
*/

object Solution {
  def numSquares(n: Int): Int = {
    val dp = collection.mutable.Map[Int, Int]()

    def numSquaresRecur(n: Int): Int = {
      if(n == 0)
        0
      else if(n == 1)
        1
      else if(dp.contains(n))
        dp(n)
      else {
        val maxSqrt = Math.sqrt(n.toDouble).toInt

        val res = (1 to maxSqrt).map{x =>
          numSquaresRecur(n - (x * x))
        }.min + 1

        dp.addOne((n, res))
        res
      }
    }

    numSquaresRecur(n)
  }
}
