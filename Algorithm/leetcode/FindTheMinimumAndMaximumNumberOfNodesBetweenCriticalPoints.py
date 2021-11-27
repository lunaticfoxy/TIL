"""
주소: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

내용
- 값이 증가하다가 감소하기 시작하는 경계, 감소하다가 증가하는 경계를 critical point 라 한다
- critical point 사이의 최소거리, 최대거리를 구하라

예제
Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

Example 4:
Input: head = [2,3,3,2]
Output: [-1,-1]
Explanation: There are no critical points in [2,3,3,2].


풀이방법
- 앞에서부터 하나씩 크리티컬 포인트를 찾아가나간다
- 마지막 크리티컬 포인트의 위치를 저장하고 새로운 크리티컬 포인트가 등장할때마다 둘 사이의 거리가 기존 최소보다 작은지 체크하여 갱신한다
- 최초 크리티컬 포인트의 위치를 저아하고 새로운 크리티컬 포인트가 등장할때마다 둘 사이의 거리가 기존 최대보다 큰지 체크하여 갱신한다

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        firstCp = -1
        lastCp = -1
        minDist = 100000
        maxDist = -1
        
        lastVal = -1
        curNode = head
        
        idx = -1
        while curNode is not None:
            idx += 1
            #print(curNode.val)
            
            if lastVal!=-1 and curNode.next is not None and ((curNode.val < lastVal and curNode.val < curNode.next.val) or  (curNode.val > lastVal and curNode.val > curNode.next.val)):
                
                
                if firstCp == -1:
                    firstCp = idx
                else:
                    if idx - lastCp < minDist:
                        minDist = idx - lastCp
                        
                    if idx -firstCp > maxDist:
                        maxDist = idx - firstCp
            
                lastCp = idx
            lastVal = curNode.val
            curNode = curNode.next
            
        if minDist == 100000:
            return [-1, -1]
        else:
            return [minDist, maxDist]
        
        
                
                
                
