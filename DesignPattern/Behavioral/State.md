### 개요
- 객체의 상태에 따라 동작이 변하는 경우 상태 자체를 별도의 인스턴스로 저장하여 객체 내부에서의 호출을 단순화 하는 방법
- 외부에서 제어하는 방식을 통일하고 객체에서는 실제로 어떤 일이 일어나는지 몰라도 되도록 구성
- Strategy 패턴과의 차이
  - 공통점
    - 변화가 자주 생기는 부분을 캡슐화
    - 내부에서 어떤 동작이 일어나는지 구체적으로 모르고 외부에서 공통된 메소드를 호출만 하면 됨
  - 차이점
    - Strategy 패턴은 호출이 일어나는 객체 자체가 나뉨
      - 객체 자체를 추상화 하고싶을때 주로 사용
      - 한번 생성된 뒤 자주 변하지 않음
    - State 패턴은 호출이 일어나는 객체는 동일하지만 내부의 상태 각체가 나뉨
      - 객체의 구체적인 동작을 추상화 하고싶을때 주로 사용
      - 객체의 상태 변화에 따라 자주 변함


### 필요성
- 파워가 on인 상태에서 전원을 누르면 off, off인 상태에서 전원을 누르면 절전, 절잔 상태에서 전원을 누르면 on 이 되는 노트북 구현
- 매 상태마다 일일히 if-else 로 구성해줘야 함
  - 상태에 따른 동작이 추가될때마다 Laptop 클래스 변경 필요

```java
public class Laptop {
    public static String ON = "on";
    public static String OFF = "off";
    public static String SAVING = "saving";
    private String powerState = "";

    public Laptop(){
        setPowerState(Laptop.OFF);
    }

    public void setPowerState(String powerState){
        this.powerState = powerState;
    }

    public void powerPush(){
        if ("on".equals(this.powerState)) {
            System.out.println("전원 off");
        }
        else if ("saving".equals(this.powerState)){
            System.out.println("전원 on");
        }
        else {
            System.out.println("절전 모드");
        }
    }
}

public class Client {
    public static void main(String args[]){
        Laptop laptop = new Laptop();
        laptop.powerPush();
        laptop.setPowerState(Laptop.ON);
        laptop.powerPush();
        laptop.setPowerState(Laptop.SAVING);
        laptop.powerPush();
        laptop.setPowerState(Laptop.OFF);
        laptop.powerPush();
        laptop.setPowerState(Laptop.ON);
        laptop.powerPush();
    }
}
```


### 패턴 적용
- 구조
  - State
    - 상태를 표현하기 위한 인터페이스
    - 동작을 수행하는 객체에서는 현재 상태를 이 State로 저장
  - ConcreteState
    - State를 상속받아 구현한 객체
    - 실제 상태와 상태에 따른 동작을 저장
  
- 실제 구성
  - 현재 상태를 표현하는 PowerState 인터페이스를 생성
    - 이를 상속받아 On, Off, Saving 클래스를 구현하고 전원 버튼을 누를때 동작하는 로직 포함
  - Labtop에서는 PowerState에 전원을 눌렀다는 이벤트만 전달
  
```java
public interface PowerState {
    public void powerPush();
}

public class On implements PowerState{
    public void powerPush(){
        System.out.println("전원 off");
    }
}

public class Off implements PowerState {
    public void powerPush(){
        System.out.println("절전 모드");
    }
}

public class Saving implements PowerState {
    public void powerPush(){
        System.out.println("전원 on");
    }
}

public class Laptop {
    private PowerState powerState;

    public Laptop(){
        this.powerState = new Off();
    }

    public void setPowerState(PowerState powerState){
        this.powerState = powerState;
    }

    public void powerPush(){
        powerState.powerPush();
    }
}

public class Client {
    public static void main(String args[]){
        Laptop laptop = new Laptop();
        On on = new On();
        Off off = new Off();
        Saving saving = new Saving();

        laptop.powerPush();
        laptop.setPowerState(on);
        laptop.powerPush();
        laptop.setPowerState(saving);
        laptop.powerPush();
        laptop.setPowerState(off);
        laptop.powerPush();
        laptop.setPowerState(on);
        laptop.powerPush();
    }
}
```
