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
