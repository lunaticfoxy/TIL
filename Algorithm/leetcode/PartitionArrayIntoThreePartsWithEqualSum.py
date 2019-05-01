"""
주소: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

내용
- 정수 어레이가 주어졌을때 세 토막으로 나눠서 각각의 합이 같게 나눌수 있는지 여부를 리턴하라

샘플
Example 1:
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

풀이방법
- 총 합은 일정하니 총 합의 1/3, 2/3 지점을 찾는다면 분할이 가능한 것이다.
- 먼저 [0, i] 까지의 합을 담고있는 리스트 sumList를 만든다
- 총 합, 1/3 지점 값, 2/3 지점 값을 구한다
- 리스트에 1/3 지점값과 2/3 지점값이 있으면 true, 하나라도 없으면 false를 리턴한다

적용가능분야
- 전체 조건이 정해져있고 부분의 특성을 탐색하는 문제

"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        
        sumList = [A[0]]
        
        for i in range(1, len(A)):
            sumList.append(sumList[-1] + A[i])
        
        if sumList[-1]%3 != 0:
            return False
        
        sumEach = int(sumList[-1]/3)
        
        fLoc = -1
        for i in range(len(A)):
            if sumEach==sumList[i]:
                fLoc = i
                break
        
        if fLoc == -1:
            return False
        
        sLoc = -1
        for i in range(fLoc+1, len(A)):
            if sumEach*2==sumList[i]:
                sLoc = i
                break
        
        if sLoc==-1:
            return False
        else:
            return True
        
