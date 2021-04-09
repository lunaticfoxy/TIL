/*
주소: https://leetcode.com/problems/elimination-game/

내용
- 자연수 n이 주어지고 이를 가지고 [1, 2, ..., n] 배열을 만든다
- 이 배열의 앞에서부터 홀수번째 있는 원소들을 모두 지운다
- 남은 배열의 뒤에서부터 홀수번째 있는 원소들을 모두 지운다
- 이 과정을 숫자가 하나만 남을때까지 반복하고 해당 숫자를 리턴한다

예시
Example 1:
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

Example 2:
Input: n = 1
Output: 1


풀이방법
- 모든 리스트를 만들어서 하면 메모리 리밋 에러 발생
- 규칙을 찾자
- 매 단계는 n이 0부터 시작하는 a*n + b 로 표현 가능
  - 1*n + 1
    - 2*n + 2
      - 4*n + 2
      - 4*n + 4
- a는 단계마다 무조건 2배씩 증가
- b는 경우의 수가 존재
  - 정방향으로 갈때는 b = a + b
  - 역방향으로 갈때는
    - 남은 배열의 길이가 짝수일때는 b = b
    - 남은 배열의 길이가 홀수일때는 b = a + b
- 이 규칙을 시뮬레이션 하고 남은 사이즈가 1이 되는 순간의 맨 앞 값을 리턴하면 됨
*/
object EliminationGame {
  def lastRemaining(n: Int): Int = {
    def lastRemainingRecur(front: Int, mult: Int, size: Int, max: Int, reverse: Boolean): Int = {
      if (size == 1)
        front
      else {
        val newFront = (
          if (!reverse)
            front + mult
          else {
            if (size % 2 == 0)
              front
            else
              front + mult
          })

        lastRemainingRecur(newFront, mult * 2, size / 2, max, !reverse)
      }
    }

    lastRemainingRecur(1, 1, n, n, false)

  }

  def main(args: Array[String]): Unit = {
    println(lastRemaining(1))
    println(lastRemaining(9))
  }
}
