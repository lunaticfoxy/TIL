### 개요
- 작업 처리의 일부분을 서브 클래스로 캡슐화 하여 일의 수행 구조를 최대한 유지하는 패턴
- 전체적으로 동일하고 부분적으로 다른 메서드의 코드 중복 최소화
- 동일한 기능을 상위 클래스에서 정의하고, 확장/변화가 필요한 부분만 서브클래스에서 구현


### 필요성
- 여러 회사의 모터를 지원하는 엘리베이터 시스템 예시
- 문제점
  - HyundaiMotor와 LGMotor 사이에 중복 코드 다수 존재
    - Door 클래스와의 연관
    - MotorStatus 필드
    - getMotorStatus, setMotorStatus
    - move 메서드 내의 내용중 상
    
```java
public enum DoorStatus { CLOSED, OPENED }
public enum MotorStatus { MOVING, STOPPED }

public class Door {
  private DoorStatus doorStatus;

  public Door() { doorStatus = DoorStatus.CLOSED; }
  public DoorStatus getDoorStatus() { return doorStatus; }
  public void close() { doorStatus = DoorStatus.CLOSED; }
  public void open() { doorStatus = DoorStatus.OPENED; }
}

public class HyundaiMotor {
  private Door door;
  private MotorStatus motorStatus;

  public HyundaiMotor() {
    this.door = door;
    motorStatus = MotorStatus.STOPPED; // 초기: 멈춘 상태
  }
  private void moveHyundaiMotor(Direction direction) {
    // Hyundai Motor를 구동시킴
  }
  public MotorStatus getMotorStatus() { return motorStatus; }
  private void setMotorStatus() { this.motorStatus = motorStatus; }

  /* 엘리베이터 제어 */
  public void move(Direction direction) {
    MotorStatus motorStatus = getMotorStatus();
    
    // 이미 이동 중이면 아무 작업을 하지 않음
    if (motorStatus == MotorStatus.MOVING) return;

    DoorStatus doorStatus = door.getDoorStatus();
    
    // 만약 문이 열려 있으면 우선 문을 닫음
    if (doorStatus == DoorStatus.OPENED) door.close();

    // Hyundai 모터를 주어진 방향으로 이동시킴
    moveHyundaiMotor(direction);

    // 모터 상태를 이동 중으로 변경함
    setMotorStatus(MotorStatus.MOVING);
  }
}

public class LGMotor {
  private Door door;
  private MotorStatus motorStatus;

  public LGMotor() {
    this.door = door;
    motorStatus = MotorStatus.STOPPED; // 초기: 멈춘 상태
  }
  private void moveLGMotor(Direction direction) {
    // LG Motor를 구동시킴
  }
  public MotorStatus getMotorStatus() { return motorStatus; }
  private void setMotorStatus() { this.motorStatus = motorStatus; }

  /* 엘리베이터 제어 */
  public void move(Direction direction) {
    MotorStatus motorStatus = getMotorStatus();
    
    // 이미 이동 중이면 아무 작업을 하지 않음
    if (motorStatus == MotorStatus.MOVING) return;

    DoorStatus doorStatus = door.getDoorStatus();
    
    // 만약 문이 열려 있으면 우선 문을 닫음
    if (doorStatus == DoorStatus.OPENED) door.close();

    // LG 모터를 주어진 방향으로 이동시킴
    moveLGMotor(direction); // (이 부분을 제외하면 HyundaiMotor의 move 메서드와 동일)

    // 모터 상태를 이동 중으로 변경함
    setMotorStatus(MotorStatus.MOVING);
  }
}

public class Client {
  public static void main(String[] args) {
    Door door = new Door();
    HyundaiMotor hyundaiMotor = new HyundaiMotor(door);
    hyundaiMotor.move(Direction.UP); // 위로 올라가도록 엘리베이터 제어
    
    LGMotor lgMotor = new lgMotor(door);
    lgMotor.move(Direction.UP); // 위로 올라가도록 엘리베이터 제어
  }
}
```

### 적용 방법
- 구조
  - AbstractClass
    - 템플릿 메소드를 정의
    - 하위 클래스들에서 공통으로 사용할 알고리즘 정의
    - 하위 클래스에서 구현될 기능을 hook 메소드로 정의
  - ConcreteClass
    - 상속받은 hook 메소드의 내부 구현

- 구현 방법 1
  - 공통 부분을 포함한 상위 클래스를 만들고 이를 상속받아 구현
```java
/* HyundaiMotor와 LGMotor의 공통적인 기능을 구현하는 클래스 */
public abstract class Motor {
  protected Door door;
  private MotorStatus motorStatus; // 공통 2. motorStatus 필드

  public Motor(Door door) { // 공통 1. Door 클래스와의 연관관계
    this.door = door;
    motorStatus = MotorStatus.STOPPED;
  }
  
  // 공통 3. etMotorStatus, setMotorStatus 메소드
  public MotorStatus getMotorStatus() { return MotorStatus; }
  protected void setMotorStatus(MotorStatus motorStatus) { this.motorStatus = motorStatus; }
  
  // 공통적으로 구현해야 하는 move 메소드
  public abstract void move(Direction direction);
}

/* Motor를 상속받아 HyundaiMotor 클래스를 구현 */
public class HyundaiMotor extends Motor{
  public HyundaiMotor(Door door) { super(door); }
  private void moveHyundaiMotor(Direction direction) {
    // Hyundai Motor를 구동시킴
  }
  
  @Override
  public void move(Direction direction) {
    MotorStatus motorStatus = getMotorStatus();
    
    // 이미 이동 중이면 아무 작업을 하지 않음
    if (motorStatus == MotorStatus.MOVING) return;

    DoorStatus doorStatus = door.getDoorStatus();
    
    // 만약 문이 열려 있으면 우선 문을 닫음
    if (doorStatus == DoorStatus.OPENED) door.close();

    // Hyundai 모터를 주어진 방향으로 이동시킴
    moveHyundaiMotor(direction);

    // 모터 상태를 이동 중으로 변경함
    setMotorStatus(MotorStatus.MOVING);
  }
}

/* Motor를 상속받아 LGMotor 클래스를 구현 */
public class LGMotor extends Motor{
  public LGMotor(Door door) { super(door); }
  private void moveLGMotor(Direction direction) {
    // LG Motor를 구동시킴
  }
  
  @Override
  public void move(Direction direction) {
    MotorStatus motorStatus = getMotorStatus();
    
    // 이미 이동 중이면 아무 작업을 하지 않음
    if (motorStatus == MotorStatus.MOVING) return;

    DoorStatus doorStatus = door.getDoorStatus();
    
    // 만약 문이 열려 있으면 우선 문을 닫음
    if (doorStatus == DoorStatus.OPENED) door.close();

    // LG 모터를 주어진 방향으로 이동시킴
    moveLGMotor(direction); // (이 부분을 제외하면 HyundaiMotor의 move 메서드와 동일)

    // 모터 상태를 이동 중으로 변경함
    setMotorStatus(MotorStatus.MOVING);
  }
}
```

- 구현방법 2
  - 부분중복되는 메소드도 세부 메소드로 나누고 상속을 활용해 코드 중복 최소화
```java
/* HyundaiMotor와 LGMotor의 공통적인 기능을 구현하는 클래스 */
public abstract class Motor {
  protected Door door;
  private MotorStatus motorStatus; // 공통 2. motorStatus 필드

  public Motor(Door door) { // 공통 1. Door 클래스와의 연관관계
    this.door = door;
    motorStatus = MotorStatus.STOPPED;
  }
  // 공통 3. etMotorStatus, setMotorStatus, moveMotor 메서드
  public MotorStatus getMotorStatus() { return MotorStatus; }
  protected void setMotorStatus(MotorStatus motorStatus) { this.motorStatus = motorStatus; }
  protected abstract void moveMotor(Direction direction);
  
  // HyundaiMotor와 LGMotor의 move 메서드에서 공통되는 부분만을 가짐
  public void move(Direction direction) {
    MotorStatus motorStatus = getMotorStatus();
    // 이미 이동 중이면 아무 작업을 하지 않음
    if (motorStatus == MotorStatus.MOVING) return;

    DoorStatus doorStatus = door.getDoorStatus();
    // 만약 문이 열려 있으면 우선 문을 닫음
    if (doorStatus == DoorStatus.OPENED) door.close();

    // 모터를 주어진 방향으로 이동시킴
    moveMotor(direction); // (HyundaiMotor와 LGMotor에서 오버라이드 됨)
    // 모터 상태를 이동 중으로 변경함
    setMotorStatus(MotorStatus.MOVING);
  }
}

/* Motor를 상속받아 HyundaiMotor 클래스를 구현 */
public class HyundaiMotor extends Motor{
  public HyundaiMotor(Door door) { super(door); }
  
  @Override
  protected void moveMotor(Direction direction) {
    // Hyundai Motor를 구동시킴
  }
}

/* Motor를 상속받아 LGMotor 클래스를 구현 */
public class LGMotor extends Motor{
  public LGMotor(Door door) { super(door); }
  
  @Override
  protected void moveMotor(Direction direction) {
    // LG Motor를 구동시킴
  }
}
```
