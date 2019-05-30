#### Spark 구동시 None.get 에러 발생하는 경우

##### 원인
- Runtime에 Scala 기본 라이브러리에서 발생하는 에러
  - None 타입의 객체에서 get 함수를 호출할때 발생
  - 주로 어레이나 리스트 내부의 원소를 순회할때 None이 끼어있어서 발생
- Spark에서 발생하는 경우
  - 낮은 버전의 Spark에서 (아마 2.3 이하) count, fileter 등 DF, RDD를 순회할 경우 간혹 발생
    - 단 한번 발생한 쿼리는 반드시 발생
  - 잘못된 데이터가 끼어있을때 여기다가 get 연산을 수행해서 발생하는 에러
  - 2.3버전부터 해결된 것으로 확인
    - 관련 한글 블록: https://knight76.tistory.com/entry/spark-spark-20-21-사용시-주의사항
    - 이슈: https://github.com/apache/spark/pull/17290
    - 해결 커밋 로그 1: https://github.com/apache/spark/commit/27234e154db18cbc614053446713636a69046090
    - 해결 커밋 로그 2: https://github.com/apache/spark/commit/5da4bcffa1b39ea8c83fe63a09e68297be371784
    
##### 해결방법
- 코드를 직접 수정 가능할 때
  - get 대신 getOrElse 를 사용한다
  - 직접 get 하기보단 map 또는 flatMap으로 순회한다
- Spark 레벨
  - 버전을 올린다
  - 버전을 올리는게 불가능할 땐
    - 데이터 자체를 변경한다
    - 데이터를 읽을때 포맷에 따라 구조가 달라지므로 최대한 단순화 하면 문제가 사라진다
      - ex) spark의 parquet으로 저장되고 입력 출력 포맷이 따로 지정된 테이블을 hive에서 컬럼과 파티션만 지정해준 테이블로 바꾸면 잘 동작한다
    
