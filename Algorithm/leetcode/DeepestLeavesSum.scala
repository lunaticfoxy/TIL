/*
주소: https://leetcode.com/problems/deepest-leaves-sum/

내용
- 자연수로 이루어진 바이너리 트리가 주어진다
- 트리의 가장 깊은 레벨 노드들의 합을 구하라

샘플
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


풀이방법
- 레벨 순회 
- 노드 + 레벨을 저장하는 케이스 클래스 별도 구성
- 순회하면서 자기 자식들을 큐에 넣고 레벨 단위 합을 계속 구함
- 순회가 끝났을때 마지막 레벨의 합을 리턴
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
    def deepestLeavesSum(root: TreeNode): Int = {
        
        case class TreeNodeWithLevel(_level: Int = 0, _treeNode: TreeNode = null) {
            val level: Int = _level
            val treeNode: TreeNode = _treeNode
        }
        
        def funcRecur(queue: Array[TreeNodeWithLevel], levelSum: Array[Int]): Int = {
            if(queue.size == 0)
                return levelSum.last
            
            val curNode = queue(0).treeNode
            val curLevel = queue(0).level
            
            val appendLeft = if(curNode.left != null) Array(TreeNodeWithLevel(curLevel + 1, curNode.left))
                else Array[TreeNodeWithLevel]()
            
            val appendRight = if(curNode.right != null) Array(TreeNodeWithLevel(curLevel + 1, curNode.right))
                else Array[TreeNodeWithLevel]()
            
            val newQueue = queue.drop(1) ++ appendLeft ++ appendRight
            
            val newLevelSum = if(levelSum.size <= curLevel)
                            levelSum ++ Array(curNode.value)
                        else
                            (0 until levelSum.size).map{i => 
                                if(i == curLevel)
                                    levelSum(i) + curNode.value
                                else
                                    levelSum(i)
                            }.toArray
                
            funcRecur(newQueue, newLevelSum)
        }
        
        funcRecur(Array(new TreeNodeWithLevel(0, root)), Array(0))
    }
}
