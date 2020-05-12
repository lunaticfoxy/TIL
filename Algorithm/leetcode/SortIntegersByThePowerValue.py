"""
주소: https://leetcode.com/problems/sort-integers-by-the-power-value/

내용
- 어떤 값 x가 주어졌을때 이 x는 1이 될때까지 다음 식으로 계속 변화한다
  - x가 짝수: x = x/2
  - x가 홀수: x = 3*x + 1
- 이렇게 1이 될때까지 변하는 횟수를 해당 값의 power value 라 한다
- 자연수의 범위와 k가 주어질때 자연수의 power value를 오름차순으로 정렬시 k번째 자연수를 구하라
  - power value가 같으면 자연수 값을 기준으로 정렬한다
  
샘플
Example 1:

Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.

Example 2:
Input: lo = 1, hi = 1, k = 1
Output: 1

Example 3:
Input: lo = 7, hi = 11, k = 4
Output: 7
Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.

Example 4:
Input: lo = 10, hi = 20, k = 5
Output: 13

Example 5:
Input: lo = 1, hi = 1000, k = 777
Output: 570


풀이방법
- 재귀 + DP로 해결
- 재귀적으로 탐색되면서 1씩 증가될 것이다
- 단 이를 매번 계산하면 당연히 안되므로 DP로 저장해놓는다
- 인덱스는 넉넉하게 100000까지

"""
pow_val = [-1 for _ in range(1000000)]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        pow_val[0] = 0
        pow_val[1] = 0
        
        def getPowVal(x):
            #print(x)
            if pow_val[x] == -1:
                if x%2==0:
                    pow_val[x] = getPowVal(int(x/2)) + 1
                else:
                    pow_val[x] = getPowVal(3*x + 1) + 1
            
            return pow_val[x]
        
        pows = [[x, getPowVal(x)] for x in range(lo, hi+1)]
        
        def getKey(x):
            return 1000000*x[1]+x[0]
        
        pows = sorted(pows, key = getKey)
        #print(pow_val)
        return pows[k-1][0]
            
