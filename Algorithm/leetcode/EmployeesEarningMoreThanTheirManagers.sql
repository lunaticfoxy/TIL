/*
주소: https://leetcode.com/problems/employees-earning-more-than-their-managers/

내용
- 직원들의 이름, 급료, 매니저 가 포함된 테이블이 주어진다
- 자신의 매니저보다 더 많은 급여를 받는 직원의 이름을 구하라

예제
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+


풀이방법
- 단순 구현
- 셀프 조인으로 매니저를 찾고 매니저와 자신의 급료를 비교

*/


# Write your MySQL query statement below

SELECT e.Name as Employee
FROM Employee m
INNER JOIN Employee e
ON m.Id = e.ManagerId
WHERE m.Salary < e.Salary
;
