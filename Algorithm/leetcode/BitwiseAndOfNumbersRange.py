
"""
주소: https://leetcode.com/problems/bitwise-and-of-numbers-range/

난이도: Medium

문제 내용
- n>=m 인 두 0 이상의 정수 n, m 이 주어졌을때 [n, m] 범위 내의 모든 숫자들의 AND 연산 결과를 구하라

샘플
Input: [5,7]
Output: 4
Input: [0,1]
Output: 0
       
풀이 설명
- 다 해보면 당연히 타임리밋 날거다
- 어차피 두 정수 사이에 변하는 값은 맨 아래 비트부터 바뀌겠지?
- 그리고 사이에 한번이라도 0이 들어가면 안될거고
- 따라서 두 정수 사이의 상위 비트중 일치하는 부분까지만 보면 된다
  - 19와 17의 경우 10011, 10001 이므로 바뀌지 않는 맨 앞 두자리만 확인 => 10000 => 16
  - 16과 15의 경우 10000, 01111 이므로 바뀌지 않는 값이 없음 => 0
- 계산하기 쉽게 문자열로 치환한다음 비교
- 길이가 다르면 당연히 0 (엣지 케이스)
- 한 비트씩 비교하면서 기존 값에 2를 곱해서 비트 이동
- 비트연산자 활용은 할수는 있겠지만 패스
  - 속도는 오르겠지만 뭐 실제로 적용할일은 없을테니

어떤 경우에 활용 가능할까
- 두 값 범위 사이의 규칙 탐색에 비슷한 경우가 많을듯
- 다른거 필요없이 날짜 비교만 해도 그렇지

"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mBitStr = "{0:b}".format(m)
        nBitStr = "{0:b}".format(n)
        
        if len(nBitStr)!=len(mBitStr):
            return 0
        
        res = 0
        add = True
        for i in range(len(mBitStr)):
            res *= 2
            if add and mBitStr[i]==nBitStr[i]:
                res += int(mBitStr[i])
            else:
                add = False
                
        return res
