"""
주소: https://leetcode.com/problems/degree-of-an-array/

내용
- 0 이상의 정수로 이루어진 어레이가 주어진다
- 이 어레이 내에서 가장 많은 빈도로 나타나는 숫자가 모두 포함될 수 있는 subarray의 최소 길이를 구하라
  - 단 빈도가 최대인 숫자가 여러개일경우 그중에 subarray의 길이가 최소인걸 찾아라

샘플
Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6


풀이방법
- 매 아이템을 순회하면서 해당 숫자가 몇번 나왔는지와 첫번째 나온 위치를 맵에 저장한다
- 나온 횟수가 최대일 경우 해당 숫자를 모두 포함하는 subarray의 최소 길이를 구한다
  - (subarray의 최소 길이) = (현재 인덱스 위치) - (해당 숫자가 처음 나타난 인덱스 위치)
  - 이때 유의할점은 기존에 같은 최대 빈도가 있더라도 비교해서 최소 길이가 더 작은 값으로 갱신해줘야 한다
- 이를 반복하면 최소 길이에 답이 저장된다

"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        item = dict()
        maxFreq = 0
        minLen = 0
        
        for i in range(len(nums)):
            if not nums[i] in item:
                item[nums[i]] = [1, i]
            else:
                item[nums[i]][0] += 1
                
            if maxFreq < item[nums[i]][0]:
                maxFreq = item[nums[i]][0]
                minLen = i-item[nums[i]][1]+1
            elif maxFreq == item[nums[i]][0] and i-item[nums[i]][1]+1<minLen:
                minLen = i-item[nums[i]][1]+1
        
        return minLen
