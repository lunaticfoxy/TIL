## RDD 와 관련한 내용을 정리하는 글

#### DataFrame -> RDD 시 주의할점
- DataFrame은 DataSet[Row] 이므로 RDD로 전환시 RDD[Row] 가 된다
- 따라서 바로 전환하면 실수하는 케이스가 많으니 Row를 풀어서 RDD[원하는 데이터 타입] 으로 변환하는 과정이 필요하다

### RDD의 union
- sc.union(Seq(RDD1, RDD2)) 형태로 union이 가능하다

### RDD 문제점
- RDD는 이미 최소 데이터 단위라 추가 최적화 어려움
  - 컴파일러 지원 불가능
  - 코드에따라 성능 하락 발생 가능
- 가능한 Dataframe 객체 연산으로 전환
