/*
주소: https://leetcode.com/problems/delete-duplicate-emails/

내용
- 주어진 테이블에서 이메일이 같은 유저를 가장 작은 Id만 남기고 삭제하라

예제
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+



풀이방법
- delete 내에서 비교 조건 사용 필요
- a, b를 참조하고, 이중에 a를 삭제할 대상으로 지정한 뒤 조건 설정
*/
# Write your MySQL query statement below
DELETE a 
FROM  Person a, Person b
WHERE a.Id > b.Id AND a.Email=b.Email;
