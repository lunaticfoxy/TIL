### Hive SQL의 조건문 처리 방법

#### 1. IF
- 한개의 조건을 체크하고 리턴
- IF(condition, true_case, false_case) 형태로 사용
- 예시
```sql
SELECT IF(1=1,'true','false') AS IF_CONDITION_TEST;
```

#### 2. CASE
- IF-ELSE 문과 동일하다 생각하면 됨
- 조건에는 수식이 들어갈 수 있음
- 어떤 값이 여러개의 조건중 매칭되는 첫번째 값 체크
- CASE WHEN a THEN b [WHEN c THEN d]… [ELSE e] END 형태로 사용
- 예시
```sql
SELECT
  CASE WHEN age<10 THEN 0
    WHEN age<20 THEN 1
    WHEN age<30 THEN 2
    WHEN age<40 THEN 3
    ELSE 4
  END AS age_area
FROM table;
```

#### 3. NULL 체크
- Boolean 체크
  - isnull(a): a가 NULL 이면 true 리턴
  - isnotnull(a): a가 NULL 이 아니면 true 리턴
- NULL 값 대치
  - NVL(check_value, change_value): check_value가 NULL이 아니면 check_value, NULL이면 change_value 리턴
  - coalece(value1, value2, ...): value중 NULL 이 아닌 최초의 값 리턴, 모두 NULL이면 NULL 리턴
- 예시
```sql
SELECT isnull(NULL);

SELECT isnotnull(NULL);

SELECT nvl(NULL,'value is null');

SELECT coalesce(null,'a',null,'b');
```

#### 4. Decode
- C의 switch-case 문과 동일하다 생각하면 됨
- 여러 값 중 주어진 값과 동일한 값을 찾고 해당 값에 매칭되는 결과 리턴
  - 주어진 값을 인덱스로 사용하는 맵
- decode(<expr>, <search1>, <result1>, … <search N>, <result N>, <default>) 형태
- 예시
```sql
SELECT
  event,
  decode(day_of_week,
    1, "Monday",
    2, "Tuesday",
    3, "Wednesday",
    4, "Thursday",
    5, "Friday",
    6, "Saturday",
    7, "Sunday",
    "Unknown day")
FROM calendar;
```
