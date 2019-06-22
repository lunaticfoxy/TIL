"""
주소: https://leetcode.com/problems/house-robber/

내용
- 강도가 집에서 물건을 훔치는데 집마다 훔쳤을때 가치를 알고있다
- 붙어있는 집은 연속해서 훔칠수 없다고 할때 강도가 훔칠수 있는 최대 가치를 구하라

샘플
Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

풀이방법
- 바로 옆집은 훔치지 못하므로 한 집을 훔친 뒤에는 2칸 뒤, 3칸 뒤 집을 훔쳐야 한다
- 4칸 이상부터는 2칸, 2칸 씩 훔치는게 무조건 이익이므로 2칸, 3칸 케이스만 보면 된다
- 따라서 dp를 통해 풀면서 i 지점에서 i-2, i-3지점의 값 중 큰 값에다가 현재 집의 값을 더하면 된다
- 리턴시에는 배열의 맨 뒤 두개중 큰 값을 리턴한다
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln==0:
            return 0
        elif ln==1:
            return nums[0]
        elif ln==2:
            return max(nums[0], nums[1])
        
        dp = [nums[0], nums[1], nums[0] + nums[2]]
        
        for i in range(3, ln):
            dp.append(max(dp[i-3], dp[i-2]) + nums[i])

        return max(dp[-1], dp[-2])
