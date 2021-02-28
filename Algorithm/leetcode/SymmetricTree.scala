/*
주소: https://leetcode.com/problems/symmetric-tree/

내용
- 바이너리 트리가 주어진다
- 이 바이너리 트리가 거울대칭인지 확인하라

예제
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

풀이방법
- 단순구현
- 두 트리를 재귀로 내려가면서 left == right 인지 체크한다
- 하나라도 false면 모두 false
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
  def compareTwoRecur(node1: TreeNode, node2: TreeNode): Boolean = {
    if(node1 == null){
      if(node2 == null)
        true
      else
        false
    }
    else if(node2 == null)
      false
    else{
      if(node1.value == node2.value)
        compareTwoRecur(node1.left, node2.right) && compareTwoRecur(node1.right, node2.left)
      else
        false  
    }
    
  }

  def isSymmetric(root: TreeNode): Boolean = {
    if(root == null)
      true
    else
      compareTwoRecur(root.left, root.right)
  }
}
