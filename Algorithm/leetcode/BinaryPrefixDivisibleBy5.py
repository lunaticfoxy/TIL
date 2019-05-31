"""
주소: https://leetcode.com/problems/binary-prefix-divisible-by-5/

내용
- 바이너리 숫자가 앞에서부터 한자리씩 주어지고 해당 자리까지만을 계산해서 현재 숫자로 지정한다
- 현재 숫자가 5로 나누어 떨어지는지 여부를 리스트로 리턴하라

샘플
Example 1:
Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: [1,1,1]
Output: [false,false,false]

Example 3:
Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]

Example 4:
Input: [1,1,1,0,1]
Output: [false,false,false,false,false]


풀이방법
- 단순 구현문제 연습용
"""
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        
        lv = 0
        for i in range(len(A)):
            lv = 2*lv + A[i]
            if lv%5==0:
                res.append(True)
            else:
                res.append(False)
        
        return res
