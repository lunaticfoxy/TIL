/*
주소: https://leetcode.com/problems/integer-replacement/

내용
- 짝수는 2로 나누고 홀수는 1을 더하거나 1을 뻬는 식으로 연산을 반복한다
- 값이 1이 되면 연산을 종료한다
- 연산을 종료할때까지 반복해야 하는 최소 횟수를 구하라

예제
Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2

풀이방법
- 단순 구현
- 함정으로 INT_MAX 가 주어지면 + 1을 할때 스택오버플로우가 남
  - 이를 해결 + 연산을 한번이라도 줄이기 위해 + 1, - 1 을 직접 하지않고 바로 2로 나눠서 나머지를 버리거나 2로 나눈뒤 1을 더해주고 2번 연산으로 침
  - 값이 증가하는 케이스를 없앰
*/
object Solution {
  def integerReplacement(n: Int): Int = {
    if(n == 1)
      0
    else {
      if (n % 2 == 0)
        integerReplacement(n / 2) + 1
      else
        Math.min(integerReplacement(n / 2), integerReplacement((n / 2) + 1)) + 2
    }
  }
}
