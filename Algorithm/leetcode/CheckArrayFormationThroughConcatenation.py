"""
주소: https://leetcode.com/problems/check-array-formation-through-concatenation/

내용
- 하나의 큰 어레이 A와 작은 어레이의 어레이 B가 주어진다
- B의 원소를 concat해서 A를 만들수 있는지 여부를 리턴하라


예제
Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Example 2:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 3:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 4:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Example 5:
Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false


풀이방법
- 단순 부르트포스
- 딕셔너리 등을 활용해서 속도 향상은 가능
  - 단 기본 방법은 동일
"""
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        global check_remain
        check_remain = len(arr)
        
        def compareList(arr1: List[int], arr2: List[int], check: List[bool]):
            global check_remain
            for i in range(len(arr1)):
                if i >= len(arr2):
                    return False
                elif check[i] or (arr1[i] != arr2[i]):
                    return False
                else:
                    check[i] = True
                    check_remain -= 1
        
            return True
        
        check = [False for _ in arr]
        for piece in pieces:
            for i in range(len(arr)):
                if arr[i]==piece[0]:
                    if not compareList(piece, arr[i:], check[i:]):
                        return False
        
        if check_remain == 0:
            return True
        else:
            return False
