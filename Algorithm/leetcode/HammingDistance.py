"""
주소: https://leetcode.com/problems/hamming-distance/submissions/

문제 내용
- 0 이상의 정수 x y 가 주어질때 x와 y의 Hamming Distance (비트값 차이) 를 계산하라

샘플
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

풀이 설명
- 타 언어로 구현시 비트 연산자 사용 가능
- 파이썬에서 비트연산자? 빠르지만 복잡. 조금 느리더라도 돌아가자
- 어차피 한 비트끼리만 비교하면 되고, 한 비트씩은 (value/2)%2 형태를 통해 접근 가능
- x와 y를 맨 끝 비트만 비교하면서 둘다 0이 되면 루프 종료
- 둘중에 하나라도 0보다 크면 최소한 1인 값이 위에 하나는 있는거니... 별 상관 없음

어떤 경우에 활용 가능할까
- 만약 문제가 아니라 실전이라면 DP를 통해 푸는게 나을수도 있음 => hammingDistance(32,2)=hammingDistance(8,0)+2 와 동일하니
- 두 one-hot 벡터 사이의 euclidian distance 계산시 사용 가능 => 현실적으로 비교할일은 많이 없지만 가끔 있음 (실제 tf에는 사용할지도)
- 꼭 비트단위 연산이 아니더라도 비슷한 문제 (두 값의 차이 계산) 에서 개념 적용 가능 => 일부씩 비교하면서 차이를 누적해간다
- 위와 같은 면에선 비트연산자를 활용하지 않는게 좀 더 보편적인 해답일 수 있음

"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x>0 or y>0:
            if x%2!=y%2:
                dist += 1
                
            x = int(x/2)
            y = int(y/2)
        
        return dist
        
