/*
주소: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

내용
- 문자열의 배열과 타겟 문자열이 주어진다
- 배열안의 문자열을 조합하여 타겟 문자열을 만들수 있는 경우의 수를 구하라
  - 같은 문자열이라도 여러번 등장했다면 서로 다른 문자열로 취급한다


예제
Example 1:
Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

Example 2:
Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"

Example 3:
Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"

풀이방법
- 재귀로 매 케이스 체크
- 아직 못품
*/
object Solution {
  def numOfPairs(nums: Array[String], target: String): Int = {

    def recurFunc(cur: String, nums: Array[(String, Int)], target: String): Int = {
      println(nums.mkString(","))
      if(cur == target)
        1
      else if(nums.isEmpty)
        0
      else {
        nums.filter{num =>
          (cur.length + num._1.length) <= target.length
        }.map{num =>
          recurFunc(cur + num._1, nums.filter(x => x._2 != num._2), target)
        }.sum
      }
    }

    recurFunc("", nums.zipWithIndex, target)
  }
}
