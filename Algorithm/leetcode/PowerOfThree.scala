/*
주소: https://leetcode.com/problems/power-of-three/

내용
- 어떤 숫자가 3의 n승인지 확인하라
- 단, 루프나 재귀 없이 구현해봐라

샘플
Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Example 4:
Input: n = 45
Output: false


풀이방법
- log_3(x) 가 자연수라면 3의 n승일것임
- log_3(x) = log_10(x) / log_10(3) 이므로 이를 계산하여 자연수인지 체크
*/
object Solution { 
    def isPowerOfThree(n: Int): Boolean = {
        val loged = Math.log10(n) / Math.log10(3)
        
        if(loged == loged.toInt.toDouble)
          true
        else
          false
    }
}

