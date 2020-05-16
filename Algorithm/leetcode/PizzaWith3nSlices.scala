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
- DP로 해결
  - 문제를 단순화 해보면
    - 연속되는 값만 선택되지 않도록 n/3 개의 값을 뽑았을때 최대값을 구하는 문제
  - DP로 구성시
    - 배열의 길이가 n일때 m개를 뽑았을때 최대 합을 구하는 형태
    - 배열의 길이를 1부터 1씩 증가시키면서 새로 들어오는 값을 넣을지 아닐지 여부를 결정한다
      - 뽑는다면 연속해서 뽑을수는 없으므로 n-2 지점에서 더하고, 1개 덜 넣은데서 (m-1) 넣어야 되니깐 dp[n-2][m-1] + 뽑은값 형태
      - 뽑지 않는다면 m개 뽑은 가장 마지막 지점 값을 이어와야 되니깐 dp[n-1][m] 형태
  - 이때 circular 를 계산하기 복잡하다
    - 어차피 맨 마지막것과 맨 첫번째꺼는 동시에 뽑을수 없다
    - 그럼 맨 마지막꺼를 빼놓고 계산하고, 맨 첫번째꺼를 빼놓고 계산한다음 둘중에 큰 값을 리턴하자
"""
object Solution {
    def maxSizeSlices(slices: Array[Int]): Int = {
        def maxSum(slices: Array[Int], max_pick: Int, minus2: Array[Int], minus1: Array[Int]): Int = {
            if(minus1 == null)
                maxSum(slices, max_pick, null, (0 to max_pick).map(i => 0).toArray)
            else if(minus2 == null)
                maxSum(slices.drop(1), max_pick, minus1, Array(0) ++ (1 to max_pick).map(i => slices(0)).toArray)
            else if(slices.size == 0) {
                minus1.last
            }
            else {
                maxSum(slices.drop(1),
                       max_pick,
                       minus1,
                       (0 to max_pick).map{i => if(i == 0) 0 else Math.max(minus1(i), minus2(i-1) + slices(0))}.toArray
                )
            }
        }
        
        Math.max(maxSum(slices.drop(1), slices.size/3, null, null), maxSum(slices.take(slices.size-1), slices.size/3, null, null)) 
    }
}
