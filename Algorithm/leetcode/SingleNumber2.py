"""
주소: https://leetcode.com/problems/single-number-ii/

난이도: Medium

문제 내용
- 정수가 들어있는 리스트가 주어지는데 이 안에는 한개의 숫자만 빼고 동일한 숫자가 3개씩 들어있다.
- 이 한개의 숫자를 찾아라
- O(n) time complexity & O(1) space complexity
- Single Number와 동일하지만 동일한 숫자가 3개

샘플
Input: [2,2,3,2]
Output: 3
Input: [0,1,0,1,0,1,99]
Output: 99
       
풀이 설명
- 처음엔 Single Number처럼 비트 연산 반복으로 시도
  - nor 연산으로 3개인게 지워지긴 함
  - 다만 원래 값을 찾을수 없으므로 사용 불가능
- 그럼 한번 나온 값만 남기고 없애버리자
- 한번, 두번, 세번 나온 값을 저장하는 공간 생성
- 값을 직접 계산하긴 애매하니 비트로 체크하자
- 루프를 돌며 다음 로직 반복
  - 두번 나온 비트와 동일한 비트를 있으면 세번 나온비트로 넘김 (& 처리)
  - 한번 나온 비트와 동일한 비르를 두번 나온 비트에 더해주고 (or 처리), 세번 나온 비트는 빼줌 (nand 처리)
  - 새로 나온 비트를 한번 나온 비트에 더해주고 (or 처리) 두번 나온 값과 세번 나온 비트는 빼줌 (nand 처리)
- 그럼 마지막에 first에 남는건 한번만 나온 비트들 뿐

어떤 경우에 활용 가능할까
- 얘도 중복된 값 제거에 쓸 수 있긴 함
  - 물론 현실적으로 쓸지는 별개지만
- 데이터는 사실 비트 단위로 체크하면 된다는 기본개념 체크 
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0
        third = 0
        for num in nums:
            third = second & num                            # 3번 나온 값은 2번나온값&현재값
            second = (second | (first & num)) & (~third)    # 2번 나온 값은 한번나온값&현재값 + 원래2번나온값 - 3번나온값
            first = (first | num) & (~second) & (~third)    # 1번 나온 값은 현재값 - 2번나온값 - 3번나온값
        return first
