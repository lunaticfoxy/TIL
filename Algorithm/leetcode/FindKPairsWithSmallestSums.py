"""
주소: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ret_val = []
        
        if len(nums1)==0 or len(nums2)==0:
            return []
            
        for i in range(len(nums1)):
            if i > k:
                break
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            
        i = 0
        while len(heap)>0 and i<k:
            cur, ori, add = heapq.heappop(heap)
            ret_val.append([nums1[ori], nums2[add]])
                
            if add+1 < len(nums2):
                heapq.heappush(heap, (nums1[ori] + nums2[add+1], ori, add+1))
            i += 1
            
        return ret_val
