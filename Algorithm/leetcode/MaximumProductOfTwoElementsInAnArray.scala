"""
주소: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

내용
- 자연수의 배열이 주어진다
- 이 배열 내에서 두 값 x, y 를 뽑아 만들수 있는 (x-1)*(y-1) 의 최대값을 구하라


샘플
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
Input: nums = [3,7]
Output: 12


풀이방법
- 단순 구현문제
- 단, 소팅하면 느리니 Top2 만 뽑아 계산한다

"""
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        
        def maxTwo(nums:Array[Int]): Array[Int] = {
            if(nums.size <= 2)
                nums
            else {
                val pivot = nums(0)
                
                val bigger = nums.filter(_ > pivot)
                
                if(bigger.size >= 2)
                    maxTwo(bigger)
                else if(bigger.size == 1)
                    bigger ++ Array(pivot)
                else {
                    val pivotArr = nums.filter(_ == pivot)
                    
                    if(pivotArr.size >= 2)
                        pivotArr.take(2)
                    else
                        pivotArr ++ Array(nums.filter(_ < pivot).max)
                }
            }
        }
        
        val maxs = maxTwo(nums)
        
        (maxs(0) - 1) * (maxs(1) - 1)
    }
}
