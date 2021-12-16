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


### task group
- 태스크 여러개를 묶어 하나의 그룹으로 지정 가능
- 각 task는 group_id가 task_id 앞에 접두사로 붇게 됨
- 그룹 내에선 병렬처리, 그룹 간에는 지정한대로 동작
```python
with TaskGroup('processing_tasks') as processing_tasks:
        task_2 = BashOperator(
            task_id = 'task_2',
            bash_command = 'sleep 3'
        )

        task_3 = BashOperator(
            task_id = 'task_3',
            bash_command = 'sleep 3'
        )

task_1 >> processing_tasks >> task_4
```


### 실패시 재시도 방법
- 파라미터에 retries 옵션을 넣으면 된다
```python
args={
    'owner' : 'Anti',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date':days_ago(1)# 1 means yesterday
}
```
