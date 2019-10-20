"""
주소: https://leetcode.com/problems/check-if-it-is-a-straight-line/

내용
- 주어진 좌표의 점들이 직선상에 있는지 확인하라

예시
Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


풀이방법
- 단순 구현문제로 기울기만 구해서 비교하면 됨
- 단 함정으로 기울기가 무한대일경우가 있으므로 그부분만 따로 처리

"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<2:
            return True
        
        coor = coordinates
        
        if coor[1][0]==coor[0][0]:
            for i in range(2, len(coor)):
                if coor[i][0] != coor[0][0]:
                    return False
            return True
        else:
            slope = float(coor[1][1] - coor[0][1])/float(coor[1][0] - coor[0][0]) 

            for i in range(2, len(coor)):
                newSlope = float(coor[i][1] - coor[0][1])/float(coor[i][0] - coor[0][0])
                if newSlope != slope:
                    return False

            return True
