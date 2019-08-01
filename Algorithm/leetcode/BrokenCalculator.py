"""
주소: https://leetcode.com/problems/broken-calculator/

내용
- 계산기가 고장나서 *2 와 -1 밖에 안된다
- X에서 시작해서 Y를 만들기 위한 최소 연산 횟수를 구하라

샘플
Example 1:
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:
Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:
Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example 4:
Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.

풀이 과정
- X에서 Y만들기보다 Y에서 X만들기가 쉬워서 코드 작성 (반대도 거의 유사할듯)
  - Y기준에선 /2 와 +1 연산만 가능
- X가 Y보다 클 경우는 같아질때까지 Y에 계속 1을 더하면 된다
- Y가 X보다 크면서 짝수일때는 Y를 반으로 나눈 뒤 과정을 반복한다
- Y가 X보다 크면서 홀수일때는 Y에 1을 더해줘서 짝수로 만든 뒤 과정을 반복한다

"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        cnt = 0
        while Y!=X:
            if Y < X:
                cnt += (X-Y)
                Y = X
            else:
                if Y%2 == 0:
                    Y /= 2
                else:
                    Y += 1
                cnt += 1
        return int(cnt)
