## Airflow의 DAG에 관한 내용 정리

### 최대 동작 작업수 설정
- max_active_runs
  - 동시 실행 DAG 수
  - 한 대그가 동시에 몇 개 실행될 수 있는가
- concurrency
  - 동시 실행 task 수
  - 이 대그에 포함된 task는 동시에 몇 개 실행 될 수 있는가
  - 실행중인 대그 전체를 통틀어 task 수 카운트
    - ex) concurrency 가 5라면 해당 대그가 여러개 실행중이더라도 동시 실행되는 task의 합이 5개라는 뜻
- 참조: https://jybaek.tistory.com/923
