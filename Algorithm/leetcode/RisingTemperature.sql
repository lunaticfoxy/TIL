/*
주소: https://leetcode.com/problems/rising-temperature/

내용
- index, 날짜, 기온 이 있는 테이블이 주어진다
- 전날에 비해 기온이 증가한 날의 index를 리턴하라
  - recordDate는 정렬되어 있지 않다

예제

Weather
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Result table:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
In 2015-01-02, temperature was higher than the previous day (10 -> 25).
In 2015-01-04, temperature was higher than the previous day (20 -> 30).


풀이방법
- 날짜를 하루씩 더한 결과 b를 기존 테이블 w와 날짜를 기준으로 조인한다
- 이때 b의 기온이 w의 기온보다 작으면 기온이 증가한 것이므로 그때 w의 index를 리턴한다
*/
# Write your MySQL query statement below
SELECT
  w.id as id
FROM Weather w
INNER JOIN (SELECT DATE_ADD(recordDate, INTERVAL 1 DAY) AS bdate, temperature FROM Weather) b
ON w.recordDate = b.bdate
WHERE w.temperature > b.temperature
;
