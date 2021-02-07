### 개요
- 순간적으로 생성되었다가 사라지는 형태가 반복되는 인스턴스를 공유하여 사용하는 패턴
- new로 일어나는 메모리 낭비 최소화

### 필요성
- 여러 색상을 지닌 원형 도형의 속성을 출력하는 예제
- 문제점
  - 매 출력때마다 Circle이 새로 new로 만들어졌다가 사라져서 메모리 낭비 발생
  - gc가 돌때까지 메모리 낭비 지속
  
```java
public interface Shape {
  public void draw();
}

publci class Circle implements Shape {
  private String color;
  private int x;
  private int y;
  private int radius;
  
  public Circle(String color) {
    this.color = color
  }
  
  public void setColor(String color) {
    this.color = color
  }
  
  public void setX(int x) {
    this.x = x
  }
  
  public void setY(int y) {
    this.y = y
  }
  
  public void setRadius(int radius) {
    this.radius = radius
  }
  
  @Override
  public void draw() {
    System.out.println("Cicle [color=" + color + ", x=" + x + ", y=" + y + ", radius=" + radius + "]")
  }
}

public class Client {
  public static void main(String[] args) {
    String[] colors = {"Red", "Green", "Blue", "Yello"}
    
    for(int i=0; i<10; ++i) {
      Circle circle = new Circle(colors[(int)(Math.random()*4)]);
      circle.setX((int) (Math.random()*100));
      circle.setY((int) (Math.random()*4));
      circle.setRadius((int) (Math.random()*10));
      circle.draw();
    }
  }
}
```

### 패턴 적용
- 구조
  - Flyweight
    - 공유할 객체들이 참조할 인터페이스
  - ConcreteFlyWeight
    - 실제 공유가 일어날 객체를 정의하는 클래스
  - FlyweightFactory
    - Flyweight의 인터페이스를 생성 혹은 공유
    
- 적용 방법
  - ShapeFactory 클래스를 만들어 내부에 한번 생성된 객체를 저장하고 있음
  - 이후 객체 생성 요청을 팩토리 함수로 요청하면 팩토리 내에서 재사용 가능할 경우 재사용

```java
public interface Shape {
  public void draw();
}

publci class Circle implements Shape {
  private String color;
  private int x;
  private int y;
  private int radius;
  
  public Circle(String color) {
    this.color = color
  }
  
  public void setColor(String color) {
    this.color = color
  }
  
  public void setX(int x) {
    this.x = x
  }
  
  public void setY(int y) {
    this.y = y
  }
  
  public void setRadius(int radius) {
    this.radius = radius
  }
  
  @Override
  public void draw() {
    System.out.println("Cicle [color=" + color + ", x=" + x + ", y=" + y + ", radius=" + radius + "]")
  }
}

public class ShapeFactory {
  private static final HashMap<String, Circle> circleMap = new HashMap<>();
  
  public static Shape getCircle(String color) {
    Circle circle = (Circle)circleMap.get(color);
    
    if(circle == null {
      circle = new Circle(color);
      circleMap.put(color, circle);
      System.out.println("==== 새로운 객체 생성 : " + color + "색 원 ====");
    }
    
    return circle;
  }
}

public class Client {
  public static void main(String[] args) {
    String[] colors = {"Red", "Green", "Blue", "Yello"}
    
    for(int i=0; i<10; ++i) {
      Circle circle = (Circle)ShapeFactory.getCircle(colors[(int) (Math.random()*4)]);
      circle.setX((int) (Math.random()*100));
      circle.setY((int) (Math.random()*4));
      circle.setRadius((int) (Math.random()*10));
      circle.draw();
    }
  }
}
```
