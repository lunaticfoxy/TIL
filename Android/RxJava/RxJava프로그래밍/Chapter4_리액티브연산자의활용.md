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
- 별도의 Support 스레드에서 시간을 발행하므로 메인 쓰레드가 블로킹시에도 동작
- 영구 동작이 기본
  - 폴링 용도로 자주 사용
  - take로 동작 횟수 지정 가능
    - 횟수 만큼 동작 후 onComplete 
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
  
  public static void i(Object obs) {
    System.out.println(getThreadName() + " | " + "value = " + obj; // 로그를 출력: "동작스레드 | 값" 형태
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
- 파라미터로 지연시간, 시간단위를 입력받음
- 발생시 0L 값 하나 전달 (사실상 큰 의미 없음)
```java
CommonUnits.exampleStart(); // 시작 시간을 표시

Observable<Long> source = Observable.timer(500L, TimeUnit.MILLISECONDS)   // 500ms 지연 후 동작
  .map(notUsed -> {
    return new SimpleDateFormat("yyyy/MM/dd HH:mm:ss").format(new Date()) // 현재 날짜 리턴
  });

source.subscribe(Log::it);  // 발행 될때 로그 출력

CommonUtils.sleep(1000);    // 스레드가 죽지 않게 하기 위해 슬립

// RxComputationThreadPool-1 | 739 | value = 2021/01/24 21:15:54
```


### 4.1.3 range() 함수
- 주어진 값 n 부터 m 개의 Integer 객체 발행
  - 시간 관련된 함수와 다르게 Integer 임 (Long 아님)
- 메인 스레드에서 동작
```java

Observable<Long> source = Observable.range(1, 10)   // 1부터 10까지 발행
  .filter(number -> number % 2 == 0);               // 발행값이 짝수인 경우에만 구독자한테 전달

source.subscribe(Log::i);  // 발행 될때 로그 출력
// main | value = 2
// main | value = 4
// main | value = 6
// main | value = 8
// main | value = 10
```


### 4.1.4 intervalRange() 함수
- interval과 range의 혼합
  - interval처럼 일정 간격으로 데이터 발행
  - range처럼 범위에 대항하는 값만 발행 후 onComplete
- Long 타입 리턴
- 별도의 쓰레드에서 동작

```java
Observable<Long> source = Observable.invervalRange(1, 5, 100L, 100L, TimeUnit.MILLISECONDS);  // 1부터 5개의 숫자를 100ms 지연 후 100ms 마다 발행

source.subscribe(Log::i);                                                                     // 발행 될때 로그 출력

CommonUtils.sleep(1000);                                                                      // 스레드가 죽지 않게 하기 위해 슬립
// RxComputationThreadPool-1 | value = 1
// RxComputationThreadPool-1 | value = 2
// RxComputationThreadPool-1 | value = 3
// RxComputationThreadPool-1 | value = 4
// RxComputationThreadPool-1 | value = 5
```

- interval로 intervalRange만들기
  - interval과 map, take를 조합하여 동일한 기능을 하는 함수 구현 가능
```java

Observable<Long> source = Observable.inverval(100L, TimeUnit.MILLISECONDS);  // 100ms 지연 후 100ms 마다 0부터 발행
  .map(val -> val + 1)                                                       // 발행값에 1 추가
  .take(5);                                                                  // 5개만 발행

source.subscribe(Log::i);                                                    // 발행 될때 로그 출력

CommonUtils.sleep(1000);                                                     // 스레드가 죽지 않게 하기 위해 슬립
// RxComputationThreadPool-1 | value = 1
// RxComputationThreadPool-1 | value = 2
// RxComputationThreadPool-1 | value = 3
// RxComputationThreadPool-1 | value = 4
// RxComputationThreadPool-1 | value = 5
```


### 4.1.5 defer() 함수
- subscribe가 호출되는 순간 (= 구독자가 요청을 보내는 순간) Observable 생성
  - subscribe를 호출하는 순간 callable이 호출
  - Observable의 생성 자체를 원할때까지 미룰 수 있음
    - 이미 생성된 Observable의 발행을 미루는것과 살짝 다름

```java
Iterator<String> numbers = Arrays.asList("1", "3", "5", "6").iterator();   // [1,3,5,6] 으로 이루어진 리스트의 이터레이터를 리턴

// 번호를 발행하는 Observable 생성
public Observable<String> getObservable() {
  if(numbers.hasNext) {                                                    // 이터레이터가 순회할 다음 값이 있으면
    String number = numbers.next();                                        // 해당 값을 리턴
    return Observable.just(number);
  }
  else                                                                     // 순회활 다음 값이 없으면
    return Observable.empty();                                             // 빈 값 리턴
}

Callable<Observable<String>> supplier = () -> getObservable();             // 호출하는 순간에 새로운 Observable을 만드는 Callable 생성
                                                                           // 호출할때마다 서로 다른 Observable 생김
/*
// 아래와 같은 의미
Callable<Observable<String>> supplier = new Callable<Observable<String>>{
  @Override
  Observable<String> call() throws Exception {
    return getObservable();
  }
}
*/

Observable<String> source = Observable.defer(supplier);                   // defer를 통해 Observable을 만들면 함수 호출 순간에는 실제로 Observable이 생성되지 않음
source.subscribe(val -> Log.i("Subscriber #1:" + val)                     // 구독자가 들어오는 순간에 실제 Observable 생성 (첫번째 값인 1을 발행하는 Observable)
source.subscribe(val -> Log.i("Subscriber #2:" + val)                     // 구독자가 들어오는 순간에 실제 Observable 생성 (두번째 값인 3을 발행하는 Observable)
// main | value = Subscriber #1:1
// main | value = Subscriber #2:3


Observable<String> source2 = getObservable();                              // 직접 getObservable 호출시 바로 Observable이 생성 (세번째 값인 5를 발행하는 Observable)
source2.subscribe(val -> Log.i("Subscriber #3:" + val)                     // 구독자가 들어오는 순간에 이미 생성된 Observable에서 발행만 일어남 (5 발행)
source2.subscribe(val -> Log.i("Subscriber #4:" + val)                     // 구독자가 들어오는 순간에 이미 생성된 Observable에서 발행만 일어남 (5 발행)
// main | value = Subscriber #3:5
// main | value = Subscriber #4:5
```


### 4.1.6 repaet() 함수
- 지정된 횟수만큼 연속 발행
  - 횟수 미지정시 무한히 발행
- 서버에 heart beat를 보낼때 자주 사용
```java
String[] balls = {"1", "3", "5"}
Observable<String> source = Observable.fromArray(balls).repaet(3);  // 1,3,5를 3번 반복해서 발행

source.doOnComplete(() -> Log.d("onComplete"))                      // onComplete 체크를 위한 출력값 지정
  .subscribe(Log::i);                                               // 발행 값 출력
// main | value = 1
// main | value = 3
// main | value = 5
// main | value = 1
// main | value = 3
// main | value = 5
// main | value = 1
// main | value = 3
// main | value = 5
// main | debug = onComplete
```

- 실습 예제: heart beat 구현하기
  - 2초마다 서버에 ping 보내기
  - timer와 repeat의 조합
```java
CommonUtils.exampleStart();
String.serverUrl = "https://api.github.com/zen";

// 2초 간격으로 서버에 ping 보내기
Observable.timer(2, TimeUnit.SECONDS)
  .map(val -> servalUrl)
  .map(OkHttpHelper::get)                                 // 대충 주어진 주소에 get request 날리고 결과 값 파싱해서 리턴하는 함수
  .repeat()                                               // 무한히 반복할거다
  .subscribe(res -> Log.it("Ping Result : " + res));      // 결과는 로그로 찍어라

CommonUtils.sleep(10000);
// RxComputationThreadPool - 1 | 4409 | value = Ping Result : Blah Blah
// RxComputationThreadPool - 2 | 6639 | value = Ping Result : Blah Blah
// RxComputationThreadPool - 3 | 8930 | value = Ping Result : Blah Blah
```



## 4.2 변환 연산자

### 4.2.1 concatMap() 함수
- flatMap과 유사하지만 순서 보장
  - flatMap은 연산 속도때문에 순서가 보장되지 않을 수 있음
  - 단, 속도는 flatMap이 훨씬 빠름
    - 블록 없이 연산 종료후 바로 발행
    - concatMap은 앞의 발행이 끝나야 다음값이 발행되므로 블로킹 발생
- 예제 생략


### 4.2.2 switchMap() 함수
- flatMap과 유사하지만 앞의 값이 발행되기전에 새로운 값이 들어오면 기존 작업 중단
- "최신 값만" 중요할 때 사용
- 예제 생략


### 4.2.3 groupBy() 함수
- 어떤 기준으로 단일 Observable을 여러개의 Observable 그룹 (GroupedObservable) 으로 변환
- GroupedObservable에는 key, value 존재
  - key: 그룹으로 묶은 기준 값
  - value: 묶인 객체
```java
String[] obs = {"6-B", "4-B", "2-T", "2-B", "6-T", "4-T"};
Observable<GroupedObservable<String, String>> source = Observable.fromArray(objs)
                                                                .groupBy(CommonUtils.getShape); // CommonUtils.getShape: 대충 - 뒤에 붙은 값 리턴하는 함수
                                                                                                // 여기서는 -T 붙은애들끼리 묶이고 -B 붙은 애들끼리 묶임
                                                                                                // 실제 발행되는 값은 그룹으로 묶인값
                                                                                                
source.subscribe(obs -> {                                                                       // source를 구독하면 GroupedObservable을 받아 obs로 넘김
  obj.subscribe(val -> System.out.println("GROUP:" + obj.getKey() + "\t Value:" + val));        // obs로 넘어온 GroupedObservable을 다시 구독
});

// GROUP:B    Value:6-B
// GROUP:B    Value:4-B
// GROUP:T    Value:2-T
// GROUP:B    Value:2-B
// GROUP:T    Value:6-T
// GROUP:T    Value:4-T
// 그룹간 출력 순서는 보장되지 않음

source.subscribe(obs -> {                                                                       // source를 구독하면 GroupedObservable을 받아 obs로 넘김
  obj.filter(val -> obs.getKey().equals("B"))                                                   // 그룹 중 B만 남김
     .subscribe(val -> System.out.println("GROUP:" + obj.getKey() + "\t Value:" + val));        // obs로 넘어온 GroupedObservable을 다시 구독
});
// GROUP:B    Value:6-B
// GROUP:B    Value:4-B
// GROUP:B    Value:2-B
```
