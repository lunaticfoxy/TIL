# ML과 관련하여 매번 헷갈리는 기초 지식 기록

### Bias - Variance Trade off
- Bias (편향)
  - 예측값과 정답이 얼마나 많이 떨어져 있는가
    - 오답률이 높을수록 Bias가 낮음
  - Bias가 낮다면 학습 자체가 제대로 되지 않은것
    - 모델이 너무 단순해서 Underfitting (과소적합) 이 발생했을 가능성 있음

- Variance (분산)
  - 예측값간의 차이가 얼마나 벌어져 있는가
    - Train, Test 의 차이가 클수록 Variacne가 큼
  - Variacne 가 크다면 일반화가 제대로 되지 않은것
    - 모델이 너무 복잡해서 Overfitting (과적합) 이 발생했을 가능성 있음

- Bias - Variance Trade off
  - 모델의 복잡도가 Bias - Variance 에 각각 긍정 - 부정적인 영향을 끼침
  - 양쪽을 모두 완벽하게 만족시킬수는 없으니 Bias + Variance가 최소가 되는 지점을 찾아야 함



### 1x1 Convolution
- Convolution
  - 다차원 데이터의 차원 변환 기법
  - 인접한 데이터에 대해 일정 연산을 수행하여 해당 범위 값에 대한 특성을 찾아냄
  - 차원 수는 매번 다름
    - ex) 32x32 사이즈의 이미지가 흑백으로 표현되어 있고 (1차원) 이를 Convolution 한다면
      - 필터 사이즈 2x2x1x4 : 32x32x1 -> 31x31x4
      - 필터 사이즈 3x3x1x6 : 32x32x1 -> 30x30x6
    - ex) 32x32 사이즈의 이미지가 RGB로 표현되어 있고 (3차원) 이를 Convolution 한다면
      - 필터 사이즈 2x2x3x4 : 32x32x3 -> 31x31x4
      - 필터 사이즈 3x3x3x6 : 32x32x3 -> 30x30x6
- 1x1 Convolution
  - 말 그대로 필터 사이즈가 1x1인 convolution 필터를 사용하는것을 의미
  - 왜 사용할까
    - 차원 축소 (채널 축소)
      - axbxn 차원의 데이터를 axbxy 차원의 데이터로 줄일 수 있음
      - 영상의 경우 채널 정보를 축소하는 형태로 이해 가능
    - 비선형셩 증가
      - axbxn 차원의 데이터를 그대로 유지하면서 각 채널의 정보만 비선형적으로 변환
- 참조
  - https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578
  - https://gaussian37.github.io/dl-dlai-network_in_network/


### Maximum Likelihood Estimation (MLE) vs Maximum A Posteriori (MAP)
- MLE
  - 의미
    - 어떠한 사건 Z가 발생했을때 Z를 발생시킬 가능성이 가장 높은 분포를 탐색
    - 사전 확률의 최대화
    - p(Z|A) vs P(Z|B)
  - 예시: 어떤 머리카락이 나왔을때, 남자의 머리카락이 확률, 여자의 머리카락일 확률을 계산해서 더 높은 쪽을 선택
- MAP
  - 의미
    - 어떠한 사건 Z가 발생했을때 각 분포별로 X가 발생했을 가능성을 계산하고 이중 가장 값이 높은것을 탐색
    - 사후 확률의 최대화
    - P(A|Z) vs P(B|Z)
  - 예시: 어떤 머리카락이 나왔을때, 남자가 나타나서 머리카락을 흘렸을 확률과, 여자가 나타나서 머리카락을 흘렸을 확률중 더 높은쪽을 선택
- 어느쪽이 더 좋을까?
  - 이론상으로는 MAP가 더 좋을 수 밖에 없음
  - P(A|Z) = P(Z|A)*P(A)/P(Z)
  - 따라서 MAP는 MLE를 이미 고려한 뒤 분포가 나타날 확률까지 추가로 고려했다고 이야기 할 수 있다
  - P(A), P(B) 의 차이가 크면 클 수록 MAP가 더 정확해짐
    - 예시에서 남녀 성비가 차이날수록 MAP가 더 정확해진다고 할 수 있음
- 항상 MAP를 쓰면 될까?
  - P(A|Z) 를 단순히 찾는건 현실적으로 어려움 -> P(Z|A), P(A), P(Z) 를 구한뒤 이를 계산하는 수밖에 없음
    - 남자가 나타난 다음 머리카락을 흘릴 확률을 어떻게 구해...
  - P(A), P(B), P(Z)를 정답에 가깝게 구할 수 있는가? (= 데이터 양이 충분한가?)
    - Yes: MAP 사용
    - No: MAP 사용 불가능
- 그런데 머신러닝에서는?
  - 일반적인 Discriminative Model: 주어진 데이터로 가장 잘 설명되는 확률 분포를 탐색 => P(Z|A)
    - 전체에 대한 확률이 아니므로 조건부 확률
    - P(A), P(B), P(Z)는 모른다고 할 수 있음
  - Generative Model: 확률 분포를 통해 데이터 자체를 생성 => P(A|Z)
    - P(A), P(B), P(Z) 또한 학습을 통해 적절히 찾아갈 수 있음
    - 다만 데이터 양이 매우 많이 필요



### Singular Value Decomposition (SVD - 특이값 분해)
- 고유값 분해와 유사하게 대각 행렬을 만드는 방법
  - 차이점?
    - 정사각행렬이 아니어도 가능하다
    - 모든 행렬에 대해 가능하다
- A = U * S * V_T
  - A: 주어진 mxn 행렬
  - U: mxm 직교 행렬
    - A * A_T 를 고유값 분해해서 얻어진 직교 행렬
  - S: mxn 대각 행렬 (= min(m, n) 차원의 벡터)
  - V: nxn 직교 행렬
    - A_T * A 를 고유값 분해해서 얻어진 직교 행렬
  - U, S, V_T를 이용하여 A의 복원이 가능하다
- 어디에 사용할까?
  - S의 차원을 k로 줄인다면?
    - U: mxk 행렬
    - S: k차원 벡터
    - V: kxn 행렬
  - k < m, n 이라면 차원 축소의 효과 발생
    - 원본 복원은 안되지만, 원본을 가장 잘 설명하는 차원으로 축소 가능
  - 이렇게 얻은 벡터는 딥러닝을 통해 얻은 임베딩 벡터와 뭐가 다를까?
    - SVD는 선형변환
    - 임베딩 벡터는 비선형 변환
