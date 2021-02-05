### 개요
- 여러 서브클래스로 구성된 시스템을 클라이언트가 간단하게 접근할 수 있는 인터페이스를 제공해주는 패턴
- 반복적인 기능 실행은 퍼사드 내에서 수행하고, 클라이언트는 퍼사드의 메소드만 실행하면 동작하도록 구성


### 필요성 
- 영화를 보면서 음료수를 먹는 예제
- 문제점
  - 어떤 영화를 보고 어떤 음료를 먹던지 계속 같은 패턴 반복
  - 클라이언트는 이 반복되는 패턴을 계속 구현해줘야 함

```java
public class Remote_Control {
    public void Turn_On() { System.out.println("TV를 켜다"); }
    public void Turn_Off() { System.out.println("TV를 끄다"); } 
}

public class Movie {
    private String name="";
    
    public Movie(String name) { this.name = name; }
    
    public void Search_Movie() { System.out.println(name+" 영화를 찾다"); }
    public void Charge_Movie() { System.out.println("영화를 결제하다"); }
    public void play_Movie() { System.out.println("영화 재생"); } 
}

public class Beverage {
    private String name="";
    
    public Beverage(String name) { this.name = name; }
    
    public void Prepare() { System.out.println(name+" 음료 준비 완료 "); }
}


public class Client()
{
    public void main(String[] args) {
        Beverage beverage = new Beverage("콜라");
        Remote_Control remote= new Remote_Control();
        Movie movie = new Movie("어벤져스");

        beverage.Prepare();  //음료 준비
        remote.Turn_On();   //tv를 켜다
        movie.Search_Movie();  //영화를 찾다
        movie.Charge_Movie();  // 영화를 결제하다
        movie.play_Movie();   //영화를 재생하다
    }
}
```

### 구성 방법
- 구조
  - Subsystem
    - 실제 구현이 들어가 있는 퍼사드 외의 나머지 클래스들
    - Subsystem 사이의 관계는 따로 고려
  - Facade
    - Subsystem을 호출하는 패턴을 정리한 클래스
    - Subsystem의 메소드를 조합하여 실제 클라이언트에서 호출할 메소드를 내부에 구현
- 퍼사드를 이용하여 클라이언트 호출을 단순화하는 예제
```java
public class Facade {
    
    private String beverage_Name ="";
    private String Movie_Name="";
    
    public Facade(String beverage,String Movie_Name) {
        this.beverage_Name=beverage_Name;
        this.Movie_Name=Movie_Name;
    }
    
    public void view_Movie() {
        Beverage beverage = new Beverage(beverage_Name);
        Remote_Control remote= new Remote_Control();
        Movie movie = new Movie(Movie_Name);
        
        beverage.Prepare();
        remote.Turn_On();
        movie.Search_Movie();
        movie.Charge_Movie();
        movie.play_Movie();
    }
}


public class Client()
{
    public void main(String[] args) {
        Facade facade = new Facade("콜라","어벤져스");
        facade.view_Movie();
    }
}
```
