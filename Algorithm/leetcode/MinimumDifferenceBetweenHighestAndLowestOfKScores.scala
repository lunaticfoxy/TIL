/*
주소: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

내용
- 0 이상의 정수로 구성된 배열과 1 이상, 배열의 크기 이하의 자연수 k 가 주어진다
- 배열에서 k개의 원소를 뽑았을때 가장 큰 값과 가장 작은 값의 차이의 최소값을 구하라

예제
Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.


풀이방법
- k개를 뽑았을때 가장 큰 값, 작은 값 차이가 가장 작으려면 두 값이 정렬되었을때 k-1 만큼 떨어져 있어야 한다
- 따라서 먼저 배열을 정렬하고 배열을 순회하며 x 번째 지점, x + k -1 번째 자점 사이의 차이를 계산한다
- 이 차이중 가장 작은값이 답이 된다

*/

object Solution {
  def minimumDifference(nums: Array[Int], k: Int): Int = {
    val sortedNums = nums.sorted

    (0 to sortedNums.size - k).map{x =>
      sortedNums(x + k - 1) - sortedNums(x)
    }.min
  }
}
