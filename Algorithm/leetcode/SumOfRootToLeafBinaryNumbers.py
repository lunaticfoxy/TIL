"""
주소: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

내용
- Binary Tree에 노드별로 1 또는 0이 들어가 있다
- 루트부터 리프노드까지 값을 이어서 2진수로 생각한다
  - 리프노드의 기준은 자식이 하나도 없는 노드
- 나타나는 모든 이진수의 합을 구하라

샘플
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

풀이방법
- 단순 재귀로 풀 수 있음
- 기존 값이 한단계씩 내려올때마다 2배가 되고 거기다 현재 값이 더해지는 형태
- 속도가 느리긴 하지만 반복 or 다른 방법으로 해결 가능해보임

적용가능분야
- 트리 형테 데이터의 값 누적에 사용 가능함
- 다만 이런 형태보다는 반대 형태가 많을듯

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sumRecur(node, val):
            val = val*2 + node.val
            
            if node.left == None:
                if node.right == None:
                    return val
                else:
                    return sumRecur(node.right, val)
            elif node.right == None:
                return sumRecur(node.left, val)
            else:
                return sumRecur(node.left, val) + sumRecur(node.right, val)
                
        return sumRecur(root, 0)
        
