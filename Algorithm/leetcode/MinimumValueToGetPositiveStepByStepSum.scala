"""
주소: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

내용
- 어떤 시작값이 있고, 이 시작값에 배열의 원소를 차례대로 더하려 한다
- 배열의 원소를 더하는동안 시작값이 1 미만으로 내려가지 않도록 하려 한다
- 이때 시작값의 최소 값을 구하라

샘플
Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
                  
Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

Example 3:
Input: nums = [1,-2,-3]
Output: 5

풀이방법
- 단순 구현
"""
object Solution {
    def minStartValue(nums: Array[Int]): Int = {
        
        def recurFunc(nums: Array[Int], before: Int, minVal: Int): Int = {
            if(nums.size == 0)
                1 - minVal
            else {
                val curVal = before + nums(0)
                recurFunc(nums.drop(1), curVal, Math.min(minVal, curVal))
            }
        }
                          
        recurFunc(nums, 0, 0)
    }
}
