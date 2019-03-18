object Currying {

    ///////////////////////////// 통계 함수들 ///////////////////////////////
    def statGetMax(data:List[Double]):Double = {
        def max(a:Double, b:Double) = if(a<b) b else a
       
        def getMaxRecur(sum:Double, remain:List[Double]):Double = {
            if(remain.isEmpty) sum
            else getMaxRecur(sum + remain.head, remain.tail)
        }

         getMaxRecur(data.head, data.tail)
     }
   
    def statGetSum(data:List[Double]):Double = {
        def getSumRecur(sum:Double, remain:List[Double]):Double = {
            if(remain.isEmpty) sum
            else getSumRecur(sum + remain.head, remain.tail)
       }
       
       getSumRecur(data.head, data.tail)
   }
   
    def statGetCnt(data:List[Double]):Double = {
        def getCntRecur(cnt:Double, remain:List[Double]):Double = {
            if(remain.isEmpty) cnt
            else getCntRecur(cnt + 1, remain.tail)
        }
       
        getCntRecur(1, data.tail)
    }
   
    def statGetAvg(data:List[Double]):Double = {
        val sum = statGetSum(data)
        val cnt = statGetCnt(data)
       
        sum/cnt.toDouble
    }
    ///////////////////////////////////////////////////////////////////
   

    ///////////////////////////// 전처리 함수들 ///////////////////////////////
    def preCut(data:List[Double]):List[Double] = {
        if(data.isEmpty) Nil
        else if(data.head<0) 0 :: preCut(data.tail)
        else data.head :: preCut(data.tail)
    }
   
    def abs(x:Double):Double = if(x<0) -x else x
   
    def preAbs(data:List[Double]):List[Double] = {
        if(data.isEmpty) Nil
        else abs(data.head) :: preAbs(data.tail)
    }
    ///////////////////////////////////////////////////////////////////
   
    // 커링을 사용하지 않고 데이터를 전처리한 후 통계값을 뽑는 함수
    def getStatisticNorm(preProc:List[Double]=>List[Double], stat:List[Double]=>Double, data:List[Double]):Double = {
        stat(preProc(data))
    }

    // 커링을 사용하여 데이터를 전처리한 후 통계값을 뽑는 함수 (출력은 위와 동일)
    def getStatisticCurr(preProc:List[Double]=>List[Double])(stat:List[Double]=>Double)(data:List[Double]):Double = {
        stat(preProc(data))
    }
  
   def main(args: Array[String]) {
      val a = 1.0 :: 2.0 :: 3.5 :: 3.6 :: -1.0 :: -2.5 :: 6.0 :: Nil
      val b = 2.0 :: 4.0 :: 6.0 :: 8.0 :: 10.0 :: 12.0 :: 14.0 :: Nil
      val c = -1.0 :: 2.0 :: -3.5 :: 5.5 :: -8.0 :: 11.0 :: -14.5 :: Nil
      
      println("--------with getStatisticNorm--------")
      println("--------cut+avg--------")
      println(getStatisticNorm(preCut, statGetAvg, a))
      println(getStatisticNorm(preCut, statGetAvg, b))
      println(getStatisticNorm(preCut, statGetAvg, c))
      
      println("--------abs+avg--------")
      println(getStatisticNorm(preAbs, statGetAvg, a))
      println(getStatisticNorm(preAbs, statGetAvg, b))
      println(getStatisticNorm(preAbs, statGetAvg, c))
      
      println("--------abs+max--------")
      println(getStatisticNorm(preAbs, statGetMax, a))
      println(getStatisticNorm(preAbs, statGetMax, b))
      println(getStatisticNorm(preAbs, statGetMax, c))
      println("-----------------------")
      println()
      
      
      println("--------with getStatisticCurr--------")
      val withCutAvg = getStatisticCurr(preCut)(statGetAvg) _
      
      val withAbs = getStatisticCurr(preAbs) _
      val withAbsAvg = withAbs(statGetAvg)
      val withAbsMax = withAbs(statGetMax)
      
      println("--------abs+avg--------")
      println(withCutAvg(a))
      println(withCutAvg(b))
      println(withCutAvg(c))
      
      println("--------abs+max--------")
      println(withAbsAvg(a))
      println(withAbsAvg(b))
      println(withAbsAvg(c))
      
      println("--------abs+max--------")
      println(withAbsMax(a))
      println(withAbsMax(b))
      println(withAbsMax(c))
      println("-----------------------")
   }
}

