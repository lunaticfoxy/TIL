/*
주소: https://leetcode.com/problems/kth-distinct-string-in-an-array/

내용
- 문자열로 이루어진 배열과 자연수 K가 주어진다
- 배열의 원소중 distinct 한 원소를 찾아 그중 k번째로 나타난 원소를 구하라
- distinct 한 원소가 k개가 안되면 "" 를 리턴하라

예제
Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


풀이방법
- 재귀로 배열을 순환하며 맵에 문자열과 처음 나타난 지점을 저장
  - 두번 이상 나타날 경우 처음 나타난 지점을 -1로 체크하고 최종 리턴시에 필터링
- 이후 나타난 순서대로 정렬하여 k-1 인덱스에 있는 문자열을 리턴 

*/

object Solution {
  def kthDistinct(arr: Array[String], k: Int): String = {

    def recurFunc(arr: Array[String], m: Map[String, Int], idx: Int): Map[String, Int] = {
      if(arr.isEmpty)
        m.filter(_._2 >= 0)
      else {
        if(m.contains(arr.head))
          recurFunc(arr.drop(1), m.updated(arr.head, -1), idx + 1)
        else
          recurFunc(arr.drop(1), m ++ Map((arr.head, idx)), idx + 1)
      }
    }

    val m = recurFunc(arr, Map[String, Int](), 0)

    val sortedArr = m.toArray.sortBy(_._2)

    if(sortedArr.length < k)
      ""
    else
      sortedArr(k - 1)._1
  }
}
