"""
주소: https://leetcode.com/problems/cousins-in-binary-tree/

내용
- 이진 트리와 값 두개가 주어진다.
- 이 값 두개에 매칭되는 노드를 찾아 두 노드가 cousine인지 케크하라
- cousine은 같은 레벨에 있으면서 부모가 다른 노드이다


샘플
Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


풀이방법
- queue를 이용해서 레벨 탐색을 하고, 이때 노드 정보 뿐만 아니라 레벨과 부모 노드또한 함께 포함시킨다.
- 탐색중 x와 y값을 가진 노드가 있으면 해당 노드의 정보를 따로 저장해둔다

적용가능분야
- 같은 레벨에 있는 탐색이 필요한 모든 경우?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        
        q.append([root, None, 0])
        xInfo = None
        yInfo = None
        
        while len(q)>0 and not (xInfo and yInfo):
            cur, par, lvl = q.popleft()
            
            if not xInfo and cur.val==x:
                xInfo = [par, lvl]
            
            if not yInfo and cur.val==y:
                yInfo = [par, lvl]
            
            if cur.left:
                q.append([cur.left, cur, lvl+1])
            
            if cur.right:
                q.append([cur.right, cur, lvl+1])
            
        if not (xInfo and yInfo):
            return False
        
        if xInfo[1]==yInfo[1] and not xInfo[0]==yInfo[0]:
            return True
        else:
            return False
            
        
        
        
        
        
