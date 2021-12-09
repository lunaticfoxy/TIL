"""
주소: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

내용
- 링크드리스트가 주어진다
- 이 링크드리스트에서 가운데 원소를 삭제한 뒤 헤드를 리턴하라
- 링크드리스트가 짝수라면 n/2 + 1 번째 원소를 지워라

예제
Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


풀이방법
- 두개의 리스트 포인터를 만들고 하나는 중간, 하나는 끝을 가리키게 한다
- 중간을 가리키는 포인터는 한번에 한칸, 끝을 가리키는 포인터는 두칸씩 이동한다
- 끝을 가리키는 포인터가 리스트의 끝에 다다르면 중간 포인터가 가리키는 노드를 삭제한다
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        middle = head
        middle_before = None
        
        while last.next != None:
            middle_before = middle
            middle = middle.next
            last = last.next
            
            if last.next != None:
                last = last.next
        
        if middle_before == None:
            return None
        else:
            middle_before.next = middle.next
            return head
        
        
