/*
주소: https://leetcode.com/problems/product-of-array-except-self/

내용
- 정수 배열이 주어진다
- 자기 자신을 제외한 나머지 값들의 곱을 구하라
- 단 모든 수의 곱은 32비트 정수 내의 값이 나온다는걸 보장한다

예제
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


풀이방법
- 단순 구현이나 몇가지 고려사항 필요
- case 1. 0이 1개 있을때
  - 모든 수의 곱은 0이므로 0만 제외하고 나머지를 곱한다
  - 0에서는 나머지 수의 곱, 나머지 수에서는 0을 리턴한다
- case 2. 0이 2개 이상 있을때
  - 무조건 0만 리턴한다
- case 3. 0이 없을 때
  - 전체의 곱에서 현재의 값을 나눈 값을 리턴한다
*/

object Solution {
  def productExceptSelf(nums: Array[Int]): Array[Int] = {
    val filtered = nums.filter(_ != 0)
    val prodAll = if(filtered.isEmpty) 0 else filtered.product
    val zeroCont = nums.count(_ == 0)

    nums.map{x =>
      if(zeroCont >= 2)
        0
      else {
        if(x == 0)
          prodAll
        else if(zeroCont >= 1)
          0
        else
          prodAll / x
      }
    }
  }
}
