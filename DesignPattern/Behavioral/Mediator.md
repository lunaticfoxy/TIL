# = 중재자 패턴, 조정자 패턴

### 개요
- 컴포넌트 사이의 상호작용을 하나의 Mediator를 통해 수행하는 패턴
- N:M 의 복잡한 관계를 1:N 으로 강제시켜 줌
- 동작
  - 송신자는 수신자와 이벤트를 Mediator에게 전달
  - Mediator는 수신자를 체크하여 해당 수신자에게 송신자 정보와 이벤트 전달


### 패턴 적용
- 구성
  - Colleague
    - Mediator를 통해 상호작용 할 객체들의 부모가 되는 인터페이스
    - 내부에 mediator 객체의 주소를 가지고 있음
    - 이벤트 발생시 mediator의 이벤트 메소드 실행
  - ConcreteColleague
    - Colleague를 상속받아 상호작용을 하는 클래스
    - 내부에 각 객체가 수행할 비즈니스 로직 포함
  - Meidator
    - 중재자 역할을 하기 위한 인터페이스
  - ConcreteMediator
    - 실제 Mediator의 동작을 정의하는 클래스
    - 내부에 통신에 의한 비즈니스 로직 포함
    - 이벤트 수신시 colleague 이벤트의 메소드 실행

- 예제 1. 양방향 통신
  - 유저간 채팅
  - ChatMediator 를 통해 ChatUser 사이에 양뱅향 통신이 이루어짐
  
```java
interface Mediator {
    public void addColleague(Colleague colleague);
    public void onEvent(Colleague colleague, String event);
}

interface Colleague {
    public setMediator(Mediator mediator);
    public receive(String msg);
}

public class ChatUser implements Colleague {
    private Mediator mediator;
    private String name;

    public ChatUser(String name) {
        this.name = name;
    }
    
    @Override
    public setMediator(Mediator mediator) {
        this.mediator = mediator;
        this.mediator.addColleague(this);
    }

    @Override
    public void receive(String msg) {
        System.out.println(name + " Message received : " + msg);
    }

    public void send(String msg) {
        System.out.println(name + " Sending Message = " + msg);
        mediator.onEvent(this, msg);
    }
}

public class ChatMediator implements Mediator {
    private List<Colleague> colleagues = new ArrayList<>();

    public void onEvent(Colleague colleague, String msg) {
        colleagues.stream()
              .filter(c -> c != colleague)
              .forEach(c -> c.receive(msg));
    }

    public ChatMediator addColleague(Colleague colleague) {
        colleagues.add(colleague);
        return this;
    }
}

public class Client {
    public static void main(String[] args) {
        ChatMediator mediator = new ChatMediator();

        ChatUser john = new ChatUser("John");
        ChatUser alice = new ChatUser("Alice");
        ChatUser bob = new ChatUser("Bob");
        
        john.setMediator(mediator);
        alice.setMediator(mediator);
        bob.setMediator(mediator);

        john.send("Hi every one!");
    }
}
```
  
    
    
- 예제 2. 일방향 통신
  - 시스템 이벤트가 발생할때마다 로그를 남기고 동시에 화면에 출력
  - Colleague를 ISource와 IDestination으로 나누어 송신자와 수신자를 분리
  - ISource 내부에만 mediator를 지님
    - ISource 만 이벤트 발생 가능
  - IDestination만 Mediator에 등록
    - IDestination만 이벤트 구독 가능
```java
interface Mediator {
    public void addDestination(IDestination destination);
    public void onEvent(String from, String event);
}

interface ISource{ 
    public void setMediator(Mediator mediator); 
    public void eventOccured(String event);
}

interface IDestination{
    public void receiveEvent(String from, String event); 
}

class TcpComm implements ISource{
    private Mediator mediator;

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public void eventOccured(String event){ // 이벤트의 전달
        mediator.onEvent("TCP", event);
    }
}


class SystemSignal implements ISource{
    private Mediator mediator;

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }
    
    @Override
    public void eventOccured(String event){
        mediator.onEvent("System", event);
    }
}

class Display implements IDestination{
    @Override
    public void receiveEvent(String from, String event){
        System.out.println("Display : from " + from + " event : " + event);
    }
}


class Log implements IDestination{
    @Override
    public void receiveEvent(String from, String event){
        System.out.println("Log : from " + from + " event : " + event);
    }
}


class SystemMediator implements Mediator {
    List<IDestination> destinations = new ArrayList<IDestination>();
    
    @Override
    public void addDestination(IDestination destination) { destinations.add(destination); }

    @Override
    public void onEvent(String from, String event) {
        destinations.stream()
            .forEach(d -> d.receiveEvent(from, event));
    }
}
```
