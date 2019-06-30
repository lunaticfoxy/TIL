"""
주소: https://leetcode.com/problems/distribute-candies-to-people/

내용
- 사탕이 candies개만큼 주어지고 이를 num_people명의 사람들에게 줄것이다
- 사탕을 첫 사람부터 1개, 2개, 3개 식으로 주고, n명까지 준 뒤에는 첫 사람으로 돌아와서 n+1개, n+2개, ... 식으로 준다
- 사탕이 모자라면 해당 번째 사람에게 남은 사탕을 다 주고 끝낸다
- 사람별로 나눠준 사탕 리스트를 구하라

샘플
Example 1:
Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

Example 2:
Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].


풀이방법
- 단순 구현이므로 생략

"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:   
        res = [0 for _ in range(num_people)]
        i = 1
        while True:
            if candies<=i:
                res[(i-1)%num_people] += candies
                break
            
            res[(i-1)%num_people] += i
            candies -= i
            i += 1
        
        return res
