"""
주소: https://leetcode.com/problems/deepest-leaves-sum/

내용
- 자연수로 이루어진 바이너리 트리가 주어진다
- 트리의 가장 깊은 레벨 노드들의 합을 구하라

샘플
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

풀이방법
- 레벨 순회 
- 노드 + 레벨을 저장하는 케이스 클래스 별도 구성
- 순회하면서 자기 자식들을 큐에 넣고 레벨 단위 합을 계속 구함
- 순회가 끝났을때 마지막 레벨의 합을 리턴
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([[root, 0]])
        lv_sum = []
        
        while len(queue) > 0:
            cur, level = queue.pop()
            
            if len(lv_sum) <= level:
                lv_sum.append(cur.val)
            else:
                lv_sum[-1] += cur.val
            
            if cur.left:
                queue.appendleft([cur.left, level + 1])
            
            if cur.right:
                queue.appendleft([cur.right, level + 1])
                
        return lv_sum[-1]
