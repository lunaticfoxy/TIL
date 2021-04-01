/*
주소: https://leetcode.com/problems/human-traffic-of-stadium/

내용
- 매일 경기장의 경기일, 입장인원을 저장한 테이블이 주어진다
  - 주말로 인해 경기일 사이에 빈 날짜가 있을 수 있다
- 3일 이상 연속해서 100명이 들어온 날짜의 id, 날짜, 입장인원을 출력하라

예제
Table: Stadium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the primary key for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
No two rows will have the same visit_date, and as the id increases, the dates increase as well.

Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
Return the result table ordered by visit_date in ascending order.
The query result format is in the following example.


Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+

Result table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.


풀이방법
- 3개씩 값을 묶어 첫째날, 둘째날, 셋째날로 간주하여 조건에 맞는 날을 리턴한다
- 이때 4일 이상 연속된 경우 중복 출력이 되므로 중복 제거 로직을 넣어준다
  - distinct로 해도 되지만 group by 로 묶었다
*/

# Write your MySQL query statement below
SELECT id, visit_date, people
FROM
    (SELECT a.id, a.visit_date, a.people
    FROM Stadium a, Stadium b, Stadium c
    WHERE a.people >= 100 AND b.people >= 100 AND c.people >= 100
        AND ((a.id = b.id - 1 AND a.id = c.id - 2)
            OR (a.id = b.id + 1 AND a.id = c.id - 1)
            OR (a.id = b.id + 2 AND a.id = c.id + 1))) d
GROUP BY id, visit_date, people
ORDER BY id
;
