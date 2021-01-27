## 5.1 스케줄러 개념 배우기
- 기존 코드 참조
```java
Observable.just("Hello", "RxJava 2!!").subscribe(Log::i);
// main | value = Hello
// main | value = RxJava 2!!
```
- 출력이 main 스레드에서 동작
  - 일반적인 경우 대부분의 기능이 main에서 동작
- 실무에서는 요구사항에 맞게 비동기로 동작할 수 있도록 수정 필요
  - 이때 스케줄러 사용
  - 스케줄러를 통해 동작할 스레드 지정 가능



```java
String[] objs = {"1-S", "2-T", "3-P"};

Observable<String> source = Observable.fromArray(objs)
  .doOnNext(data -> Log.v("Observable data = " + data))  // onNext 실행시에 로그 찍기
  .subscribeOn(Schedulers.newThread())                   // 구독자가 동작할 스레드 지정
  .observeOn(Schedulers.newThread())                     // Observable의 발행 과정이 어디서 동작할지 지정
  .map(Shape::flip);

source.subscribe(Log::i);
CommonUtils.sleep(500);
// RxNewThreadScheduler - 1 | Original data = 1-S        -> 발행이 새로운 스레드1 에서 일어남
// RxNewThreadScheduler - 1 | Original data = 2-T
// RxNewThreadScheduler - 1 | Original data = 3-P
// RxNewThreadScheduler - 2 | value = (flipped)1-S       -> 구독이 새로운 스레드2 에서 일어남
// RxNewThreadScheduler - 2 | value = (flipped)2-T
// RxNewThreadScheduler - 2 | value = (flipped)3-P

Observable<String> source2 = Observable.fromArray(objs)
  .doOnNext(data -> Log.v("Observable data = " + data))  // onNext 실행시에 로그 찍기
  .subscribeOn(Schedulers.newThread())                   // 구독자가 동작할 스레드 지정
  //.observeOn(Schedulers.newThread())                      아까와 다르게 발행 과정에 별도 스레드 생성 안함
  .map(Shape::flip);

source2.subscribe(Log::i);
CommonUtils.sleep(500);
// RxNewThreadScheduler - 3 | Original data = 1-S        -> 발행이 새로운 스레드3 에서 일어남
// RxNewThreadScheduler - 3 | value = (flipped)1-S       -> 구독도 새로운 스레드3 에서 일어남
// RxNewThreadScheduler - 3 | Original data = 2-T        -> 한 스레드에서 일어나므로 동작이 순차적
// RxNewThreadScheduler - 3 | value = (flipped)2-T
// RxNewThreadScheduler - 3 | Original data = 3-P
// RxNewThreadScheduler - 3 | value = (flipped)3-P
```

- 스케줄러 핵심 내용
  - 스케줄러는 RxJava 코드를 어떤 스레드에서 실행할지 지정 가능
  - subscribeOn, observeOn 함수를 모두 지정하면 데이터 발행 스레드와 구독 스레드 분리 가능
  - subscribeOn 함수만 지정하면 모든 흐름을 한 스레드에서 실행되게 지정 가능
  - 스케줄러를 지정하지 않으면 현재 스레드 (main) 에서 동작 실행


## 5.2 스케줄러의 종류
- 스케줄러 종류
  - 뉴 스레드 스케줄러: newThread()
  - 싱글 스레드 스케줄러: single()
    - 2.x 에서만 지원
  - 계산 스케줄러: computation()
  - IO 스케줄러: io()
  - 트램펄린 스케줄러: trampoline()
  - 메인 스레드 스케줄러: immediate()
    - 1.x 에서만 지원
  - 테스트 스케줄러: test()
    - 1.x 에서만 지원


### 5.2.1 뉴 스레드 스케줄러
- 가장 기본적인 새 스레드 생성 로직
- Schedulers.newThread() 로 생성
  - 불릴때마다 새로운 스레드 생성
- 가장 단순하지만 계산 스케줄러나 IO 스케줄러로 대체 가능하므로 이를 사용하길 권장

```java
String[] orgs = {"1", "3", "5"};

Observable.fromArray(orgs)
  .doOnNext(data -> Log.v("Original data: " + data))
  .map(data -> "<<" + data + ">>")
  .subscribeOn(Schedulers.newThread())                 // 새로운 스케줄러에서 구독
  .subscribe(Log::i);

CommonUtils.sleep(500);
// RxNewThreadScheduler-1 | Original Value : 1       => 1번 스레드에서 동작
// RxNewThreadScheduler-1 | value = <<1>>
// RxNewThreadScheduler-1 | Original Value : 3
// RxNewThreadScheduler-1 | value = <<3>>
// RxNewThreadScheduler-1 | Original Value : 5
// RxNewThreadScheduler-1 | value = <<5>>

Observable.fromArray(orgs)
  .doOnNext(data -> Log.v("Original data: " + data))
  .map(data -> "##" + data + "##")
  .subscribeOn(Schedulers.newThread())                 // 새로운 스케줄러에서 구독
  .subscribe(Log::i);

CommonUtils.sleep(500);
// RxNewThreadScheduler-2 | Original Value : 1       => 2번 스레드에서 동직
// RxNewThreadScheduler-2 | value = ##1##
// RxNewThreadScheduler-2 | Original Value : 3
// RxNewThreadScheduler-2 | value = ##3##
// RxNewThreadScheduler-2 | Original Value : 5
// RxNewThreadScheduler-2 | value = ##5##
```

### 5.2.2 계산 스케줄러
- CPU에 대응하는 계산용 스케줄러
  - I/O 작업을 하지 않음
  - 스레드 풀 내의 스레드 개수는 프로세서 수와 동일
- interval 함수 내부에서 활용하고 있음
- 계산 스레드중 어디에 할당할지는 내부적으로 결정

```java
String[] orgs = {"1", "3", "5"};

Observable<String> source = Observable.fromArray(orgs)
  .zipWith(Observable.interval(100L, TimeUnit.MILLISECONDS), (a, b) -> a);

// 구독 #1
source.map(item -> "<<" + item + ">>")
  .subscribeOn(Schedulers.computation())                 // 계산 스레드에서 구독
  .subscribe(Log::i);

// 구독 #2
source.map(item -> "##" + item + "##")
  .subscribeOn(Schedulers.computation())                 // 계산 스레드에서 구독
  .subscribe(Log::i);

CommonUtils.sleep(500);
// RxComputationThreadPool-3 | value = <<1>>           => 3번 계산 스레드에서 동작
// RxComputationThreadPool-4 | value = ##1##           => 4번 계산 스레드에서 동작
// RxComputationThreadPool-3 | value = <<3>>
// RxComputationThreadPool-4 | value = ##3##
// RxComputationThreadPool-3 | value = <<5>>
// RxComputationThreadPool-4 | value = ##5##


// 또는

// RxComputationThreadPool-3 | value = <<1>>           => 3번 계산 스레드에서 동작
// RxComputationThreadPool-3 | value = ##1##           => 3번 계산 스레드에서 동작
// RxComputationThreadPool-3 | value = <<3>>
// RxComputationThreadPool-3 | value = ##3##
// RxComputationThreadPool-3 | value = <<5>>
// RxComputationThreadPool-3 | value = ##5##
```


### 5.2.3 IO 스케줄러
- 네트워크상의 요청 처리나 입출력 작업 실행
- 필요할 때 마다 스레드 계속 생성

```java
// C 드라이브 루트 디렉토리에 파일 목록 생성
String root = "C:\\";
File[] files = new File(root).listFiles();

Observable<String> source = Observable.fromArray(files)
  .filter(f -> !f.isDirectory())
  .map(f -> f.getAbsolutePath())
  .subscribeOn(Schedulers.io());

source.subscribe(Log::i);
CommonUtils.sleep(500);
// RxCachedThreadScheduler-1 | value = c:\bootmgr
// RxCachedThreadScheduler-1 | value = c:\BOOTNXT
// RxCachedThreadScheduler-1 | value = c:\TEST.txt
```

### 5.2.4 트램펄린 스케줄러
- 새로운 스레드 생성 없이 작업 큐 생성
  - 스케줄러를 사용하지 않는 경우는 작업 순서 미보장
  - 트램펄린 스케줄러를 사용하면 작업 순서 보장
    - 진행중인 작업이 끝난 뒤에 다음 작업 실행
    - 먼저 구독한 데이터가 먼저 연산

```java
String[] orgs = {"1", "3", "5"};

Observable<String> source = Observable.fromArray(orgs);

// 구독 #1
source.subscribeOn(Schedulers.trampolin())               // 트램펄린 스케줄러로 구독
  .map(item -> "<<" + item + ">>")
  .subscribe(Log::i);

// 구독 #2
source.subscribeOn(Schedulers.trampolin())               // 트램펄린 스케줄러로 구독
  .map(item -> "##" + item + "##")
  .subscribe(Log::i);


CommonUtils.sleep(500);
// main | value = <<1>>           => 메인스레드에서 동작하며 무조건 앞에 연산되는 것을 보장
// main | value = <<3>>
// main | value = <<5>>
// main | value = ##1##           => 메인스레드에서 동작하며 무조건 뒤에 연산되는 것을 보장
// main | value = ##3##
// main | value = ##5##
```


### 5.2.5 싱글 스레드 스케줄러
- 스레드풀이 아닌 단일 스래드를 새로 생성하여 동작
  - single이 여러번 불리더라도 한개의 스레드만 생성하고 그 안에서 동작
- 크게 활용할일은 없음

```java
String[] orgs = {"1", "3", "5"};

Observable<Integer> numbers = Observable.range(100, 5); // 100, 101, 102, 103, 104 생성
Observable<String> chars = Observable.range(0, 5)
  .map(CommonUtils.numberToAlphabet);                   // 대충 A, B, C, D, E 생성한다는 이야기

// 구독 #1
numbers.subscribeOn(Schedulers.single())                 // 싱글 스케줄러로 구독
  .subscribe(Log::i);

// 구독 #2
chars.subscribeOn(Schedulers.single())                   // 싱글 스케줄러로 구독
  .subscribe(Log::i);

CommonUtils.sleep(500);
// RxSingleScheduler-1 | value = 100                    => 새로운 싱글 스레드에서 동작
// RxSingleScheduler-1 | value = 101
// RxSingleScheduler-1 | value = 102
// RxSingleScheduler-1 | value = 103
// RxSingleScheduler-1 | value = 104
// RxSingleScheduler-1 | value = A                      => 위와 같은 싱글 스레드에서 동작
// RxSingleScheduler-1 | value = B
// RxSingleScheduler-1 | value = C
// RxSingleScheduler-1 | value = D
// RxSingleScheduler-1 | value = E
```


### 5.2.6 Executor 변환 스케줄러
- 자바에서 제공하는 Executor 변환하여 스케줄러 생성 가능
  - 단, 자바의 Executor 동작과 스케줄러의 동작 방법이 다르므로 추천하진 않음
  - 기존 Executor 재사용 할때만 활용

```java
final int THREAD_NUM = 10;

String data[] = {"1", "3", "5"};
Observable<String> source = Observable.fromArray(data);
Executor executor = Executors.newFixedThreadPool(THREAD_NUM); // 스레드가 10개 있는 스레드풀을 만들고 executor에 할당

source.subscribeOn(Schedulers.from(executer))                 // executer의 스레드 활용
  .subscribe(Log::i);

source.subscribeOn(Schedulers.from(executer))                 // executer의 스레드 활용
  .subscribe(Log::i);

CommonUtils.sleep(500);
// pool-1-thread-1 | value = 1                                => executor의 스레드중 1번 활용
// pool-1-thread-1 | value = 3
// pool-1-thread-1 | value = 5
// pool-1-thread-2 | value = 1                                => executor의 스레드중 2번 활용
// pool-1-thread-2 | value = 3
// pool-1-thread-2 | value = 5
```


<<<<<<< HEAD
## 5.3 스케줄러를 활용하여 콜백 지옥 벗어나기
- 1번 서버에 요청을 보내고, 성공 응답시 2번 서버에 요청을 보내서 결과를 받는 애플리케이션
  - 기존 방법대로 구현시
```java
public class CallbackHell {
  private static final String FIRST_URL = "https://api.github.com/zen";
  private static final String SECOND_URL = "https://raw.githubusercontent.com/yudong80/reactivejava/master/samples/callback_hell";

  private final OkHttpClient client = new OkHttpClient();                       // 통신을 위한 클라이언트 생성 

  public void run() {
    Request request = new Request.Builder().url(FIRST_URL).build();             // 1차 통신을 위한 요청 생성

    client.newCall(request).enqueue(new Callback() {                            // 1차 통신에 대한 콜백 등록
      @Override
      public void onFailure(Call call, IOException e) {
        e.printStackTrace();
      }

      @Override
      public void onResponse(Call call, Response response) throws IOException { // 1차 통신 성공시
        Log.i(response.body().string());

        Request request = new Request.Builder().url(SECOND_URL).build();        // 2차 통신을 위한 요청 생성

        client.newCall(request).enqueue(new Callback() {                        // 2차 통신에 대한 콜백 등록
          @Override
          public void onFailure(Call call, IOException e) {
            e.printStackTrace();
          }

          @Override
          public void onResponse(Call call, Response response) throws IOException {
            Log.i(response.body().string());                                    // 최종 결과 출력  
          }
        });                             
      }
    }
  }

  public static void main(String[] args) {
    CallbackHell demo = new CallbackHell();
    demo.run();
  }
}
```

  - RxJava2를 이용하여 구현시
```java
public class CallbackHeaven {
  private static final String FIRST_URL = "https://api.github.com/zen";
  private static final String SECOND_URL = "https://raw.githubusercontent.com/yudong80/reactivejava/master/samples/callback_hell";

  public void run() {
    CommonUtils.exampleStart();

    Observable<String> source = Obsrvable.just(FIRST_URL)       // 1차 통신을 위한 옵저버블 생성
      .subscribeOn(Schedulers.io())                             // io 스레드에서 동작
      .map(OkHttpHelper::get)                                   // 1차 통신 요청후 결과 리턴
      .concatWith(                                              // 1차 통신이 성공했다면 이어서 진행
        Observable.just(SECOND_URL)                             // 2차 통신을 위한 옵저버블 생성
          .map(OkHttpHelper::get)                               // 2차 통신 요청후 결과 리턴
      );
    
    source.subscribe(Log::it);                                  // 2차 통신 결과 구독
    CommonUtils.sleep(5000);
  }

  public static void main(String[] args) {
    CallbackHeaven demo = new CallbackHeaven();
    demo.run();
  }
}
```

- 병렬로 통신하고 결과 결합
```java
public class CallbackHeaven {
  private static final String FIRST_URL = "https://api.github.com/zen";
  private static final String SECOND_URL = "https://raw.githubusercontent.com/yudong80/reactivejava/master/samples/callback_hell";

  public void run() {
    CommonUtils.exampleStart();

    Observable<String> source = Obsrvable.just(FIRST_URL)       // 1차 통신을 위한 옵저버블 생성
      .subscribeOn(Schedulers.io())                             // io 스레드에서 동작
      .map(OkHttpHelper::get);                                  // 1차 통신 요청후 결과 리턴

    Observable<String> second = Obsrvable.just(SECOND_URL)      // 2차 통신을 위한 옵저버블 생성
      .subscribeOn(Schedulers.io())                             // io 스레드에서 동작
      .map(OkHttpHelper::get);                                  // 2차 통신 요청후 결과 리턴
      
    Observable.zip(first, second, (a, b) -> ("\n>> " + a + "\n>> " + b)) // 1, 2차 통신을 둘다 수행하고 결과를 묶어서 두줄로 출력
      .subscribe(Log::it);
  
    CommonUtils.sleep(5000);
  }

  public static void main(String[] args) {
    CallbackHeaven demo = new CallbackHeaven();               
    demo.run();
  }
}
```



## 5.4 observeOn() 함수의 활용
- 발행후 처리된 결과를 구독자에게 전달하는 스레드 지정
  - subscribeOn
    - 데이터를 발행하는 스레드 지정
    - 한번에 여러번 호출해도 마지막 것만 반영
  - observeOn
    - 발행된 데이터를 처리하는 스레드 지정
    - 호출 시점을 기준으로 이전과 이후의 연산을 수행할 스레드가 나뉨

- 날씨를 가져오는 예제
  - REST API 결과를 가져와서 현재 온도, 도시 이름, 국가 를 얻고자 함
  - 단순 구현시 차가운 Observable의 한계로 한번에 하나밖에 구독하지 못함
    - 매번 REST API 요청 필요
```java
public class OpenWeatherMapV1 {
  private static final URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=";

  private String parseTemperature(String json) { return parse(json, "\"temp\":[0-9]*.[0-9]*")}
  private String parseCityName(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}
  private String parseCountry(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}

  public void run() {
    Observable<String> source = Observable.just(URL + "API_KEY")            // REST API 접근을 위한 Observable 생성
      .map(OkHttpHelper::getWithLog)                                        // API 호출 명령
      .subscribeOn(Schedulers.io());                                        // io 스레드에서 수행

    Observable<String> temperature = source.map(this::parseTemperature);    // API를 호출해서 온도를 가져오는 옵저버블 생성
    Observable<String> city = source.map(this::parseCityName);              // API를 호출해서 도시 이름을 가져오는 옵저버블 생성
    Observable<String> country = source.map(this::parseCountry);            // API를 호출해서 국가를 가져오는 옵저버블 생성

    CommonUtils.exampleStart();

    Observable.concat(temperature, city, country)                           // 온도, 도시 이름, 국가 옵저버블을 순차적으로 이어붙임
      .observeOn(Schedulers.newThread())                                    // 새로운 스레드에서 구독
      .subscribe(Log::it);

    CommonUtils.sleep(3000);
  }

  public static void main() {
    OpenWeatherMapV1 demo = new OpenWeatherMapV1();
    demo.run();
  }
}
```

  - REST API 호출을 한번으로 줄이기 
    - ConnectableObservable을 사용
      - 차가운 Observable 을 뜨거운 Observable처럼 동시 구독이 가능하게 하기
    - share 함수 사용
      - publish + refCount 
      - refCount
        - 첫번째 구독자가 들어올때 자동으로 Connect 해줌
        - 참조 https://javaexpert.tistory.com/797
      
```java
public class OpenWeatherMapV1 {
  private static final URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=";

  private String parseTemperature(String json) { return parse(json, "\"temp\":[0-9]*.[0-9]*")}
  private String parseCityName(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}
  private String parseCountry(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}

  public void run() {
    CommonUtils.exampleStart();

    Observable<String> source = Observable.just(URL + "API_KEY")
      .map(OkHttpHelper::getWithLog)
      .subscribeOn(Schedulers.io())
      .share()  // .publish().refCount()                                   // ConnectableObseverble 로 변경 후 구독자가 들어오면 자동 연결하겠다
      .observeOn(Scheduler.newThread());                                   // 이후 작업은 매번 새로운 스레드를 만들어서 하겠다

    source.map(this::parseTemperature).subcribe(Log.it);                   // 온도에 대한 결과를 파싱해서 구독
    source.map(this::parseCityName).subcribe(Log.it);                      // 도시 이름에 대한 결과를 파싱해서 구독
    source.map(this::parseCountry).subcribe(Log.it);                       // 국가에 대한 결과를 파싱해서 구독

    CommonUtils.sleep(3000);
  }

  public static void main() {
    OpenWeatherMapV1 demo = new OpenWeatherMapV1();
    demo.run();
  }
}
```

  - 추가
    - 사실 현재 예시는 좋지 않아보임
      - 지금은 get 연산 결과가 오기전에 다른 구독이 모두 시작되어서 결과가 정상적으로 나옴
      - 하지만 연산이 매우 빨라서 다른 구독 시작전에 연산이 끝나버리면 정상 동작하지 않음
    - 진짜 정상 동작을 위해서는 직접 커넥트를 해야할듯
```java
public class OpenWeatherMapV1 {
  private static final URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=";

  private String parseTemperature(String json) { return parse(json, "\"temp\":[0-9]*.[0-9]*")}
  private String parseCityName(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}
  private String parseCountry(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}

  public void run() {
    CommonUtils.exampleStart();

    ConnectableObservable<String> source = Observable.just(URL + "API_KEY")
      .map(OkHttpHelper::getWithLog)
      .subscribeOn(Schedulers.io())
      .publish();                                                          // ConnectableObseverble 로 변경

    source.map(this::parseTemperature).subcribe(Log.it);                   // 온도에 대한 결과를 파싱해서 구독
    source.map(this::parseCityName).subcribe(Log.it);                      // 도시 이름에 대한 결과를 파싱해서 구독
    source.map(this::parseCountry).subcribe(Log.it);                       // 국가에 대한 결과를 파싱해서 구독
    
    source.connect();                                                      // 구독자가 다 들어왔으니 발행 시작


    CommonUtils.sleep(3000);
  }

  public static void main() {
    OpenWeatherMapV1 demo = new OpenWeatherMapV1();
    demo.run();
  }
}
```

  - 또는 autoConnect를 3으로 주기
```java
public class OpenWeatherMapV1 {
  private static final URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=";

  private String parseTemperature(String json) { return parse(json, "\"temp\":[0-9]*.[0-9]*")}
  private String parseCityName(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}
  private String parseCountry(String json) { return parse(json, "\"country\":\"[a-zA-Z]*\"")}

  public void run() {
    CommonUtils.exampleStart();

    ConnectableObservable<String> source = Observable.just(URL + "API_KEY")
      .map(OkHttpHelper::getWithLog)
      .subscribeOn(Schedulers.io())
      .publish().autoConnect(3);                                           // 구독자 3개가 생기면 자동 connect 하겠다

    source.map(this::parseTemperature).subcribe(Log.it);                   // 온도에 대한 결과를 파싱해서 구독
    source.map(this::parseCityName).subcribe(Log.it);                      // 도시 이름에 대한 결과를 파싱해서 구독
    source.map(this::parseCountry).subcribe(Log.it);                       // 국가에 대한 결과를 파싱해서 구독      => 이 순간 구독자가 3개가 되니 자동 연결

    CommonUtils.sleep(3000);
  }

  public static void main() {
    OpenWeatherMapV1 demo = new OpenWeatherMapV1();
    demo.run();
  }
}
```
=======
 
>>>>>>> 16662efe7dcae9b8627bca753eb95210f3dc3946
