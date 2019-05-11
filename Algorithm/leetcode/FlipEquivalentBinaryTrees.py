"""
주소: https://leetcode.com/problems/flip-equivalent-binary-trees/

내용
- 두개의 바이너리 트리가 주어진다
- 이 트리의 노드들을 좌우로 뒤집기만 해서 같은 트리로 만들수 있는지 여부를 리턴하라

샘플
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

풀이방법
- 좌우로 뒤집기만 해서 같은 트리가 된다는 이야기는 부모-자식 관계가 모두 일치하면 된다는 말
- 따라서 부모의 값을 비교해서 같으면 자식중 값이 같은 애들끼리 다시 재귀를 수행해서 결과를 리턴하면 됨
- 다음과 같이 재귀 반복
  - 먼저 엣지케이스
    - 두 노드 다 None이면 True 리턴
    - 한 노드만 None이면 False 리턴
  - 이후 두 노드의 값을 체크해서 다르면 False 리턴
  - 그리고 왼쪽자식-왼쪽자식에 대해 재귀 수행
    - 위 결과가 True면 오른쪽자식-오른쪽자식에 대해 재귀 수행 결과를 리턴
    - 위 결과가 False면 왼쪽자식-오른쪽자식에 대해 재귀 수행
      - 위 결과가 True면 오른쪽자식-왼쪽자식에 대해 재귀 수행 결과를 리턴
      - 위 결과가 False면 False 리턴


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1:
            if not root2:
                return True
            else:
                return False
        elif not root2:
            return False
        elif not root1.val==root2.val:
            return False
        
        rev = False
        leftRes = self.flipEquiv(root1.left, root2.left)
        
        if not leftRes:
            rev = True
            leftRes = self.flipEquiv(root1.left, root2.right)
        
        if not leftRes:
            return False
        
        if rev:
            return self.flipEquiv(root1.right, root2.left)
        else:
            return self.flipEquiv(root1.right, root2.right)
