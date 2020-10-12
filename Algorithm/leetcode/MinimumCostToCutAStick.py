"""
주소: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

내용
- 길이가 n인 나무에서 일정 지점들을 자르려한다
  - 이 지점은 리스트로 주어진다
- 이때 자르기 전 길이가 나무를 자르는 비용이다
- 나무를 가장 최소한의 비용으로 자르려 할때 드는 비용을 구하라

예제
Example 1:
Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).

Example 2:
Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.


풀이방법
- 기본적으로는 dfs 이다
  - 모든 경우를 다 고려해본다
- 이때 dp로 이미 계산했던 지점은 저장해두고 다시 계산하지 않는다
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        INF = 99999999
        dp = dict()
        
        dp[0] = dict()
        for cut in cuts:
            dp[cut] = dict()
        
        def dfs(start, end):
            if end in dp[start]:
                return dp[start][end]
            
            cur_val = INF
            for c in cuts:
                if c > start and c < end:
                    left_val = dfs(start, c)
                    right_val = dfs(c, end)
                    cur_val = min(cur_val, left_val + right_val)
            
            if cur_val == INF:
                dp[start][end] = 0
            else:
                dp[start][end] = end - start + cur_val
            
            return dp[start][end]
        
        return dfs(0, n)
