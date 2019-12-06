### 타입힌트에 관한내용 정리

#### 타입힌트란?
- 파이썬에서 타입을 미리 지정해줄수 있는 방법
- 3.5부터 일부지원 3.6부터 정식지원
- 실제 해당 타입을 꼭 넣어줄필요는 없다
  - ide, 개발자 편의

#### 사용법
- typing 내 사용할 타입 임포트
  - from typing import *
- 기본 사용법
  - 변수명 : 타입 형태로 사용
  - 함수의 리턴값은 기존 정의 -> 리턴타입 으로 표시
  - 리스트나 배열등은 []를 통해 세부타입 지정
```python
text: str = "hello, world!" 
number: int = 10

def func1(url: str) -> str:
    return "hello, world!"

def func2(url: str) -> None: 
    print("hello, world!")

Vector = List[float]

dictionary = Dict[str, int] 
tupleArr = Tuple[str, int]
```
- 타입 별칭 지정
  - NewType(별칭, 타입) 을 통해 타입의 별칭 지정가능
  - 이후 별칭(값) 형태로 사용
```python
UserId = NewType('UserId', int) 
id = UserId(10)
```

- 특별타입
  - None: 값없음 또는 모든 타입 가능
  - Any: 모든 타입
  - Union[a, b, ...]: 이중 하나
```python
a = None
b = Any 

def foo(bar: Any) -> int: 
    return 1

data = "" def legacy(text: Any) -> Any: 
    return data

def unionFunc(p: Union[int, float]) -> float:
    return p
```

- 타입검사
  - mypy라는 별도의 파이썬 실행 라이브러리를 통해 타입 체크가능
  - pip3 install mypy 로 설치
  - mypy file.py 로 실행
