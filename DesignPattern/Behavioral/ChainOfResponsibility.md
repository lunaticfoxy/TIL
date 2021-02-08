### 개요
- 특정 작업을 여러 객체가 연쇄적으로 처리 기회를 가지는 패턴
- 한 객체가 작업을 처리하려 시도
  - 성공시 해당 작업 결과를 리턴
  - 실패시 다음 객체에게 처리 기회를 넘김
- 장점
  - 요청의 발생자와 수신자 구분이 명확
  - 클라이언트는 처리 객체의 내부를 알 필요 없음
  - 처리 순서 변경이나 추가 및 삭제 용이
  - 새로운 요청이 추가될때 처리 편리
- 단점
  - 디버깅이 어려움
  - 내부에서 사이클 발생 가능
- 대표적인 예시: java의 try - catch 구문
```java
try {
  ...
} catch (IllegalArgumentException e) {
  someCode();
} catch (SecurityException e) {
  someCode();
} catch (IllegalAccessException e) {
  someCode();
} catch (NoSuchFieldException e) {
  someCode();
} finally {
  ...
}
```


### 구현
- 구조
  - Sender
    - 작업을 발생시키는 객체
    - 내부에 책임 연쇄가 시작될 Handler를 포함하고 있음
  - Handler
    - 작업을 처리하기 위한 내용을 담은 인터페이스
    - 작업 처리를 위한 메소드, 자기 다음 객체를 지정할 메소드를 포함
  - ConcreteHandler
    - Handler를 상속받는 클래스
    - 실제 작업을 처리하는 로직 포함
    - 자신이 작업을 처리하지 못하면 다음 객체에게 전달
- 예시: 동전을 거슬러주는 프로그램
  - 100원 -> 10원 -> 1원 단위로 거슬러줌
```java
interface DispenseChain{
    void setNextChain(DispenseChain nextChain);
    void dispense(Currency cur);
}

class Currency{
    private int amount;
    
    public Currency(int amt) {
        this.amount=amt;
    }
    
    public int getAmount() {
        return this.amount;
    }
}

class Won100Dispenser implements DispenseChain{
    private DispenseChain chain;
    
    @Override
    public void setNextChain(DispenseChain nextChain) {
        this.chain=nextChain;
    }
    
    @Override
    public void dispense(Currency cur) {
        if(cur.getAmount()>=100){
            int num=cur.getAmount()/100;
            int remainder=cur.getAmount()%100;
            
            System.out.println("Dispensing " +num+" 100₩ note");
            
            if(remainder!=0) this.chain.dispense(new Currency(remainder));    
        }
        else this.chain.dispense(cur);
    }
}

class Won10Dispenser implements DispenseChain{
private DispenseChain chain;
    
    @Override
    public void setNextChain(DispenseChain nextChain) {
        this.chain=nextChain;
    }
    
    @Override
    public void dispense(Currency cur) {
        if(cur.getAmount()>=10){
            int num=cur.getAmount()/10;
            int remainder=cur.getAmount()%10;
            
            System.out.println("Dispensing " +num+" 10₩ note");
            
            if(remainder!=0) this.chain.dispense(new Currency(remainder));    
        }
        else this.chain.dispense(cur);
    }
}
 
class Won1Dispenser implements DispenseChain{
private DispenseChain chain;
    
    @Override
    public void setNextChain(DispenseChain nextChain) {
        this.chain=nextChain;
    }
    
    @Override
    public void dispense(Currency cur) {
        int num=cur.getAmount()/1;
        System.out.println("Dispensing " +num+" 1₩ note");
    }
}

public class ChainOfResponsibilityPattern {
    private DispenseChain c1;
    
    public ChainOfResponsibilityPattern(){
        this.c1=new Won100Dispenser();
        DispenseChain c2=new Won10Dispenser();
        DispenseChain c3=new Won1Dispenser();
        
        c1.setNextChain(c2);
        c2.setNextChain(c3);
    }
    
    public static void main(String[] args) {
        ChainOfResponsibilityPattern atmDispenser = new ChainOfResponsibilityPattern();
        atmDispenser.c1.dispense(new Currency(378));
    }
}
```

