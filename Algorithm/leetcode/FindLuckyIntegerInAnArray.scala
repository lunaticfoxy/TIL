"""
주소: https://leetcode.com/problems/find-lucky-integer-in-an-array/

내용
- 자연수로 이루어진 배열이 주어지고 배열 내에 자기 자신의 값과 같은 수만큼 들어있는 값을 lucky integer라고 한다
- 배열내에서 가장 큰 lucky integer를 찾아라

샘플
Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Example 4:
Input: arr = [5]
Output: -1

Example 5:
Input: arr = [7,7,7,7,7,7,7]
Output: 7

풀이방법
- 단순 구현문제

"""
object Solution {
    def findLucky(arr: Array[Int]): Int = {
        (arr.groupBy(x => x).map(x => (x._1, x._2.size)).filter(x => x._1 == x._2).map(x => x._1) ++ Array(-1)).max
    }
}
