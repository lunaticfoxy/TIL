"""
주소: https://leetcode.com/problems/distance-between-bus-stops/

내용
- 버스정류장이 늘어서있고 각각의 거리를 나타내는 배열이 주어진다
- i번째 배열에는 i번째 정류장과 (i+1)%n번째 정류장의 거리가 주어진다
  - n은 정류장의 수
  - 배열의 마지막 값에는 마지막 정류장과 첫 정류장의 거리가 주어진다고 생각하면 됨
- 이때 주어진 시작점부터 끝점까지의 가장 가까운 거리를 구하라

예시
Example 1:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.


풀이방법
- 버스 정류장이 원형으로 연결되어 있다.
- 따라서 왼쪽으로 돌거나 오른쪽으로 도는 길밖에 없으니 두 경우를 비교하면 된다.
- 직접 돌면서 합을 구해서 비교해도 통과된다
  - 실제 테스트 해봄
- 단 어차피 부분합 개념이므로 전체 합을 구한뒤 구간의 합을 구하는건 쉽다. => 오른쪽 방향으로 회전
- 그리고 왼쪽 방향으로 회전하는 구간의 합은 전체 구간 - 오른쪽 방향으로 회전하는 구간 이므로 쉽게 구할수 있다.
- 주의할점은 목적지가 시작점보다 앞에있으면 왼쪽 방향, 오른쪽 방향이 바뀐다
  - 목적지를 항상 시작점 뒤에 놓도록 변경하여 해결
"""
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            temp = start
            start = destination
            destination = temp
        
        sumList = [distance[0]]
        
        for i in range(1, len(distance)):
            sumList.append(sumList[-1] + distance[i])
        
        print(sumList)
        leftSum = sumList[destination - 1]
        
        if start > 0:
            leftSum -= sumList[start - 1]
        
        rightSum = sumList[-1] - leftSum
        
        return min(leftSum, rightSum)
