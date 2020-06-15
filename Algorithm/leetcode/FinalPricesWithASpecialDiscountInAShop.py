"""
주소: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

내용
- 물건의 시간별 가격이 주어진다
- 먼저 물건을 샀을때 이후에 더 낮거나 같은 가격이 나오면 이후가격만큼 할인해서 상품의 최종 가격은 이전가격-이후가격 이된다
- 각 시점에 구매한 상품의 최종 가격을 배열로 리턴하라

샘플
Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
For items 3 and 4 you will not receive any discount at all.

Example 2:
Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.

Example 3:
Input: prices = [10,1,1,6]
Output: [9,0,1,6]

풀이방법
- 단순 구현문제
- n^2 보다 빨리 풀수있을거같지만 일단 패스
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            res.append(prices[i])
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res[-1] = prices[i] - prices[j]
                    break
        
        return res
