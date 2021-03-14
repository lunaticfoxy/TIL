/*
주소: https://leetcode.com/problems/duplicate-emails/

내용
- 중복된 이메일 주소를 찾아라


예제
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

풀이방법
- 단순 구현
*/

# Write your MySQL query statement below
SELECT o.Email
FROM (SELECT c.Email, count(*) as cnt
      FROM Person c
      GROUP BY c.Email
     ) o
WHERE o.cnt >= 2
;
