"""
주소: https://leetcode.com/problems/self-dividing-numbers/

내용
- 자기 자신의 자리수로 나누어떨어지는 값을 self dividing number라고 한다
- 주어진 범위 내의 모든 self dividing number를 구하라

샘플
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

풀이방법
- 그냥 left부터 right까지 한 값씩 체크해본다
- 별도로 함수를 만들어서 체크하며
  - 함수 내에서는 한 값씩 10의 나머지를 비교해가면서 나누어 떨어지는지 확인한다

"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def isSelfDividing(number):
            cp = number
            while cp > 0:
                div = cp%10
                if div==0 or not number%div==0:
                    return False
                cp = cp // 10
                
            return True
        
        res = []
        
        for i in range(left, right+1):
            if isSelfDividing(i):
                res.append(i)
        
        return res
