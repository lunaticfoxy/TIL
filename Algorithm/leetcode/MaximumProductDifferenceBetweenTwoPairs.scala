/*
주소: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

내용
- 1 이상의 자연수로 이루어진 크기 4 이상의 배열이 주어진다
- 이 배열의 원소중 두개씩 두쌍을 선택하여 각각 쌍 내에 속항 원소의 곱의 차이의 최대값을 구하라


얘제
Example 1:
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:
Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.


풀이방법
- 단순구현
- 가장 큰 값 2개, 가장 작은 값 2개 탐색
*/

object Solution {
    def maxProductDifference(nums: Array[Int]): Int = {
        val sortedNums = nums.sorted
        
        (sortedNums(sortedNums.length - 1) * sortedNums(sortedNums.length - 2)) - (sortedNums(0) * sortedNums(1))
    }
}
