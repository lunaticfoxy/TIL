"""
주소: https://leetcode.com/problems/diameter-of-binary-tree/

내용
- 바이너리 트리가 주어진다
- 이 바이너리 트리 내에서 발생할 수 있는 노드의 최대 거리를 찾아라

샘플
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].


풀이방법
- 바이너리 트리에서 부모 노드는 항상 자식 트리들의 교차점이 된다
- 따라서 자식 노드에서 측정한 최대 거리의 결과는 항상 부모 노드의 결과보다 작거나 같을수밖에 없다
  - 재귀로 풀수있다.
- 세개의 케이스로 나눠서 생각 가능하다
  - 왼쪽 자식 노드에서 발생한 거리가 제일 클 경우 => 왼쪽 자식 노드 거리 리턴
  - 오른쪽 자식 노드에서 발생한 거리가 제일 클 경우 => 오른쪽 자식 노드 거리 리턴
  - 왼쪽 자식의 높이 + 오른쪽 자식의 높이 가 제일 클경우 => 두 자식의 높이의 합 리턴
    - 자식의 높이를 계산해서 리턴값을 두개로 넣는다
    - 둘중에 큰 자식의 높이 + 1을 현재 노드의 높이로 리턴한다
- 이를 루트에서 리프까지 반복하면 결과를 구할 수 있

"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def recFunc(node):
            if node==None:
                return 0, 0
            
            left = recFunc(node.left)
            right = recFunc(node.right)
            
            return max(left[0], right[0])+1, max(left[0]+right[0], left[1], right[1])
        
        return recFunc(root)[1]
