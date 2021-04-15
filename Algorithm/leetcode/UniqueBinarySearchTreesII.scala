/*
주소: https://leetcode.com/problems/unique-binary-search-trees-ii/

내용
- 자연수 n이 주어진다
- [1, n] 범위의 숫자를 넣어서 나올 수 있는 서로 다른 모든 Binary Search Tree를 리턴하라

예제
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]


풀이방법
- 중복제거를 나중에 하는건 어렵다
- 처음부터 중복이 생기지 않게 만들자
- 중간 노드 기준으로 left와 right의 중복을 각각 막는다
  - 중간 값을 먼저 결정하고 그것보다 작은 값은 left, 큰 값은 right로 보낸다
  - 이를 값이 없어질때까지 계속 반복한다
  - 그리고 나타난 left, right의 리스트의 모든 조합을 현재 노드에 연결한다
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
  def generateTrees(n: Int): List[TreeNode] = {
    genBST(1, n)
  }


  def genBST(start: Int, end: Int): List[TreeNode] = {
    if(start > end)
      List[TreeNode](null)
    else{
      (start to end).flatMap{mid =>
        genBST(start, mid - 1).flatMap{left =>
          genBST(mid + 1, end).map{right =>
            new TreeNode(mid, left, right)
          }
        }
      }.toList
    }
  }
}
