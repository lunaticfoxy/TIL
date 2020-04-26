"""
주소: https://leetcode.com/problems/longest-happy-string/submissions/

내용
- a, b, c로만 문자열을 만들려 하고 문자열 내에는 같은 문자가 연속해서 3개 이상 나타나면 안된다
- 최대 사용가능한 a, b, c의 개수가 주어질때 만들수 있는 가장 긴 문자열을 출력하라
  - 복수정답 허용

샘플
Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 


풀이과정
- 3개중 가장 많이 남은 값을 이어 붙이는 과정을 반복하면 된다
- 이때 min(2, 남은값)을 출력한다
- 만약 가장 많이 남은 값이 기존에 붙인 값이라면 그 다음 많이 남은 값을 한개만 출력한다
- 이어 붙일 값이 없다면 종료한다
- 추가 가능한 시도
  - min(2, 2위와 1위의 차이)
  - 2개 이어붙인 뒤에는 반드시 1개 이어붙이기

"""
object Solution {
    def longestDiverseString(a: Int, b: Int, c: Int): String = {
        
        case class ArrVal(remained:Int, strVal:String) {
        }
        
        
        def mkString(str:String, vals:Array[ArrVal], last:ArrVal): String = {
            //println("--------------")
            //println(str)
            val newVals = vals.sortBy(_.remained).reverse
            //println(newVals.map(_.remained).mkString(","))
            
            if(newVals(0).remained == 0)
                return str
            
            //println(last)
            val insertIdx = if(last==null || (newVals(0).strVal != last.strVal)) 0
                            else if(newVals(1).remained > 0) 1
                            else 2
            
            val insertCnt =  Math.min(if(insertIdx==0) 2 else 1, newVals(insertIdx).remained)
            
            if(insertCnt == 0)
                return str
            
            //println(insertIdx)
            //println(insertCnt)
            val appendStr = (0 until insertCnt).map(x => newVals(insertIdx).strVal).mkString("")
            val newStr = str + appendStr
            val nextVals = newVals.map(x => if(x.strVal == newVals(insertIdx).strVal) ArrVal(x.remained - insertCnt, x.strVal) else x)
            val newLast = newVals(insertIdx)
            
            ///println(newStr)
            //println(newLast)
            
            return mkString(newStr, nextVals, newLast)
            
            
        }
        val arrVals = Array(ArrVal(a, "a"), ArrVal(b, "b"), ArrVal(c, "c"))
        
        return mkString("", arrVals, null)
        
    }
}
