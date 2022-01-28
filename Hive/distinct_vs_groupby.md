## distinct를 사용해서 중복값을 제거하는 것과 group_by 의 차이
- 두 쿼리를 사용해서 동일한 결과를 낼 수 있음

```sql
SELECT date_id, COUNT(DISTINCT item)
FROM test_db.tb_test
WHERE date_id BETWEEN "2021-05-01" AND "2021-05-05"
GROUP BY date_id
;


SELECT date_id, COUNT(*)
FROM
    (SELECT date_id, item
    FROM test_db.tb_test
    WHERE date_id BETWEEN "2021-05-01" AND "2021-05-05"
    GROUP BY date_id, item) sub
;
```

- group by 가 한단계가 더 들어가서 복잡해보임
- 속도는?
  - 데이터가 많으면 group by 가 더 빠르다
- 이유?
  - map-reduce 관점에서 group by 는 mapper에서, distinct는 reducer에서 일어남
  - 따라서 group by 연산은 mapper 단계에서 병렬화가 되고, distinct는 병렬화가 되지 않음
  - 병렬화시 성능 개선이 용이한 큰 데이터에서는 group by, 작은양의 데이터에서는 distinct가 유리
