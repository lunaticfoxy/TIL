
#### 21.1 암시적 변환이란
- 서로 다른 타입을 자동으로 변환
  - 여기서의 타입은 클래스도 포함
  - 서록를 고려하지 않고 구성된 두 소프트웨어를 병합하는데 유리
- 자바의 방식대로 구성하려면 구성해야할 사전 준비가 많음
  - 모든 클래스 재정의 필요
- 스칼라에서는 핵심 정보만 포함하고 동작하게 하고싶음

```scala
implicit def function2ActionListener(f: ActionEvent => Unit) =
   new ActionListener {
       def actionPerformed(event: ActionEvent) = f(event)
   }
// 요걸 작성해놓으면

button.addActionListener(
    (_: ActionEvent) => println("pressed!")
)
// 에서 자동으로 변환됨
```


#### 21.2 암시 규칙
- 암시적 정의: 컴파일러가 타입 오류를 고치기 이해 삽입할 수 있는 정의들
  - ex) x+y에 에러가 있다면 컴파일러가 convert(x)+y 시도
  - 여기서 convert는 사용 가능한 암시적 변환 중 하나

- 컴파일러가 암시적 변화는 처리하는 일반 규칙
  - 1. 표시규칙: implicit 으로 표시한 정의만 검토 대상이다
  - 2. scope 규칙: 삽입된 implicit 변환은 scope 내에서 단일 식별자로만 존재하거나, 반환의 결과나 원래 타입과 연관이 있어야된다
    - 단일식별자 규칙에서 예외: 원 타입 변환이나 반환 결과 타입의 동반 객체에 있는 암시적 정의도 살펴본다
  - 3. 한번에 하나만의 규칙: 오직 하나의 암시적 변환만 사용한다
  - 4. 명시적 우선 규칙: 코드가 그 상태로 타입 검사를 통과한다면 변환을 시도하지 않는다
  - 5. 암시적 변환 이름 붙이기: 명시적으로 유저가 사용할때 필요하다
- 암시가 쓰이는 부분
  - 1. 값을 컴파일러가 원하는 타입으로 변환
  - 2. 어떤 선택의 수신 객체를 변환
  - 3. 암시적 파라미터를 지정


#### 21.3 예상 타입으로의 암시적 변환
- 컴파일러가 Y타입이 필요한 위치에서 X타입을 봤다면 X를 Y로 변환하는 암시적 함수를 찾는다.
- 이때 intToDouble은 문제가 없지만, doubleToInt 처럼 정보가 손실되는 암시적 타입 변환은 사용하지 않는게 좋음


#### 21.4 호출 대상 객체 변환
- 메소드를 호출하는 대상이 되는 객체인 수신 객체에도 적용할 수 있음
- 용도
  - 1. 수신 객체 변환을 통해 새 클래스를 기존 클래스 계층 구조에 매끄럽게 통합 가능
    - ex) Int + Rational 은 에러가 나지만 IntToRational 을 만들어두면 자동으로 Rational + Rational로 면환 발생
  - 2. 언어 안에서 도메인 특화언어를 만드는 일을 지원
    - ex) 실제 Map(1 -> (1,2,3)) 형태의 -> 도 암시적 변환으로 구성된것
- 암시적 클래스
  - implicit 이 class 앞에 있는 클래스
  - 컴파일러가 클래스 생성자를 이용해서 암시적 클래스로 가는 암시적 변환을 만들어냄
```scala
case class Rectangle(width: Int, height: Int)

implicit class RectangleMaker(width: Int) {
    def x(height: Int) = Rectangle(width, height)
}

// 요렇게 해놓으면

val a = 3x4 // a에 Rectangle(3,4) 가 저장된다
```
    
    
    
    
    
    
    
