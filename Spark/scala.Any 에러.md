### Class Not Found scala.Any 에러에 대한 해결 방법 모음

#### 발생원인
- 스파크는 데이터를 Serialize 해서 사용한다
- 이때 너무 범위를 크게 잡을 경우 공통되는 타입이 Any 밖에 없을 수 있다
  - 대부분 null 값 처리시에 나타남
- 그리고 Any는 Serialize 하기에는 너무 범용적인 값이라 에러가 난다

#### 해결방법
- 모든 null을 없앤다
  - Boolean은 False, String은 "", Integer는 -1 등
  - 혹은 임의의 값을 지정해주고 마지막 순간에 따로 처리해준다
