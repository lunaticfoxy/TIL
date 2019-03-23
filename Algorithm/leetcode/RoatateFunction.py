"""
주소: https://leetcode.com/problems/rotate-function/

난이도: Medium

문제 내용
- 리스트 A가 주어지고 n번 배열을 회전시킨 sum(i*A[i]) 를 계산한 값을 F[n] 이라 하자
- max(F[0]~F[len(A)-1]) 를 찾아라

샘플
Input: A = [4, 3, 2, 6]
Output: 26
Explanation
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
       
풀이 설명
- 먼저 무식하게 다 해본건 당연히 타임리밋
- F[n]과 F[n-1] 사이의 점화식을 찾아보자
  - 미리 전체 배열의 합 계산해서 X 라 하자
  - F[0] = A[0]*0 + A[1]*1 + A[2]*2 + ... + A[p]*p
  - F[1] = A[0]*1 + A[1]*2 + A[2]*3 + ... + A[p]*0
  - F[1] - F[0] = A[0] + A[1] + ... + A[p-1] - A[p]*p
  - F[1] = sum(A[0]~A[p-1]) - A[p]*p + F[0] = sum(A[0]~A[p]) - A[0]*(p+1) + F[0] = X - A[p]*(p+1) + F[0]
  - 이걸 일반화하면 F[n] = X - A[p-(n-1)]*(p+1) + F[n-1]
- 찾은 점화식을 구현하기만 하면 된다
- 그리고 그중에 제일 큰값 리턴

어떤 경우에 활용 가능할까
- 계단식 합은 대부분 점화식을 따른다
- 실제 날짜별로 가중치를 두고 날짜별 값을 구하는 경우에 사용 가능
- 날짜뿐만 아니라 시퀀셜한 모든 데이터에서 사용 가능
- 만약 기준점 양옆으로 멀어질수록 가중치가 낮아지는 형태의 attention? 을 준다면 활용 
"""
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        F = []
        sumAll = sum(A)
        
        f0 = 0
        for i in range(len(A)):
            f0 += i*A[i]
            
        F.append(f0)
        
        for i in range(len(A)-1):
            F.append(F[i] + sumAll - len(A)*A[(-i-1)%len(A)])
        
        return max(F)
