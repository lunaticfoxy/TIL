/*
주소: https://leetcode.com/problems/find-target-indices-after-sorting-array/

내용
- 중복 가능한 정수로 구성된 배열과 배열 내에 포함된 값 중 한 값이 주어진다
- 배열 내의 원소가 정렬된 뒤 주어진 값이 어떤 인덱스에 저장될지를 구하라


예제
Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

Example 4:
Input: nums = [1,2,5,2,3], target = 4
Output: []
Explanation: There are no elements in nums with value 4.


풀이방법
- 배열 내에서 주어진 값보다 작은 값의 개수를 구한다
- 배열 내에서 주어진 값의 개수를 구한다
- [(주어진 값보다 작은 값의 개수), (주어진 값보다 작은 값의 개수) + 1, (주어진 값보다 작은 값의 개수) + 2, ... , (주어진 값보다 작은 값의 개수) + (주어진 값의 개수) - 1] 이 답이된다

*/

object Solution {
    def targetIndices(nums: Array[Int], target: Int): List[Int] = {
        val lessCnt = nums.filter(_ < target).size
        val targetCnt = nums.filter(_ == target).size
        
        (lessCnt to (lessCnt + targetCnt - 1)).map(x => x).toList
    }
}
