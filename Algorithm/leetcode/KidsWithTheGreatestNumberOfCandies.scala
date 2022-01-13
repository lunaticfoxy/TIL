/*
주소: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/

내용
- 아이들별로 가진 사탕 수와 내가 줄 수 있는 추가 사탕개수가 주어진다
- 어떤 아이에게 사탕을 줬을때 그 아이가 가장 많은 사탕을 가진 아이가 되는지 여부를 리턴하라


예제
Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]


풀이방법
- 단순구현

*/
object Solution {
    def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
        val maxCandy = candies.max
        
        candies.map{x =>
            (x + extraCandies) >= maxCandy
        }.toList
    }
}
