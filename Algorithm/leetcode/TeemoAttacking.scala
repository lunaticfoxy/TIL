/*
주소: https://leetcode.com/problems/teemo-attacking/

내용
- 티모가 주어진 timeSeries 시간마다 공격을 하고 독 효과가 duration 만큼 지속된다
- 독이 중복되지 않을때 티모가 입히는 독 데미지의 총량을 구하라

예제
Example 1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

풀이방법
- 남은 공격횟수가 없으면 현재 값 리턴
- 남은 공격횟수가 1이면 duration 리턴
- 남은 공격횟수가 2이상이고 현재 공격 시점과 다음 공격 시점 사이의 간격이 duration 보다 짧으면 차이만큼, 더 크면 duration 만큼 더해줌

*/
object Solution {
    def findPoisonedDuration(timeSeries: Array[Int], duration: Int): Int = {
        
        def recurFunc(ts: Array[Int], duration: Int, res: Int): Int = {
            if(ts.isEmpty)
                res
            else if(ts.length == 1)
                res + duration
            else
                recurFunc(ts.drop(1), duration, res + Math.min(duration, ts(1) - ts(0)))
        }
        
        recurFunc(timeSeries, duration, 0)
    }
}
