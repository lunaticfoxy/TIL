### 개요
- 클라이언트가 주체에게 직접 요청을 보내지 않고 프록시 클래스를 통해 요청하고 응답을 처리하는 형태
- 주체는 클라이언트의 요청과 무관하게 메인 로직에만 신경 쓸 수 있음
- 프록시가 사용되는 대표적인 경우
  - Virtual Proxy
    - 주체가 리소스 집약적인 경우 (큰 리소스를 가지고 있는 경우)
    - 매번 리소스를 일일히 체크하지 않고 프록시에서 전처리나 캐싱등을 통해 리소스 최적화
    - 꼭 필요한 경우에만 주체에게 요청
  - Protection Proxy
    - 주체에 대한 접근을 제어하는 경우
    - 클라이언트의 접근 권한에 따라 주체의 메소드 접근 가능 여부 체크
  - Remote Proxy
    - 프록시는 로컬에 두고 주체 클래스는 Remote로 존재하는 경우
    - 구글 독스처럼 전체 자원은 서버에 저장이 되고 당장 필요한 자원만 로컬로 가져와서 처리하는 형태의 동작
    
    
### 패턴 적용
- 구성
  - Subject
    - Proxy와 RealSubject의 부모 인터페이스
    - 클라이언트가 직접 인터렉션 하는 단위
  - RealSubject
    - 실제 비즈니스 로직이 들어가는 클래스
    - Subject를 상속받아 동일한 메소드 지님
  - Proxy
    - 사용자가 메소드 호출시 실제 실행되는 메소드를 담은 클래스
    - Proxy에서 입력을 처리한 후 RealSubject의 접근이 필요한 경우에만 접근하는 매개체 역할
- 예시
  - 창고에서 물건을 쌓고 정리하는 예제
  - Warehouse에는 비즈니스 로직만 포함
  - 여러개의 창고 관리 및 창고 내 물건 존재 체크등의 전처리는 OrderFulfilment 프록시에서 동작
  
```java
public interface IOrder {
    boolean fulfillOrder(Order order);
}

public class Warehouse implements IOrder {
    private Hashtable<Integer, Integer> stock;
    private String address;

    @Override
    public void fulfillOrder(Order order) {
        for (Item item: order.getItemList()) {
            Integer sku = item.getSku();
            this.stock.replace(sku, stock.get(sku) - 1);
            
            /* 포장, 배송 등 기타 작업들이 추가적으로 이루어질 수 있음 */
            
            processOne();
            processTwo();
            processThree();
            
        }
    }

    public int currentInventory(Item item) {
        return stock.getOrDefault(stock.get(item.getSku()), 0);
    }
}

public class OrderFulfillment implements IOrder {
    private List<Warehouse> warehouses = new LinkedList<Warehouse>();
    
    public void addWarehouse(Warehouse warehouse) { 
      warehouses.add(warehouse);
    }

    @Override
    public void fulfillOrder(Order order) {
        for (Item item: order.getItemList()) {
            for (Warehouse warehouse: warehouses) {
                if (warehouse.currentInventory(item) != 0) {
                    warehouse.fulfillOrder();
                }
            }
        }
    }
}

public class Client {
  public static void main(String[] args) {
    Warehouse warehouse1 = new Warehouse();
    Warehouse warehouse2 = new Warehouse();
  
    OrderFulfillment orderfulfilment = new OrderFulfillment();
    
    orderfulfilment.addWarehouse(warehouse1);
    orderfulfilment.addWarehouse(warehouse2);
    
    orderfulfilment.fulfillOrder(new NameOrder());
  
  }
}


```
