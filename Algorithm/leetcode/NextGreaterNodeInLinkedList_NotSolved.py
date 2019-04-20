"""
제목: Next Greater Node In Linked List

주소: https://leetcode.com/problems/next-greater-node-in-linked-list/

내용
- 현재 위치에서 현재 값 뒤에 있는 값중 제일 큰 값을 저장하라
- 자기 뒤에 자기보다 큰 값이 없으면 0을 저장하라

샘플
Input: [2,1,5]
Output: [5,5,0]

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]

풀이과정
- 해결중
- 현재 문제가 되는 부분이 0이 되는 지점 찾는 방법
- 스택을 사용해서 해결할 수 있을듯 한데 나중에 다시 시도할것

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        greater = []
        reverse = []
        
        cnt = 0
        before = head.val
        cur = head.next
        idx = -1
        last_val = before
        while cur:
            cnt += 1
            idx += 1
            
            print("---" + str(idx))
            if cur.val > before:
                for _ in range(cnt):
                    greater.append(cur.val)
                cnt = 0
                last_val = cur.val
            elif cur.val <= last_val:
                print("in")
                greater.append(0)
                cnt -= 1
            
            before = cur.val
            cur = cur.next
        
        for _ in range(cnt+1):
            greater.append(0)
        return greater
    
