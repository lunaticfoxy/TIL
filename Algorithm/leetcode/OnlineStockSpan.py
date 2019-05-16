"""
주소: https://leetcode.com/problems/online-stock-span/

내용
- 주식의 가격이 하루단위로 들어온다
- 이 가격을 보고 해당 날짜를 포함해서 들어온 가격이 최대값이었던 연속된 구간의 길이를 찾아라


샘플
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.


풀이방법
- 해당 날짜가 최대값이란 이야기는 해당 날짜 이전에 자기보단 큰 값이 나타난 마지막 지점을 찾으란 이야기
- Stack을 사용해서 자기보다 큰 값만 앞에 밑에 놔두고 빼버리자
  - 그리고 빼는 과정에서 나타난 날짜들만큼 더해주면 구간의 길이가 나타남
  - 이때 계산을 위해 값뿐만 아니라 해당 값이 나타난 위치도 저장해놓자

"""
class StockSpanner:
    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        lastIdx = self.idx
        res = 0
        while True:
            if len(self.stack)==0:
                res += (lastIdx+1)
                break
            elif self.stack[-1][0]>price:
                res += (lastIdx - self.stack[-1][1])
                break
            else:
                temp = self.stack.pop()
                res += (lastIdx - temp[1])
                lastIdx = temp[1]
                
        
        self.stack.append([price, self.idx])
        self.idx += 1
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
