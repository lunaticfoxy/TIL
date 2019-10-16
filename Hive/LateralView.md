### lateral view 에 관한내용 기록

#### lateral view 란
- map이나 array와 같이 필드내에 구조화되어 들어있는 데이터 처리
- 내부적으로 임시 뷰를 생성하여 연산

#### explode
- map이나 array의 원소를 풀어서 원소별로 하나씩 로우 생성
- 해당 필드 외의 필드들은 모두 동일한 값을 지님
```sql
select key, value, other
from table1
lateral view explode(mapcolumn) k as key, value

select elem, other
from table2
lateral view explode(arrcolumn) a as elem
```

#### json tuple
- json object를 파싱하기위한 함수
- 다음과같이 이중으로도 파싱가능
```sql
select v2.name,v2.id 
from clients c 
lateral view json_tuple(c.client, 'info') v1 as info
lateral view json_tuble(v1.info,'id','name') v2 as id,name
``` 
