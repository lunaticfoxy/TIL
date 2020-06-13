"""
주소: https://leetcode.com/problems/stone-game-iii/

내용
- 정수가 들어있는 배열이 주어지고 Alice와 Bob이 앞에서 부터 1~3개 씩을 선택한다
- 선택한 정수의 합을 점수로 계산했을때 누가 이길지 여부를 리턴하라

풀이방법
- 각자 턴에서 자기 점수를 최대화, 상대편 점수를 최소화 하는 선택을 한다고 한다
- 이를 재귀로 구성하면
  - 1개 선택, 2개 선택, 3개 선택을 재귀로 시뮬레이션
  - 결과중 내 점수 max, 상대편 점수 min 인 값을 선택
- 물론 타임리밋나서 아직 해결필요

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

"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        
        def recurFunc(turn, idx, score_a, score_b):
            if len(stoneValue) <= idx:
                return score_a, score_b
            
            s1 = stoneValue[idx]
            s2 = stoneValue[idx] + stoneValue[idx+1] if(len(stoneValue) > idx+1) else -3000
            s3 = stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2] if(len(stoneValue) > idx+2) else -3000
            
            if turn == 0:
                new_s_a_1, new_s_b_1 = recurFunc(1, idx + 1, score_a + s1, score_b)
                new_s_a_2, new_s_b_2 = recurFunc(1, idx + 2, score_a + s2, score_b)
                new_s_a_3, new_s_b_3 = recurFunc(1, idx + 3, score_a + s3, score_b)
                
                max_a = max(new_s_a_1, new_s_a_2, new_s_a_3)
                min_b = min(new_s_b_1, new_s_b_2, new_s_b_3)
                """
                print("---Alice---")
                print("idx: " + str(idx))
                print("1: " + str(new_s_a_1) + ", " + str(new_s_b_1))
                print("2: " + str(new_s_a_2) + ", " + str(new_s_b_2))
                print("3: " + str(new_s_a_3) + ", " + str(new_s_b_3))
                print("select: " + str(max_a) + ", " + str(min_b))
                """
                if max_a == new_s_a_1 and min_b == new_s_b_1:
                    return new_s_a_1, new_s_b_1
                elif max_a == new_s_a_2 and min_b == new_s_b_2:
                    return new_s_a_2, new_s_b_2
                else:
                    return new_s_a_3, new_s_b_3
            else:
                new_s_a_1, new_s_b_1 = recurFunc(0, idx + 1, score_a, score_b + s1)
                new_s_a_2, new_s_b_2 = recurFunc(0, idx + 2, score_a, score_b + s2)
                new_s_a_3, new_s_b_3 = recurFunc(0, idx + 3, score_a, score_b + s3)
                
                min_a = min(new_s_a_1, new_s_a_2, new_s_a_3)
                max_b = max(new_s_b_1, new_s_b_2, new_s_b_3)
                """
                print("---Bob---")
                print("idx: " + str(idx))
                print("1: " + str(new_s_a_1) + ", " + str(new_s_b_1))
                print("2: " + str(new_s_a_2) + ", " + str(new_s_b_2))
                print("3: " + str(new_s_a_3) + ", " + str(new_s_b_3))
                print("select: " + str(min_a) + ", " + str(max_b))
                """
                if min_a == new_s_a_1 and max_b == new_s_b_1:
                    return new_s_a_1, new_s_b_1
                elif min_a == new_s_a_2 and max_b == new_s_b_2:
                    return new_s_a_2, new_s_b_2
                else:
                    return new_s_a_3, new_s_b_3
            
        score_a, score_b = recurFunc(0, 0, 0, 0)
        
        diff = score_a - score_b
        
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"
        
