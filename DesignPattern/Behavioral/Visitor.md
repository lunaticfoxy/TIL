### 개요
- 실제 로직을 가지고 있는 객체 (Visitor) 가 로직을 적용할 객체 (Element)를 방문하면서 로직을 실행
  - Element는 최소한의 로직만 포함
  - 구체적인 비즈니스 로직은 Visitor에 포함
  - Visitor의 메소드에 파라미터로 Element를 전달해서 동작
- 로직과 구조를 분리
  - 구조를 수정하지 않고도 새로운 로직을 추가할 수 있음
  - 구조는 자주 변하지 않는데 로직만 추가되는 경우가 많을때 용이
  - 구조가 변하는 경우 오히려 수정사항이 커질 수 있음
  
  
### 필요성
- 회원 등급별로 혜택을 주는 서비스
- 문제점
  - 새로운 혜택이 추가될 때마다 인터페이스부터 구체적인 구현 내부 모두 변경 필요
  
```java
public interface Member {
    void point();
    void discount();
    void gift();
}

public class GoldMember implements Member {
    public void point() { System.out.println("Point for Gold Member"); }
    public void discount() { System.out.println("Discount for Gold Member"); }
    public void gift() { System.out.println("Gift for Gold Member"); }
}

public class VipMember implements Member {
    public void point() { System.out.println("Point for Vip Member"); }
    public void discount() { System.out.println("Discount for Vip Member"); }
    public void gift() { System.out.println("Gift for VIP Member"); }
}

public class Main {
    public static void main(String[] args) {
        Member goldMember = new GoldMember();
        Member vipMember = new VipMember();

        goldMember.point();
        vipMember.point();
        goldMember.discount();
        vipMember.discount();
        goldMember.gift();
        vipMember.gift();
    }
}
```

### 패턴 적용
- 구조
  - Element
    - 실제 클라이언트가 인식하는 객체를 표현하기 위한 인터페이스
    - 객체가 Visitor와 연결되기 위한 메소드 포함
  - ConcreteElement
    - Element를 상속받아 구현
    - 실제 클라이언트가 인식하는 객체를 생성하는 클래스
    - 최소한의 로직만 포함
  - Visitor
    - Element를 통해 일어나는 로직을 표현하기 위한 인터페이스
    - 객체가 Element와 연결되기 위한 메소드 포함
  - ConcreteVisitor
    - Visiotr를 상속받아 구현
    - Element를 통해 일어나는 구체적인 로직을 담은 클래스
    
- 구현
  - 혜택을 표현하기 위한 Visitor인 Benefit 인터페이스 구현
    - 이를 상속받아 ConcreteVisitor인 DiscountBenefit, PointBenefit, GiftBenefit 구현
    - 각 ConcreteVisitor 마다 멤버 등급별 구체적인 혜택 명시
  - Member 에는 Benefit과 연결하기 위한 getBenefit 메소드만 남김
  - 클라이언트가 호출시 Memeber와 Benefit을 별도로 만듬
    - 특정 Member에게 혜택을 주려 할때는 Member.getBenefit(Benefit) 형태로 

```java
public interface Member {
    void getBenefit(Benefit benefit);
}

public class GoldMember implements Member {
    @Override
    public void getBenefit(Benefit benefit) {
        benefit.getBenefit(this);
    }
}

public class VipMember implements Member {
    @Override
    public void getBenefit(Benefit benefit) {
        benefit.getBenefit(this);
    }
}

public interface Benefit {
    void getBenefit(GoldMember member);
    void getBenefit(VipMember member);
}

public class DiscountBenefit implements Benefit {
    @Override
    public void getBenefit(GoldMember member) {
        System.out.println("Discount for Gold Member");
    }

    @Override
    public void getBenefit(VipMember member) {
        System.out.println("Discount for Vip Member");
    }
}

public class PointBenefit implements Benefit {
    @Override
    public void getBenefit(GoldMember member) {
        System.out.println("Point for Gold Member");
    }

    @Override
    public void getBenefit(VipMember member) {
        System.out.println("Point for Vip Member");
    }
}


public class GiftBenefit implements Benefit {
    @Override
    public void getBenefit(GoldMember member) {
        System.out.println("Gift for Gold Member");
    }

    @Override
    public void getBenefit(VipMember member) {
        System.out.println("Gift for Vip Member");
    }
}

public class Main {
    public static void main(String[] args) {
        Member goldMember = new GoldMember();
        Member vipMember = new VipMember();
        Benefit pointBenefit = new PointBenefit();
        Benefit discountBenefit = new DiscountBenefit();
        Benefit giftBenefit = new GiftBenefit();

        goldMember.getBenefit(pointBenefit);
        vipMember.getBenefit(pointBenefit);
        goldMember.getBenefit(discountBenefit);
        vipMember.getBenefit(discountBenefit);
        goldMember.getBenefit(giftBenefit);
        vipMember.getBenefit(giftBenefit);
    }
}
```
