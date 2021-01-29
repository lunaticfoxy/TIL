### 개요
- 구체적인 클래스에 의존하지 않고 연관성있거나 의존적인 객체들의 조합을 만드는 인터페이스를 팩토리 형태로 제공
  - 단순하게 팩토리 자체를 다시 한번 추상화 한 개념
- 싱글톤, 팩토리 메소드 패턴을 조합해서 활용
- 팩토리 메소드와의 비교
  - 공통점
    - 팩토리 클래스를 사용하여 객체 생성
    - 추상 클래스와 인터페이스에 맞춰 코드 작성 가능
  - 차이점
    - 팩토리에서의 객체 생성 지원 범위
      - 팩토리 메소드
        - 한 팩토리 클래스에 1개의 create 메소드
        - 한 메소드 내에서 조건에 따라 여러 종류의 객체가 생성됨
      - 추상 팩토리
        - 한 팩토리 클래스에 여러개의 create 메소드
        - 상속을 통해 한 메소드는 한 객체를 생성하는게 보장
    - 팩토리 메소드가 만드는 객체 종류
      - 팩토리 메소드: 인자에 따라 다른 종류의 객체
      - 추상 팩토리: 인자에 따라 다른 종류의 팩토리
    - 결합도를 낮추는 대상
      - 팩토리 메소드: ConcreteProduct & Client
      - 추상 팩토리: ConcreteFactory & Client
    - 포커스
      - 팩토리 메소드
        - 메소드 레벨에서 포커스
        - 클라이언트의 ConcreteProduct 생성에 대한 책임 덜어줌
      - 추상 팩토리
        - 클래스 레벨에서 포커스
        - 각 Product들이 다른 클래스와 함께 사용될 때의 제약사항을 강제할 수 있음
          - 필수적으로 조합을 지정할 수 있음
          - 아래 예시 참조


### 필요성
- 엘리베이터의 모터에 문을 장착하는 예시
  - LG, 현대, 삼성에서 각각 모터와 문을 만듬
  - 팩토리 메소드 패턴으로 묶어 생성
    - MotorFactory, DoorFactory 존재
- 문제점
  - 제조사가 생길때매다 MotorFactory, DoorFactory 하나씩 수정 필요
  - 모든 팩토리 클래스에서 수정이 발생
  - 현실적으로는 LG 모터는 LG 문, 삼성 모터는 삼성 문과만 사용되겠지만 이를 강제하지 못함

```java
/* Motor, Door, 그리고 이를 상속받은 클래스들은 제외 */

public enum VendorID { LG, HYUNDAI, SAMSUNG }

public class MotorFactory {
  // vendorID에 따라 LGMotor 또는 HyundaiMotor 객체 또는 SamsungMotor 객체를 생성함
  public static Motor createMotor(VendorID vendorID) {
    Motor motor = null;

    switch (vendorID) {
      case LG:
        motor = new LGMotor();
        break;
      case HYUNDAI:
        motor = new HyundaiMotor();
        break;
      case SAMSUNG:
        motor = new SamsungMotor();
        break;
    }
    return motor;
  }
}

public class DoorFactory {
  // vendorID에 따라 LGDoor 또는 HyundaiDoor 객체 또는 SamsungDoor 객체를 생성함
  public static Door createDoor(VendorID vendorID) {
    Door door = null;
    
    switch (vendorID) {
      case LG:
        door = new LGDoor();
        break;
      case HYUNDAI:
        door = new HyundaiDoor();
        break;
      case SAMSUNG:
        door = new SamsungDoor();
        break;
    }
    
    return door;
  }
}


public class Client {
  public static void main(String[] args) {
    Door lgDoor = DoorFactory.createDoor(VendorID.LG); // 팩토리 메서드 호출
    Motor lgMotor = MotorFactory.createMotor(VendorID.LG); // 팩토리 메서드 호출
    lgMotor.setDoor(lgDoor);
    lgDoor.open();
    lgMotor.move(Direction.UP);
    
    Door hyundaiDoor = DoorFactory.createDoor(VendorID.HYUNDAI); // 팩토리 메서드 호출
    Motor hyundaiMotor = MotorFactory.createMotor(VendorID.HYUNDAI); // 팩토리 메서드 호출
    hyundaiMotor.setDoor(lgDoor);
    hyundaiDoor.open();
    hyundaiMotor.move(Direction.UP);
  }
}
```

### 패턴 적용
- 구성
  - Factory
    - 팩토리 클래스를 만들기 위한 추상 클래스
    - 클라이언트에서 각각의 팩토리 매소드로 부를 모든 생성 메소드를 포함
  - ConcreteFactory
    - Factory를 상속받아 구현하는 클래스
    - 구체적인 생성 메소드를 구현
      - 한 생성 메소드는 ConcreteProduct 만 생성
  - Product
    - 실제 사용자에게 제공되는 객체의 추상 클래스
    - 객체의 기본 요소 및 메소드 포함
  - ConcreteProduct
    - Product를 상속받아 구현하는 클래스
    - Product의 구체적인 동작 구현

- 적용 방법
  - ElevatorFactory 라는 상위 팩토리 클래스를 만들고 내부에 모터와 문을 생성하는 메소드 지정
  - 이를 상속받아 제조사별로 팩토리 클래스 생성
  - 각 제조사별 팩토리 클래스는 자기 제조사의 문과 모터만 생성
  
```java
/* Motor, Door, 그리고 이를 상속받은 클래스들은 제외 */

/* 추상 부품을 생성하는 추상 팩토리 클래스 */
public abstract class ElevatorFactory {
  public abstract Motor createMotor();
  public abstract Door createDoor();
}

/* LG 부품을 생성하는 팩토리 클래스 */
public class LGElevatorFactory extends ElevatorFactory {
  public Motor createMotor() { return new LGMotor(); }
  public Door createDoor() { return new LGDoor(); }
}

/* Hyundai 부품을 생성하는 팩토리 클래스 */
public class HyundaiElevatorFactory extends ElevatorFactory {
  public Motor createMotor() { return new HyundaiMotor(); }
  public Door createDoor() { return new HyundaiDoor(); }
}

/* Samsung 부품을 생성하는 팩토리 클래스 */
public class SamsungElevatorFactory extends ElevatorFactory {
  public Motor createMotor() { return new SamsungMotor(); }
  public Door createDoor() { return new SamsungDoor(); }
}


/* 주어진 업체의 이름에 따라 부품을 생성하는 Client 클래스 */
public class Client {
  public static void main(String[] args) {
    ElevatorFactory factory = null;
    String vendorName = args[0];

    // 인자에 따라 LG 또는 Hyundai 또는 Samsung 팩토리를 생성
    if(vendorName.equalsIgnoreCase("LG"))
      factory = new LGElevatorFactory();
    else if(vendorName.equalsIgnoreCase("Hyundai"))
      factory = new HyundaiElevatorFactory();
    else
      factory = new SamsungElevatorFactory();

    Door door = factory.createDoor(); // 해당 업체의 Door 생성
    Motor motor = factory.createMotor(); // 해당 업체의 Motor 생성
    motor.setDoor(door);

    door.open();
    motor.move(Direction.UP);
  }
}
```
