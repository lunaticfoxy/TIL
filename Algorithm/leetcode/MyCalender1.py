"""
주소: https://leetcode.com/problems/my-calendar-i/

내용
- 일정의 시작과 끝이 연속해서 들어온다
- 순차적으로 일정을 넣었을때 넣을 수 있는 경우는 True, 아닌 경우는 False를 리턴하라

샘플
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


풀이 방법
- 더 빠른 방법 (트리? DP?) 가 있겠지만 일단 가장 단순한 방법으로 풀었음
- 단순히 리스트를 만들고
- 리스트를 순회하면서 다음칸으로 넘길지를 결정한다
  - 넘기는 기준은 현재 칸의 end가 새로운 값의 start보다 작은지를 체크한다
- 다음칸으로 넘길수 없을때 현재 위치에 넣을 수 있는지를 확인한다
  - 이때는 현재 칸의 start가 새로운 값의 end보다 큰지를 체크한다
- 넘기지도 못하는데 넣지도 못하면 False를 리턴한다

"""
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        idx = 0
        
        while True:
            if len(self.booked)==idx:
                self.booked.append([start, end])
                return True
            else:
                if self.booked[idx][1]<=start:
                    idx += 1
                elif self.booked[idx][0]>=end:
                    self.booked.insert(idx, [start, end])
                    return True
                else:
                    return False
            
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
