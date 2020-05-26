"""
주소: https://leetcode.com/problems/path-with-maximum-gold/
"""
object Solution {
    def getMaximumGold(grid: Array[Array[Int]]): Int = {
        
        def recurFunc(grid: Array[Array[Int]], i: Int, j: Int, visited: Set[Int], cur_val: Int): Int = {
            Math.max(cur_val + grid(i)(j),
                Math.max(
                    if(i > 0 && grid(i - 1)(j) > 0 && !visited.contains((i - 1)*100 + j))
                       recurFunc(grid, i - 1, j, visited + ((i - 1) * 100 + j), cur_val + grid(i)(j))
                    else
                        -1,
                    Math.max(
                        if(i < grid.size - 1 && grid(i + 1)(j) > 0 && !visited.contains((i + 1)*100 + j))
                           recurFunc(grid, i + 1, j, visited + ((i + 1) * 100 + j), cur_val + grid(i)(j))
                        else
                            -1,
                        Math.max(
                            if(j > 0 && grid(i)(j - 1) > 0 && !visited.contains(i * 100 + j - 1))
                               recurFunc(grid, i, j - 1, visited + (i* 100 + j - 1), cur_val + grid(i)(j))
                            else
                                -1,
                            if(j < grid(0).size - 1 && grid(i)(j + 1) > 0 && !visited.contains(i * 100 + j + 1))
                               recurFunc(grid, i, j + 1, visited + (i * 100 + j + 1), cur_val + grid(i)(j))
                            else
                                -1
                        )
                    )
                )
            )
        }
        
        (0 until grid.size).map{i =>
            (0 until grid(0).size).map{j =>
                if(grid(i)(j) == 0)
                    -1
                else
                    recurFunc(grid, i, j, Set(i*100 + j), 0)
            }.max
        }.max
    }
}
