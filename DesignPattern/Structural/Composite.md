### 개요
- 복합 객체와 단일 객체를 클라이언트에서 구분하지 않고 동일하게 사용할 수 있게 만드는 패턴
- 전체의 특성이 부분의 특성의 조합으로 만들어지는 경우에 유리
  - 컴퓨터의 가격은 부품가격의 합
  - 파일과 폴더 구조
    - OS는 모두 하나의 객체로 취급
    - 하지만 폴더를 삭제하면 아래 모든 파일도 동일하게 작업 일어남
    - 세부 구현은 다름
- Decorator 패턴과의 비교
  - 공통점
    - 한 추상 클래스를 상속받아 동일한 메소드를 지닌 다양한 객체를 만듬
    - 만들어진 객체를 조합하여 사용 가능
  - 차이점
    - Decorator 패턴은 기본 클래스와 추가 구현된 클래스의 레벨이 동일
    - Composite 패턴은 부분 클래스를 포함하고 있는 상위 Composite 클래스가 있어 전체-부분 관계를 

### 필요성
- 컴퓨터의 구성 요소를 만드는 예제
- 문제점
  - 부품이 하나씩 추가될 때 마다 Computer 객체 수정 필요
  
```java
// 부품에 대한 특징 포함
public class Keyboard {
  private int price;
  private int power;
  public Keyboard(int power, int price) {
    this.power = power;
    this.price = price;
  }
  
  public int getPrice() { return price; }
  public int getPower() { return power; }
}

public class Body { 동일한 구조 }

public class Monitor { 동일한 구조 }

public class Speaker { 동일한 구조 }

// 전체 컴퓨터에 대한 내용
public class Computer {
  private Keyboard Keyboard;
  private Body body;
  private Monitor monitor;
  private Speaker speaker;

  public addKeyboard(Keyboard keyboard) { this.keyboard = keyboard; }
  public addBody(Body body) { this.body = body; }
  public addMonitor(Monitor monitor) { this.monitor = monitor; }
  public addSpeaker(Speaker monitor) { this.speaker = speaker; }

  public int getPrice() {
    int keyboardPrice = keyboard.getPrice();
    int bodyPrice = body.getPrice();
    int monitorPrice = monitor.getPrice();
    int speakerPrice = speaker.getPrice();
    return keyboardPrice + bodyPrice + monitorPrice + speakerPrice;
  }
  
  public int getPower() {
    int keyboardPower = keyboard.getPower();
    int bodyPower = body.getPower();
    int monitorPower = monitor.getPower();
    int speakerPower = speaker.getPower();
    return keyboardPower + bodyPower + monitorPower + speakerPower;
  }
}

public class Client {
  public static void main(String[] args) {
    // 컴퓨터의 부품으로 Keyboard, Body, Monitor, Speaker 객체를 생성
    Keyboard keyboard = new Keyboard(5, 2);
    Body body = new Body(100, 70);
    Monitor monitor = new Monitor(20, 30);
    Monitor speaker = new Monitor(10, 5);

    // Computer 객체를 생성하고 부품 객체들을 설정
    Computer computer = new Computer();
    computer.addKeyboard(keyboard);
    computer.addBody(body);
    computer.addMonitor(monitor);
    computer.addSpeaker(speaker);

    // 컴퓨터의 가격과 전력 소비량을 구함
    int computerPrice = computer.getPrice();
    int computerPower = computer.getPower();
    System.out.println("Computer Price: " + computerPrice + "만원");
    System.out.println("Computer Power: " + computerPower + "W");
  }
}
```


### 구성 방법
- 구조
  - Component
    - 모든 클래스들의 원형이 되는 추상 클래스
    - 모든 클래스들에서 공통으로 포함되는 함수 선언
  - Leaf
    - 구체적인 부분 클래스
    - Composite 객체의 부품으로 사용되는 객체
  - Composite
    - Decorator 패턴과의 가장 큰 차이점
    - 전체 클래스
    - 복수개의 Component를 가질 수 있음
      - 복수개의 Leaf를 부분으로 지님
      - 또는 복수개의 Composite를 부분으로 지닐수도 있음
    - void addComponent(Component component) : 새로운 컴포넌트 추가
    - void removeComponent(Component component) : 기존 컴포넌트 제거
- 적용
  - 컴퓨터의 모든 구성 요소를 의미하는 ComputerDevice 추상 클래스 구성
  - ComputerDevice를 상속받아 컴퓨터의 부품을 의미하는 Keyboard, Body, Monitor, Speaker 클래스 구성
  - ComputerDevice를 상속받아 컴퓨터 전체를 의미하는 Computer 클래스 구성
    - Computer 클래스에 Component에 대한 리스트를 넣고 여기에 부품을 추가
 

```java
public abstract class ComputerDevice {
  public abstract int getPrice();
  public abstract int getPower();
}

public class Keyboard extends ComputerDevice {
  private int price;
  private int power;
  
  public Keyboard(int power, int price) {
    this.power = power;
    this.price = price;
  }
  
  public int getPrice() { return price; }
  public int getPower() { return power; }
}

public class Body extends ComputerDevice { 동일한 구조 }

public class Monitor extends ComputerDevice { 동일한 구조 }

public class Speaker extends ComputerDevice { 동일한 구조 }


public class Computer extends ComputerDevice {
  // 복수 개의 ComputerDevice 객체를 가리킴
  private List<ComputerDevice> components = new ArrayList<ComputerDevice>();

  // ComputerDevice 객체를 Computer 클래스에 추가
  public addComponent(ComputerDevice component) { components.add(component); }
  
  // ComputerDevice 객체를 Computer 클래스에서 제거
  public removeComponent(ComputerDevice component) { components.remove(component); }

  // 전체 가격을 포함하는 각 부품의 가격을 합산
  public int getPrice() {
    int price = 0;
    for(ComputerDevice component : components) {
      price += component.getPrice();
    }
    return price;
  }
  
  // 전체 소비 전력량을 포함하는 각 부품의 소비 전력량을 합산
  public int getPower() {
    int power = 0;
    for(ComputerDevice component : components) {
      price += component.getPower();
    }
    return power;
  }
}

public class Client {
  public static void main(String[] args) {
    // 컴퓨터의 부품으로 Keyboard, Body, Monitor, Speaker 객체를 생성
    Keyboard keyboard = new Keyboard(5, 2);
    Body body = new Body(100, 70);
    Monitor monitor = new Monitor(20, 30);
    Speaker speaker = new Speaker(20, 30);

    // Computer 객체를 생성하고 addComponent()를 통해 부품 객체들을 설정
    Computer computer = new Computer();
    computer.addComponent(keyboard);
    computer.addComponent(body);
    computer.addComponent(monitor);
    computer.addComponent(speaker);

    // 컴퓨터의 가격과 전력 소비량을 구함
    int computerPrice = computer.getPrice();
    int computerPower = computer.getPower();
    System.out.println("Computer Price: " + computerPrice + "만원");
    System.out.println("Computer Power: " + computerPower + "W");
  }
}
```
