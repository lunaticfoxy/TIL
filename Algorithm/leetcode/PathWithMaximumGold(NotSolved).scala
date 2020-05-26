"""
주소: https://leetcode.com/problems/path-with-maximum-gold/
"""

object Solution {
    def getMaximumGold(grid: Array[Array[Int]]): Int = {
        
        def recurFunc(grid: Array[Array[Int]], i: Int, j: Int, visited: Set[Int], cur_val: Int): Int = {
            
            val u = if(i > 0 && grid(i - 1)(j) > 0 && !visited.contains((i - 1)*100 + j))
               recurFunc(grid, i - 1, j, visited + ((i - 1) * 100 + j), cur_val + grid(i)(j))
            else
                -1
            
            val d = if(i < grid.size - 1 && grid(i + 1)(j) > 0 && !visited.contains((i + 1)*100 + j))
               recurFunc(grid, i + 1, j, visited + ((i + 1) * 100 + j), cur_val + grid(i)(j))
            else
                -1
            
            val l = if(j > 0 && grid(i)(j - 1) > 0 && !visited.contains(i * 100 + j - 1))
               recurFunc(grid, i, j - 1, visited + (i* 100 + j - 1), cur_val + grid(i)(j))
            else
                -1
            
            
            val r = if(j < grid(0).size - 1 && grid(i)(j + 1) > 0 && !visited.contains(i * 100 + j + 1))
               recurFunc(grid, i, j + 1, visited + (i * 100 + j + 1), cur_val + grid(i)(j))
            else
                -1
            
            Math.max(cur_val + grid(i)(j), u, d, l, r)
        }
        
        (0 until grid.size).map{i =>
            (0 until grid(0).size).map{j =>
                recurFunc(grid, i, j, new Set[Int], 0)
            }
        }.max
    }
}
