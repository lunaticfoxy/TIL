# Chapter2. Observable 처음 만들기
- Observable 클래스와 그의 파생 클래스들
  - Observable은 흐름에 맞게 알림을 보내 구독자가 데이터를 처리하게 함
  - RxJava에서 제일 중요한 개념
- 객체 종류
  - RxJava 1.0
    - Single
    - Observable
  - RxJava 2.0
    - Single
    - Observable
    - Maybe: 데이터가 발행되지 않을 수 있음
    - Flowable: 데이터의 발행 속도가 처리 속도보다 빠를 경우 발생하는 Back Pressure 이슈 대응 기능 추가
      - 6, 8장에서 설명


## 2.1 Observable 클래스
- Observable은 옵서버 패턴을 구현해놓은 것
  - 객체의 상태 변환를 관찰하는 관찰자 (옵서버) 목록을 객체에 등록
  - 상태 변화가 있을때마다 메소드를 호출하여 변화 알림
  - 라이프사이클은 존재하지 않고 단일 함수를 통해 상태 변화만 전달
  - ex) 버튼 클릭시 onClick 메소드 호출

- 알림 종류
  - onNext : 데이터의 발행을 구독자에게 알림
  - onComplete
    - 데이터의 발행이 끝났음을 알림
    - 발생한 후에는 onNext가 일어나지 않음
  - onError
    - 에러가 발생했음을 알림
    - 이후 onNext, onComplete 발생하지 않음

- Observable 생성시 직접 인스턴스를 만들지 않고 정적 팩토리 함수 호출
  - RxJava 1.X: create, jus, from
  - RxJava 2.X 추가 (from 함수의 세분화): fromArray, fromIterable, fromCallable, fromFuture, fromPublisher
  - 기타: interval, range, timer, defer 등
  - 4.1장에서 자세히 다룸
 

### 2.1.1 just 함수
- 인자로 넣은 데이터를 차례대로 발행하기 위한 함수
  - 실제 발행은 subscribe 함수 호출 시 일어남
- 최대 10개의 데이터 입력 가능
  - 타입은 고정
- 동작 과정
  - subscribe 호출
  - just 내에 포함된 인자를 하나씩 onNext로 전달
    - 이 과정에서 subscribe에 지정된 함수에 전달된 값을 넣어 실행
  - 모든 인자가 전달되면 onComplete 호출
```java
public class FirstExample {
    public void emit() {
        Observable.just(1, 2, 3, 4, 5, 6)
            .subscribe(System.out::println);
    }
}

// 동작 과정
// System.out.println(1)
// System.out.println(2)
// ...
// System.out.println(6)
```


### 2.1.2 subscribe() 함수와 Disposable 객체
- 동작시키기 위한 것을 미리 정의해둔 뒤 실행되는 시점 조절 가능
  - 이때 동작시키는 시점에 호출하는 것이 subscribe 함수
  - subscribe 함수가 호출되기 전까지는 Observable에서 데이터 발행이 일어나지 않음

- 인자에 따른 분류
  - subscribe() : 파라미터가 없는 경우 onError 이벤트만 동작하여 에러 발생 (테스트 및 디버깅용)
  - subscribe(onNext) : 파라미터가 1개인 경우 onNext 이벤트, onError 이벤트만 발생
  - subscribe(onNext, onError) : 파라미터가 2개인 경우 onNext, onError 이벤트가 발생하며, onError시에도 에러를 내지 않고 지정된 함수 호출
  - subscribe(onNext, onError, onComplete) : 파라미터가 3개인 경우 onNext, onError, onComplete 모두 발생

- subscribe의 리턴은 Disposable 인터페이스
  - Disposable은 RxJava1.X의 Subscription (구독) 객체에 해당
  - 두개의 함수 존재
    - void dispose() : 구독 종료
    - booelan isDisposed() : 구독이 종료되었는지 여부 체크
  - onComplete 발생시 구독은 자동으로 종료되므로, 일반적인 경우 굳이 호출할 일은 없음


### 2.1.3 create() 함수
- onNext, onComplete, onError 같은 알림을 개발자가 직접 호출해야 함
  - 데이터 변경을 알려줘야 하는 시점마다 개발자가 onNext 호출
  - 모든 데이터의 발행이 완료되면 개발자가 onComplete 호출

- 예시 코드
  - 차가운 Observable? source 생성
    - 차가운 Observable vs 뜨거운 Observable은 2.4장에 나옴
  - ObservableEmitter를 입력으로 받아 내부 동작을 정의한 람다 함수를 인자로 넘겨줌
```java
Observable<Integer> source = Observable.create(
    (ObservableEmitter<Integer> emitter) -> {
        emitter.onNext(100);
        emitter.onNext(200);
        emitter.onNext(300);
        emitter.onComplete();
    }
);

source.subscribe(data -> System.out.println("Result : " + data));
// println("Result: 100")
// println("Result: 200")
// println("Result: 300")
```
- 가능하면 메서드 레퍼런스, 람다 표현식을 사용하는것을 지향
- create 함수는 RxJava에 익숙한 사용자만 사용하는 것을 권고
  - dispose시 등록된 콜백을 해제하지 않으면 메모리 누수 발생
  - 구독자가 있는 경우에만 onNext, onComplete 실행
    - 기본 예외처리 없음
  - onError로만 예외 전달
  - back pressure 직접 처리

- RxJava2의 Consumer와 자바 8의 Consumer는 동일
  - java.util.function.Consumer, Predicate, Function
  - io.reactive.functions.Consumer, Predicate, Function
  - RxJava2의 함수는 자바 6부터 사용 가능



### 2.1.4 fromArray() 함수
- fromXXX() 계열 함수를 통해 단일 데이터가 아닌 데이터 처리 가능
  - RxJava 2 부터 지원

- fromArray() 를 통해 배열 데이터를 처리 가능
```java
Integer[] arr = {100, 200, 300};
Observable<Integer> source = Observable.fromArray(arr);
source.subscribe(System.out::println);
```
- 주의사항
  - int값 대신 Integer, double 대신 Double 사용
  - 객체단위로 동작하게 되어있어 int가 저장된 주소만 전달하게 됨


### 2.1.5 fromIterable() 함수
- 모든 Iterable 구현 클래스에서 사용 가능
  - Iterator를 통해 동작
  - 자바의 많은 컬렉션에 해당
    - ArrayList, LinkedList, ArrayBlockingQueue, HashSet, Stack, TreeSet, Vector 등
    - Map에는 없음
```java
List<String> names = new ArrayList<String>();
names.add("Jerry");
names.add("William");
names.add("Bob");

Observable<String> source = Observable.fromIterable(names);
source.subscribe(System.out::println)
```


### 2.1.6 fromCallable() 함수
- 비동기 클래스나 인터페이스와의 연동을 위한 함수
- Java의 Callable 인터페이스를 기반으로 동작
  - Runnable과 비슷하지만 리턴값 존재
    - run 대신 call 함수 존재
  - 잠재적으로 다른 스레드에서 실행됨
```java
Callable<String> callable = () -> {
    Thread.sleep(1000);
    return "Hello Callable";
};
/*
Callable<String> callable = new Callable<String>() {
    @Override
    public String call() throws Exception {
        Thread.sleep(1000);
        return "Hello Callable";
    }
};
*/

Observable<String> source = Observable.fromCallable(callable);
source.subscribe(System.out::println);
```


### 2.1.7 fromFuture() 함수
- 마찬가지로 비동기 계산의 결과를 활용하기 위한 함수
- Java의 Future 인터페이스 활용
  - Executer 인터페이스에 Callable 객체를 인자로 넣어 Future 객체 반환
  - get 메소드 호출 시 Callable의 결과가 나올때까지 블로킹

```java
Future<String> future = Executors.newSingleThreadExecuter().submit(() -> {
    Thread.sleep(1000);
    return "Hello Future";
});
/*
Future<String> future = Executors.newSingleThreadExecuter().submit(new Callable<String>() {
    @Override
    public String call() throws Exception {
        Thread.sleep(1000);
        return "Hello Callable";
    }
});
*/

Observable<String> source = Observable.fromFuture(future);
source.subscribe(System.out::println);
```

- Executors는 단일 스레드 이외에도 스레드풀 지원
  - 하지만 RxJava에서는 자체 스케줄러를 활용하기 권장
  - 5장에서 내용 언급


### 2.1.8 fromPublisher() 함수
- 자바 9의 Publisher 인터페이스와 연동
  - Flow API의 일부

- org.reactivestreams 패키지 안에 존재
- create() 와 동일하게 onNext, onComplete 호출 가능

```java
Publisher<String> publisher = (Subscriber<? super String> s -> {
    s.onNext("Hello Observable.fromPublisher()");
    s.onComplete();
});
/*
Publisher<String> publisher = new Publisher<String>() {
    @Override
    public void subscribe(Subscriber<? super String> s) {
        s.onNext("Hello Observable.fromPublisher()");
        s.onComplete();
    }
};
*/

Observable<String> source = Observable.fromPublisher(publisher);
source.subscribe(System.out::println);
```

## 2.2 Single 클래스
- Observable의 특이한 형태
  - 오직 1개의 데이터와 발행
  - 결과가 유한한 서버 API 호출시 유용하게 사용 가능

- onNext, onComplete가 onSuccess로 통합

### 2.2.1 just() 함수
```java
Single<String> source = Single.just("Hello Single");
source.subscribe(System.out::println);
```

### 2.2.2 Observable에서 Single 클래스 사용
- Observable에서 Single로 변환 가능

```java
Observable<String> source = Observable.just("Hello Single");

Single.fromObservable(source).subscribe(System.out::println);               // Hello Single
source.single("default item").subscribe(System.out::println);               // Hello Single
source.first("default item").subscribe(System.out::println);                // Hello Single
Obsrvable.empty().first("default item").subscribe(System.out::println);     // default item
source.take(1).single("default item").subscribe(System.out::println);       // Hello Single
```


### 2.2.3 Single 클래스의 올바른 사용 방법
- just 함수에 값을 여러게 넣으면 에러 발생



## 2.3 Maybe 클래스
- Observable의 특이한 형태
  - Single처럼 한개의 데이터만 가질 수 있음
  - 데이터 발행 없이 데이터 발생을 완료 할 수 있음
    - Single에서 onSuccess 없이 onComplete만 호출 가능한 형태
    - 데이터 발행 없이 dispose 시킬 수 있음


## 2.4 뜨거운 Observable
- 차가운 Observable
  - subscribe를 호출하기 전까지는 데이터 발행하지 않음
    - lazy한 접근
  - 내가 파라미터를 넣으면 그 순간에 요청을 보내고 결과를 가져오는 형태
  - 사용 예시
    - 웹 요청
    - 데이터베이스 쿼리
    - 파일 읽기

- 뜨거운 Observable
  - 구독자의 존재 여부와 관계 없이 데이터 발행
  - 여러 구독자 고려 가능
    - 구독자가 모든 데이터를 수신할것이라 보장 불가
    - 구독을 시작한 시점부터 발생하는 데이터를 받아옴
    - 여러 구독자란?
      - 데이터의 원천은 하나이지만 결과 데이터가 여러 종류일 경우
      - 한 서버에서 날씨, 시간, 지역 정보를 가져오고, 이를 여러 군데서 사용하는 경우
  - 사용 예시
    - 마우스, 키보드, 시스템 이벤트
    - 센서 데이터
    - 주식 가격

- 뜨거운 Observable에는 배압 (back pressure) 존재
  - Flowable이라는 특화 클래스를 통해 처리 가능

- Subject 객체나 ConnectableObservable 클래스를 통해 차가운 Observable을 뜨거운 Observable로 변경 가능


## 2.5 Subject 클래스
- Observable의 속성과 구독자의 속성을 동시에 지님
  - 데이터를 발행할 수 있음
  - 발행된 데이터를 바로 처리할 수 있음

### 2.5.1 AsyncSubject 클래스
- Observable에서 마지막으로 발행한 데이터를 얻어올 수 있는 클래스
  - 이전 데이터는 무시
  - onComplete가 되는 순간 구독자들에게 마지막 데이터 전달
```java
AsyncSubject<String> subject = AsyncSubject.create();
subject.subscribe(data -> System.out.println("Subscriber #1 => " + data))
subject.onNext("1");
subject.onNext("3");
subject.subscribe(data -> System.out.println("Subscriber #2 => " + data))
subject.onNext("5");
subject.onComplete();   // Subscriber #1 => 5
                        // Subscriber #2 => 5
```

- AsyncSubject 클래스는 구독자로도 동작 가능
  - Subject 클래스 자체가 Observable 클래스를 상속하고 Observer 인터페이스를 구현하고 있기 때문에 가능

```java
Float[] temperature = {10.1f, 13.4f, 12.5f};
Observable<Float> source = Observable.fromArray(temperature);

AsyncSubject<Float> subject = AsyncSubject.create();
subject.subscribe(data -> System.out.println("Subscriber #1 => " + data));

source.subscribe(subject);  // Subscriber #1 -> 12.5
```

- AsyncSubject 클래스에서 onComplte() 호출 후 이를 구독시
  - 동일하게 마지막 발행된 값 리턴
```java
AsyncSubject<Integer> subject = AsyncSubject.create();
subject.onNext(10);
subject.onNext(11);
subject.subscribe(data -> System.out.println("Subsrciber #1 => " + data));
subject.onNext(12);
subject.onComplete();                                                       // Subscriber #1 -> 12
subject.onNext(13);
subject.subscribe(data -> System.out.println("Subsrciber #2 => " + data));  // Subscriber #2 -> 12
subject.subscribe(data -> System.out.println("Subsrciber #3 => " + data));  // Subscriber #3 -> 12
```


### 2.5.2 BehaviorSubject 클래스
- 구독자가 구독을 하면 가장 최근 값 혹은 기본값을 넘겨줌
  - ex) 온도 센서의 경우 가장 최근의 온도 값을 반환함, 온도를 처음 얻을때는 초기값을 반환함

```java
BehaviorSubject<String> subject = BehaviorSubject.createDefault("6");
subject.subscribe(data -> System.out.pritnln("Subscriber #1 => " + data));      // Subscriber #1 -> 6
subject.onNext("1");                                                            // Subscriber #1 -> 1
subject.subscribe(data -> System.out.pritnln("Subscriber #2 => " + data));      // Subscriber #2 -> 1
subject.onNext("3");                                                            // Subscriber #1 -> 3
                                                                                // Subscriber #2 -> 3
subject.onNext("5");                                                            // Subscriber #1 -> 5
                                                                                // Subscriber #2 -> 5
subject.onComplete();
```

### 2.5.3 PublishSuject 클래스
- 가장 평범한 Subject 클래스
- 구독자가 subscribe 함수 호출시 값을 발행하기 시작
  - 마지막 값만 발행하거나 발행한 값이 없을 때 기본값을 대신 발행하지도 않음
  - 새로 발생한 데이터는 구독자에게 그대로 전달

```java
PublishSubject<String> subject = PublishSubject.create();
subject.subscribe(data -> System.out.pritnln("Subscriber #1 => " + data));
subject.onNext("1");                                                        // Subscriber #1 -> 1
subject.onNext("3");                                                        // Subscriber #1 -> 3
subject.subscribe(data -> System.out.pritnln("Subscriber #2 => " + data));
subject.onNext("5");                                                        // Subscriber #1 -> 5
                                                                            // Subscriber #2 -> 5
subject.onComplete();

```


### 2.5.4 ReplaySubject 클래스
- 가장 특이하고 사용시 주의 필요
- Subject를 차가운 Observable 처럼 동작하게 함
  - 구독자가 새로 생길때마다 기존의 발행된 모든 데이터를 전달
  - 과거 데이터 저장 과정에서 메모리 누수 발생 가능

```java
ReplaySubject<String> subject = ReplaySubject.create();
subject.subscribe(data -> System.out.pritnln("Subscriber #1 => " + data));
subject.onNext("1");                                                        // Subscriber #1 -> 1
subject.onNext("3");                                                        // Subscriber #1 -> 3
subject.subscribe(data -> System.out.pritnln("Subscriber #2 => " + data));  // Subscriber #2 -> 1
                                                                            // Subscriber #2 -> 3
subject.onNext("5");                                                        // Subscriber #1 -> 5
                                                                            // Subscriber #2 -> 5
subject.onComplete();
```


## 2.6 ConnectableObservable 클래스
- 차가운 Observable을 뜨거운 Observable로 변환
  - 원 데이터 하나를 여러 구독자에게 동시에 전달할 때 사용
- subscribe를 호출해도 아무 동작도 일어나지 않음
  - 차가운 Observable에서는 데이터 구독 + 발행 시작
  - ConnectableObservable 에서는 오로지 구독만
  - 데이터 발행은 connect 함수가 호출된 이후부터 시작
- Observable에서 publish() 가 일어나면서 ConnectableObservable 이 생성
- 5.4장의 일기예보 예제에서 상세히 다룸

```java
String dt[] = {"1", "3", "5"}
Observable<String> balls = Observable.interbal(100L, TimeUnit.MILLISECONDS) // 100ms 마다 데이터를 0부터 1씩 증가시키며 발행 (0, 1, 2, ...)
  .map(Long::intValue)  // Long 으로 들어오는 값을 int로 변환
  .map(i -> dt[i])      // int로 변환된 값을 index로 dt에서 값을 가져옴
  .take(dt.length);     // dt의 길이만큼 데이터를 발행 (dt의 모든 데이터를 발행)
ConnectableObservable<String> source = balls.publish();
source.subscribe(data -> System.out.pritnln("Subscriber #1 => " + data));
source.subscribe(data -> System.out.pritnln("Subscriber #2 => " + data));
source.connect();                                                           // Subscriber #1 -> 1
                                                                            // Subscriber #2 -> 1
CommonUtils.sleep(250);                                                     // Subscriber #1 -> 3
                                                                            // Subscriber #2 -> 3
source.subscribe(data -> System.out.pritnln("Subscriber #3 => " + data));
CommonUtils.sleep(100);                                                     // Subscriber #1 -> 5
                                                                            // Subscriber #3 -> 5
                                                                            // Subscriber #3 -> 5
```


## 2.7 마치며
- Observable의 생성은 팩토리 함수를 이용
- 팩토리 함수 이외에도 다양한 연산자 제공
  - 이를 함께 이용하는 것을 메소드 체이닝 이라고 부름
  - 람다 표현식과 함께 사용하면 가독성 높은 코드 작성 가능
- Observable을 확장한 Subject 제공

