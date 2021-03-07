/*
주소: https://leetcode.com/problems/balanced-binary-tree/

내용
- 이진 트리의 각 left, right 서브 트리의 depth가 1 이하 차이를 가지고, 이 조건을 모든 서브트리에 대해 만족하는 트리를 balanced binary tree 라고 한다
- 주어진 트리가 balanced binary tree 인지 여부를 리턴하라

예제
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


풀이방법
- 현재 트리가 balanced 할 조건은
  - left, right 서브 트리가 모둔 balanced 하며
  - left, right의 depth 차이가 1 이하여야 한다
- 따라서 재귀로 돌면서 현재 트리의 balanced 여부와 depth를 리턴한다

*/
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def isBalanced(root: TreeNode): Boolean = {
    isBalancedRecur(root, 0)._1
  }
    
  def isBalancedRecur(root: TreeNode, curDepth: Int): (Boolean, Int) ={
    if(root == null)
      (true, curDepth)
    else {
      val ld = isBalancedRecur(root.left, curDepth + 1)
      val rd = isBalancedRecur(root.right, curDepth + 1)

      (ld._1 && rd._1 && Math.abs(ld._2 - rd._2) <= 1, Math.max(ld._2, rd._2))
    }
  }  
}
