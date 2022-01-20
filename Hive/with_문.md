## With 문에 대한 자료 정리
- 참조: https://heodolf.tistory.com/71

### with 문이란?
- 이름을 가진 SubQuery를 정의한 후 사용하는 구문.
  - Query의 전체적인 가독성을 높이고, 재사용할 수 있는 장점이 있음.
  - 대부분의 DBMS에서 지원함
  - 계층형 쿼리 구현 가능
 

- 기본 구조
```sql
WITH [ 별명1 ] [ (컬럼명1 [,컬럼명2]) ] AS (
    SUB QUERY
)[, 별명2 AS ... ]
MAIN QUERY
```
- WITH [ 별명 ] AS ( SUB QUERY )
- 컬럼명은 생략 가능
- 쉼표(,)로 구분하여 여러개를 정의할 수 있음.
- 먼저 생성된 SubQuery는 나중에 생성하는 SubQuery에서 사용할 수 있음.
  - ex) [ 별명2 ]에서 [ 별명1 ]을 사용 가능

 

- 예제
   - DEPT테이블에서 부서번호와 근무지를 출력하시오.
```sql
/** SUB QUERY를 이용한 방법 **/
SELECT T1.*
  FROM (
       SELECT A.DEPTNO
            , A.LOC
         FROM SCOTT.DEPT A
       ) T1
 WHERE 1=1
;
 
/** WITH문을 이용한 방법 **/
WITH DEPT_LOC ( DEPTNO, LOC ) AS (
    SELECT A.DEPTNO
         , A.LOC
      FROM SCOTT.DEPT A
)
SELECT T1.*
  FROM DEPT_LOC
 WHERE 1=1
;
```

- EMP테이블에서 사원번호, 사원명, 부서명, 부서의 인원이 몇명인지 출력하시오.
```sql
/** SUB QUERY를 이용한 방법 **/
SELECT T1.EMPNO
     , T1.ENAME
     , T2.DNAME
     , T2.DCNT
  FROM SCOTT.EMP T1
  LEFT OUTER JOIN (
          SELECT A.DEPTNO
             , MAX(A.DNAME) AS DNAME
             , COUNT(B.EMPNO) AS DCNT
          FROM SCOTT.DEPT A
          LEFT OUTER JOIN SCOTT.EMP B
            ON B.DEPTNO = A.DEPTNO
         WHERE 1=1
         GROUP BY A.DEPTNO
  ) T2
    ON T2.DEPTNO = T1.DEPTNO
 WHERE 1=1
;
 
/** WITH문을 이용한 방법 **/
WITH DEPT_CNT AS (
    SELECT A.DEPTNO
         , MAX(A.DNAME) AS DNAME
         , COUNT(B.EMPNO) AS DCNT
      FROM SCOTT.DEPT A
      LEFT OUTER JOIN SCOTT.EMP B
        ON B.DEPTNO = A.DEPTNO
     WHERE 1=1
     GROUP BY A.DEPTNO
)
SELECT T1.EMPNO
     , T1.ENAME
     , T2.DNAME
     , T2.DCNT
  FROM SCOTT.EMP T1
  LEFT OUTER JOIN DEPT_CNT T2
    ON T2.DEPTNO = T1.DEPTNO
 WHERE 1=1
;
```
