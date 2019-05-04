"""
주소: https://leetcode.com/problems/add-to-array-form-of-integer/

내용
- 각 자리수마다의 숫자를 표시한 어레이와 다른 0 이상의 정수가 주어진다
- 두 수의 합을 구하고 이를 어레이로 표현하라

샘플
Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


풀이방법
- 쉬운문제 어렵게풀기...?
- 단순히 한 자리수마다 비교하면 되지만 올림수를 처리하는게 이슈
- 가장 단순한 방법 사용
  - 매 자리마다 실제로 덧셈을 계산한 다음
  - 결과값을 마지막에 어레이로 변환
- 더 빠르게 할 수 있는 방법?
  - 변환과정없이 바로 어레이로 집어넣기
  - 이 경우 자릿수는 10 이상일경우 플래그를 두고 다음 자리 계산시 더하면 됨
"""
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res:int = 0
        mp:int = 1
        for i in range(len(A)):
            res += int(mp*((K%10)+A[-(i+1)]))
            mp *= 10
            K = K//10
            
        res += K*mp
        resList = []
        
        if res==0:
            return [0]
        
        while res>0:
            resList.append(int(res%10))
            res = res//10
            
        
        return resList[::-1]
