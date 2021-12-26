## task 에 관한 내용 정리

- Airflow Operator
  - 각 Airflow DAG는 여러 Task로 이루어져 있음
  - operator나 sensor가 하나의 Task로 만들어짐
  - Airflow는 기본적인 Task를 위해 다양한 operator를 제공
    - BashOperator : bash command를 실행
    - PythonOperator : Python 함수를 실행
    - EmailOperator : Email을 발송
    - MySqlOperator : sql 쿼리를 수행
    - Sensor : 시간, 파일, db row, 등등을 기다리는 센서
  - Airflow에서 기본으로 제공하는 operator 외에도 커뮤니티에서 만든 수많은 operator들 존재

