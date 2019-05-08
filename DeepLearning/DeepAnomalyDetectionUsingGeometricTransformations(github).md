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
- 이후 어떻게 탐지하나...

##### institution_experiments.py
- 하나의 클래스를 transform 할때마다 다른 class로 만들어서 학습시키고
- 탐지시에는 각 클래스별로 출력된 확률을 평균내서 스코어 계산
  - 정확히 어떻게 하는건지는 확인 필요
