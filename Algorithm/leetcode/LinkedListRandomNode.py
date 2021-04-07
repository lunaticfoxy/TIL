"""
주소: https://leetcode.com/problems/linked-list-random-node/

내용
- 주어진 링크드리스트에서 랜덤하게 값을 뽑아내라

예제
Example 1
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.

풀이방법
- 단순구현
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.vals = []
        
        cur = head
        while cur != None:
            self.vals.append(cur.val)
            cur = cur.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        
        return self.vals[random.randrange(0, len(self.vals))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
