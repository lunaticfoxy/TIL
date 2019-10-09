"""
주소: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

내용
- 정수로 이루어진 바이너리 트리가 주어진다
- 이 트리의 각 레벨별 원소의 합을 계산했을때 가장 큰 합을 가지는 레벨을 리턴하라
- 레벨은 1부터 시작된다


예시
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


풀이방법
- 레벨순회를 할수 있는지 묻는 문제
- 큐를 쓰면 된다 나머지는 단순 구현
"""
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        maxLevel = -1
        maxLS = -1
        
        lastLevel = 0
        levelSum = 0
        q = deque()
        q.append([root, 1])
        
        
        while len(q)>0:
            cur, level = q.popleft()
            
            if level != lastLevel:
                if maxLevel==-1 or levelSum > maxLS:
                    maxLS = levelSum
                    maxLevel = lastLevel
                
                lastLevel = level
                levelSum = 0
            
            levelSum += cur.val
            
            if cur.left:
                q.append([cur.left, level + 1])
            
            if cur.right:
                q.append([cur.right, level + 1])
        
        if maxLevel==-1 or levelSum > maxLS:
            maxLS = levelSum
            maxLevel = lastLevel
        
        
        return maxLevel
