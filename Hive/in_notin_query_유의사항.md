### IN, NOT IN 쿼리 구성시에 유의해야 할 사항

#### 출처: https://wjheo.tistory.com/entry/IN%EA%B3%BC-NOT-IN%EC%9D%98-%ED%95%A8%EC%A0%95

#### 요약
- 조건 리스트 내에 null 이 있으면 동작하지 않을 수 있다

#### IN 의 함정
- A IN (B1, B2, ... Bn) 쿼리는 실제로 (A=B1 or A=B2 or ... A=Bn) 으로 바뀌어 동작
- hobby가 null 이거나 '낚시' 인 경우
  - hobby in (null, '낚시') 는 hobby가 '낚시' 일때만 동작
    - hobby=null or hobby='낚시' 로 변환됨
    - null 값 비교에 = 혹은 <> (!=) 를 사용하면 무조건 false 리턴
    
#### NOT IN 의 함정
- A NOT IN (B1, B2, ... Bn) 쿼리는 실제로 (A<>B1 and A<>B2 and ... A<>Bn) 으로 바뀌어 동작
- hobby가 null 과 '낚시' 가 아닌경우
  - hobby not in('낚시', null) 는 무조건 동작하지 않음
    - (hobby<>'낚시' and hobby<>null) 로 변환됨
    - hobby<>null 은 무조건 false 리턴되므로 (null에 <>를 사용할 수 없으므로) 무조건 false

### NOT IN 에서 "Cartesian products are disabled for safety reasons" 에러가 발생할 경우
- 원인: NOT IN은 모든 결과물을 N*M 으로 조인한 뒤 체크하기 때문에 hive에서 strict 모드일 경우 오류가 발생
- 해결 방법
  - 설정 변경: set hive.mapred.mode=nonstrict;
  - NOT IN -> EXCEPT 로 변경 (hive에서는 동작하지 않음)
```sql
SELECT ProductID   
FROM Production.Product  
EXCEPT  
SELECT ProductID   
FROM Production.WorkOrder
;  
```
  - NOT IN -> LEFT OUTER JOIN + 조인키에 대한 IS NULL 체크
```sql
SELECT a.ProductID   
FROM Production.Product a
LEFT OUTER JOIN Production.WorkOrder b
ON a.ProductID = b.ProductID
WHERE b.ProductID IS NULL
;
```
