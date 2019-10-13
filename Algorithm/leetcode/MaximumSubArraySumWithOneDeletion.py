"""
주소: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

내용
- 정수로 이루어진 리스트가 주어진다
- 이 리스트의 subarray의 최대 합을 구하라. 단 원소를 1개 빼도 된다
  - 안빼도 된다
  
예제
Example 1:
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

Example 2:
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.

Example 3:
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.


풀이방법
- DP로 풀되 2가지 경우로 나뉘어서 저장한다
  - 삭제가 한번이라도 들어가는 경우 delList
    - 초기값은 -(무한대)
    - 이후 현재 값을 지우거나 이전에 값이 지워진적 있는데서 현재값을 더하는 형태로 진행한다
      - 현재값을 지우는 경우 => noDelList[-1]
      - 값이 과거에 지워진적이 있는 경우 => delList[-1] + item
    - 둘중 큰 값을 저장하며 계속 진행한다
  - 삭제가 한번도 들어가지 않는 경우
    - 초기값은 arr[0]
    - 이후 현재값과 삭제되지 않은 최대값 + 현재값 중에 큰 값을 저장하는 형태로 진행한다
      - 현재값을 저장하는 경우 => item
      - 삭제되지 않은 최대값 + 현재값을 저장하는 경우 => noDelList[-1] + item
- DP로 위 테이블을 만들어가면서 나타난 최대 값을 가지고 있다가 리턴한다

"""
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        delList = []
        notDelList = []
        res = -100000
        
        for i, item in enumerate(arr):
            if i==0:
                delList.append(-100000)
                notDelList.append(item)
            else:
                delList.append(max(notDelList[-1], delList[-1] + item))
                notDelList.append(max(notDelList[-1] + item, item))
            
            res = max(res, delList[-1], notDelList[-1])
        
        return res
