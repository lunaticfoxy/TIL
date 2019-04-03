"""
주소: https://leetcode.com/problems/range-sum-query-2d-immutable/

난이도: Medium

문제 내용
- 2D Integer Matrix가 주어지고 이걸 생성자에서 받아 만들어지는 NumMatrix라는 객체가 존재한다.
- sumRegion 함수에 원하는 영역을 넣고 호출하면 영역의 합이 리턴되도록 객체를 만들어라

샘플
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
       
풀이 설명
- 당연하게 DP로 풀어야함
- 생성자에서 DP로 0,0부터 해당 지점까지의 합을 저장하는 sumMat 생성 해놓고 이용
  - 이때 i, j 위치의 값은 현재값 + 위의값 + 왼쪽값 - 왼쪽 위 값 이 됨
  - 이건 그림 보면 바로 이해되니 패스 (중복 더해진값을 빼는 정도로 생각)
  - 코드로는 sumMat[i][j] = matrix[i][j] + sumMat[i-1][j] + sumMat[i][j-1] - sumMat[i-1][j-1]
- sumRegion 호출시에도 동일 (이하 R 로 표현)
  - R(i1, j1, i2, j2) 범위의 값은 i2, j2 까지 합에서 왼쪽 범위값, 오른쪽 범위 값을 빼고, 중복으로 빼진 값을 더해주면 계산 가능
  - 코드로 표현하면 R(i1, j1, i2, j2) = R(0, 0, i2, j2) - R(0, 0, i1-1, j2) - R(0, 0, i2, j1-1) + R(0, 0, i1-1, j1-1)
  - 근데 여기서 R(0, 0, x, y)=sumMat(x, y) 이므로
  - R(i1, j1, i2, j2) = sumMat(i2, j2) - sumMat(i1-1, j2) - sumMat(i2, j1-1) + sumMat( i1-1, j1-1)

어떤 경우에 활용 가능할까
- 영역 누적은 매우 많이 사용되는 알고리즘
- 영상처리에서 부분합 구할때도 쓰고
- convolution - pooling 시에 부분합 구할때도 사용 가능
- 꼭 2D가 아니더라도 모든 범위에 적용 
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        
        if self.rows==0:
            self.SumMat = [[]]
            return
        
        self.cols = len(matrix[0])
        
        self.sumMat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.sumMat[0][0] = matrix[0][0]
        
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.sumMat[i][j] = matrix[i][j]
                
                if j>0:
                    self.sumMat[i][j] += self.sumMat[i][j-1]
                
                if i>0:
                    self.sumMat[i][j] += self.sumMat[i-1][j]
                    
                if i>0 and j>0:
                    self.sumMat[i][j] -= self.sumMat[i-1][j-1]
        
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sumMat[row2][col2]
        
        if row1>0:
            res -= self.sumMat[row1-1][col2]
        
        if col1>0:
            res -= self.sumMat[row2][col1-1]
            
        if row1>0 and col1>0:
            res += self.sumMat[row1-1][col1-1]
    
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
