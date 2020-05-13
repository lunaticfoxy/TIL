"""
주소: https://leetcode.com/problems/pizza-with-3n-slices/

내용
- 피자판이 3n의 조각으로 잘라져 있고 이게 배열로 주어진다
- 내가 n번째 조각을 선택하면 다른 사람들이 n-1, n+1 번째 조각을 선택한다
- 이렇게 선택하는 과정을 반복할때 내가 얻을 수 있는 조각의 크기의 합의 최대를 구하라

샘플
Example 1:
Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

Example 2:
Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.

Example 3:
Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21

Example 4:
Input: slices = [3,1,2]
Output: 3

풀이방법
- 재귀 시도
  - 답 자체는 나옴
  - 하지만 당연하게도 메모리 리밋 발생
    - 꼬리재귀도 안되니
- DP로 시도 예정
"""
object Solution {
    def maxSizeSlices(slices: Array[Int]): Int = {
        if(slices.size == 0)
            0
        else if(slices.size == 3)
            slices.max
        else
            (0 to slices.size - 1).map{x =>
                (if(x == 0)
                    maxSizeSlices(slices.drop(2).take(slices.size - 3))
                else if(x == slices.size - 1)
                    maxSizeSlices(slices.drop(1).take(slices.size - 3))
                else
                    maxSizeSlices(slices.take(x - 1) ++ slices.drop(x + 2))) + slices(x) 
            }.max
        
    }
}
