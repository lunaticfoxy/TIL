/*
주소: https://leetcode.com/problems/same-tree/

내용
- 두 바이너리 트리가 주어진다
- 두 트리의 내용이 동일한지 체크하라

예제
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

풀이방법
- 단순 구현
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
    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        if(p == null) {
            if (q == null)
                true
            else
                false
        }
        else if(q == null)
            false
        else {
            if(p.value != q.value)
                false
            else
                (isSameTree(p.left, q.left) && isSameTree(p.right, q.right))
        }
        
    }
}
