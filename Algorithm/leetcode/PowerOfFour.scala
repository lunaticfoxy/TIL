"""
주소: https://leetcode.com/problems/power-of-four/

내용
- 4의 Power 인지 여부를 리턴하라
- 반복문과 재귀를 쓰지 않고 풀 수 있겠는가?

샘플
Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false


풀이방법
- 0보다 작거나 같은 경우 제외
- 일단 2의 Power인지 체크
  - x*(x-1) == 0 이면 2의 Power이다
- 그리고 b1010 1010 1010 1010 1010 1010 1010 1010 과 and 연산을 해본다
  - 4의 Power는 100, 10000, 1000000 형태니깐 무조건 0이 나와야 한다
"""
object Solution {
    def isPowerOfFour(num: Int): Boolean = {
        if(num <= 0)
            false
        else {
            if(((num & (num - 1)) == 0) && ((0xAAAAAAAA & num) == 0))
                true
            else
                false
        }
    }
}
