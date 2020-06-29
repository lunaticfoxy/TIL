"""
주소: https://leetcode.com/problems/the-k-strongest-values-in-an-array/

내용
- 정수로 이루어진 배열이 주어진다
- 배열의 두 원소를 비교할때 배열의 중간값과의 절대값 차이를 비교해서 차이가 더 큰 원소가 stronger 하다고 한다
- 차이가 같으면 배열의 값이 더 큰 값이 stronger 하다고 한다
- 임의의 자연수 k가 주어질때 배열내에서 가장 strong 한 원소 k개를 순서대로 리턴하라




"""
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = sorted(arr)[int((len(arr)-1)/2)]
        
        def getKey(x):
            return abs(x[0] - med)*10000 + x[0]
            
        arr_with_idx = [[x, i] for i, x in enumerate(arr)]
        
        sorted_arr = [x[0] for x in sorted(arr_with_idx, key = getKey, reverse = True)]
        print(sorted_arr)
        
        return sorted_arr[:k]
