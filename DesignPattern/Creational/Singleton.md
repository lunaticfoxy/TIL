### 개요
- 전역변수를 사용하지 않고 객체를 하나만 생성하도록 하는 패턴
- 생성된 객체는 어디에서나 참조할 수 있음
- 단 하나의 인스턴스만 생성되며, 모든 클라이언트는 동일한 인스턴스를 받아서 작업


### 구현 방법
- 프린터 한개를 10명이 공유해 사용하는 경우로 예시
- 방법 1-1. 자기 자신에 static 변수를 만들어 인스턴스를 가져오는 순간에 초기화
  - 문제점: 여러 쓰레드에서 동시 참조시 레이스 컨디션 발생가능
```java
public class Printer {
    // 외부에 제공할 자기 자신의 인스턴스
    private static Printer printer = null;
    private Printer() { }
    // 자기 자신의 인스턴스를 외부에 제공
    public static Printer getPrinter(){
      // 조건 검사 구문 (문제의 원인!)
      if (printer == null) {
        try {
          // 스레드 스케줄링 변경(스레드 실행 1ms동안 정지)
          Thread.sleep(1);
        } catch (InterruptedException e) { }

        // Printer 인스턴스 생성
        printer = new Printer();
      }
      return printer;
    }
    public void print(String str) {
      System.out.println(str);
    }
}

public class UserThread extends Thread{
  public UserThread(String name) { super(name); }
  public void run() {
    Printer printer = printer.getPrinter();
    printer.print(Thread.currentThread().getName() + " print using " + printer.toString());
  }
}

public class Client {
  private static final int THREAD_NUM = 5;
  public static void main(String[] args) {
    UserThread[] user = new UserThread[THREAD_NUM];
    for (int i = 0; i < THREAD_NUM; i++) {
      // UserThread 인스턴스 생성
      user[i] = new UserThread((i+1));
      user[i].start();
    }
  }
}
```

- 방법 1-2. 자기 자신에 static 변수를 만들어 인스턴스를 가져오는 순간에 초기화하되 인스턴스 생성 메소드를 임계 구간으로 변경
  - 여러 스레드에서 동시에 인스턴스 생성을 막음
  - 문제점: 사실상 단일 스레드 환경이면 아무 의미 없고 락을 걸고 푸는 과정에서 오버헤드 발생
```java
public class Printer {
  // 외부에 제공할 자기 자신의 인스턴스
  private static Printer printer = null;
  private int counter = 0;
  private Printer() { }

  // 인스턴스를 만드는 메소드 동기화 (임계 구역)
  public synchronized static Printer getPrinter(){
    if (printer == null) {
      printer = new Printer(); // Printer 인스턴스 생성
    }
    return printer;
  }
  public void print(String str) {
    // 오직 하나의 스레드만 접근을 허용함 (임계 구역)
    // 성능을 위해 필요한 부분만을 임계 구역으로 설정한다.
    synchronized(this) {
      counter++;
      System.out.println(str + counter);
    }
  }
}
```

- 방법2. static 변수에 바로 인스턴스를 초기화
  - 문제점: 한번도 불리지 않는 클래스들도 모두 초기화되기 때문에 자원 낭비 발생
    - 단 현실적으로 큰 문제가 되는 경우는 자주 없을것으로 보임
```java
public class Printer {
   // static 변수에 외부에 제공할 자기 자신의 인스턴스를 만들어 초기화
   private static Printer printer = new Printer();
   private Printer() { }
   // 자기 자신의 인스턴스를 외부에 제공
   public static Printer getPrinter(){
     return printer;
   }
   public void print(String str) {
     System.out.println(str);
   }
}
```

- 방법 3. 정적 클래스 
  - 정적 메소드로만 이루어진 클래스를 활용
  - 컴파일타임에 바인딩되므로 실행시 바인딩되는 기존 방법들에 비해 성능 우수
  - 문제점
    - 인터페이스 구현이 필요한 경우 정적 메소드는 인터페이스에서 사용 불가능
```java
public class Printer {
      private static int counter = 0;
      // 메소드 동기화 (임계 구역)
      public synchronized static void print(String str) {
        counter++;
        System.out.println(str + counter);
      }
}
```
