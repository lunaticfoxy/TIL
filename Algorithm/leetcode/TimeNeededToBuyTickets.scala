/*
주소: https://leetcode.com/problems/time-needed-to-buy-tickets/

내용
- 사람들이 티켓을 사려고 줄을 서있다
- 이때 사람들마다 사려는 티켓의 수가 주어지고, 티켓은 한번에 한장씩만 살 수 있다
- 맨 뒷사람까지 티켓을 한장씩 산 뒤에 다시 앞사람에게 기회가 돌아온다
- k번째 사람이 티켓을 모두 살때까지 걸리는 시간을 구하라

예제

풀이방법
- 단순히 앞에서부터 하나씩 빼가면서 계산함
- 재귀로 한바퀴씩 계산할하고 다음 단계로 넘기는 식으로 구현
  - 꼬리재귀 사용
- 가장 작은 값을 기준으로 묶어서 재귀 횟수를 줄이면 좀 더 빨리질것으로 보임
*/

object Solution {
    def timeRequiredToBuy(tickets: Array[Int], k: Int): Int = {
        
        def funcRecur(tickets: Array[Int], k: Int, res: Int): Int = {
            //println(tickets.mkString(",") + " / " + k.toString + " / " + res)
            
            if(tickets(k) == 0)
                res
            else if(tickets(k) == 1)
                res + tickets.take(k).filter(_ > 0).length + 1
            else
                funcRecur(tickets.map(_ - 1), k, res + tickets.filter(_ > 0).length)
        }
        
        funcRecur(tickets, k, 0)
    }
}
