/*
주소: https://leetcode.com/problems/most-beautiful-item-for-each-query/

내용
- 각 상품의 가격과 가치가 주어진다
- 주어진 돈으로 구할 수 있는 가장 높은 가치의 상품을 찾아라


예제
Example 1:
Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.

Example 2:
Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  

Example 3:
Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.



풀이방법
- 아직 미해결
- 먼저 가격으로 묶어서 같은 가격에서 가장 큰 가치만 남김
- 이후 리니어 서치로 하면 타임리밋이 나므로 바이너리 서치로 변경 필요

*/
object Solution {
    def maximumBeauty(items: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        
        val maxItems = items.map(i => (i(0), i(1))).groupBy(_._1).map(x => x._1 -> x._2.maxBy(_._2)._2).toMap
        
        queries.map{q =>
            val filtered = maxItems.filter(_._1 <= q).toMap
            
            if(filtered.isEmpty)
                0
            else
                filtered.values.max
        }
    }
}
