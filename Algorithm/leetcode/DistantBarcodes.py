"""
주소: https://leetcode.com/problems/distant-barcodes/

내용
- 자연수로 이루어진 바코드가 주어진다
  - 최대값 10000, 최대 길이 10000
- 이 바코드를 연속되는 값이 없도록 재정렬 하라
- 단 반드시 답이 존재


샘플
Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]


풀이과정
- 반드시 답이 존재한다니 엣지케이스 생각 안한 로직
- 답이 존재하려면 (제일 많은 값의 개수)+1<=(나머지 값의 수) 여야 한다
- 계속해서 위 조건이 만족하니 앞의 값과 같지 않은 제일 많은 값을 이어붙이면 된다
- 이때 힙을 사용해서 수행하고 연속되는 값이 들어가지 않도록 별도의 조치를 취한다
  - 이부분도 개선 가능
  - 지금은 매번 넣고 빼는데 어차피 1개씩밖에 못넣으니 그냥 다음꺼 연속으로 넣어도 될듯
- 개선방안
  - 지금 타임리밋 아슬아슬하게 통과한듯
  - 어차피 최대값 10000에 최대 길이 10000이니깐 미리 배열 만들어서 인덱스로 접근하면 빨라질듯 함
"""
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = dict()
        
        for code in barcodes:
            if code in cnt:
                cnt[code] += 1
            else:
                cnt[code] = 1
        
        cntHeap = []
        for code in cnt:
            heapq.heappush(cntHeap, (-cnt[code], code))
        
        res = []
        while len(cntHeap)>0:
            temp = []
            
            while True:
                temp.append([x for x in heapq.heappop(cntHeap)])
                if len(res)==0 or temp[-1][1]!=res[-1]:
                    res.append(temp[-1][1])
                    temp[-1][0] += 1
                    
                    for item in temp:
                        if item[0]!=0:
                            heapq.heappush(cntHeap, tuple(item))
                    break
            
        return res
        
        
