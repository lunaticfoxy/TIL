/*
주소: https://leetcode.com/problems/subsets-ii/

내용
- 주어진 배열에서 가능한 모든 부분집합을 구하라
- 내부 원소가 동일하면 동일한 집합으로 친다

예제
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


풀이방법
- 재귀 구현
- 현재 원소를 넣던지 or 넣지 않던지를 재귀로 구현한다
- 마지막에 내부 원소가 동일한지 여부 체크를 위해 정렬후 distinct 수행
*/

object Solution {
  def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {

    def subsetRecur(nums: Array[Int], left: Int): List[List[Int]] = {
      //println(nums.mkString(","))
      if(nums.length == 0 || left == 0 || nums.length < left)
        List[List[Int]](List[Int]())
      else
        subsetRecur(nums.drop(1), left - 1).map { x =>
          List(nums(0)) ++ x
        } ++ subsetRecur(nums.drop(1), left)
    }

    (0 until nums.length + 1).map{i =>
      subsetRecur(nums, i)
    }.reduce(_ ++ _).map{_.sorted}.distinct
  }
}
