/*
주소: https://leetcode.com/problems/count-and-say/

내용
- 11 => 2개의 1 => 21, 1111 => 4개의 1 => 41 형태로 세는것을 표현하고 싶다
- 단 n이 입력됐을때 countAndSay(n-1)의 결과를 센것을 countAndSay(n)의 결과로 활용하려 한다
  - countAndSay(1) = "1"


예제
Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


풀이방법
- 단순 구현
- 중간에 dp를 활용한 가지치기
*/
object Solution {
  def countAndSay(n: Int): String = {
    val dp = collection.mutable.HashMap[Int, String]()

    def getCount(n: String): String = {
      n.size.toString + n.head.toString.toInt
    }

    def groupingRecur(n: String, last: Char, cur: String, g: Array[String]): Array[String] = {
      if(n.isEmpty) {
        g ++ Array(cur)
      } else {
        if(n.head == last)
          groupingRecur(n.drop(1), last, cur + n.head.toString, g)
        else {
          groupingRecur(n.drop(1), n.head, n.head.toString, if(cur == "") g else g ++ Array(cur))
        }
      }
    }

    def countAndSayRecur(n: Int): String = {
      if(n == 1)
        "1"
      else if(dp.contains(n))
        dp(n)
      else {
        val lastN = countAndSayRecur(n - 1)
        val temp = groupingRecur(lastN, 'x', "", Array[String]()).map(getCount).reduce(_ + _)
        dp.addOne((n, temp))
        temp
      }
    }

    countAndSayRecur(n)
  }
}
