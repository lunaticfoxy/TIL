### 개요
- 어떠한 행위 자체를 캡슐화 하여 동적으로 행위를 변환 가능
- 입력하는 객체를 변경함으로써 로직의 변경이 발생
- 상황에 따라 동작이 변경되어야 할 때 용이
  - ex) 게임 캐릭터가 상황에 따라 공격하는 방식 변경
  
### 필요성
- 로봇 추상 클래스를 만들고 이를 상속받아 실제 로봇을 생성하는 예시
- 로봇에 attack, move 방식이 변경될 때 마다 실제 로봇 객체의 변경 필요
  - ex) Atom을 걷게만 하려면? vs TaekwonV를 날게 하려면?
- 새로운 로봇이 추가될 때 기존 로봇에 있는 로직 중복 발생 가능
  - ex) Sungard를 만들어 미사일을 쏘게 하려면? - 이미 TaekwonV에 있는 기능
```java
public abstract class Robot {
  private String name;
  public Robot(String name) { this.name = name; }
  public String getName() { return name; }
  // 추상 메서드
  public abstract void attack();
  public abstract void move();
}

public class TaekwonV extends Robot {
  public TaekwonV(String name) { super(name); }
  public void attack() { System.out.println("I have Missile."); }
  public void move() { System.out.println("I can only walk."); }
}

public class Atom extends Robot {
  public Atom(String name) { super(name); }
  public void attack() { System.out.println("I have strong punch."); }
  public void move() { System.out.println("I can fly."); }
}

public class Sungard extends Robot {
  public Sungard(String name) { super(name); }
  public void attack() { System.out.println("I have Missile."); } // 중복
  public void move() { System.out.println("I can only walk."); }
}

public class Client {
  public static void main(String[] args) {
    Robot taekwonV = new TaekwonV("TaekwonV");
    Robot atom = new Atom("Atom");

    System.out.println("My name is " + taekwonV.getName());
    taekwonV.move();
    taekwonV.attack();

    System.out.println()
    System.out.println("My name is " + atom.getName());
    atom.move();
    atom.attack();
  }
}
```

### 적용 방법
- 구조
  - Strategy: 인터페이스나 추상 클래스를 통해 외부에서 동일한 방법으로 알고리즘을 호출하도록 명시
  - ConcreteStrategy: 실제 구현된 Strategy
  - Context
    - 스트래티지 패턴을 이용하는 역할
    - Strategy 를 입력받아 로직을 결정하는 setter 메소드 제공
- 예시

```java
// 로봇 기본 Context 구현
public abstract class Robot {
  private String name;
  private AttackStrategy attackStrategy;
  private MovingStrategy movingStrategy;

  public Robot(String name) { this.name = name; }
  public String getName() { return name; }
  public void attack() { attackStrategy.attack(); }
  public void move() { movingStrategy.move(); }

  // 집약 관계, 전체 객체가 메모리에서 사라진다 해도 부분 객체는 사라지지 않는다.
  // setter 메서드
  public void setAttackStrategy(AttackStrategy attackStrategy) {
    this.attackStrategy = attackStrategy; 
  }
  
  public void setMovingStrategy(MovingStrategy movingStrategy) {
    this.movingStrategy = movingStrategy; 
  }
}

// Context를 상속받아 실제 로봇 구현
public class TaekwonV extends Robot {
  public TaekwonV(String name) { super(name); }
}

public class Atom extends Robot {
  public Atom(String name) { super(name); }
}


// attack을 위한 Strategy 인터페이스
interface AttackStrategy { public void attack(); }

// attack을 위한 ConcreteStrategy 클래스
public class MissileStrategy implements AttackStrategy {
  public void attack() { System.out.println("I have Missile."); }
}

public class PunchStrategy implements AttackStrategy {
  public void attack() { System.out.println("I have strong punch."); }
}

// move를 위한 Strategy 인터페이스
interface MovingStrategy { public void move(); }

// move를 위한 ConcreteStrategy 클래스
public class FlyingStrategy implements MovingStrategy {
  public void move() { System.out.println("I can fly."); }
}

public class WalkingStrategy implements MovingStrategy {
  public void move() { System.out.println("I can only walk."); }
}


public class Client {
  public static void main(String[] args) {
    Robot taekwonV = new TaekwonV("TaekwonV");
    Robot atom = new Atom("Atom");

    /* 수정된 부분: 전략 변경 방법 */
    taekwonV.setMovingStrategy(new WalkingStrategy());
    taekwonV.setAttackStrategy(new MissileStrategy());
    atom.setMovingStrategy(new FlyingStrategy());
    atom.setAttackStrategy(new PunchStrategy());

    /* 아래부터는 동일 */
    System.out.println("My name is " + taekwonV.getName());
    taekwonV.move();
    taekwonV.attack();

    System.out.println()
    System.out.println("My name is " + atom.getName());
    atom.move();
    atom.attack();
  }
}
```
