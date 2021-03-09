/*
주소: https://leetcode.com/problems/department-highest-salary/

내용
- 직원의 급여 테이블과 부서 정보 테이블이 있고, 두 테이블은 조인 가능하다
- 부서별 가장 많은 급여를 받는 직원의 부서, 이름, 급여를 출력하라

예시
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

풀이방법
- 먼저 부서별 가장 많은 급여를 찾은뒤 해당부서에서 해당급여를 받는 직원을 찾는다
- 이후 해당 직원의 부서명을 가져와서 
*/

SELECT
    d.Name AS Department, me.Name AS Employee, me.Salary as Salary
FROM
    (SELECT e.Name, e.Salary, e.DepartmentId
    FROM Employee e
    INNER JOIN 
        (SELECT DepartmentId AS did, MAX(Salary) AS ms
        FROM Employee 
        GROUP BY DepartmentId) m
    ON m.did=e.DepartmentId AND m.ms=e.Salary) me
INNER JOIN Department d
ON me.DepartmentId=d.Id
;
