"""
주소: https://leetcode.com/problems/even-odd-tree/

내용
- 자연수로 이루어진 바이너리 트리가 주어진다
- 이 바이너리 트리의 짝수 레벨에는 오직 홀수값만 들어가야 하며 같은 레벨 내에서 값이 증가해야 하고,
- 홀수 레벨에는 오직 짝수값만 들어가야 하며 같은 레벨 내에서 값이 감소해야 한다.
- 해당 트리가 조건에 만족하는지 여부를 리턴하라

예제
Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Example 4:
Input: root = [1]
Output: true

Example 5:
Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
Output: true


풀이방법
- queue를 이용한 level 순회 구현 문제
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque([])
        queue.append([root, 0])
        
        last_level = -1
        last_val = -1
        while len(queue) > 0:
            cur_node, level = queue.popleft()
            
            if cur_node.val%2 == level%2:
                return False
            
            if level == last_level:
                if level%2 == 0:
                    if cur_node.val <= last_val:
                        return False
                else:
                    if cur_node.val >= last_val:
                        return False
        
            if cur_node.left:
                queue.append([cur_node.left, level + 1])
            
            if cur_node.right:
                queue.append([cur_node.right, level + 1])
                
            last_level = level
            last_val = cur_node.val
        
        return True
            
            
                
