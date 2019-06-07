"""
주소: https://leetcode.com/problems/flood-fill/

내용
- 2D 이미지가 주어지고 시작 좌표가 주어진다
- 해당 좌표에 그림판의 페인트 (flood fill) 기능을 수행한다
  - 해당 좌표와 같은 색깔을 지닌 영역을 지정한 색깔로 모두 바꾼다
- 수행 이후 결과 이미지를 리턴하라


샘플
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.


풀이방법
- 단순한 너비우선 탐색 문제
- 스택을 사용해서 해결
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srcMap = [[False for _ in range(len(image[i]))] for i in range(len(image))]
        
        start = image[sr][sc]
        stack = [[sr, sc]]
        
        while len(stack)>0:
            cur = stack.pop()
            
            image[cur[0]][cur[1]] = newColor
            srcMap[cur[0]][cur[1]] = True
            
            if cur[0]>0:
                if image[cur[0]-1][cur[1]]==start and not srcMap[cur[0]-1][cur[1]]:
                    stack.append([cur[0]-1, cur[1]])
            
            if cur[0]<len(image)-1:
                if image[cur[0]+1][cur[1]]==start and not srcMap[cur[0]+1][cur[1]]:
                    stack.append([cur[0]+1, cur[1]])
                    
            if cur[1]>0:
                if image[cur[0]][cur[1]-1]==start and not srcMap[cur[0]][cur[1]-1]:
                    stack.append([cur[0], cur[1]-1])
                
            if cur[1]<len(image[0])-1:
                if image[cur[0]][cur[1]+1]==start and not srcMap[cur[0]][cur[1]+1]:
                    stack.append([cur[0], cur[1]+1])
            
        return image
