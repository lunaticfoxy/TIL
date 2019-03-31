"""
주소: https://leetcode.com/problems/single-number-iii/

난이도: Medium

문제 내용
- 정수가 들어있는 리스트가 주어지는데 이 안에는 두 개의 숫자만 빼고 동일한 숫자가 2개씩 들어있다.
- 두 개의 숫자는 한번씩만 나온다
- 이 두개의 숫자를 찾아 리스트로 리턴하라
- O(n) time complexity & O(1) space complexity
- Single Number와 동일하지만 찾아야 하는 숫자가 2개

샘플
Input:  [1,2,1,3,2,5]
Output: [3,5]
       
풀이 설명
- 일단 Single Number처럼 비트 연산 반복하면 두번 나오는 숫자는 싹 날릴 수 있음
- 그럼 남은 값은 구해야 하는 두 값의 xor 결과 -> 이걸 어떻게 분리해야 할까
- xor 결과에 따르면 두 값이 완전히 같으면 0 이겠지 -> 그럴 가능성은 없으니 확실히 다른 비트 한개는 존재함
  - 그렇다면 그 다른 비트 1개를 기준으로 탐색하자
  - 서로 다른 비트 1개를 찾은다음 해당 비트가 0인것과 1인걸 나눠서 보면 됨
  - 다른 비트 찾는건 그냥 외워둘만한 테크닉
    - lowerDiffBit = val&~val 이렇게 하면 가장 작은 자리의 비트만 1인 값이 리턴됨
    - ex) 1100 & -(1100) = 1100 & 0011+1 = 1100 & 0100 = 0100
- 이렇게 다른 비트를 하나 찾았으면 다시 루프 한번 수행
  - 루프 내에서 다른 비트가 0인것 끼리 xor 수행
  - 다른 비트가 1인것 끼리도 xor 수행
- 그 결과로 각각 해당 비트가 0인 값과 1인 값이 남게됨

어떤 경우에 활용 가능할까
- xor연산 결과를 분리해야 할 경우 사용 가능
- 다른 최하위 비트 찾는 연산은 외워둘 가치가 있음 
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for num in nums:            # 일단 중복 제거
            res ^= num
        
        last_bit = res&-res         # 맨 마지막에 1로 세팅된 비트 체크
        
        val1 = 0
        val2 = 0
        for num in nums:            # 해당 비트가 1인 값들과 0인 값들을 나눠서 xor 하면 중복 제거됨
            if (num&last_bit)==0:
                val1 ^= num
            else:
                val2 ^= num
        
        return [val1, val2]
