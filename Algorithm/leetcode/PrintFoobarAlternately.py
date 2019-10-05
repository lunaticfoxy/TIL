"""
주소: https://leetcode.com/problems/print-foobar-alternately/

내용
- 두개의 스레드로 동작하는 애플리케이션이 있다
- 각각의 스레드는 foo와 bar를 출력한다
- foobar 형태의 출력이 입력 횟수만큼 반복되도록 구성하라

예시
Example 1:
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.


풀이방법
- 스레드 락 사용법을 알고있는지 확인하는 문제
- 김에 익히고 넘어가자
  - 직접 status를 줄수 있지만 너무 느려짐

"""
from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.flock = Lock()
        self.block = Lock()
        self.flock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.block.acquire()
            printFoo()
            self.flock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.flock.acquire()
            printBar()
            self.block.release()
