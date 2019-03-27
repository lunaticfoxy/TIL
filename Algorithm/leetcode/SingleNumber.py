"""
주소: https://leetcode.com/problems/single-number/

난이도: Easy

문제 내용
- 정수가 들어있는 리스트가 주어지는데 이 안에는 한개의 숫자만 빼고 동일한 숫자가 2개씩 들어있다.
- 이 한개의 숫자를 찾아라
- O(n) time complexity & O(1) space complexity

샘플
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
       
풀이 설명
- 한 숫자에 xor 연산을 두번하면 0이 된다.
- 모든 값에 xor 연산을 하면 된다.

어떤 경우에 활용 가능할까
- 중복된 값 제거에 쓸 수 있긴 함 - 현실적으로 쓸지는 별개지만r- xo
dasdfasdfas"""
- 계산하기 쉽게 문자열로 치환한다음 비교
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
            
        return nums[0]
