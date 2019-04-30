"""
주소: https://leetcode.com/problems/transpose-matrix/

내용
- 매트릭스의 가로 세로를 뒤집어라

샘플
Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


풀이방법
- 심플 is Best


적용가능분야
- 매트릭스의 가로 세로를 뒤집는 일은 많다
- 하지만 웬만하면 뒤집지 말고 가로 세로의 인덱스만 바꾸자
  - 자료구조를 바꾸는거보다 참조 인덱스만 바꾸는게 비용이 덜든다


"""
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newList = []
        for i in range(len(A[0])):
            newList.append([])
            for j in range(len(A)):
                newList[i].append(A[j][i])
        
        return newList
