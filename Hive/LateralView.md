### lateral view 에 관한내용 기록

#### lateral view 란
- map이나 array와 같이 필드내에 구조화되어 들어있는 데이터 처리
- 또는 필드의 값을 연산하여 새로운 데이터 컬럼을 생성하고 이를 기존 테이블에 이어붙이는 형태로도 사용가능
  - ex) json 데이터의 연산
- 내부적으로 임시 뷰를 생성하여 연산
- 주의할점
  - lateral view 연산은 앞 연산이 이루어진 후 이루어질수밖에 없다
  - 컴파일러의 지원 불가능, 코드 구성하는대로 그대로 돌아간다
  - lateral view가 n회 사용될때마다 최대 연산 시간 n배 증가 가능
    - 최대한 몰아서 처리 필요

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

### json value
- json object를 파싱하여 값 하나만을 추출하기 위한 함수
- 사용법: JSON_VALUE({json필드}, '$.json.값.경로.입력') AS 필드명
```sql
  JSON_VALUE(jsonCol, '$.info.address.PostCode') AS PostCode,
```
- 유의사항
  - 여러 필드를 파싱해야 할 경우 JSON_TUPLE 보다 느림
  - 한 필드만 파싱할 경우 JSON_TUPLE 보다 빠름
