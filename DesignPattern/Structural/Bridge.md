### 개요
- 구현부와 추상층을 분리하여 독립적으로 변형 및 확장이 용이하게 구성하는 패턴
- 기능과 구현면에서 두 개의 클래스를 별도로 생성
  - 기능 추가, 세부 구현 변경을 각각 별개의 클래스에서 적용 가능

### 적용
- 구성
  - Abstraction
    - 가장 베이스가 되는 추상 클래스
    - Implementor 객체를 멤버 변수로 가지고 있음
      - 이를 통해 구현부에 연결
    - 이외 기본 기능들에 대한 함수 원형 포함
  - RefindAbstraction
    - Abstration을 상속받은 클래스
    - Implementor의 기능을 조합하여 기능 구현
  - Implementor
    - 기능 구현을 위한 추상 클래스 (혹은 인터페이스)
    - 구현이 필요한 부분을 멤버변수로 포함
      - 해당 멤버변수들은 기능부에서 참조 가능
  - ConcreteImplementor
    - Implementor를 상속받아 구현하는 클래스
    - 실제 세부 로직이 구현되는 부분

- 예시: 화면에 다양한 방법으로 출력값을 찍는 예제
```java
// 기능 클래스 계층
public class Display {
	
	// impl 필드는 Display 구현을 나타내는 인스턴스 입니다. 
	// 이 필드가 두 클래스 계층의 '다리'가 됩니다.
	private DisplayImpl impl; 

	public Display(DisplayImpl impl) {
		this.impl = impl;
	}
	
	public void open(){
		impl.rawOpen();
	}
	
	public void print(){
		impl.rawPrint();
	}
	
	public void close(){
		impl.rawClose();
	}
	
	public final void display(){
		open();
		print();
		close();
	}

}

// 기능 클래스 계층
public class CountDisplay extends Display {

	public CountDisplay(DisplayImpl impl) {
		super(impl);
	}

	public void multiDisplay(int times){
		open();
		for(int i = 0; i< times; i++){   	// times회 반복해서 표시한다
			print();
		}
		close();
	}

}

// 구현 클래스 계층
public abstract class DisplayImpl {
	public abstract void rawOpen();
	public abstract void rawPrint();
	public abstract void rawClose();
}

// 구현 클래스 계층
public class StringDisplayImpl extends DisplayImpl {
	
	private String string;			   // 표시해야 할 문자열
	private int width;				   // 바이트 단위로 계산할 문자열의 '길이'
	

	public StringDisplayImpl(String string) {		// 생성자에서 전달된 문자열 string을
		this.string = string;						// 필드에 기억해둔다.
		this.width = string.getBytes().length; 	    // 그리고 바이트 단위의 길이도 필드에 기억해두고 나중에 사용한다.
	}

	@Override
	public void rawOpen() {
		printLine();
	}

	@Override
	public void rawPrint() {
		System.out.println("|" + string + "|");    // 앞뒤에 "|" 를 붙여서 표시한다.
	}

	@Override
	public void rawClose() {
		printLine();

	}
	
	private void printLine() {
		System.out.print("+");		           // 테두리의 모서리를 표현하는 "+" 마크를 표시한다.
		for (int i = 0; i < width; i++) {	   // width개의 "-"를 표시해서
			System.out.print("-");			   // 테두리 선으로 이용한다.
		}
		System.out.println("+");	           // 테두리 모서리를 표시하는 "+" 마크를 표시한다.
	}

}

public class Main {
	public static void main(String[] args) {
		
		Display d1 = new Display(new StringDisplayImpl("Hello, Korea!"));
		Display d2 = new CountDisplay(new StringDisplayImpl("Hello, World!"));
		
		CountDisplay d3 = new CountDisplay(new StringDisplayImpl("Hello, Universe!"));
		
		d1.display();
		d2.display();
		d3.display();
		
		d3.multiDisplay(5);
	}
}
```

