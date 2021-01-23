### 연산자 카테고리
- 종류가 많고 쓰임새를 짐작하기 쉬움
- 생성 연산자
  - Observable로 데이터 생성
  - just, fromXXX, create, interval, range, timer, intervalRange, defer, repeat
- 변환, 필터 연산자
  - 데이터 흐륾을 원하는 방식으로 변형
  - 변환: map, flatMap, concatMap, switchMap, groupBy, scan, buffer, window
  - 필터: filter, take, skip, distinct
- 결합 연산자
  - 여러개의 Observable을 조합하여 활용 가능
  - zip, combineLastest, merge, concat
- 조건 연산자
  - amb. takeUtil, skipUtil, all
- 에러 처리 연산자
  - 7장에 등장
  - onErrorReturn, onErrorResumeNext, retry, retryUntill
- 기타 연산자
  - subscribe, subscribeOn, onbserveOn, reduce, count
  
  
## 4.1 생성 연산자
- 데이터의 흐름을 만드는 것
  - Observable 계열
- 2장 외의 생성 연산자들 다룸

### 4.1.1 interval() 함수
- 일정 시간 간격으로 데이터 생성
