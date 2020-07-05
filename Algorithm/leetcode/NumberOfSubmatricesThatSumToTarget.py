"""
주소: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

내용
- 정수로 이루어진 행렬이 주어진다
- 이 행렬의 sub 행렬중 원소의 합이 target이 되는 sub 행렬의 수를 구하라
- 단 빈 행렬은 무시한다

샘플
Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.


풀이방법
- [0, 0]부터의 합을 모두 구해놓은 뒤 sub sum 을 구하는 방식은 너무 오래걸림
  - 답은 나오나 타임리밋 발생
- row 단위로만 subsum을 구해놓고 이후에 인덱스를 조정해서 부분합을 구해보자
- 먼저 line 내에서 0번째부터 i번째 지점까지의 합을 i 지점에 저장하는 row_sum 행렬을 만듬
- 이후 col의 시작 인덱스를 i, 끝 인덱스를 j로 주고 row의 순환 시작
  - row의 인덱스인 k를 하나씩 증가시키면서 [0, i] 부터 [k, j] 까지의 sub_sum을 계속 구함
  - 이때 이 구간의 sub_sum은 [0, i] 부터 [k-1, j] 까지의 sub_sum에다가 [k, i] 부터 [k, j] 까지의 sub_sum을 더하여 계산할 수 있음
    - [k, i] 부터 [k, j] 까지의 sum_sum은 [k, j] 의 row_sum 에서 [k, i-1] 의 row_sum 을 빼서 계산할 수 있음
  - 나타나는 sub_sum이 바로 target이면 결과에 1 더해줌
  - 혹시 과거에 나타는 sub_sum 중에 현재 sub_sum - target 값이 나타난 적이 있다면 결과에 나타난 횟수를 더해줌
    - 해당 지점 이후로의 합이 target 이란 이야기니
  - 그리고나서 새로 나타난 sub_sum을 다시 과거에 나타난 sub_sum을 저장하는 dict에 포함시켜줌
    - 미리 포함시켜주면 위의 과거 체크 단계에서 꼬일 수 있으므로 주의


"""
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row_sum = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        for i in range(num_rows):
            row_sum.append([matrix[i][0]])
            for j in range(1, num_cols):
                row_sum[-1].append(row_sum[-1][-1] + matrix[i][j])
        
        res = 0
        for i in range(num_cols):
            for j in range(i, num_cols):
                sub_sum = 0
                found = dict()
                
                for k in range(num_rows):
                    if i == 0:
                        sub_sum += row_sum[k][j]
                    else:
                        sub_sum += (row_sum[k][j] - row_sum[k][i-1])
                    
                    if sub_sum == target:
                        res += 1
                    if sub_sum - target in found:
                        res += found[sub_sum - target]
                        
                    if sub_sum in found:
                        found[sub_sum] += 1
                    else:
                        found[sub_sum] = 1
                    
        return res
