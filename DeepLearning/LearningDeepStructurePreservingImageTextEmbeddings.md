#### 주소: https://arxiv.org/abs/1511.06078

#### 논문 이름: Learning Deep Structure-Preserving Image-Text Embeddings

#### 목적
- 이미지와 텍스트를 연결하기 위한 임베딩을 만들고자 한다
- 이때 텍스트의 구조적 특징 정보를 유지하면서 성능이 높은 임베딩을 만들어 보자

#### 기존 연구
- Canonical Correlation Analysis (CCA)
  - PCA와 유사하게 correlation이 가장 높은 프로젝션을 찾는 방법
- Kernel CCA
  - CCA에 Kernel을 적요하여 non-linear하게 변경
- A joint embedding space usign SGD with a ranking loss


#### 제안하는 모델
- 구조
  - X (Image), Y (Text) 를 각각 벡터로 임베딩 하고 L2 Norm 적용한 뒤 이를 concat해서 fully connected 결과를 embedding vector로 사용
  - X와 Y의 계산을 각각 branch라고 하고, 각각의 branch는 마지막 단계에 fully connected layer를 포함
  - 이미지 부분
    - 19-Layer VGG 사용
    - 4,096개 벡터 추출
  - 텍스트 부분
    - Fisher Vector 사용
      - 원래 이미지를 기반으로 추출하는 방법
      - 여기서는 자연어 처리에 적용
    - 300차원의 word vector에 30개의 센터가 있어서 300*30*2 = 18k 벡터 추출
      - 이후 PCA를 통해 6k 벡터로 줄임
    - Fisher Vector에서 제안한걸 다 안쓰고 HGLMM만 사용
- Loss Function => 주 Contribution
  - 컨셉 자체는 직관적
  - d(x_i, y_j) + m < d(x_i, y_k)
    - i, j의 거리가 i, k의 거리보다 m 이상 가까워야 한다
    - j는 i와 매칭되는 값, k는 매칭이 안되는 값
    - 여기서 k는 너무 많으니깐 random sampling 해서 사용
  - d(x_i, x_j) + m < d(x_i, x_k)
    - i, j의 거리가 i, k의 거리보다 m 이상 가까워야 한다
    - j는 i와 neighbor인 값, k는 neighbor가 아닌 값
    - neighbor가 주어진 데이터셋이 존재해서 사용 가능한 loss
  - 이후 이를 가중치 람다1,2,3 을 곱해서 더함...
    - 람다값은 랩실 애들이 갈아넣어졌겠지
- Triplet sampling
  - random sampling 시 top 50에 있는 것만 사용해서 학습 속도를 향상


#### 특이사항
- object detection은 하지 않음
- bounding box에서 찾아진 이미지에다만 적용
