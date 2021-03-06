# Dagger2 와 관련된 자료를 정리하는 스레드

## 개요
- Dagger란?



## 구성 요소 및 액션

### Component
- 의존성 주입을 수행하는 객체
- 의존성 그래프를 관리하는 역할

### Module
- 의존성 주입을 위한 객체 명세
- Binds 작업 내용 명시

### Binds
- 의존성 주입시 객체간 상속 관계 등을 표시하기 위한 방법
- 의존성을 주입할 명시된 클래스가 있다면 불필요
- 명시된 클래스가 없을때는 필요
  - ex) interface에 의존성을 주입할 필요가 있을 경우 해당 interface를 어떤 클래스로 넣을것인가
  
### Scope
- 한 컴포넌트에서 생성된 객체가 언제까지 유지될지 지정하는 범위
- 미지정시
  - 매번 새로운 객체 생성
- 지정시
  - 컴포넌트와 클래스에 각각 지정
  - 컴포넌트에 Scope가 지정될 경우 해당 컴포넌트에서 생성한 객체중 동일한 Scope가 지정된 객체는 해당 컴포넌트와 동일한 생명주기를 지님
- Scope 지정 방법
  - 기본으로 Singleton 존재
  - annotaion class 에 @Scope annotation을 붙여 생성 가능
