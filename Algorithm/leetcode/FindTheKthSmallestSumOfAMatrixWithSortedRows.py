"""
주소: https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

내용
- m*n 매트릭스가 주어지고 이 매트릭스의 한 행에는 5000 이하의 자연수가 오름차순으로 정렬되어 들어있다
- 이 매트릭스의 행마다 하나씩 값을 뽑아 합을 계산하려 한다
- 자연수 k 가 주어질때 k번째 작은 합을 구하라

샘플
Example 1:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  

Example 2:
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Example 3:
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  

Example 4:
Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12


풀이방법
- 문제를 나눠서 생각하자
- 두 행간의 합을 정렬해서 구하고 이를 반복해서 모든 매트릭스에 계산한다
- 두 행간의 합을 정렬해서 구하는 방법은
  - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ 요 문제와 사실 같다
  - 일단 1번째 행의 모든 값과 두번째 행의 첫번째 값을 더하여 힙에 넣는다
    - 힙에 합 뿐만 아니라 첫번째 행과 두번째 행에서 선택한 인덱스도 함께 넣어준다
    - 이 때 모든 값을 넣을필요는 없고 k 까지만 넣으면 된다
  - 이후 이 값을 하나씩 pop 하면서 첫번째 행의 값은 그대로, 두번째 행의 값만 늘려서 다시 넣어준다
  - 이 과정을 힙이 빌때까지 반복한다
    - 속도를 빠르게 하기 위해 k 에서 끊을수도 있다

"""
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        def recurFunc(res, mat, k):
            if len(mat)==0:
                return res[k-1]
            
            heap = []
            ret = []
            
            for i in range(len(res)):
                if i > k:
                    break
                heapq.heappush(heap, (res[i] + mat[0][0], i, 0))
            
            i = 0
            while len(heap)>0 and i<k:
                cur, ori, add = heapq.heappop(heap)
                ret.append(cur)
                
                if add+1 < len(mat[0]):
                    heapq.heappush(heap, (res[ori] + mat[0][add+1], ori, add+1))
                
                i += 1
            
            return ret
                
        res = mat[0]
        for i in range(1, len(mat)):
            res = recurFunc(res, mat[i:], k)
        
        return res[k-1]
