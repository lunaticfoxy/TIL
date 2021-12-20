/*
주소: https://leetcode.com/problems/maximum-ice-cream-bars/

내용
- 아이스크림의 가격을 담은 배열과 가지고 있는 돈이 주어진다
- 가진 돈으로 아이스크림을 최대 몇개 살 수 있는지 리턴하라

예제
Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.


풀이방법
- 아이스크림 가격을 정렬한뒤 앞에서부터 빼면서 카운트
*/

object Solution {
    def maxIceCream(costs: Array[Int], coins: Int): Int = {
        
        def recurFunc(sortedCosts: Array[Int], coins: Int, cnt: Int): Int = {
            if(sortedCosts.isEmpty)
              cnt
            else if(sortedCosts.head > coins)
              cnt
            else {
                recurFunc(sortedCosts.drop(1), coins - sortedCosts.head, cnt + 1)
            }
        }
        
        recurFunc(costs.sorted, coins, 0)
    }
}
