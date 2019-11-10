"""
주소: https://leetcode.com/problems/count-number-of-nice-subarrays/

내용
- 자연수로 이루어진 array와 1 이상의 자연수 k가 주어진다
- array내에서 홀수가 k개만큼 포함된 모든 subarray의 개수를 구하라


예시
Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


풀이방법
- 먼저 홀수값들의 인덱스를 저장하는 배열을 만들고 슬라이딩 윈도우를 사용한다
  - 이때 슬라이딩 윈도우의 크기는 k가 된다
- 슬라이딩 윈도우를 하나씩 옆으로 옮기면서 시작지점의 앞과 끝지점의 뒤에서 나타날수 있는 경우의 수를 계산한다
  - [2 1 2 1 2 2 1] 에서 슬라이딩 윈도우가 [1, 3] 일경우 => [2 1 2 1], [1 2 1], [2 1 2 1 2], [1 2 1 2], [2 1 2 1 2 2], [1 2 1 2 2]
- 이를 반복하면서 나타나는 모든 경우의 수를 더하면 결과가 나온다

"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIdxs = []
        
        for i, num in enumerate(nums):
            if num%2==1:
                oddIdxs.append(i)
        
        start = 0
        oddSIdx = 0
        oddEIdx = k - 1
        res = 0
        
        while oddEIdx < len(oddIdxs):
            if oddSIdx == 0:
                start = 0
            else:
                start = oddIdxs[oddSIdx - 1] + 1
            
            if oddEIdx == len(oddIdxs) - 1:
                end = len(nums) - 1
            else:
                end = oddIdxs[oddEIdx + 1] - 1
            
            res += ((oddIdxs[oddSIdx] - start + 1) * (end - oddIdxs[oddEIdx] + 1))
            oddSIdx += 1
            oddEIdx += 1
        
        return res
        
