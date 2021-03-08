/*
주소: https://leetcode.com/problems/number-of-islands/

내용
- 1과 0으로 구성된 매트릭스의 상하좌우가 1로 연결되어있으면 하나의 섬으로 친다
- 맵 내에 몇개의 섬이 있는지 구하라

예제
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


풀이방법
- 단순 구현
*/

object Solution {
  def numIslands(grid: Array[Array[Char]]): Int = {

    def findIsland(queue: List[(Int, Int)], island: Set[(Int, Int)]): Set[(Int, Int)] = {
      if(queue == null || queue.isEmpty)
        island
      else {
        val cur = queue.head

        val left = (if(cur._2 > 0 && grid(cur._1)(cur._2 - 1) == '1' && !island.contains(cur._1, cur._2 - 1))
          List((cur._1, cur._2 - 1))
        else
          List[(Int, Int)]()
          )

        val right = (if(cur._2 < grid(cur._1).length - 1 && grid(cur._1)(cur._2 + 1) == '1' && !island.contains(cur._1, cur._2 + 1))
              List((cur._1, cur._2 + 1))
            else
              List[(Int, Int)]()
          )
          
        val up = (if(cur._1 > 0 && grid(cur._1 - 1)(cur._2) == '1' && !island.contains(cur._1 - 1, cur._2))
          List((cur._1 - 1, cur._2))
        else
          List[(Int, Int)]()
          )
          

        val down = (if(cur._1 < grid.length - 1 && grid(cur._1 + 1)(cur._2) == '1' && !island.contains(cur._1 + 1, cur._2))
          List((cur._1 + 1, cur._2))
        else
          List[(Int, Int)]()
          )

        //println(queue.drop(1) ++ left ++ right ++ up ++ down)
        //println(island ++ left.toSet ++ right.toSet ++ up.toSet ++ down.toSet)
        findIsland(queue.drop(1) ++ left ++ right ++ up ++ down, island ++ left.toSet ++ right.toSet ++ up.toSet ++ down.toSet)
      }
    }


    val visited = collection.mutable.HashSet[(Int, Int)]()

    grid.indices.map{ i =>
      grid(i).indices.map{ j =>
          
        if(grid(i)(j)=='1' && !visited.contains((i, j))) {
          visited ++= findIsland(List((i, j)), Set((i, j)))
          1
        }
        else
          0
      }.sum
    }.sum
  }
}
