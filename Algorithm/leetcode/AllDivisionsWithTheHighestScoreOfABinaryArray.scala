/*
주소: https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

*/
object Solution {
    def maxScoreIndices(nums: Array[Int]): List[Int] = {
        
        def countOne(nums: Array[Int], sums: Array[Int]): Array[Int] = {
            if(sums.isEmpty)
                countOne(nums, Array(0))
            else if(nums.isEmpty)
                sums
            else
                countOne(nums.dropRight(1), Array[Int](sums.head + nums.last) ++ sums)
        }
        
        def countZero(nums: Array[Int], sums: Array[Int]): Array[Int] = {
            if(sums.isEmpty)
                countZero(nums, Array(0))
            else if(nums.isEmpty)
                sums
            else
                countZero(nums.drop(1), sums ++ Array[Int](sums.last + (if(nums.head == 0) 1 else 0)))
        }
        
        val cntOne = countOne(nums, Array[Int]())
        val cntZero = countZero(nums, Array[Int]())
        
        def recurFunc(cntOne: Array[Int], cntZero: Array[Int], idx: Int, res: List[Int], maxScore: Int): List[Int] = {
            if(idx >= cntOne.size)
                res
            else {
                val score = cntOne(idx) + cntZero(idx)
                val newRes = if(score == maxScore) res ++ List(idx)
                    else if(score > maxScore) List(idx)
                    else res
                
                recurFunc(cntOne, cntZero, idx + 1, newRes, Math.max(score, maxScore))
            }
        }
        recurFunc(cntOne, cntZero, 0, List[Int](), 0)
    }
}
