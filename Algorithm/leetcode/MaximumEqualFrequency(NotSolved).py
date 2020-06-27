"""
주소: https://leetcode.com/problems/maximum-equal-frequency/

내용
- 자연수로 이루어진 배열이 있다
- 배열의 앞에서부터 체크하여 한 원소만 제거했을때 모든 값이 같은 횟수만큼 나오는 최대 배열의 길이를 구하라


샘플
Example 1:
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:
Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Example 3:
Input: nums = [1,1,1,2,2,2]
Output: 5

Example 4:
Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8


풀이방법
- 단순 dictionary 갱신으로 시도
  - 답은 나오나 타임리밋 발생

"""

def checkPossible(dp):
    if len(dp) == 1:
        return True
    
    cntDict = dict()
    
    for key in dp:
        if dp[key] in cntDict:
            cntDict[dp[key]] += 1
        else:
            cntDict[dp[key]] = 1
    
    if len(cntDict) >= 3:
        return False
    elif len(cntDict) == 2:
        kv = [[key, cntDict[key]] for key in cntDict]
        
        if kv[0][1] == 1:
            if kv[0][0] == 1 or kv[0][0] - 1 == kv[1][0]:
                return True
            else:
                return False
        elif kv[1][1] == 1:
            if kv[1][0] == 1 or kv[1][0] - 1 == kv[0][0]:
                return True
            else:
                return False
        else:
            return False
    elif 1 in cntDict:
        return True
    else:
        return False

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        dp = dict()
        maxIdx = 0
        
        
        for i in range(len(nums)):
            if nums[i] in dp:
                dp[nums[i]] += 1
            else:
                dp[nums[i]] = 1
            
            if checkPossible(dp):
                maxIdx = i
                
        
        return maxIdx + 1
            
            
