### Hive에서 작은 파일들 합치는 방법

#### 참조 주소: https://kidokim509.wordpress.com/2015/06/10/hive-query%EC%9D%98-output-%ED%8C%8C%EC%9D%BC%EC%9D%B4-%EC%9E%91%EC%9D%80-%EC%9A%A9%EB%9F%89%EC%9C%BC%EB%A1%9C-%EC%AA%BC%EA%B0%9C%EC%A0%B8-%EC%9E%88%EB%8A%94-%EA%B2%BD%EC%9A%B0/

#### 원인
- 기존 데이터가 잘게 쪼개져있어서 그대로 map
- 기존 데이터가 너무 큰데비해 block 사이즈가 작아 잘게 분할

#### 해결 방법
- 리듀서 조정 방법
  - 기본으로 Hive는 아웃풋 용량 256MB를 기준으로 1개의 리듀서 생성 (버전에 따라 1GB)
    - mapred.reduce.tasks 값이 -1 일 경우 위의 방식대로 동작
    - hive.exec.reducers.bytes.per.reducer 의 값으로 기준 아웃풋 용량 지정
  - 강제로 리듀서의 수를 1개로 줄이거나 기준 아웃풋 용량을 크게 하여 한개 값이 나오게 할 수있음
  - 단 리듀스 없이 맵만 처리하는 연산에서는 위 방법 불가능
- 하이브 머지 기능 활용
  - 하이브 자체적으로 작은 파일을 머지하는 기능 제공
    - hive.merge.mapredfiles 옵션을 true로 지정시 동작
    - hive.mergejob.maponly 옵션을 true로 지정시 맵만 하는 연산에서도 머지 동작
      - false일경우 리듀스가 들어간 경우에만 동작
  - 머지 파일 max 크기는 hive.merge.size.per.task 옵션을 따름 (기본 256MB)
  - 머지 파일 평균 크기는 hive.merge.smallfiles.avgsize 옵션을 따름 (기본 160MB)
  
