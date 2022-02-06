/*
주소: https://leetcode.com/problems/partition-array-according-to-given-pivot/

내용
- 정수 배열과 정수 pivot이 주어진다
- pivot을 기준으로 작은값은 왼쪽, 큰 값은 오른쪽으로 오도록 배열을 재정렬하라
- 작은값, 큰값 사이의 순서는 기존 배열의 순서를 유지한다

예제
Example 1:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

Example 2:
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.


풀이방법
- 의도는 이진 탐색 + 순서 유지인듯
- 하지만 단순 필터 후 재조합으로 시간 복잡도는 동일하게 구현 가능
*/
object Solution {
    def pivotArray(nums: Array[Int], pivot: Int): Array[Int] = {
        val bigger = nums.filter(_ > pivot)
        val same = nums.filter(_ == pivot)
        val smaller = nums.filter(_ < pivot)
        
        smaller ++ same ++ bigger
    }
}
