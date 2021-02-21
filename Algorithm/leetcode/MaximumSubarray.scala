/*
주소: https://leetcode.com/problems/maximum-subarray/

내용
- 배열이 주어진다
- 배열 내에서 가장 큰 Subarray의 합을 구하라

예제
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-100000]
Output: -100000


풀이방법
- 인덱스 0부터 합을 구해가면서 반복한다
- 현재값이 음수일 경우
  - 최대값을 현재값 or 기존 최대값으로 갱신
  - 현재 값 하나만 포함한 경우가 최대인 경우를 가정
- 현재값이 0 이상인 경우
  - 최대값을 (현재까지의 합 - 합의 최소값) or 기존 최대값으로 갱신
  - 가장 밑까지 내려간 지점에서 얼마나 올라왔는지를 계산
  
*/

object Solution {
    def maxSubArray(nums: Array[Int]): Int = {
        
        def maxDiffRecur(nums: Array[Int], sumBefore: Int, min: Int, maxRes: Int): Int = {
            if(nums.isEmpty)
                maxRes
            else {
                val newSumBefore = sumBefore + nums.head
                val newMin = Math.min(newSumBefore, min)
                
                val newMaxRes = if(nums.head < 0)
                    Math.max(nums.head, maxRes)
                else
                    Math.max(newSumBefore - newMin, maxRes)
                
                
                maxDiffRecur(nums.drop(1), newSumBefore, newMin, newMaxRes)      
            }
        }
        
        if(nums.isEmpty)
            0
        else
            maxDiffRecur(nums.drop(1), nums.head, Math.min(0, nums.head), nums.head)   
    }
}
