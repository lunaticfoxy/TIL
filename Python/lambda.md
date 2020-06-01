### 파이썬에서의 람다 함수

#### 사용법
- lambda param1, param2, ..., param n: expression
- 예시
```python
lambda x, y: x + y
```

#### 관련 함수
- map
  - iterable 원소를 하나씩 순회하면서 연산하여 리턴
  - iterable 여러개의 상호 연산에도 사용 가능
  - map(function, iterable1, iterable2, ...)
  - 예시
```python
a = [1,2,3,4]
b = [17,12,11,10]
list(map(lambda x, y:x+y, a,b))
# [18, 14, 14, 14]
```
- filter
  - iterable 원소를 하나씩 순회하면서 연산하여 True인 값만 모아서 리턴
  - map(function, iterable)
  - 예시
```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
list( filter(lambda x: x % 3 == 0, foo) )
# [18, 9, 24, 12, 27]
```
