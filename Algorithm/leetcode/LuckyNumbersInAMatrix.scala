"""
주소: https://leetcode.com/problems/lucky-numbers-in-a-matrix/

내용
- row 중에서 가장 작고, col 중에서 가장 큰 값을 lucky number라 한다
- 매트릭스가 주어질때 모든 lucky number를 구하라
- 단, 매트릭스의 모든 원소는 distinct 하다

샘플
Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]


풀이방법
- 단순 구현 문제
- 모든 원소가 distinct 하다는 조건이 있으므로 row 단위 min, col 단위 max만 구해서 교집합을 구한다
- 만약 distinct가 아닐경우 인덱스로 row 단위 min, col 단위 max 위치를 구한다음 교집한을 구하고 값을 찾아야 한다

"""
object Solution {
    def luckyNumbers (matrix: Array[Array[Int]]): List[Int] = {
        val minInRows = matrix.map(x => x.min)
        val maxInCols = (0 until matrix(0).size).map(i => matrix.map(y => y(i)).max)
        minInRows.toSet.intersect(maxInCols.toSet).toList
    }
}
