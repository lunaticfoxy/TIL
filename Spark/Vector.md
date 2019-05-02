#### Spark에서의 벡터

##### 개요
- 패키지 위치: org.apache.spark.ml.linalg
- 용도
  - 말 그대로 수학의 벡터 값을 저장
  - ML 등에 활용
- 종류
  - Vector (기본 클래스)
  - DenseVector
  - SparseVector
  
##### SparseVector
- org.apache.spark.ml.linalg.SparseVector
- org.apache.spark.ml.linalg.Vector를 상속받아 생성됨
- 구성
  - size: 벡터 전체 크기
  - indices: 0이 아닌 값의 인덱스 리스트
  - values: indices 리스트에 해당하는 값
- 사용법
  - table 저장시 알아서 저장됨
  - 불러올때 df.select("피쳐이름") 으로 로드해서 사용 가능
    - ex) model.transform(df.select("features"))
