### Impyla 를 통한 Python에서의 Hive 연동 방법

#### Impyla란?
- python에서 하둡에 설치된 Impala에 접근하기 위한 라이브러리
- 지만 Hive용으로 사용할 수 있다

#### 기본 사용법
- 단계 (내맘대로 정한거)
  - Connect: Hive 서버와의 커넥션을 생성한다
  - Get Cursor: 커넥션에서 쿼리를 수행할 커서를 가져온다
  - Execute Query: 커서에 쿼리를 보내고 Hive에서 동작을 수행한다
  - Get Data: 데이터를 가져올 경우에는 커서에 출력을 요청한다
- 중요한점
  - 하둡은 "대용량" 파일 시스템이다. 한번에 너무 많은 데이터를 가져오면 못버틴다
  - 적당히 나눠서 가져올것
- 실제 사용 객체 예시
```python
from impala.dbapi import connect
from impala.util import as_pandas

class HiveConn():
    def __init__(self):
        self.conn=connect(host='Hive서버주소',
             port=포트번호,
             auth_mechanism='인증방법',
             kerberos_service_name='인증서비스명'
            )
        
        self.cursors = dict()
    
    def setTableCursor(self, dbName, tableName):  # 데이터를 가져올 커서 지정, 데이터를 나눠서 가져오려고 커서만 만들어둠
        cursor = self.conn.cursor()
        cursor.execute("select * from " + dbName + "." + tableName)
        self.cursors[dbName + "." + tableName] = cursor
    
    def getTableData(self, dbName, tableName, count): # 지정된 커서에서 count개 만큼 데이터 가져옴
        return self.cursors[dbName + "." + tableName].fetchmany(count)
```
    
