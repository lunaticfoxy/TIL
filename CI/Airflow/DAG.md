## Airflow의 DAG에 관한 내용 정리

### DAG란?
- Airflow 에서의 작은 실행 단위인 Task 의 모음이며, 각 Task 를 의존성을 가진 그래프로 표현한 것
- 복잡한 의존성 관리가 가능
- backfill(과거부터 채우는 작업), 중간 실패 지점부터 다시 시작할 수 있는 등의 다양한 기능을 제공함
- execution_date 이라는 특정 시점을 기준으로 잡을 실행
- schedule_interval 이라는 cron 표현식으로 스케줄링(https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html)
- DAG 이름이 DAG id 이며 유일해야 함


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
  - ${group_id}.${task_id} 형태
  - ex) group_id 가 "test_group", task_id가 "test_task" 일 경우 외부에서 보이는 task_id 는 "test_group.test_task"
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
- 태스크 그룹의 동적 생성도 가능
  - 단 매번 생성할때마다 별도의 그룹 아이디를 지정해줘야 오류가 발생하지 않음
```python
for g_id in range(1,3):
    with TaskGroup(group_id=f'group{g_id}') as tg1:
        t1 = DummyOperator(task_id='task1')
        t2 = DummyOperator(task_id='task2')

        t1 >> t2
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


### Execution Date
- DAG의 자체 실행 시간이 아닌 DAG가 파라미터로 넘겨주는 시간
- 실행 시간과 배치 작업의 대상 시간이 다른 경우에 유용
  - excution date만 동일하게 준다면 실제 어느 시점에 실행되더라도 같은 시간에 실행시킨것과 동일하게 동작
  - 장기간의 데이터 소급에 유리
