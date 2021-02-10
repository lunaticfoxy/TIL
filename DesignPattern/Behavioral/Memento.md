### 개요
- 객체의 상태를 저장했두고 이후 필요할때 해당 상태로 되돌리는 패턴
- 특정 시점의 상태로 롤백이 필요할 경우 주로 사용
  - 뒤로가기, 실행취소, 게임의 세이브 등


### 패턴 적용
- 구성
  - Originator
    - 실제 클라이언트에서 사용되는 클래스
    - 필수 포함 요소
      - Memento saveStateToMemento() : 현재 상태를 Memento 에 저장하기 위한 메소드
      - void getStateToMemento(Memento memento) : Memento 로부터 정보를 가져와 상태를 복구하는 메소드
  - Memento
    - 복구할 정보를 저장하는 클래스
    - Originator에서 저장 & 복구가 필요한 상태 정보를 저장
    - 특수 목적이 아닌 이상 생성자 이외의 set 메소드는 필요 없음
  - CareTaker
    - Memento를 관리하는 클래스
    - Originator가 상태 저장을 위해 Memento를 생성할때 이를 넘겨받아 관리하는 역할 수행
    - 비즈니스 로직에 따라 Originator에게 적절한 Memento 전달
      - 실행 취소의 경우 가장 최근 Memento
      - 특정 시점의 값으로 복구하고자 할때는 해당 시점보다 빠른 시점중 마지막에 저장된 Memento

- 실제 구현
  - Information 클래스에 데이터를 저장하고, 복구시 저장된 가장 마지막 시점으로 되돌리는 패턴

```java
import java.util.List;
import java.util.ArrayList;

public class Information {
    private String Data1;
    private int Data2;
    
    public Information(String Data1, int Data2) {
        this.Data1 = Data1;
        this.Data2 = Data2;
    }
    
    public Memento saveStateToMemento() {
        return new Memento(this.Data1,this. Data2);
    }
    
    public void getStateToMemento(Memento memento) {
        this.Data1 = memento.getData1();
        this.Data2 = memento.getData2(); 
    }
    
    public void setData1(String Data1) { this.Data1 = Data1; }
    public void setData2(int Data2) { this.Data2 = Data2; }
    
    public String getData1() { return this.Data1; }
    public int getData2() { return this.Data2; }
}
 

public class Memento {
    private String Data1;
    private int Data2;
    
    public Memento(String Data1,int Data2) {
        this.Data1 = Data1;
        this.Data2 = Data2;
    }
    
    public String getData1() { return this.Data1; }
    public int getData2() { return this.Data2; }
}


public class CareTaker {
    Stack<Memento> mementos = new Stack<>();    //Memento 관리를 위한 Stack
    
    public void push(Memento memento) {
        mementos.push(memento);
    }
    
    public Memento pop() {
        return mementos.pop();
    }
}


public class Client {
    public static void main(String[] args)
    {
        Information info  = new Information("Data1",10);
        CareTaker caretaker = new CareTaker();
        
        //현재 Information의 상태 정보를 가지는 Memento를 생성하여 CareTaker에 추가
        caretaker.push(info.CreateMemento());
        
        //Information 정보를 수정                                                
        info.setData1("Data2");
        info.setData1(20);
        
        //현재 Information의 상태정보를 출력
        System.out.println("현재 Data1 : " + info.getData1());
        System.out.println("현재 Data2 : " + info.getData2());
        
        //가장 최근에 생성 된 Memento를 가지고와서 상태 정보를 복원
        info.RestorMemento(caretaker.pop());
        
        //상태 정보를 복원 한 후에 Information의 상태 정보를 출력
        System.out.println("복구된 Data1 : " + info.getData1());
        System.out.println("복구된 Data2 : " + info.getData2());
    }
}

```
