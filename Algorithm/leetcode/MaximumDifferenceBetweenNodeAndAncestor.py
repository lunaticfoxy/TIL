"""
주소: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

내용
- 바이너리 트리가 주어지고 노드에는 정수 값이 들어간다
- 자식 노드와 조상 노드로 연결된 두 노드 값의 차이의 최대값을 구하라

샘플
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

풀이방법
- 트리이므로 웬만하면 재귀겠지
- 차이의 최대값은 사실상 경로 상에서 최대값과 최소값을 구하라는 이야기이다
  - 최대값 - 최소값 = 차이의 최대값 이니깐
- 먼저 루트의 값을 최대값, 최소값에 저장하고 루트를 최초 탐색 노드로 지정한다
- 이후 자식을 탐색하면서 최대값, 최소값을 재귀로 넘겨준다
- 만약 자식의 값이 최소값보다 작으면 최소값 갱신, 최대값보다 크면 최대값을 갱신한다
- 그리고 탐색할 노드가 None이면 최대값-최소값을 리턴한다


적용 가능 분야
- 트리를 탐색하되 정확한 값이 아닌 이런 대략적인 통계치? 가 필요한 

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def getMaxDiffRecur(node:TreeNode, minVal:int, maxVal:int) -> int:
            if node==None:
                return maxVal-minVal
            
            if node.val < minVal:
                minVal = node.val
            elif node.val > maxVal:
                maxVal = node.val
            
            return max(getMaxDiffRecur(node.left, minVal, maxVal),
                       getMaxDiffRecur(node.right, minVal, maxVal))
        
        if root:
            return getMaxDiffRecur(root, root.val, root.val)
        else:
            return 0
