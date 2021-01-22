### 개요
- 기능을 캡슐화하여 호출자와 수신자 사이에 캡슐화된 기능으로 작업을 지시하는 패턴
- 실행할 기능이 다양하고 변경이 잦을 경우에 용이


### 필요성
- 버튼을 눌렀을 때 램프의 불이 켜지는 프로그램
- 알람을 추가한다면?
  - 기능이 새로 생길때마다 계속 Button 클래스의 수정 필요
```java
public class Lamp {
  public void turnOn(){ System.out.println("Lamp On"); }
}

ublic class Alarm {
  public void start(){ System.out.println("Alarming"); }
}

public class Button {
  private Alarm theAlarm;
  public Button(Alarm theAlarm) { this.theAlarm = theAlarm; }
  public void pressed() { theAlarm.start(); }
}

public class Client {
  public static void main(String[] args) {
    Lamp lamp = new Lamp();
    Alarm alarm = new Alarm();
    Button lampButton = new Button(lamp);
    Button alarmButton = new Button(alarm);
    lampButton.pressed();
    alarmButton.pressed();
  }
}
```

- 버튼의 선택 횟수에 따라 다른 동작을 한다면?
  - 버튼을 처음 눌렀을때는 램프, 두 번 눌렀을때는 알람 동작
  - 이경우에도 매번 Button 수정 필요
```java
enum Mode { LAMP, ALARM };

// Button 클래스의 코드를 수정
public class Button {
  private Lamp theLamp;
  private Alarm theAlarm;
  private Mode theMode;

  // 생성자에서 버튼을 눌렀을 때 필요한 기능을 인지로 받는다.
  public Button(Lamp theLamp, Alarm theAlarm) {
    this.theLamp = theLamp;
    this.theAlarm = theAlarm;
  }
  
  // 램프 모드 또는 알람 모드를 설정
  public void setMode(Mode mode) { this.theMode = mode; }
  
  // 설정된 모드에 따라 램프를 켜거나 알람을 울림
  public void pressed() {
    switch(theMode) {
     case LAMP: theLamp.turnOn(); break;
     case ALARM: theAlarm.start(); break;
    }
  }
}
```

### 해결책
- 구조
  - 기능을 전달하는 있는 Command 인터페이스
    - void execute() : 실제 기능 동작
  - ConcreteCommand : 실제 구현된 기능
  - Invoker : Command를 실행하는 주체
    - void setCommand(Command newCommand) : 동작을 수행할 기능 지정
    - Command theCommand : 기능을 저장하는 변수
  - Receiver
    - 실제 Command의 실행 내용 포함
    - Command의 execute에서 기능 실행
    
```java
public interface Command { public abstract void execute(); }

public class Button {
  private Command theCommand;
  
  // 생성자에서 버튼을 눌렀을 때 필요한 기능을 인지로 받는다.
  public Button(Command theCommand) { setCommand(theCommand); }
  public void setCommand(Command newCommand) { this.theCommand = newCommand; }
  
  // 버튼이 눌리면 주어진 Command의 execute 메서드를 호출한다.
  public void pressed() { theCommand.execute(); }

  public class Lamp {
  public void turnOn(){ System.out.println("Lamp On"); }
}

/* 램프를 켜는 LampOnCommand 클래스 */
public class LampOnCommand implements Command {
  private Lamp theLamp;
  
  public LampOnCommand(Lamp theLamp) { this.theLamp = theLamp; }
  
  // Command 인터페이스의 execute 메서드
  public void execute() { theLamp.turnOn(); }
}

public class Client {
  public static void main(String[] args) {
    Lamp lamp = new Lamp();
    Command lampOnCommand = new LampOnCommand(lamp);
    Alarm alarm = new Alarm();
    Command alarmStartCommand = new AlarmStartCommand(alarm);

    Button button1 = new Button(lampOnCommand); // 램프 켜는 Command 설정
    button1.pressed(); // 램프 켜는 기능 수행

    Button button2 = new Button(alarmStartCommand); // 알람 울리는 Command 설정
    button2.pressed(); // 알람 울리는 기능 수행
    button2.setCommand(lampOnCommand); // 다시 램프 켜는 Command로 설정
    button2.pressed(); // 램프 켜는 기능 수행
  }
}
```
