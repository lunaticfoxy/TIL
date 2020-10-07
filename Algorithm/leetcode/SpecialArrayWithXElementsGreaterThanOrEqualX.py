"""
주소: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

내용
- 0 이상의 값으로 이루어진 배열이 주어진다
- 이 배열의 원소가 임의의 수 x 보다 크거나 같은 값이 x 개 있다면 special array 라고 한다
  - x의 값은 뭐라도 될 수 있다
- 이 배열이 special array 라면 그 x, 아니라면 -1을 리턴하라

예시
Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

Example 4:
Input: nums = [3,6,7,7,0]
Output: -1


풀이방법
- 배열을 정렬한다음 생각한다
- i값을 뒤에서부터 i번째랑 비교해서
  - 뒤에서부터 i번째 지점의 값이 i 이상이고
  - 뒤에서부터 i+1 번째 지점의 값이 i 미만일경우 통과
- 예외 케이스로 i == len(nums) 일 경우를 고려해준다
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        length = len(nums)
        for i in range(1, length + 1):
            if i == length:
                if nums[0] >= i:
                    return i
            elif nums[-i] >= i and nums[-i-1] < i:
                return i
        
        return -1
