"""
주소: https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

내용
- 0 이상의 정수로 이루어진 배열이 주어진다
  - 정수 배열내 원소의 순서는 원하는대로 조정 가능하다
- 그리고 구간들의 시작 지점과 끝 지점을 담은 배열이 주어진다
- 정수 배열 원소를 이 구간내에 나타난 횟수만큼 더해 합을 구하려 한다
- 이때 나올 수 있는 합의 최대값을 구하라


예시
Example 1:
Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.

Example 2:
Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].

Example 3:
Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
Output: 47
Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].


풀이방법
- 배열의 아이템별로 몇번 나타나야 하는지에 대해 저장하는 배열을 새로 만든다
  - 이를 단순히 진행하면 n^2 이 나와 타임리밋이 발생한다
  - 여기서 사용할 수 있는 트릭으로
    - 모든 배열을 0으로 초기화
    - requests의 아이템을 순회
      - request의 시작점의 값 1 증가, 끝지점+1 의 값 1 감소
    - 배열을 앞에서부터 순회하며 (n+1 지점의 값) = (n+1 지점의 값) + (n 지점의 값) 으로 갱신
- 이를 내림차순으로 정렬하고, 배열의 원소도 내림차순으로 정렬하여 같은 인덱스에 있는 원소끼리 곱한다
"""
import heapq

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        num_cnt = [0 for _ in range(len(nums))]
        
        for s, e in requests:
            num_cnt[s] += 1
            if e + 1 < len(num_cnt):
                num_cnt[e + 1] -= 1
        
        for i in range(1, len(num_cnt)):
            num_cnt[i] += num_cnt[i - 1]
        
        num_cnt = sorted(num_cnt)
        nums = sorted(nums)
        
        res = 0
        
        for i in range(len(nums)):
            res = (res + nums[i] * num_cnt[i])%1000000007
            
        return res
