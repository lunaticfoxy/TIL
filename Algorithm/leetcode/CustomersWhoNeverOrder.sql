/*
주소: https://leetcode.com/problems/customers-who-never-order/

내용
- 고객 리스트와 고객의 구매 내역이 저장된 테이블이 주어진다
- 한번도 물건을 구매하지 않은 고객의 리스트를 출력하라

예제
Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+



풀이방법
- 단순 구현
*/

# Write your MySQL query statement below
SELECT c.Name as Customers
FROM Customers c
WHERE c.Id NOT IN (SELECT CustomerId FROM Orders)
;
