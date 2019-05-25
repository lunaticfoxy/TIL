"""
주소: https://leetcode.com/problems/last-stone-weight/

내용
- 돌들의 무게가 들어있는 리스트가 주어진다
- 이 리스트 내에서 제일 무거운 돌 두개를 빼내서 둘을 충돌시키면 작은 돌은 부서지고 큰 돌은 작은 돌 만큼의 무게가 사라진다
- 남은 돌을 다시 리스트에 넣는것을 반복 했을때 마지막 남은 돌의 무게를 구하라
  - 돌이 완전히 부서지면 리스트에 넣지 않는다
  - 리스트에 남은 돌이 없으면 0을 리턴한다
  
샘플
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


풀이방법
- 제일 무거운 돌 2개를 꺼낸다 => heap
- 다시 넣는다 => heap을 순환하면서 결과를 다시 넣기
- 종료조건 => heap 내에 들어있는 원소의 개수가 2개 미만일 경우

"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
            
        while len(heap)>=2:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            
            n = f-s
            
            if not n==0:
                heapq.heappush(heap, n)
        
        if len(heap)==0:
            return 0
        else:
            return -heap[0]
