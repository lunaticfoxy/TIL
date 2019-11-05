## python의 eval 과 관련한 내용 정리

#### eval
- expression 인자에 string 넣을 경우 해당 값 바로 출력
  - 단순 연산
  - 함수나 객체도 실행 가능
```python
eval("(5*10)/2") // 25 리턴
eval("max([1,2,3,4])") // 4 리턴
```
- 인터프리터 언어라서 가능한 형태
- 위험성
  - 코드 injection 가능
```python
x = str(input(">> input some text for mathematical expression : ")
print eval(x)

# __import__('os').system('ls /') 입력시 루트 폴더의 내용 출력
# __import__('os').system('rm -rf /') 입력시는...
```
    - 최대한 사용하지 말자...
  - 가독성도 떨어짐

#### literal_eval
- 기본 함수는 아니지만 ast 안에 정의되어 있음
- eval 함수의 래퍼 형태
- 기본 자료형 정도에 대한 연산만 지원
```python
import ast

str_dict = "{'a': 3, 'b': 5}"

print(type(str_dict))           # <type 'str'>

convert_dict = ast.literal_eval(str_dict)

print(type(convert_dict))   # <type 'dict'>
print(convert_dict['a'])    #  3
print(convert_dict['b'])    #  5

print(ast.literal_eval('__import__("os").system("ls /")'))      # ValueError: malformed string 에러 발생
print(ast.literal_eval("10 * 2"))                               # ValueError: malformed string 에러 발생
```
- 구지 관련 기능을 쓸 필요가 있다면 eval 대신 literal_eval을 사용하자
