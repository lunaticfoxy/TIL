/*
주소: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

내용
- 정수 배열과 자연수 k 가 주어진다
- 배열에서 임의의 k 개 원소를 제거했을때 남길수 있는 가장 적은 수의 unique 한 원소의 수를 찾아라

샘플
Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

풀이방법
- counter 형태로 만든 뒤 오름차순으로 정렬하고
- 이후 앞에서부터 하나씩 빼면서 k가 0보다 작아지는 지점 직전에서 멈춘다
- 그리고 남은 원소의 개수를 구한다
*/
object Solution {
    def findLeastNumOfUniqueInts(arr: Array[Int], k: Int): Int = {
        val sorted = arr.groupBy(x => x).mapValues(_.size).toArray.sortWith(_._2 < _._2)
        
        def findLeast(arr: Array[(Int, Int)], k: Int): Int = {
            if(k==0)
                arr.size
            else {
                if(arr(0)._2 <= k)
                    findLeast(arr.drop(1), k - arr(0)._2)
                else
                    arr.size
            }
                
        }
        
        findLeast(sorted, k)
    }
}
