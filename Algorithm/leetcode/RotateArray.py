"""
주소: https://leetcode.com/problems/rotate-array/

내용
- 리스트와 정수 k가 주어진다
- 이 리스트를 k만큼 회전시켜라
- 단 O(1) 공간만을 사용하라


샘플
Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



풀이방법
- 단순히 풀라면 엄청 쉽지만 O(1) 공간이 문제
- 먼저 1바퀴 이상 도는건 무의미하므로 k를 k%len(nums) 로 간소화
- 이후에 리스트 뒤집기를 사용하면 풀이 가능
  - 뒤에서부터 k개를 뒤집음
  - 남은것들을 뒤집음
  - 전체를 뒤집음
  - 예시
    - [1,2,3,4,5,6], k = 2
      -> [1,2,3,4,6,5]
      -> [4,3,2,1,6,5]
      -> [5,6,1,2,3,4]
- 실제 구현시에는 앞에서부터 뒤집음

  

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverseList(nums, start, end):
            length = end - start + 1
            for i in range(int(length/2)):
                temp = nums[end-i]
                nums[end-i] = nums[start+i]
                nums[start+i] = temp
        
        k = k%len(nums)
        
        reverseList(nums, 0, len(nums)-k-1)
        reverseList(nums, len(nums)-k, len(nums)-1)
        reverseList(nums, 0, len(nums)-1)
