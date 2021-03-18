/*
주소: https://leetcode.com/problems/missing-number/

내용
- 0 부터 N 까지 값중 하나가 빠진 N 길이의 배열이 주어진다
- 이중에서 어떤 값이 빠졌는지를 찾아라
- 단 시간 복잡도는 O(N), 공간복잡도는 O(1) 로 해결하라

예제
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.


풀이방법
- 0 부터 N 까지의 합을 구하고 여기서 배열의 원소의 합을 빼면 빠진 원소가 나온다
*/
object Solution {
  def missingNumber(nums: Array[Int]): Int = {
    val sReal = nums.sum
    val sOri = (0 to nums.length).sum

    sOri - sReal
  }
}
