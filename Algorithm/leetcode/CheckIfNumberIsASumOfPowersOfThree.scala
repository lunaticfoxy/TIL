/*
주소: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

내용
- 자연수가 주어진다
- 이 자연수를 3의 k 제곱의 합으로 표현할 수 있는지 여부를 리턴하라
  - k는 0 이상의 정수
  - k는 중복되지 않음


예제
Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false


풀이방법
- k = 0 부터 하나씩 증가시키며 dfs 형태로 탐색한다
  - 3^k를 포함시킬지 말지에 따라 분기
  - 남은 합이 0이면 true를 리턴한다
  - 남은 합이 3^k보다 작으면 false를 리턴한다

*/

object Solution {
    def checkPowersOfThree(n: Int): Boolean = {
        
        def recurFunc(n: Int, curP: Int): Boolean = {
            if(n == 0)
                true
            else if(n < curP)
                false
            else
                recurFunc(n - curP, curP * 3) || recurFunc(n, curP * 3)
        }
        
        recurFunc(n, 1)
    }
}

