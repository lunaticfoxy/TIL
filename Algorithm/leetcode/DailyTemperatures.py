"""
주소: https://leetcode.com/problems/daily-temperatures/

내용
- 매일매일 기온의 리스트가 주어진다
- 해당 날짜 기준으로 해당 날짜보다 며칠이 지나야 더 높은 기온이 등장하는지를 리스트로 반환하라
- 해당 날짜 이후에 해당 날짜보다 높은 기온이 없으면 0을 리스트로 넣는다

샘플
T = [73, 74, 75, 71, 69, 72, 76, 73]
output should be [1, 1, 4, 2, 1, 1, 0, 0].

풀이방법
- 어차피 정해진 길이의 리스트를 반환하니 미리 정답 리스트를 0으로 초기화하고 계산하면서 값을 넣는다
- 스택에 새로운 값을 넣되 내림차순으로 쌓이게 한다
- 전체 리스트를 반복하면서
  - 혹시 스택이 비어있으면 값을 이어서 붙이고
  - 스택의 top이 현재 값보다 커도 이어 붙인다.
  - 스택의 top을 비교하면서 top이 현재값보다 작으면 값을 꺼내서 정답 리스트 내에서 해당 값의 위치에 현재 값의 위치의 차이만큼을 넣는다

"""
from collections import deque

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(T))]
        
        for i in range(len(T)):
            while len(stack)>0 and stack[-1][0]<T[i]:
                temp = stack.pop()
                res[temp[1]] = i-temp[1]
            stack.append([T[i], i])
        
        return res
