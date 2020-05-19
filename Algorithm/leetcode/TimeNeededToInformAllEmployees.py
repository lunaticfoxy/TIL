"""
주소: https://leetcode.com/problems/time-needed-to-inform-all-employees/

내용
- n명으로 구성된 회사의 조직원들이 각자 0부터 n-1까지의 인덱스를 가지고 있다
- 자기 상사의 인덱스, 자기가 자기 부하 직원한테 정보를 전달하는데 걸리는 시간, 회사의 보스의 인덱스 가 주어진다
- 이때 보스가 명령을 내렸을때 회사 전체에 퍼지는 시간을 구하라

샘플
Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

Example 3:
Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.

Example 4:
Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.

Example 5:
Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076

풀이방법
- 트리로 아래쪽으로 내려가면서 max만 남겨서 위로 올리면 된다
  - 마치 트리 레벨 계산하듯이
- 단 일반적으로는 부모 -> 자식이 주어지지만 여기서는 자식 -> 부모가 주어져서 이를 부모 -> 자식으로 바꾸는 과정이 필요하다
- 이를 위해 managerMap을 만들어 i번째 직원을 상사로 삼는 직원들의 인덱스를 한번 저장
- 이후 managerMap을 활용하면 i번째 직원이 가지는 부하 직원들을 찾을 수 있고, 이를 children 이라는 변수로 재귀 함수에 전달한다

"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def recurFunc(curNode, children, informTime):
            if len(children[curNode]) == 0:
                return 0
            else:
                max_time = 0
                
                for i in children[curNode]:
                    temp = recurFunc(i, children, informTime)
                    if temp > max_time:
                        max_time = temp
                
                return max_time + informTime[curNode]
        
        
        children = [[] for _ in range(n)]
        
        for i, m in enumerate(manager):
            if not m == -1:
                children[m].append(i)
        
        return recurFunc(headID, children, informTime)
