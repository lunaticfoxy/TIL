"""
주소: https://leetcode.com/problems/validate-stack-sequences/

내용
- 시퀀스가 주어지고, 이 시퀀스를 stack에 넣었다가 모두 pop할 예정이다.
- push와 pop만 사용해서 popped 시퀀스가 생성될수 있는지 여부를 리턴하라


샘플
Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


풀이방법
- 간단하다 해보면 된다.
- 각 아이템별로 pop 된단 이야기는 stack의 top에 해당 아이템이 존재한다는 이야기
- 따라서 stack의 top에 해당 아이템이 존재할때까지 시퀀스를 push해서 아이템이 나타나는지 보면 된다.
- 이게 모든 아이템에 대해 성립하면 가능한 시퀀스
- 한 아이템이라도 안된다면 불가능한 시퀀스

"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushIdx = 0
        
        for item in popped:
            while len(stack)==0 or not stack[-1]==item:
                if pushIdx>=len(pushed):
                    return False
                
                stack.append(pushed[pushIdx])
                pushIdx += 1
            stack.pop()
            
        return True
