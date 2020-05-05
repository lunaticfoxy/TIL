/*
주소: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

내용
- 0과 1로 이루어진 배열이 주어진다
- 자연수 k가 주어질때 배열 내 1 사이의 거리가 k 이상인지 여부를 리턴하라

샘플
Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:
Input: nums = [0,1,0,1], k = 1
Output: true


풀이방법
- 단순 구현문제
*/
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        
        def funRecur(nums: Array[Int], k: Int, last: Int): Boolean = {
            if(nums.size==0)
                true
            else {
                if(nums.head == 0) {
                    if(last == -1) 
                        funRecur(nums.drop(1), k, last)
                    else
                        funRecur(nums.drop(1), k, last + 1)
                }
                else {
                    if((last == -1) || (last >= k))
                        funRecur(nums.drop(1), k, 0)
                    else
                        false
                }
            }
            
        }
        
        funRecur(nums, k, -1)
    }
}
