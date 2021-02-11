### 개요
- 객체를 생성할 때 매번 파라미터를 지정해주지 않고 프로토타입을 만들어두고 여기에서 카피해오는 방법
- 필요한 경우
  - 동일한 상태값을 지니는 객체를 만들 일이 자주 있을때 용이
  - 객체의 생성에 드는 오버헤드가 객체의 카피에 드는 오버헤드보다 클 때 용이
    - ex) DB에서 데이터를 가져와야 하는 경우
- Java에서는 Clonable 인터페이스를 통해 쉽게 구현 가능
  - 단 내부의 Object clone() 메소드가 protected 로 지정되어 있으므로 외부에서 호출하려면 public 으로 재정의 필요
  - 재정의시 throws CloneNotSupportedException 을 붙여줘서 클론이 가능한 객체인지 체크 필요
    - Cloneable하지 않은 객체에서 타 객체의
    
### 필요성
- 직원들의 리스트를 디비에서 가져와서 관리하는 예제
- 문제점
  - 객체가 생성될때마다 DB와의 연결 (예제에서는 loadData 메소드) 이 필요
  - 오버헤드 발생

```java
public class Employees {
    private String manager;
    private List<String> empList;
	
    public Employees(){
        this.manager = manager;
        empList = new ArrayList<String>();
    }
	
    public Employees(List<String> list){
        this.empList=list;
    }
    
    public void loadData(){
        //read all employees from database and put into the list
        empList.add("Pankaj");
        empList.add("Raj");
        empList.add("David");
        empList.add("Lisa");
    }
	
    public List<String> getEmpList() {
        return empList;
    }
    
    public String getManager() {
        return manager;
    }
	
    public void setEmpList(ArrayList<String> empList) {
        this.empList = empList;
    }
}

public class Client {
 
    public static void main(String[] args) {
        Employees emps = new Employees("me");
        emps.loadData();
        
        Employees empsNew = new Employees("me");
        emps.loadData();
        
        Employees empsNew1 = new Employees("me");
        emps.loadData();
        
        List<String> list = empsNew.getEmpList();
        list.add("John");
        
        List<String> list1 = empsNew1.getEmpList();
        list1.remove("Pankaj");
		
        System.out.println("emps Manager: " + emps.getManager());
        System.out.println("emps List: " + emps.getEmpList());
        System.out.println("empsNew Manager: " + empsNew.getManager());
        System.out.println("empsNew List: " + list);
        System.out.println("empsNew1 Manager: " + empsNew1.getManager());
        System.out.println("empsNew1 List: " + list1);
    }
 
}
```


### 패턴 적용
- Employees를 Cloneable를 상속받도록 구성
  - 내부에 clone 함수를 재정의하여 현재 겍체를 그대로 복제하고 ArrayList 내용도 카피
  - ArrayList 는 기본적으로 주소만 카피되므로 별도 처리 없이는 기존이랑 같은 ArrayList를 가리킴
    - 이를 위해 직접 ArrayList를 카피해서 넣음
    - 또는 ArrayList 내에 사전 정의 된 clone 함수를 통해 새로운 객체에 카피할 수 도 있음
      - 이는 ArrayList에만 특이한 케이스, List 에는 없음
- 클라이언트에서 동일한 상태를 가지는 새로운 Employees 객체의 생성이 필요할 경우 clone 함수를 호출해서 활용

```java
public class Employees implements Cloneable{
    private String manager;
    private List<String> empList;
	
    public Employees(manager){
        this.manager = manager;
        empList = new ArrayList<String>();
    }
	
    public Employees(List<String> list){
        this.empList=list;
    }
    
    public void loadData(){
        //read all employees from database and put into the list
        empList.add("Pankaj");
        empList.add("Raj");
        empList.add("David");
        empList.add("Lisa");
    }
	
    public List<String> getEmpList() {
        return empList;
    }
	
    public void setEmpList(ArrayList<String> empList) {
        this.empList = empList;
    }
	
    @Override
    public Object clone() throws CloneNotSupportedException{
        Employees newEmployees = (Employees)super.clone();
        
        ArrayList<String> newEmpList = new ArrayList<String>(); 
        
        for(String s : empList){
            newEmpList.add(s);
        }
        
        newEmployees.setEmpList(newEmpList);
        
        // or 
        // newEmployees.setEmpList(empList.clone());
        
        return newEmployees;
    }
	
}

public class Client {
 
    public static void main(String[] args) throws CloneNotSupportedException {
        Employees emps = new Employees("me");
        emps.loadData();
		
        //Use the clone method to get the Employee object
        Employees empsNew = (Employees) emps.clone();
        Employees empsNew1 = (Employees) emps.clone();
        
        List<String> list = empsNew.getEmpList();
        list.add("John");
        
        List<String> list1 = empsNew1.getEmpList();
        list1.remove("Pankaj");
		
        System.out.println("emps Manager: " + emps.getManager());
        System.out.println("emps List: " + emps.getEmpList());
        System.out.println("empsNew Manager: " + empsNew.getManager());
        System.out.println("empsNew List: " + list);
        System.out.println("empsNew1 Manager: " + empsNew1.getManager());
        System.out.println("empsNew1 List: " + list1);
    }
 
}
```
