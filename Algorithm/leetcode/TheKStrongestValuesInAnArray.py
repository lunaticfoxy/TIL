"""
주소: https://leetcode.com/problems/the-k-strongest-values-in-an-array/

내용
- 어떤 배열에서 중간값과 해당 값의 차이의 절대값을 그 값의 strong 정도 라고 한다
  - 중간값은 (배열의 기리-1)/2 번째로 작은 값을 말한다
- 배열과 임의의 숫자 K가 주어질때 배열의 값 중 Strong한 순서대로 K개를 리턴하라

샘플
Example 1:
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.

Example 2:
Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].

Example 3:
Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.

Example 4:
Input: arr = [6,-3,7,2,11], k = 3
Output: [-3,11,2]

Example 5:
Input: arr = [-7,22,17,3], k = 2
Output: [22,17]


풀이방법
- 단순 정렬후 k개 추출
"""
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = sorted(arr)[int((len(arr)-1)/2)]
        
        def getKey(x):
            return abs(x[0] - med)*100000 + x[0]
            
        arr_with_idx = [[x, i] for i, x in enumerate(arr)]
        
        sorted_arr = [x[0] for x in sorted(arr_with_idx, key = getKey, reverse = True)]
        
        return sorted_arr[:k]
