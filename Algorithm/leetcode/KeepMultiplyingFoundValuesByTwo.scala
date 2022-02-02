/*
주소: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
*/

object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        val numSet = nums.toSet
        
        def recurFunc(numSet: Set[Int], num: Int): Int = {
            if(numSet.contains(num))
                recurFunc(numSet, num * 2)
            else
                num
        }
        
        recurFunc(numSet, original)
    }
}
