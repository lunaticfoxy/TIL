/*
주소: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

내용
- 정수로 이루어진 배열이 주어진다
- 이 배열은 양쪽 끝에서부터 순차적으로 접근 가능하다
  - 다시 끝으로 돌아가는데 추가 비용은 들지 않는다
- 배열을 접근해서 가장 큰 원소와 가장 작은 원소를 지우려 할때 접근하는데 걸리는 시간을 구하라


예제
Example 1:
Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation: 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

Example 2:
Input: nums = [0,-4,19,1,8,-2,-3,5]
Output: 3
Explanation: 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

Example 3:
Input: nums = [101]
Output: 1
Explanation:  
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.


풀이방법
- 먼저 가장 큰 지점과 작은 지점의 인덱스를 구한다
  - 작은 지점의 인덱스를 min_idx, 큰지점의 인덱스를 max_idx 라 하자
- 다음 4가지 케이스중 가장 작은 값을 찾아 리턴하면 된다
  - 앞에서부터 순차적으로 접근해서 두 값을 모두 지우는 경우: max(min_idx + 1, max_idx + 1)
  - 뒤에서부터 순차적으로 접근해서 두 값을 모두 지우는 경우: max(length(arr) - min_idx, length(Arr) - max_idx)
  - 앞에서는 max, 뒤에서는 min 값을 지우는 경우: length(arr) - min_idx + max_idx + 1
  - 앞에서는 min, 뒤에서는 max 값을 지우는 경우: length(arr) - max_idx + min_idx + 1

*/
object Solution {
  def minimumDeletions(nums: Array[Int]): Int = {
    val numsWithIdx = nums.zipWithIndex
    val minVal = numsWithIdx.minBy(_._1)
    val maxVal = numsWithIdx.maxBy(_._1)

    Math.min(
      Math.min(
        Math.max(minVal._2 + 1, maxVal._2 + 1),
        Math.max(nums.length - minVal._2, nums.length - maxVal._2)
      ),
      Math.min(nums.length - minVal._2 + maxVal._2 + 1, nums.length - maxVal._2 + minVal._2 + 1)
    )
  }
}
