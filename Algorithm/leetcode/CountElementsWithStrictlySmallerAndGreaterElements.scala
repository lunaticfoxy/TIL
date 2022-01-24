/*
주소: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

내용
- 정수 배열이 주어진다
- 배열내에서 자기보다 큰 값과 자기보다 작은 값이 모두 존재하는 원소의 개수를 구하라


예제
Example 1:
Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.

Example 2:
Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.


풀이방법
- 단순 구현
*/
object Solution {
    def countElements(nums: Array[Int]): Int = {
        val smallest = nums.min
        val biggest = nums.max
        
        nums.filter(x => x > smallest && x < biggest).size
    }
}
