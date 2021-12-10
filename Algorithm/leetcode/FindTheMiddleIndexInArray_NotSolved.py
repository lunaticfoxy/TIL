"""
주소: https://leetcode.com/problems/find-the-middle-index-in-array/
"""

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        
        sum_from_first = [0 for _ in range(len(nums))]
        sum_from_last = [0 for _ in range(len(nums))]
        sum_from_first[0] = nums[0]
        sum_from_last[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            sum_from_first[i] = sum_from_first[i - 1] + nums[i]
            sum_from_last[-(i + 1)] = sum_from_last[-i] + nums[-(i + 1)]
            
        m_idx = -1
        if sum_from_last[0] == 0 or (len(nums)>=2 and sum_from_last[1] == 0):
            m_idx = 0
        elif sum_from_first[-1] == 0 or (len(nums)>=2 and sum_from_first[-2] == 0):
            m_idx = len(nums) - 1
        else:
            for i in range(1, len(nums) - 1):
                if sum_from_first[i-1] == sum_from_last[i+1]:
                    m_idx = i
                    break
        
        return m_idx
