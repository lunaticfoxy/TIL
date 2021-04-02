/*
주소: https://leetcode.com/problems/combination-sum-iii/

내용
- 자연수 n, k가 주어진다
- 1부터 9 사이의 자연수 중 n개를 사용하여 합이 k인 집합을 만들려 한다
- 가능한 조합을 모두 구하라
  - 단, 같은 숫자는 한번만 사용할 수 있다.


예제
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

Example 4:
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.


풀이방법
- 단순 재귀
- 숫자를 하나씩 증가시키며 해당 숫자를 넣는 경우와 넣지 않는 경우를 모두 구해본다
- 숫자 중복이 되지 않으므로 가지치기는 필요없다
*/
object Solution {
  def combinationSum3(k: Int, n: Int): List[List[Int]] = {

    def combRecur(n: Int, rCnt: Int, rSum: Int, used: List[Int]): List[List[Int]] = {
      if(n >= 10 || rSum < n)
        List[List[Int]]()
      else if (rSum == n) {
        if(rCnt == 1)
          List(used ++ List[Int](n))
        else
          List[List[Int]]()
      } else{
        combRecur(n + 1, rCnt - 1, rSum - n, used ++ List[Int](n)) ++
          combRecur(n + 1, rCnt, rSum, used)
      }
    }

    combRecur(1, k, n, List[Int]())
  }
}
