/*
주소: https://leetcode.com/problems/multiply-strings/

내용
- 두 0이상의 정수가 문자열로 들어온다
- 두 정수의 곱을 문자열로 리턴하라
  - 한번에 한 캐릭터씩만 문자로 젼환 가능하다

예제
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"


풀이방법
- 단순 구현
- 마지막에 앞에 0 패딩된것만 제거 필요

*/

object Solution {
    def multiply(num1: String, num2: String): String = {

    def sumRecur(num1: String, num2: String, pad: Int, last: String): String = {
      if(num1.isEmpty){
        if(num2.isEmpty){
          if(pad > 0)
            pad.toString + last
          else
            last
        }
        else{
          val newVal = num2.last.toString.toInt + pad
          val newPad = (newVal / 10)
          sumRecur(num1, num2.dropRight(1), newPad, (newVal % 10).toString + last)
        }
      }
      else{
        if(num2.isEmpty) {
          val newVal = num1.last.toString.toInt + pad
          val newPad = (newVal / 10)
          sumRecur(num1.dropRight(1), num2, newPad, (newVal % 10).toString + last)
        }
        else {
          val newVal = num1.last.toString.toInt + num2.last.toString.toInt + pad
          val newPad = (newVal / 10)
          sumRecur(num1.dropRight(1), num2.dropRight(1), newPad, (newVal % 10).toString + last)
        }
      }
    }

    def multRecur(numStr: String, numInt: Int, pad: Int, last: String): String = {
      if(numStr.isEmpty){
        if(pad == 0)
          last
        else
          pad.toString + last
      }
      else{
        val newVal = numStr.last.toString.toInt * numInt + pad
        val newPad = newVal / 10

        multRecur(numStr.dropRight(1), numInt, newPad, (newVal % 10).toString + last)
      }
    }

    def removeZero(str: String): String = {
      if(str.isEmpty)
        "0"
      else if(str.head.toString == "0")
        removeZero(str.drop(1))
      else
        str
    }

    removeZero(num2.reverse.zipWithIndex.map{c =>
      val numInt = c._1.toString.toInt
      multRecur(num1, numInt, 0, "0" * c._2)
    }.reduce((a, b) => sumRecur(a, b, 0, "")))
  }
}
