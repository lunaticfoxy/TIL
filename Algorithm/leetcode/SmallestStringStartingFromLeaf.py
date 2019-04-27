"""
주소: Smallest String Starting From Leaf

내용
- 0은 a, 1은 b, ... , 25는 z 형태로 변환된 바이너리 트리가 존재한다
- 리프노드부터 루트까지 타고올라오는 경로에서 나타날 수 있는 사전 순서로 가장 작은 문자열을 구하라
  - 사전순서라는건 abc < bcd < f < ga < gb 이런 이야기
- 단 자식이 하나라도 있다면 그 자식을 무조건 포함시킨다

샘플
Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"

풀이방법
- 기본 아이디어는 단순한 재귀 트리 탐색
- 거기에 문자열을 실시간으로 생성하고 이를 비교하는 형태
- 단 이방법은 속도가 느림... (모든 노드 탐색 들어감)
- 개선 방안
  - 리프노드들을 구한다음 제일 작은것만 남기기
  - 제일 작은게 여러개면 부모로 올라간다음 다시 수행
  - 이를 하나만 남을때까지 반복
  
적용가능분야
- 트리의 역탐색이 필요한 모든 분야

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def compairStr(str1, str2):
            idx = 0

            while True:
                if len(str1)==idx:
                    return str1
                elif len(str2)==idx:
                    return str2

                diff = ord(str2[idx])-ord(str1[idx])

                if diff>0:
                    return str1
                elif diff<0:
                    return str2
                else:
                    idx += 1
                    
        def searchRecur(node:TreeNode, outStr:str):
            outStr = chr(ord("a") + node.val) + outStr
            
            if node.left==None:
                if node.right==None:
                    return outStr
                else:
                    return searchRecur(node.right, outStr)
            elif node.right==None:
                return searchRecur(node.left, outStr)
            else:
                return compairStr(searchRecur(node.left, outStr),
                                  searchRecur(node.right, outStr))
        
        resStr = searchRecur(root, "")
        return resStr
