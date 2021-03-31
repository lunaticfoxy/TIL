/*
주소: https://leetcode.com/problems/exchange-seats/

내용
- 자리 순서대로 학생들의 이름이 주어진다
- 인접한 두 학생들끼리 자리를 바꾸려 한다
- 남는 학생은 그대로 앉는다

예제
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.
The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

For the sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

Note: If the number of students is odd, there is no need to change the last one's seat.


풀이방법
- 이중 IF 문 사용
  - id가 max(id) 일 경우 짝수면 -1, 홀수면 그대로 유지
  - id가 max(id)가 아닌 경우 짝수면 -1, 홀수면 +1
*/
SELECT
    IF(id = (SELECT max(id) FROM seat),
        IF(MOD(id, 2) = 1, id, id - 1),
        IF(MOD(id, 2) = 1, id + 1, id - 1)
    ) as id,
    student
FROM seat 
ORDER BY id
;
