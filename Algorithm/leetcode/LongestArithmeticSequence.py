"""
주소: https://leetcode.com/problems/longest-arithmetic-sequence/

내용
- 0 이상 10000 이하의 값으로 구성된 어레이가 주어지고 길이는 [2, 2000] 범위 내에 있다
- 이 어레이 내에서 차이가 일정한 서브 어레이를 구성하고자 한다.
- 이때 구성할 수 있는 가장 긴 서브어레이의 길이를 구하라

샘플
Example 1:
Input: [3,6,9,12]
Output: 4
Explanation: The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation: The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: The longest arithmetic subsequence is [20,15,10,5].

풀이방법
- 가정: i-1지점 까지의 구할 수 있는 서브어레이는 i지점 까지 구할 수 있는 서브어레이의 부분 집합 일 것이다
- 따라서 longestArithSeqLengthRecur 함수를 통해 한 단계씩 subarray를 늘려나가멵서 구성
- i단계에서 다음과 같은 일이 일어남
  - 기존까지의 서브어레이를 카피
  - 새로운 인덱스 j를 만들어서 [0, i-1] 까지 순회
    - A[i]-A[j] 의 값을 계산하고 기존에 정답에 이 차이값이 들어있는지 확인
    - 들어있다면 해당 지점의 마지막 지점 중 j 인게 있는지 확인
      - 마지막 지점이 j라면 해당 위치에 저장된 값 + 1을 다시 저장하고 마지막 지점을 i로 갱신 (뒤에 이어붙여지는 경우)
        - 단 코드상에서는 매번 새로운 서브어레이를 생성
      - 마지막 지점이 j가 아니라면 마지막 지점이 i이고 값이 2인 원소를 추가 (차이는 같지만 원소가 다른 새로운 서브어레이가 시작되는 경우)
    - 들어있지 않다면 마지막 지점이 i이고 값이 2인 원소를 추가 (새로운 차이에 대한 서브어레이가 시작되는 경우)
- 이 과정을 i를 증가시켜가면서 반복하면 답 나옴

"""
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        def longestArithSeqLengthRecur(A, last):
            ALoc = len(A)-1
            newLast = dict(last)
            for i in range(len(A)-1):
                diff = A[-1]-A[i]
                
                if diff in newLast:
                    if i in newLast[diff]:
                        newLast[diff][ALoc] = newLast[diff][i] + 1
                    else:
                        newLast[diff][ALoc] = 2
                else:
                    newLast[diff] = dict()
                    newLast[diff][ALoc] = 2
            return newLast

        last = dict()
        for i in range(2, len(A)+1):
            last = longestArithSeqLengthRecur(A[:i], last)
            
        maxlen = 0
        for diff in last:
            for loc in last[diff]:
                if last[diff][loc] > maxlen:
                    maxlen = last[diff][loc]
        
        return maxlen
