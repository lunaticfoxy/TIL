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
