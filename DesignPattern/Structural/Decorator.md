### 개요
- 동일한 방식으로 사용되는 유사한 기능을 확장할 가능성이 있을 경우 사용하는 구조적 패턴
- 상위 객체를 만들고 여기에 외부 접근 함수와 기본 동작을 지정
- 추가적인 기능은 클래스의 객체 조합을 이용
  - 객체조합이란?
    - 생성자에서 필드에 대한 객체를 생성하는 경우
      - 생성할때 다른 객체를 필드에 저장해서 해당 객체의 일부분으로 사용
    - 전체 객체의 라이프타임과 부분 객체의 라이프 타임은 의존적이다.
    - 즉, 전체 객체가 없어지면 부분 객체도 없어진다.

### 필요이유
- 단순 상속으로 기능을 확장할 경우
  - 기능이 추가될때마다 기능의 조합이 들어간 클래스를 새로 하나씩 만들어줘야함
  - 기능이 하나 추가될때마다 조합의 수가 만들어야 하는 클래스 수가 2배로 증가
    - 아래 예시에서는 추가기능이 2개라 클래스 4개 존재
  
```java
// 기본 도로 표시 클래스
public class RoadDisplay {
    public void draw() { System.out.println("기본 도로 표시"); }
}

// 기본 도로 표시 + 차선 표시 클래스
public class RoadDisplayWithLane extends RoadDisplay {
  public void draw() {
      super.draw(); // 상위 클래스, 즉 RoadDisplay 클래스의 draw 메서드를 호출해서 기본 도로 표시
      drawLane(); // 추가적으로 차선 표시
  }
  private void drawLane() { System.out.println("차선 표시"); }
}

// 기본 도로 표시 + 교통량 표시 클래스
public class RoadDisplayWithTraffic extends RoadDisplay {
   public void draw() {
     super.draw(); // 상위 클래스, 즉 RoadDisplay 클래스의 draw 메서드를 호출해서 기본 도로 표시
     drawTraffic(); // 추가적으로 교통량 표시
   }
   private void drawTraffic() { System.out.println("교통량 표시"); }
}

// 기본 도로 표시 + 교통량 표시 클래스 + 차선 표시 클래스
public class RoadDisplayWithTraffic extends RoadDisplay {
   public void draw() {
     super.draw(); // 상위 클래스, 즉 RoadDisplay 클래스의 draw 메서드를 호출해서 기본 도로 표시
     drawTraffic(); // 추가적으로 교통량 표시
     drawLane(); // 추가적으로 차선 표시
   }
   private void drawLane() { System.out.println("차선 표시"); }
   private void drawTraffic() { System.out.println("교통량 표시"); }
}

public class Client {
  public static void main(String[] args) {
      RoadDisplay road = new RoadDisplay();
      road.draw(); // 기본 도로만 표시

      RoadDisplay roadWithLane = new RoadDisplayWithLane();
      roadWithLane.draw(); // 기본 도로 표시 + 차선 표시
  }
}
```

### 적용 방법
- 구조
  - 기본기능과 추가기능이 공용으로 사용할 상위 추상 클래스 생성: Component
  - 기본 기능이 정의된 클래스 생성: Concrete Component
  - 추가 기능을 넣기 위한 추상 클래스 생성: Decorator
    - Decorator의 생성자에서 다른 Component를 받아 decoratedComponent 라는 이름으로 저장해 둠
    - 실제 동작이 일어날때 decoratedComponent의 기능을 먼저 실행하고 본인의 기능을 실행
  - 실제 추가 기능이 정의된 클래스 Concrete Decorator 생성
- 실제 사용시
  - 기본 기능만 필요한 경우 Concrete Component 만 사용
  - 추가 기능이 하나만 존재하는 경우 Concrete Decorator에 Concrete Component를 넣어 사용
  - 추가 기능이 여러개 존재하는 경우 먼저 동작할 기능의 Concrete Decorator에 Concrete Component를 넣고, 이 Concrete Decorator를 두번째 기능의 Concrete Decorator에 넣음
    - 이로써 기본 기능 -> 추가 기능 1 -> 추가 기능 2 가 연속으로 동작
  
```java
public abstract class Display { public abstract void draw(); }

/* 기본 도로 표시 클래스 */
public class RoadDisplay extends Display {
  @Override
  public void draw() { System.out.println("기본 도로 표시"); }
}

/* 다양한 추가 기능에 대한 공통 클래스 */
public abstract class DisplayDecorator extends Display {
  private Display decoratedDisplay;
  // '합성(composition) 관계'를 통해 RoadDisplay 객체에 대한 참조
  public DisplayDecorator(Display decoratedDisplay) {
      this.decoratedDisplay = decoratedDisplay;
  }
  @Override
  public void draw() { decoratedDisplay.draw(); }
}

/* 차선 표시를 추가하는 클래스 */
public class LaneDecorator extends DisplayDecorator {
  // 기존 표시 클래스의 설정
  public LaneDecorator(Display decoratedDisplay) { super(decoratedDisplay); }
  @Override
  public void draw() {
      super.draw(); // 설정된 기존 표시 기능을 수행
      drawLane(); // 추가적으로 차선을 표시
  }
  // 차선 표시 기능만 직접 제공
  private void drawLane() { System.out.println("\t차선 표시"); }
}

/* 교통량 표시를 추가하는 클래스 */
public class TrafficDecorator extends DisplayDecorator {
  // 기존 표시 클래스의 설정
  public TrafficDecorator(Display decoratedDisplay) { super(decoratedDisplay); }
  @Override
  public void draw() {
      super.draw(); // 설정된 기존 표시 기능을 수행
      drawTraffic(); // 추가적으로 교통량을 표시
  }
  // 교통량 표시 기능만 직접 제공
  private void drawTraffic() { System.out.println("\t교통량 표시"); }
}

/* 교차로 표시를 추가하는 클래스 */
public class CrossingDecorator extends DisplayDecorator {
  // 기존 표시 클래스의 설정
  public CrossingDecorator(Display decoratedDisplay) { super(decoratedDisplay); }
  @Override
  public void draw() {
      super.draw(); // 설정된 기존 표시 기능을 수행
      drawCrossing(); // 추가적으로 교차로를 표시
     }
  // 교차로 표시 기능만 직접 제공
  private void drawCrossing() { System.out.println("\t교차로 표시"); }
}

public class Client {
  public static void main(String[] args) {
  // 기본 도로 표시 + 차선 표시 + 교통량 표시
	Display roadWithLaneAndTraffic =
      new TrafficDecorator(
      new LaneDecorator(
      new RoadDisplay()));
      
	roadWithLaneAndTraffic.draw();
  
  
  // 기본 도로 표시 + 차선 표시 + 교통량 표시 + 교차로 표시
	Display roadWithLaneAndTrafficAndCross =
      new CrossingDecorator(
      new TrafficDecorator(
      new LaneDecorator(
      new RoadDisplay())));
      
	roadWithLaneAndTrafficAndCross.draw();
  }
}
```
