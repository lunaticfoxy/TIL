"""
주소: https://leetcode.com/problems/sum-of-left-leaves/

내용
- 바이너리 트리가 주어진다
- 이 트리에 들어있는 모든 left leaf 노드의 합을 구하라

샘플

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


풀이방법
- 단순 구현
"""
object Solution {
    def sumOfLeftLeaves(root: TreeNode): Int = {
        if(root == null)
            0
        else {
            val leftVal = if(root.left != null) {
                if(root.left.left != null || root.left.right != null)
                    sumOfLeftLeaves(root.left)
                else
                    root.left.value
            }
            else
                0

            val rightVal = sumOfLeftLeaves(root.right)

            leftVal + rightVal
        }
    }
}
