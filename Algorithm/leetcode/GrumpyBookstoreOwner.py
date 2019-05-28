"""
주소: https://leetcode.com/problems/grumpy-bookstore-owner/

내용
- 어떤 서점에 주인이 있고 시간마다 손님이 찾아오고 시간별 손님 수가 주어진다
- 그리고 주인이 심술궂은 시간이 존재하는데 심술궂은 시간에 온 손님은 만족하지 못하고, 아닌때는 만족한다
- 이때 주인은 연속된 X시간만큼 심술궂지 않은 척 할 수 있다
- 만족한 손님 수의 최대값을 구하라

샘플
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

풀이방법
- Window가 X인 크기로 리스트를 스캔하는 문제
- 이때 X인 윈도우로 볼 수 있는 효과는 grumpy가 1인 지점만 해당되므로 해당 값을 필터로 사용해서 윈도우의 효과를 구한다
- 모든 윈도우를 순회하면서 최대의 효과를 가지는 윈도우 위치 탐색
  - 이때 window[x+1]의 값은 window[x]-value[x]+value[x+X] 가 되므로 n으로 탐색 가능
  - 이 방법을 안쓰면 O(n*X)
- 이후 grumpy가 0인 지점은 고려 안했으므로 그 값들을 모두 더해주면 됨

"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_temp = 0
        idx = 0
        
        for i in range(X):
            if grumpy[i]==1:
                max_temp += customers[i]
        
        print(max_temp)
        cur_temp_before = max_temp
        for i in range(len(customers) - X):
            cur_temp = cur_temp_before
            
            if grumpy[i]==1:
                cur_temp -= customers[i]
            
            if grumpy[i+X]==1:
                cur_temp += customers[i+X]
                
            if cur_temp>max_temp:
                max_temp = cur_temp
                idx = i+1
                
            cur_temp_before = cur_temp
            
        for i in range(len(customers)):
            if grumpy[i]==0:
                max_temp += customers[i]
        
        return max_temp
