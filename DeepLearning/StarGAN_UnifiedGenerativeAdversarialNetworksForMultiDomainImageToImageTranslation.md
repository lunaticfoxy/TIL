### 제목: StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation

### 주소: https://arxiv.org/pdf/1711.09020.pdf

### 요약
- 입력을 조건에 따라 GAN을 통해 새로운 이미지 생성
- 타 논문과의 차이점은 다양한 축을 한 모델로 구성하자
  - 차원의 확장 개념이라 생각하면 될듯
  
### 배경
- Image to Image Translation
  - pair가 있으면 큰 문제가 없지만
  - unpaired 데이터를 사용하기 위해 gan (특히 cycle gan)이 적용됨 (unsupervised)
- Multi-domain Image translation
  - 이미지를 여러 도메인으로 동시에 변환
- Cycle Gan
  - x->y인 모델 G와 y->x인 모델 F를 x -> G -> y` -> F -> x`, y -> F -> x` -> G -> y` 형태로 모델을 학습시키장

### 컨트리뷰션
- cycle gan과 뭐가 다른가
  - cycle gan은 도메인이 하나씩 늘어날때마다 학습시켜야 될 제너레이터 수가 엄청나게 증가
    - [2:2, 3:6, 4:12, 5:20, ...]
  - 하나의 범용 제너레이터만을 사용해서 이걸 해결하겠다
- 제너레이터에 추가적인 파라미터 c를 줘서 어떤 형태의 변환을 수행할지 결정한다
- 그리고 도메인별로 따로 디스크리미네이터를 학습해서 사용함

