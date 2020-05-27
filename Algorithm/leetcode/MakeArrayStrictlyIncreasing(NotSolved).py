"""
주소: https://leetcode.com/problems/make-array-strictly-increasing/

내용
- 배열이 2개 주어지고 이때 1번 배열을 증가하게 만들고싶다
  - 동일한값도 제외
- 이때 2번 배열에서 값을 바꿔치기해서 증가하게 만들수 있다
- 몇개를 바꿔치기해야 1번 배열을 증가하게 할수있는지 찾아라

샘플
Example 1:
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:
Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:
Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.

풀이방법
- 아래 코드는 1개씩만 바꿀때 동작하는 코드
- 뭉텅이로 바꿀때 동작하는 코드가 필요하다
  - 아마 먼저 뭉텅이를 찾은다음 배열2에서 구간 단위로 체크하면 될듯하다

"""
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        cnt = 0
        
        j = 0
        for i in range(len(arr1) - 1):
            if arr1[i] >= arr1[i+1]:
                while True:
                    if j >= len(arr2):
                        return -1
                    elif (i==0 or arr2[j] > arr1[i-1]) and arr2[j] < arr1[i+1]:
                        cnt += 1
                        j += 1
                        break
                    else:
                        j += 1
        
        return cnt
