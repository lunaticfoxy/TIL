"""
 주소: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
 
 내용
 - 오름차순 기준의 바이너리 서치트리가 주어진다
 - 이 트리를 Greater Sum Tree로 변환해야 된다
 - Greater Sum Tree는 자신의 값에는 오른쪽 노드 자식 값+자신의 값 을 저장하고 자기 왼쪽 자식은 부모의 값 + 자신의 값 + 오른쪽 노드 자식 값 을 값으로 가지는 트리를 말한다
   - 실제 샘플 보면 이해될것
   
샘플
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

풀이방법
- 특성을 이해하고 그대로 리커시브로 표현만 하면 된다.
- 이를 right, 자신, left 순서로 순회하면서 해결하면 됨
- 상세한 내용은 생략

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recurFunc(node, addVal):
            if not node:
                return None, 0
            
            if node.right:
                node.right, rightVal = recurFunc(node.right, addVal)
                node.val += rightVal
            else:
                node.val += addVal
            
            leftVal = node.val
            
            if node.left:
                node.left, leftVal = recurFunc(node.left, node.val)
            
            return node, leftVal
        
        root, _ = recurFunc(root, 0)
        return root
