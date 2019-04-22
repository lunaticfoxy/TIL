"""
주소: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

내용
- 배열이 주어지고 배열의 서브어레이 길이 L, M이 주어진다
- 두 서브 어레이의 합의 최대를 구하라
- 단 서브 어레이는 겹치지 않는다

샘플
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.


풀이과정
- 아직 덜풀었음. 다시 시도 예정
- 재귀로 모든 경우의 수를 따졌을때는 답은 나오지만 당연히 TLE
- 전형적인 DP문제지만 두 어레이가 겹치지 않아야 한다는게 애매함
- 어레이를 둘로 쪼개서 각각 합을 구하는 방식은 어떨까?
  - 이 경우 쪼개지는 부분에 따라 결과가 달라지므로 결국 모든 수를 따지는게 되나?
- L길이의 최대를 구하고 앞뒤에서 M만큼 뽑기도 생각했으나 (반대 케이스도 동시 고려해서 최대값) L 값이 최대가 아닌데 합이 최대가 되는 경우도 있을경우 애매함
  - [1,9,9,9,9,1] 에 L=4, M=2일경우 L의 최대는 36이지만 M이 들어갈 자리가 없으므로 

"""
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if len(A)<L or len(A)<M:
            return -10000
        
        if M==0:
            if A==0:
                return -10000
            else:
                return max(self.maxSumTwoNoOverlap(A[1:], L, 0), sum(A[:L]))
        else:
            return max(self.maxSumTwoNoOverlap(A[1:], L, M),
                      sum(A[:M]) + self.maxSumTwoNoOverlap(A[M:], L, 0),
                      sum(A[:L]) + self.maxSumTwoNoOverlap(A[L:], M, 0))
