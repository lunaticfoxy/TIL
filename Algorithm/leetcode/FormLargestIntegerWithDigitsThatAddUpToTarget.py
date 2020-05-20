"""
주소: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

내용
- 1부터 9까지의 digit 이 가지는 가중치가 인덱스 0부터 8까지의 배열에 들어있다
- digit을 뽑고 그 가중치들을 더해서 주어진 target 을 만들고 싶다
- 이때 digit을 하나씩 문자로 더해서 가장 큰 수가 되게 만들어라

샘플
Example 1:
Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "997", but "7772" is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
  
Example 2:
Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.

Example 3:
Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It's not possible to paint any integer with total cost equal to target.

Example 4:
Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
Output: "32211"


풀이방법
- 일단 DP로 푸는것 자체는 처음에 이해함
  - dp[x]는 makeString(dp[x-cost[i]], i+1) 이 최대가 되게 하는 i를 찾아 구하면 되겠지
- 처음 시도는 dictionary로 digit을 저장하고 매번 숫자로 변환
  - 977보다 7772가 더 크니깐 요거 계산하려면 digit의 저장이 필요했음
    - 그래서 매번 큰 digit부터 더해서 숫자로 변환
  - 근데 요랬을때 time limit 발생
    - 매번 계산해야되는 코스트가 너무 컸겠지
- 근데 생각해보면
  - 772 => 7727, 777 => 7772 로 넘어오는 cost는 같고
  - 앞에서부터 계산하다보면 772, 777이 모두 한번씩은 등장하겠지?
  - 그렇다면 그냥 신경쓸필요 없이 새로운 digit을 뒤에다 이어붙여도 되겠다
- 따라서 최종적으로
  - dp[0] = 0 으로 초기화
  - dp[x] = dp[x-cost[n]]*10 + (n+1) 을 최대로 만드는 n
  - 단순히 요렇게만 계산하고 마지막에 dp[target]을 

"""
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-1 for _ in range(target + 1)]
        dp[0] = 0
        
        for i in range(1, target+1):
            for j in range(9):
                if i-cost[j]>=0 and dp[i-cost[j]]!=-1:
                    temp = dp[i-cost[j]]*10 + (j+1)
                    if temp > dp[i]:
                        dp[i] = temp
        
        if dp[target] == -1:
            return "0"
        else:
            return str(dp[target])
