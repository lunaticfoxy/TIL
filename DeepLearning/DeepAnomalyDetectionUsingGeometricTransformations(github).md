#### 논문 제목: Deep Anomaly Detection Using Geometric Transformations

#### 깃헙 주소: https://github.com/izikgo/AnomalyDetectionTransformations

#### 논문 주소: https://arxiv.org/abs/1805.10917

##### 공식 깃헙 설명이 너무 부실해서 직접 정리

##### 폴더 구조
- experiments.py: 가장 기본 실험 - 클래스를 1개 주고 해당 클래스 여부를 yes, no로 평가
- institution_experiments.py: 1개 클래스를 주고, 타 1개 클래스를 anomaly로 구성하여 평가
- multiclass_experimment.py: multi-class 분류 방법 실험 (cifar10, tinyimagenet)
- transformations.py: 이미지 변환을 위한 함수들 저장
- utils.py
- models: 실험-대조군을 위한 모델 저장
  - adgan.py : Anomaly Detection with a Generative Adversarial Network
  - dagmm.py : Deep Autoencoding Gaussian Mixture Model
  - dsebm.py : Deep structured energy-based models
  - encoders_decoders.py : dsebm, dagmm 의 encoder, decoder 기본 구조 정의
  - wide_residual_networks.py : 논문에서 제안하는 모델이 사용하는 코드 - 1개 conv + 3개 * (1개 (conv+residual) + n개 conv) + dense
  
##### 평가 방법
- single class를 학습하는 모델을 만든다
  - class별로 돌아가면서 모델 구성
  - 각 모델별로 데이터가 해당 클래스인지 여부를 yes, no로 학습
- 어떤 single class에도 속하지 않는 값을 anomaly로 탐지 (? => 예상)

##### experiments.py
- 모델별로 돌아가면서 cifar10, cifar100, fashion-mnist, cats-vs-dogs 에 대해 분류 수행
- multiclass_experiments의 비교 버전
- 단 코드 현재 미동작 (데이터 미존재)

##### institution_experiments.py
- 하나의 클래스를 transform 할때마다 다른 class로 만들어서 학습시키고
- 탐지시에는 각 클래스별로 출력된 확률을 평균내서 스코어 계산
  - 각 이미지마다 8개의 클래스 생성
    - 4방향 회전
    - 대칭 이동 후 4방향 회전
- 스코어의 평균은 normal 일 경우 1에 가깝게, abnormal일경우 0에 가깝게 나타남
  - 이를 threshold를 기준으로 normal, abnormal 분류
  - 해당 내용은 없으므로 직접 score의 분포를 확인해보면 됨
- 평균 대신 Dirichlet 분포를 계산해서 하면 더 잘나온다고 함 (확인은 해보지 않음)

##### multiclass_experimment.py
- 한 클래스를 정상으로 두고 다른 클래스들을 비정상으로 탐지하는 방법
- 코드 자체는 미동작 (데이터 포맷 등에 대해 제대로 설명되어있지 않음)
