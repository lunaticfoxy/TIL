"""
주소: https://leetcode.com/problems/maximum-binary-tree/

내용: Maximum Binary Tree 만들기...

샘플
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1


풀이방법
- 쉬어가기...
- 이번 주말은 살살...
"""
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        
        max_i = 0
        max_num = nums[0]
        
        for i, num in enumerate(nums):
            if num>max_num:
                max_num = num
                max_i = i
        
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        
        return root
        
