"""
주소: https://leetcode.com/problems/check-if-it-is-a-straight-line/

내용
- x, y 좌표로 이루어진 점들이 2개 이상 주어진다
- 해당 점들이 같은 선 위에 있는지 여부를 리턴하라

샘플
Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


풀이방법
- 3가지 케이스로 나뉜다
- 점이 2개 이하일때 => 무조건 true
- x값이 일정하고 y값만 변할때 => 모든 점에 대해 x값이 coordinates[0]과 같은지 체크한다
- 나머지 경우 => y = ax + b 에서 a, b를 coordinates[0], coordinates[1] 에 대해 구하고 다른 점들이 이 식에 일치하는지 확인한다
"""
object Solution {
    def checkStraightLine(coordinates: Array[Array[Int]]): Boolean = {
        if(coordinates.size == 2)
            return true
        else {
            val x_diff = coordinates(1)(0) - coordinates(0)(0)
            val y_diff = coordinates(1)(1) - coordinates(0)(1)
            
            (if(x_diff == 0)
                coordinates.filter(x => x(0) == coordinates(0)(0)).size
            else {
                val a = y_diff.toDouble/x_diff.toDouble
                val b = coordinates(0)(1) - a*coordinates(0)(0)

                coordinates.filter(x => (a*x(0) + b) == x(1)).size
            })  == coordinates.size
        }
    }
}
