### Vue 인스턴스

#### Vue 인스턴스 만들기
- 모든 Vue 앱은 Vue 함수로 새 Vue 인스턴스를 만드는 것부터 시작

```javascript
var vm = new Vue({
  // 옵션
})
```
- 엄격히 MVVM 패턴과 관련은 없으나 Vue의 디자인은 부분적으로 영감을 받음
  - Vue 인스턴스를 참조하기 위해 종종 변수 vm(ViewModel의 약자)을 사용
- Vue 인스턴스를 인스턴스화 할 때는 options 객체를 전달
  - 데이터, 템플릿, 마운트할 엘리먼트, 메소드, 라이프사이클 콜백 등의 옵션을 포함
- Vue 생성자는 재사용 가능한 컴포넌트 생성자를 생성하도록 확장 될 수 있음
- Vue 앱은 new Vue를 통해 만들어진 루트 Vue 인스턴스로 구성
  - 선택적으로 중첩이 가능
  - 재사용 가능한 컴포넌트 트리로 구성
    - ex) Todo 앱의 컴포넌트 트리    
Root Instance
└─ TodoList
   ├─ TodoItem
   │  ├─ DeleteTodoButton
   │  └─ EditTodoButton
   └─ TodoListFooter
      ├─ ClearTodosButton
      └─ TodoListStatistics

- 확장된 인스턴스 생성 가능
  - 하지만 대개 템플릿에서 사용자 지정 엘리먼트로 선언적으로 작성
  - 모든 Vue 컴포넌트는 본질적으로 확장된 Vue 인스턴스


#### 속성과 메소드
- 각 Vue 인스턴스는 data 객체에 있는 모든 속성을 프록시 처리

```javascript
// 데이터 객체
var data = { a: 1 }

// Vue인스턴스에 데이터 객체를 추가합니다.
var vm = new Vue({
  data: data
})

// 같은 객체를 참조합니다!
vm.a === data.a // => true

// 속성 설정은 원본 데이터에도 영향을 미칩니다.
vm.a = 2
data.a // => 2

// ... 당연하게도
data.a = 3
vm.a // => 3
```
- 데이터가 변경되면 화면은 다시 렌더링
  - 유념할 점: data에 있는 속성들은 인스턴스가 생성될 때 존재한 것들만 반응형
  - 다음과 같이 새 속성을 추가시 b가 변경되어도 화면 갱신되지 않음
  - 어떤 속성이 나중에 필요하다는 것을 알고 있으며, 빈 값이거나 존재하지 않은 상태로 시작한다면 초기값을 지정할 필요가 있음
```javascript
vm.b = 'hi'  // 갱신 일어나지 않음

data: {
  newTodoText: '',
  visitCount: 0,
  hideCompletedTodos: false,
  todos: [],
  error: null
}
```
- 유일한 예외: Object.freeze () 사용하는 경우
  - 기존 속성이 변경되는 것을 막아 반응성 시스템이 추적할 수 없다는 것을 의미
``` javascript
var obj = {
  foo: 'bar'
}

Object.freeze(obj)

new Vue({
  el: '#app',
  data: obj
})
<div id="app">
  <p>{{ foo }}</p>
  <!-- obj.foo는 더이상 변하지 않습니다! -->
  <button v-on:click="foo = 'baz'">Change it</button>
</div>
```
- Vue 인스턴스는 데이터 속성 이외에도 인스턴스 속성 및 메소드를 제공
  - 다른 사용자 정의 속성과 구분하기 위해 $ 접두어 사용

```javascript
var data = { a: 1 }
var vm = new Vue({
  el: '#example',
  data: data
})

vm.$data === data // => true
vm.$el === document.getElementById('example') // => true

// $watch 는 인스턴스 메소드 입니다.
vm.$watch('a', function (newVal, oldVal) {
  // `vm.a`가 변경되면 호출 됩니다.
})
```
