"""
주소: https://leetcode.com/problems/stone-game-iii/

내용
- 정수가 들어있는 배열이 주어지고 Alice와 Bob이 앞에서 부터 1~3개 씩을 선택한다
- 선택한 정수의 합을 점수로 계산했을때 누가 이길지 여부를 리턴하라

샘플
Example 1:
Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example 2:
Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

Example 3:
Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

Example 4:
Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"

Example 5:
Input: values = [-1,-2,-3]
Output: "Tie"

풀이방법
- 각자 턴에서 자기 점수를 최대화, 상대편 점수를 최소화 하는 선택을 한다고 한다
- 이를 재귀로 구성하면
  - 1개 선택, 2개 선택, 3개 선택을 재귀로 시뮬레이션
  - 결과중 max(내 점수 - 상대편 점수) 인 값을 선택
- 이를 dp로 바꾸면
  - 맨 뒤에서부터 차례로 현재 지점을 선택했을 때 얻을수 있는 최대 점수 차를 저장한다
  - 맨 뒤에 3개는 수동으로 계산해주고
  - 다음부터는 dp[i]를 다음중 가장 큰 값으로 갱신
    - value[i] - dp[i+1]
    - value[i] + value[i+1] - dp[i+2]
    - value[i] + value[i+1] + value[i+2] - dp[i+3]
  - 이후 dp[0] 에 있는 값이 먼저 선택한 Alice가 Bob에 비해 얻을 수 있는 점수차일것
    - 0보다 크면 Alice 승리, 0이면 무승부 0보다 작으면 Bob 승리
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0 for _ in range(len(stoneValue))]
        
        if len(stoneValue) > 0:
            dp[-1] = stoneValue[-1]
        else:
            return "Tie"
        
        if len(stoneValue) > 1:
            dp[-2] = max(stoneValue[-1] + stoneValue[-2], stoneValue[-2] - stoneValue[-1])
            
        if len(stoneValue) > 2:
            dp[-3] = max(stoneValue[-1] + stoneValue[-2] + stoneValue[-3],
                        stoneValue[-2] + stoneValue[-3] - stoneValue[-1],
                         stoneValue[-3] - dp[-2])
        
        for i in range(len(stoneValue)-4, -1, -1):
            s_3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
            s_2 = stoneValue[i] + stoneValue[i+1] - dp[i+2]
            s_1 = stoneValue[i] - dp[i+1]
            
            dp[i] = max(s_1, s_2, s_3)
        
        #print(dp)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
