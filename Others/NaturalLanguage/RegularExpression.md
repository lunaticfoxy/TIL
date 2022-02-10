## 정규표현식에 관한 내용 기록


### 시작과 끝 지정
- 특정 문자열 시작: ^(문자열)
- 특정 문자열 끝: (문자열)$
```sql
SELECT * FROM test_tb WHERE str RLIKE "^abc";  # abc 로 시작하는 문자열을 찾아라
SELECT * FROM test_tb WHERE str RLIKE "abc$";  # abc 로 끝나는 문자열을 찾아라
SELECT * FROM test_tb WHERE str RLIKE "^abc$"; # abc 와 일치하는 문자열을 찾아라 (str = "abc)
```
