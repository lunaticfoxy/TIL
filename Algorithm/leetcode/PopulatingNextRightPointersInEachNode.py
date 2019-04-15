"""
주소: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

내용
- 단순 바이너리 트리가 주어진다.
- 이 트리의 같은 레벨에 있는 노드들끼리 연결되도록 리스트를 구성하라

샘플
Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
(실제로른 트리 루트가 주어지고 그 트리를 변경하면 됨)

풀이 방법
- 복잡해보이지만 별거 없다. 레벨순회일뿐
- 레벨 순회에서 사용하는 방법은 당연히 큐
- 다만 레벨 단위로 관리를 해야하기때문에 큐에 노드뿐만 아니라 현재 레벨의 위치 또한 저장하면서 순회
- 빈칸이 있을경우에는 다음 노드로 건너뛰고 레벨이 바뀔경우 새로운 노드로 시작

적용 가능 분야
- 레벨 순회 자체는 많이 사용됨
- 다만 이런 형태를 쓸 경우는 한번 순회가 아니라 자주 참조가 필요할 경우
- 구문분석에서도 비슷하게 적용 가능할것이라 
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = deque()
        
        if root:
            queue.append([root, 0])
        
        before = None
        before_level = -1
        
        while len(queue)>0:
            cur, cur_level = queue.popleft()
            
            if before_level==cur_level and before:
                before.next = cur
            
            before = cur
            before_level = cur_level
            
            if cur.left:
                queue.append([cur.left, cur_level+1])
            
            if cur.right:
                queue.append([cur.right, cur_level+1])
