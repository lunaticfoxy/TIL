"""
주소: https://leetcode.com/problems/rle-iterator/

내용
- 이해한바로는...
- RLE 형태의 데이터가 주어진다
  - 데이터 수, 데이터, 데이터 수, 데이터 가 반복해서 주어지는 형태
- 이 데이터를 순회하는 Iterator를 제작하라
- 초기화와 next를 구현해야 한다
- next는 해당 지점의 값을 출력하고 몇칸 뒤로 이동할지이다.

풀이방법
- 매우 단순한 구현문제라고 생각했느데 계속 오답... 확인 

"""

class RLEIterator:

    def __init__(self, A: List[int]):
        self.data = []
        self.idx = -1
        
        cntIdx = 0
        valueIdx = 1
        
        while len(A)>valueIdx:
            for i in range(A[cntIdx]):
                self.data.append(A[valueIdx])
            
            cntIdx += 2
            valueIdx += 2
        

    def next(self, n: int) -> int:
        self.idx += n
        
        if self.idx > len(self.data):
            return -1
        elif self.idx == len(self.data):
            retVal = self.data[-1]
        else:
            retVal = self.data[self.idx]
        self.idx += 1
        return retVal


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
