"""
주소: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

난이도: Medium

문제 내용
- 주식 가격이 리스트로 주어진다. 이 주식 가격 내에서 사고 팔아서 얻을수 있는 최대의 이익을 구하라.
- 단 주식을 판매한 뒤에는 한턴 쉬어야 된다.

샘플
Input: [1,2,3,0,2]
Output: 3
Input: [4, 2, 1]
Output: 0
       
풀이 설명
- 일단 리커시브로 구현한건 당연히 타임리밋
  - 이미 샀으면 팔지 말지
  - 안샀으면 살지 말지
  - 그리고 최대값을 리턴
- 다이나믹으로 해결해야 함
- 여기서 수익 = 그냥 내가 가지고 있는 돈 이므로 얼마에 샀는지 이런거 계산할 필요 없음
- 세개의 변수 선언
  - 현재 팔것인가
  - 현재 살것인가
  - 현재 그대로 있을 것인가
- 루프를 돌면서 계산
  - 현재 사겠다고 하면 둘 중에 큰 값을 저장
    - 가지고 있는 돈 - 주식 가격 
    - 기존에 샀을수도 있으니 기존에 샀을때 내 이익
  - 현재 팔겠다고 하면 샀을때 최대 이익 + 주식 가격
  - 현재 유지하겠다고 하면 셋 중에 그냥 셋중에 제일 큰 값을 저장
- 마지막에 제일 큰 값 리턴

어떤 경우에 활용 가능할까
- 복잡해 보이지만 그냥 상태 3개를 누적하는 것과 동일
- 상태 전이가 일어날 수 있는 모든 경우
- FSM을 그려서 상태에 따른 변화를 체크해보면 됨

첨언
- 사실 맞는지 잘 모르겠음...
- 상태까진 맞는거같은데 이상하길래 짜증나서 buy, sell, cool 막 바꿨더니 됨...
"""
class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        buy = -prices[0]
        sell = 0
        cool = 0
        
        for i in range(1, len(prices)):
            buy_temp = max(buy, cool - prices[i])
            sell_temp = buy + prices[i]
            cool_temp = max(buy, sell, cool)
            sell, buy, cool = sell_temp, buy_temp, cool_temp
        
        return max(sell, buy, cool)
    
    def maxProfitByRecur(self, prices: List[int]) -> int:
        def maxProfitRecur(prices, status, bought, profit):
            if len(prices)==0:
                return profit
            elif len(prices)==1:
                if status==1:
                    return profit + (prices[0] - bought)
                else:
                    return profit
            
            if status==0:
                return max(maxProfitRecur(prices[1:], 0, 0, profit), maxProfitRecur(prices[1:], 1, prices[0], profit))
            else:
                return max(maxProfitRecur(prices[2:], 0, 0, profit + (prices[0] - bought)), maxProfitRecur(prices[1:], 1, bought, profit))
            
        return maxProfitRecur(prices, 0, 0, 0)
