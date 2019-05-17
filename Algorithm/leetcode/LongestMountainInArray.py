"""
주소: https://leetcode.com/problems/longest-mountain-in-array/

내용
- 0 이상의 정수로 이뤄진 어레이가 주어진다
- A[i-m]<...<A[i-1]<A[i]<A[i+1]<A[i+2]<...<A[i+n] 인 구간을 산이라 하고 이 산의 길이는 n+m+1이다
- 나타나는 가장 긴 산의 길이를 구하라

샘플
Example 1:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.


풀이방법
- dp로 풀자
- 일단 앞에서부터 쭉 스캔하면서 나타나는 증가 구간의 길이를 저장한다.
- 다음으로 뒤에서부터 쭉 스캔하면서 나타나는 증가 구간의 길이를 저장한다.
- 그리고 다시 리스트를 순회하면서 앞부터 스캔한 구간과 뒤부터 스캔한 구간의 길이의 합이 가장 큰 지점을 찾는다
  - 단 이때 중심점은 두번 더해졌으니 1을 빼줘야 하고
  - 양쪽 끝은 중심점이 될 수 없으니 1~len(A)-2 내에서만 돌아야 하고
  - 중심점인지 확인하는 코드를 더해야 한다
    - 중심점인지 여부를 같이 넣으면 더 빠를것 같긴 함


"""
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        forward = [1]
        backward = [1]
        
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                forward.append(forward[-1]+1)
            else:
                forward.append(1)
        
            if A[-(i+1)]>A[-i]:
                backward.append(backward[-1]+1)
            else:
                backward.append(1)
            
        backward = backward[::-1]
        
        maxLen = 0
        for i in range(1, len(A)-1):
            temp = forward[i]+backward[i]-1
            
            if temp>maxLen and A[i]>A[i-1] and A[i]>A[i+1]:
                maxLen = temp
        
        return maxLen
