#### 제목: FaceNet: A Unified Embedding for Face Recognition and Clustering

#### 주소: https://arxiv.org/abs/1503.03832

#### 개요
- 그 유명한 facenet을 공부해보자



#### 배경지식
- face recognition의 기본 방법
  - 공통 부분 face detection -> face alighnment -> anti spoofing -> face processing
    - 학습시: feature_extraction -> loss function -> training
    - 테스트시: feature extraction -> matching -> find one
  - 기존에는 face detection~prcessing 단계가 중요 => Facenet에서는 비교적 덜 중요
- 기존 face recognition만 해도 정확도 99%
  - 단 이건 연구용 데이터
- FR Approach
  - Identification: 입력된 사진이 누구인가?
  - Verification: 두 사진이 동일인인가?
  - 기존에 Training은 Identification, Fine-tuning + Test는 Veficiation으로 하는 방법론이 있음
- 기존 방법론에 비해 Deep-Learning 기반 방법론이 훨씬 좋은 성능을 보임
- DeepFace
  - Cross Entropy로 기본 학습하고
  - Siamese Net의 chi-square 값으로 fine-tuning

#### FaceNet에선?
- 사진 2억개...
- Metric Learning 사용
  - 공간 상에서 가까운 이미지는 서로 가깝게, 먼 이미지는 서로 멀게
- 특징
  - 매우 큰 데이터
  - 매우 큰 네트워크
  - Face Alignment 미필요
  - 단일 모델
  - Metric만 사용해서 Face L2 Embedding 추출
    - Verification은 두 이미지 사이의 거리가 threshold 이하인지 확인
    - Identification은 K-NN을 통해서 체크
- 아키텍쳐 자체는 기존 방법들과 비슷함
- 이때 모든 데이터의 페어를 구하는건 현실적으로 불가능
  - 따라서 모든 데이터가 아니라 어려웠던것만 학습시키도록 하자: ㅅ갸ㅔㅣㄷ ㅣㅐㄴㄴ ㅆㄱ먀ㅜㅑㅜㅎ
  - Hard Positive: 거리가 작아야되는데 가장 큰 쌍
  - Hard Negative: 거리가 커야되는데 가장 작은 쌍
  - 배치를 1000 이상으로 줘야 함: 배치가 작을경우 튀는 값이 많음

#### 실험
- 이후 실제로 검증된적은 없음... (데이터 미공개)
- 단 VGGFace, Youtube Face 등을 통해 더 높은 성능이 나오는 것을 확인
- Dataset, Pre-processing is Very Very Improtant




