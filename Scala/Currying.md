
개념: 함수 구현시 모든 인자를 입력하지 않아도 부분 함수를 생성하는 방법

코드
- 정의 : def fName(param1:type)(param2:type)(param3:type):returnType = {}
- 사용
-- val tempA = fName(A)
-- val tempAB = tempA(B)
-- val resABC = tempAB(C)

용도
- 파라미터 반복 사용을 피해서 코드를 간결하게 구성
- 타 함수로 인자 전달시 파라미터를 제외하고 이미 구성된 부분함수만 전달 가능

유의할 점
- 메소드에 커링을 구성할 경우 호출시 맨 뒤에 _ 를 붙여 인자가 생략되었음을 알려야함
- 함수에 커링을 구성할 경우 _ 를 붙이지 않아도 알아서 판단
- 근데 메소드로 커링을 수행하면 리턴되는 부분 함수는 "함수" 이므로 이후에는 _를 붙이지 않아도 됨
- 근데x2 스칼라에서 최초 코드 구성시 "함수"는 거의 존재하지 않으므로... 코드가 일관적이지 않을수밖에 없음...

샘플코드
- https://github.com/lunaticfoxy/TIL/blob/master/Scala/Curryng.scala
