"""
주소: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

내용
- 바이너리 숫자가 문자열로 주어진다
- 이때 짝수면 2로 나누고 홀수면 1을 더한다
- 값이 1일 될때까지 몇번 연산해야되는지 알아내라

샘플
Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

Example 3:
Input: s = "1"
Output: 0

풀이방법
- 단순구현


"""
class Solution:
    def numSteps(self, s: str) -> int:
        
        def recurFunc(s, cnt):
            if s[0] == "1" and len(s) == 1:
                return cnt
            elif s[0] == "0":
                return recurFunc(s[1:], cnt + 1)
            else:
                i = 0
                changed = False
                for i in range(len(s)):
                    if s[i] == "0":
                        s[i] = "1"
                        changed = True
                        break
                    else:
                        s[i] = "0"
                
                if not changed:
                    s.append("1")
                
                return recurFunc(s, cnt + 1)
            
        rev_s = list(s)
        rev_s.reverse()
        
        return recurFunc(rev_s, 0)
            
        
