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
- frequency 기준으로 

"""
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = dict()
        numCnt = dict()
        maxIdx = 0
        minFreq = 0
        maxFreq = 0
        freqCnt = 0
        
        freq[1] = set()
        
        
        for i in range(len(nums)):
            if nums[i] in numCnt:
                numCnt[nums[i]] += 1
                freq[numCnt[nums[i]] - 1].remove(nums[i])
                
                if numCnt[nums[i]] in freq:
                    freq[numCnt[nums[i]]].add(nums[i])
                else:
                    freq[numCnt[nums[i]]] = set([nums[i]])
                    
                if len(freq[numCnt[nums[i]]]) == 1:
                    freqCnt += 1
                
                if len(freq[numCnt[nums[i]] - 1]) == 0:
                    freqCnt -= 1
                
            else:
                numCnt[nums[i]] = 1
                freq[1].add(nums[i])
                
                if minFreq == 0 or minFreq > 1:
                    minFreq = 1
                    freqCnt += 1
            
            if len(freq[minFreq]) == 0:
                minFreq += 1
            
            maxFreq = max(maxFreq, numCnt[nums[i]])
            
            if (len(numCnt) == 1):
                maxIdx = i
            elif (freqCnt==2 and len(freq[maxFreq]) == 1 and maxFreq - minFreq == 1):
                maxIdx = i
            elif (minFreq == 1 and freqCnt==2 and len(freq[minFreq]) == 1):
                maxIdx = i
            elif (minFreq == 1 and maxFreq==1):
                maxIdx = i
        
        return maxIdx + 1
