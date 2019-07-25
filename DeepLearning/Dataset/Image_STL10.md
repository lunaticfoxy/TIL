### STL10 데이터셋에 대한 정리

#### 개요
- 주소: https://cs.stanford.edu/~acoates/stl10/
- 타입: 이미지
- 클래스
  - 수: 10개
  - 종류: airplane, bird, car, cat, deer, dog, horse, monkey, ship, truck
- 데이터 수
  - labeled: 1,300
    - 500 for train
    - 800 for test
  - unlabeled: 100,000
- 데이터 형태
  - 사이즈: 96x96
  - 컬러


#### 특징
- Unlabeled 데이터가 많음
  - 해당 문제에 특화
- Unsupervised learning, Self-taught learning에 주로 사용하기 위해 제작
- Cifar-10 에서 영감을 얻어서 비슷한 형태로 구성


#### 저장 형태
- 매틀랩 파일: 2.7GB
- 바이너리 파일: 2.5GB (데이터를 읽기 위한 Python code 동봉)
