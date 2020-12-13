"""
주소: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

내용
- 바이너리 트리가 주어진다
- 트리의 같은 레벨 노드끼리 linked list 형태로 연결하고자 한다
- 이런 형태로 트리를 조정하여 루트를 리턴하라
- 가능하면 추가 메모리 없이 구성하라


예제
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
             your function should populate each next pointer to point to its next right node, just like in Figure B. 
             The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


풀이방법
- 풀이방법 1: 큐를 이용한 방법 (추가 메모리 n)
  - 큐를 사용해서 레벨 순회하며 레벨을 함께 집어넣음
  - 각 레벨별로 마지막 노드를 저장하는 lv_last를 생성
  - 현재 노드의 레벨에 해당하는 lv_last가 있을 경우 해당 lv_last 노드의 다음 노드를 현재 노드로 바꾸고, lv_last를 현재 노드로 치환
- 풀이방법 2: 재귀를 이용한 방법 (추가 메모리 0)
  - 재귀를 이용해서 dfs방식으로 순회
  - 부모의 next노드가 이어졌을거라는 기대 하에 동작
  - 현재 노드의 left와 right를 연결
  - 현재 노드의 right와 현재 노드의 next의 left (없으면 right)를 연결

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        lv_last = dict()
        q = deque([(root, 0)])
        
        while len(q) > 0:
            cur, lv = q.popleft()
            
            if lv in lv_last:
                lv_last[lv].next = cur
            
            lv_last[lv] = cur
            cur.next = None
            
            if cur.left:
                q.append((cur.left, lv + 1))
                
            if cur.right:
                q.append((cur.right, lv + 1))
        
        """
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            if root.next.left:
                root.right.next = root.next.left
            elif root.next.right:
                root.right.next = root.next.right
        
        self.connect(root.left)
        self.connect(root.right)
        """
        
        return root
