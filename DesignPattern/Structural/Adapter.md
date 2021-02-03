### 개요
- 한클래스의 인터페이스를 호환되지 않는 인터페이스로 변환하고자 할때 사용
- 클라이언트와 구현된 인터페이스 분리 가능
- 전기콘센트의 모양을 맞춰주는 것이라 이해하면 편함

### 필요성
- 예제
  - Duck과 Turkey는 외부에서 제공해주는 클래스로 변경 불가능
  - 클라이언트에서 요리 재료로 Duck 을 사용하는데 Turkey라는 재료를 대신 사용하고자 할때 이를 한 객체로 만들 수 없음
  
```java
public interface Duck {
  public void quack();
  public void fly();
}


public class MallardDuck implements Duck {
  @Override
  public void quack() {
    System.out.println("Quack");
  }

  @Override
  public void fly() {
    System.out.println("I'm flying");
  }
}

public interface Turkey {
  public void gobble();
  public void fly();
}

public class WildTurkey implements Turkey{
  @Override
  public void gobble() {
    System.out.println("Gobble gobble");
  }
  
  @Override
  public void fly() { 
    System.out.println("I'm flying a short distance");
  }
}
```

### 적용 방법
- 구성
  - Target : 어뎁터의 대상이 되는 인터페이스
  - Adapter : Target과 Adaptee를 연결시키기 위한 어댑터 클래스
  - Adaptee : 어댑터의 대상이 되는 클래스
- 적용
  - Duck을 상송받은 TurkeyAdapter 클래스를 만들어 멤버변수로 Turkey 변수 지정
  - Duck의 메소드 호출시 Turkey의 메소드를 호출하도록 내부 구현
  
```java
public class TurkeyAdapter implements Duck {
  Turkey turkey;

  public TurkeyAdapter(Turkey turkey) {
    this.turkey = turkey;
  }

  @Override
  public void quack(){ 
    turkey.gobble();
  }

  @Override
  public void fly() {
    turkey.fly();
  }
}
```
  
