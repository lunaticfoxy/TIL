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
  - 0부터 시작해서 1씩 증가하는 Long 객체 리턴
    - Integer 아님
    - long 값이 아닌 Long 객체
  - 파라미터로 초기 딜레이, 간격, 시간 단위 조정 가능
- 별도의 Support 스레드에서 시간을 조정하므로 메인 쓰레드가 블로킹시에도 동작
- 영구 동작이 기본
  - 폴링 용도로 자주 사용
  - take로 
```java
public class CommonUtils {                 // 앞으로 자주 사용할 임의의 시간 측정 클래스
  // 실행시간 표시를 위한 정적 변수
  public static long startTime;
  
  public static void exampleStart() {      // 시작 시간 체크
    startTime = System.currentTimeMills();
  }
  
  public static void sleep() {
    // 대충 쓰레드 슬립하는 내용
  }
  
  // 기타 등등
}


class Log {                               // 앞으로 자주 사용할 임의의 로그 클래스
  public static void it(Object obs) {
    long time = System.currentTimeMiils() - CommonUtils.startTime;
    System.out.println(getThreadName() + " | " + time + " | " + "value = " + obj; // 로그를 출력: "동작스레드 | 시간 | 값" 형태
  }
  
  
}


CommonUnits.exampleStart(); // 시작 시간을 표시

Observable<Long> source = Observable.interval(100L, TimeUnit.MILLISECONDS)       // 100ms 마다 동작 (초기 지연값도 100ms)
  .map(data -> (data + 1) * 100)                                                 // (값 + 1) * 100 을 리턴
  .take(5);                                                                      // 5개만 출력하고 종료
  
  
source.subscribe(Log::it);  // 발행 될때마다 로그 출력

CommonUtils.sleep(1000);    // 스레드가 죽지 않게 하기 위해 슬립
// RxComputationThreadPool-1 | 271 | value = 100
// RxComputationThreadPool-1 | 372 | value = 200
// RxComputationThreadPool-1 | 470 | value = 300
// RxComputationThreadPool-1 | 570 | value = 400
// RxComputationThreadPool-1 | 672 | value = 500



CommonUnits.exampleStart(); // 시작 시간을 표시

// 초기 지연값 외에는 위와 동일한 동작
Observable<Long> source2 = Observable.interval(0L, 100L, TimeUnit.MILLISECONDS)  // 초기 지연시간이 0이고 100ms 마다 동작
  .map(data -> (data + 1) * 100)                                                 // (값 + 1) * 100 을 리턴
  .take(5);                                                                      // 5개만 출력하고 종료

source2.subscribe(Log::it);  // 발행 될때마다 로그 출력

CommonUtils.sleep(1000);    // 스레드가 죽지 않게 하기 위해 슬립
// RxComputationThreadPool-1 | 140 | value = 100
// RxComputationThreadPool-1 | 241 | value = 200
// RxComputationThreadPool-1 | 341 | value = 300
// RxComputationThreadPool-1 | 441 | value = 400
// RxComputationThreadPool-1 | 541 | value = 500
```


### 4.1.2 timer() 함수
- interval과 유사하지만 한번만 실행
- 일정 시간 후 한 개의 데이터만 발행하고 onComplete 발생


