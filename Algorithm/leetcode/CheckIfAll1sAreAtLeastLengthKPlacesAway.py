"""
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

"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt = -1
        
        for n in nums:
            if n == 1:
                if cnt != -1 and cnt < k:
                    return False
                cnt = 0
            elif cnt != -1:
                cnt += 1
                
        return True
