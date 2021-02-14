/*
주소: https://leetcode.com/problems/container-with-most-water/

내용
- 길이가 정해진 기둥의 리스트 중 두개의 기둥을 선택해서 그 사이에 물을 가득 채우려 한다
- 채울 수 있는 물의 최대량을 구하라

예제
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2


풀이과정
- 이중 포인터로 양쪽에서 하나씩 줄여가면서 최대값을 저장한다
- 이때 왼쪽 값이 더 크면 오른쪽을 줄이고, 오른쪽이 더 크면 왼쪽을 줄인다

*/
object Solution {
    def maxAreaRecur(height: Array[Int], maxVal: Int): Int = {

    if(height == null || height.length <= 1)
      maxVal
    else{
      val newMaxVal = Math.max(maxVal, Math.min(height.head, height.last) * (height.length - 1))

      if(height.last > height.head)
        maxAreaRecur(height.drop(1), newMaxVal)
      else
        maxAreaRecur(height.dropRight(1), newMaxVal)
    }
  }

  def maxArea(height: Array[Int]): Int = {
    maxAreaRecur(height, 0)
  }
}
