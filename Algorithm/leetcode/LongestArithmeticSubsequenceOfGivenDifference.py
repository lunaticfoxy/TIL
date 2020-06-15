"""
주소: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

내용
- 정수 배열이 주어지고, 이 정소들을 순서에 맞게 뽑아 값들 사이에 difference 차이가 나는 배열을 새로 만들고 싶다
- 가능한 배열의 최대 길이를 구하라

샘플
Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].

Example 2:
Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.

Example 3:
Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].

풀이 방법
- 매 아이템마다 아이템 - 차이 가 과거에 존재했는지 확인한다
  - 존재하지 않았다면 dict[아이템] 에 1을 넣는다
  - 존재했다면 dict[이전]+1 이 dict[아이템] 보다 큰지 확인하고 갱신한다
- 이를 모든 원소에 대해 반복하고 이중 가장 큰 값을 리턴한다
"""
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        last = dict()
        max_val = 1
        
        for item in arr:
            before = item - difference
            if before in last:
                new_val = last[before] + 1
                
                if (not item in last) or last[item] < new_val:
                    last[item] = new_val
                    if new_val > max_val:
                        max_val = new_val
                
            else:
                last[item] = 1
        
        return max_val
