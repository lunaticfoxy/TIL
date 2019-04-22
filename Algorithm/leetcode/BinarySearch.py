"""
주소: https://leetcode.com/problems/binary-search/

내용
- 바이너리 서치를 구현하라
- 리턴값은 해당 target의 인덱스이다
- 내부에 target이 없으면 -1을 리턴하라

샘플
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

풀이과정
- 바이너리 서치 자체는 간단하니 패스
- 중요한건 인덱스 처리
  - 다음 단계로 넘어갈때 middle이 포함되지 않도록 주의해줘야함
  - 잘못하면 무한루프
- edge case 처리도 중요
  - 데이터 수가 0일때
  - 종료조건 저리

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRecur(nums, target, startIdx):
            if len(nums)==0:
                return -1
            
            middle = int(len(nums)/2)

            if nums[middle]==target:
                return  startIdx + middle
            elif nums[middle]>target:
                return searchRecur(nums[:middle], target, startIdx)
            else:
                return searchRecur(nums[middle+1:], target, startIdx+middle+1)
            
        def searchIter(nums, target):
            left = 0
            right = len(nums)-1
            
            while right>=left:
                middle = int((left+right)/2)
                
                if nums[middle]==target:
                    return middle
                elif nums[middle]>target:
                    right = middle-1
                else:
                    left = middle+1
            
            return -1
            
            
        #return searchRecur(nums, target, 0)
        return searchIter(nums, target)
    
    
