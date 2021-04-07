"""
주소: https://leetcode.com/problems/random-pick-index/

내용
- 자연수 배열이 주어진다
- 값이 주어지면 해당 값이 들어있는 인덱스중 하나를 랜덤하게 리턴하라


예시
Example 1:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.


풀이방법
- 단순구현
"""
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.last = 0
        self.indicies = dict()
        
        for i, num in enumerate(nums):
            if num in self.indicies:
                self.indicies[num].append(i)
            else:
                self.indicies[num] = [i]
    
        

    def pick(self, target: int) -> int:
        self.last = (self.last + 1) % len(self.indicies[target])
        return self.indicies[target][self.last]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
