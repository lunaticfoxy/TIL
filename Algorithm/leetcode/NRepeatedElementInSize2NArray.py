"""
주소: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

내용
- 길이 2N의 배열이 주어지고 이중에 한 원소만 N번 반복된다
- 나머지 원소는 모두 다른 값을 가질때 N번 반복되는 원소를 구하라

샘플
Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5


풀이방법
- 단순히 답은 쉽지만 최대한 빨리 풀기 문제
- 중요한건 나머지 원소가 모두 다른값을 가진다는 이야기와 최소 길이가 4라는 이야기
- 반복되는 원소를 x라 하자
- Case 1. x가 연속되어 [x, x] 형태로 나타날 경우 => 단순 비교로 체크
- Case 2. x가 한칸 뛰어 [x, y, x] 형태로 나타날 경우 => 단순 비교로 체크
- Case 3. x가 2칸 뛰어 [x, y, z, x] 형태로 나타날 경우
  - Case 2를 3칸짜리 윈도우로 두번 반복
  - 그리고도 안걸리면 맨 첫번째 값이 답임
- 이후부터는 큰 의미가 없는게 x가 한칸 뛸때마다 x가 뒤에 하나씩 더 붙어야 하니 Case 1, 2로 확인 가능
  - 사실상 저 3개 케이스만 고려하면 됨

"""
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(2, len(A)):
            if A[i]==A[i-1] or A[i]==A[i-2]:
                return A[i]
        
        return A[0]
