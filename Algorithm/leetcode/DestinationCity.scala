"""
주소: https://leetcode.com/problems/destination-city/

내용
- 한 도시에서 다른 도시로 이동하는 경로가 섞여서 주어진다
- 한 도시는 반드시 한번만 거친다고 하고 루프가 없다고 할 때 도착지가 어딘지 구하라

샘플
Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"


풀이방법
- 단순 구현문제
- 출발지에 나타난 도시와 도착지에 나타난 도시를 비교해서 도착지에만 나타난 도시가 최종 목적지일것이다
- Set의 diff로 계산
"""
object Solution {
    def destCity(paths: List[List[String]]): String = {
        val src = paths.map(x => x.head).toSet
        val dst = paths.map(x => x.last).toSet
        
        dst.diff(src).toSeq.head
    }
}
