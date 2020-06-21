"""
주소: https://leetcode.com/problems/longest-continuous-increasing-subsequence/

내용
- 연속적으로 증가하는 가장 긴 subsequence의 길이를 리턴하라

샘플
Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

풀이방법
- 단순 구현 생략
"""
object Solution {
    def findLengthOfLCIS(nums: Array[Int]): Int = {
        def recurFunc(nums: Array[Int], last: Int, curCnt: Int, maxCnt: Int): Int = {
            if(nums.size == 0)
                maxCnt
            else {
                if(nums(0) > last)
                    recurFunc(nums.drop(1), nums(0), curCnt + 1, Math.max(curCnt + 1, maxCnt))
                else
                    recurFunc(nums.drop(1), nums(0), 1, Math.max(1, maxCnt))
            }
        }
        
        if(nums.size == 0)
            0
        else
            recurFunc(nums.drop(1), nums(0), 1, 1)
    }
}
