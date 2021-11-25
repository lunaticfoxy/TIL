/*
주소: https://leetcode.com/problems/two-furthest-houses-with-different-colors/

내용
- 0 이상의 정수로 이루어진 배열이 주어진다
- 서로 다른 숫자 사이의 가장 먼 거리를 구하라

예제
Example 1:
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.

Example 2:
Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

Example 3:
Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.


풀이방법
- 각 숫자별로 min, max 인덱스를 계산
- min 가장 작은 값 두개, max 중 가장 큰 값 두개를 추출
  - 구현상 편이성을 위해 정렬후 두개씩 추출
- 이후 이 숫자들의 차이중 가장 큰 값을 출력

*/
object Solution {
    def maxDistance(colors: Array[Int]): Int = {

      val colorDistinct = colors.distinct

      if(colorDistinct.length <= 1)
        0
      else {
        val colorsWithIdx = colors.zipWithIndex

        val minMax = colorDistinct.map { c =>
          val indices = colorsWithIdx.filter(_._1 == c).map(_._2)

          (c, indices.min, indices.max)
        }

        val min = minMax.sortBy(_._2)
        val max = minMax.sortBy(-_._3)

        if (min(0)._1 == max(0)._1)
          Math.max(max(0)._3 - min(1)._2, max(1)._3 - min(0)._2)
        else
          max(0)._3 - min(0)._2
      }
    }
  }
