/*
주소: https://leetcode.com/problems/arithmetic-subarrays/

내용
- 정수로 이루어진 배열 1개와 (n), 0이상의 정수로 이루어진 배열 두개가 (l, r) 주어진다
- 0 <= i < length(l) 일때 n의 [ l[i] , r[i] ] 구간의 subarray 를 s[i] 라 하자
- s[i] 의 원소들의 순서를 변경하여 등차수열을 만들 수 있는지 여부를 구하라
- 그리고 그 결과를 배열로 리턴하라


예제
Example 1:
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.

Example 2:
Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]



풀이방법
- subarray를 만든뒤 각 subarray를 정렬
- 정렬한 배열이 등차수열인지 재귀로 체크한다

*/


object Solution {
  def checkArithmeticSubarrays(nums: Array[Int], l: Array[Int], r: Array[Int]): List[Boolean] = {

    def recurFunc(nums: Array[Int], lastDiff: Int, isStart: Boolean = false): Boolean = {
      if(nums.length <= 1)
        true
      else {
        if(isStart)
          recurFunc(nums.drop(1), nums(1) - nums(0))
        else if((nums(1) - nums(0)) == lastDiff)
          recurFunc(nums.drop(1), lastDiff)
        else
          false
      }
    }

    l.zip(r).map{case (a, b) =>
      val subNums = nums.dropRight(nums.length - b - 1).drop(a)

      recurFunc(subNums.sorted, -1, true)
    }.toList
  }
}
