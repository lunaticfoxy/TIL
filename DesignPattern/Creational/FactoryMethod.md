### 개요
- 객체 생성 처리를 서브 클래스로 분리해서 처리하도록 함
  - 객체의 생성 코드를 별도의 클래스나 메소드로 분리
- 객체 생성 방법의 변화에 대비
  - 기능이 추가될경우 객체 생성 코드가 변경될 가능성 높음
  - 직접 객체를 생성할 경우 객체가 생성되는 모든 곳에서 코드 수정 필요
  
### 필요성
- 엘리베이터 운영 스케줄링 코드
  - 오전에는 ResponseTimeScheduler, 오후에는 ThroughputScheduler 를 통해 스케줄링
- 문제점
  - 스케줄링 전략 추가시 requestElevator() 함수 수정 필요
  - 매번 스케줄링 전략을 담은 클래스가 새로 

```java
public class ElevatorManager {
  private List<ElevatorController> controllers;

  // 주어진 수만큼의 ElevatorController를 생성함
  public ElevatorManager(int controllerCount) {
    // 엘리베이터의 이동을 책임지는 ElevatorController 객체 생성
    controllers = new ArrayList<ElevatorController>(controllerCount);
    for (int i=0; i<controllerCount; i++) {
      ElevatorController controller = new ElevatorController(i + 1); // 변경
      controllers.add(controller);
    }
  }
  // 요청에 따라 엘리베이터를 선택하고 이동시킴
  void requestElevator(int destination, Direction direction) {
    ElevatorScheduler scheduler; // 인터페이스

    // 0..23
    int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);

    // 오전에는 ResponseTimeScheduler, 오후에는 ThroughputScheduler
    if (hour < 12)
      scheduler = new ResponseTimeScheduler();
    else
      scheduler = new ThroughputScheduler();

    // ElevatorScheduler 인터페이스를 이용해 엘리베이터를 선택함
    int selectedElevator = scheduler.selectElevator(this, destination, direction);
    // 선택된 엘리베이터를 이동시킴
    controllers.get(selectElevator).gotoFloor(destination);
  }
}
https://gmlwjd9405.github.io/2018/08/07/factory-method-pattern.html

public class ElevatorController {
  private int id; // 엘리베이터 ID
  private int curFloor; // 현재 층

  public ElevatorController(int id) {
    this.id = id;
    curFloor = 1;
  }
  
  public void gotoFloor(int destination) {
    System.out.print("Elevator [" + id + "] Floor: " + curFloor);

    // 현재 층 갱신, 즉 주어진 목적지 층(destination)으로 엘리베이터가 이동함
    curFloor = destination;
    System.out.println(" ==> " + curFloor);
  }
}

/* 엘리베이터 작업 처리량을 최대화시키는 전략의 클래스 */
public class ThroughputScheduler {
  public int selectElevator(ElevatorManager manager, int destination, Direction direction) {
    return 0; // 임의로 선택함
  }
}
```

### 해결 방법
- 구조
  - Product: 팩토리 메소드로 생성될 객체의 공통 인터페이스
  - ConcreteProduct: Product를 상속받아 실제 생성될 객체
  - Creator: 팩토리 매소드의 원형을 담고 있는 공통 인터페이스
  - ConcreteCreator: Creator를 상속받아 실제 팩토리 메소드의 동작을 담고있는 객체
  
- 동작
  - 스케줄링 전략은 외부에서 파라미터로 지정
  - Scheduler의 생성은 SchedulerFactory에 맞김
  - 스케줄러를 싱글톤으로 구현하여 한번 생성된 스케줄러는 재사용

```java
public enum SchedulingStrategyID { RESPONSE_TIME, THROUGHPUT, DYNAMIC }

public class SchedulerFactory {
  // 스케줄링 전략에 맞는 객체를 생성
  public static ElevatorScheduler getScheduler(SchedulingStrategyID strategyID) {
    ElevatorScheduler scheduler = null; // 각 전략에 의해 할당됨

    switch (strategyID) {
      case RESPONSE_TIME: // 대기 시간 최소화 전략
        scheduler = ResponseTimeScheduler.getInstance();
        break;
      case THROUGHPUT: // 처리량 최대화 전략
        scheduler = ThroughputScheduler.getInstance();
        break;
      case DYNAMIC: // 동적 스케줄링
        // 0..23
        int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
        // 오전: 대기 시간 최소화, 오후: 처리량 최대화
        if (hour < 12)
          scheduler = ResponseTimeScheduler.getInstance();
        else
          scheduler = ThroughputScheduler.getInstance();
        break;
    }
    return scheduler;
  }
}

/* 싱글턴 패턴으로 구현한 ThroughputScheduler 클래스 */
public class ThroughputScheduler {
  private static ElevatorScheduler scheduler;
  // 생성자를 private으로 정의
  private ThroughputScheduler() {}
  // 정적 메서드로 객체 생성을 구현 (싱글턴 패턴)
  public static ElevatorScheduler getInstance() {
    if(scheduler == null)
      scheduler = new ThroughputScheduler();
    return scheduler;
  }
  public int selectElevator(ElevatorManager manager, int destination, Direction direction) {
    return 0; // 임의로 선택함
  }
}

/* 싱글턴 패턴으로 구현한 ResponseTimeScheduler 클래스 */
public class ResponseTimeScheduler {
  private static ElevatorScheduler scheduler;
  // 생성자를 private으로 정의
  private ResponseTimeScheduler() {}
  // 정적 메서드로 객체 생성을 구현 (싱글턴 패턴)
  public static ElevatorScheduler getInstance() {
    if(scheduler == null)
      scheduler = new ResponseTimeScheduler();
    return scheduler;
  }
  public int selectElevator(ElevatorManager manager, int destination, Direction direction) {
    return 1; // 임의로 선택함
  }
}

public class ElevatorManager {
  private List<ElevatorController> controllers;
  private SchedulingStrategyID strategyID;

  // 주어진 수만큼의 ElevatorController를 생성함
  public ElevatorManager(int controllerCount, SchedulingStrategyID strategyID) {
    // 엘리베이터의 이동을 책임지는 ElevatorController 객체 생성
    controllers = new ArrayList<ElevatorController>(controllerCount);
    for (int i=0; i<controllerCount; i++) {
      ElevatorController controller = new ElevatorController(i + 1);
      controllers.add(controller);
    }
  }
  // 실핼 중에 다른 스케줄링 전략으로 지정 가능
  public setStrategyID(SchedulingStrategyID strategyID) {
    this.strategyID = strategyID;
  }
  // 요청에 따라 엘리베이터를 선택하고 이동시킴
  void requestElevator(int destination, Direction direction) {
    // 주어진 전략 ID에 해당되는 ElevatorScheduler를 사용함 (변경)
    ElevatorScheduler scheduler = SchedulerFactory.getScheduler(strategyID);
    System.out.println(scheduler);

    // 주어진 전략에 따라 엘리베이터를 선택함
    int selectedElevator = scheduler.selectElevator(this, destination, direction);
    // 선택된 엘리베이터를 이동시킴
    controllers.get(selectElevator).gotoFloor(destination);
  }
}

public class Client {
  public static void main(String[] args) {
    ElevatorManager emWithResponseTimeScheduler = new ElevatorManager(2, SchedulingStrategyID.RESPONSE_TIME);
    emWithResponseTimeScheduler.requestElevator(10, Direction.UP);

    ElevatorManager emWithThroughputScheduler = new ElevatorManager(2, SchedulingStrategyID.THROUGHPUT);
    emWithThroughputScheduler.requestElevator(10, Direction.UP);

    ElevatorManager emWithDynamicScheduler = new ElevatorManager(2, SchedulingStrategyID.DYNAMIC);
    emWithDynamicScheduler.requestElevator(10, Direction.UP);
  }
}
```
