/*
주소: https://leetcode.com/problems/a-number-after-a-double-reversal/

내용
- 어떤 숫자를 뒤집었을때 자리수가 유지되는지 여부를 리턴하라


예제
Example 1:
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.


풀이방법
- 단순 구현


*/
object Solution {
    def isSameAfterReversals(num: Int): Boolean = {
        if(num == 0)
            true
        else if(num % 10 == 0)
            false
        else
            true
    }
}
