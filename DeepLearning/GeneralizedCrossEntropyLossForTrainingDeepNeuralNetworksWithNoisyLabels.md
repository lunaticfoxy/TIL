#### 요약
- Categorical Cross Entropy (CCE)는 학습이 빠르지만 noise에 민감하고, Mean Absolute Error (MAE)는 noise에 robust하지만 학습이 느리니 중간지점을 찾아보자
- EM과 유사한 data pruning을 두어서 noisy 데이터를 자동으로 버리도록 만들어보자

#### 관련 연구
- MAE가 CCE에 비해 노이즈에 강건한 이유
  - CCE의 경우 분모에 벡터간 로스 크기에 반비례하는 텀이 들어가는데 이로 인해 빠른 학습이 들어갈 수 있음
  - 하지만 이로인해 노이지 데이터의 반영 비율도 올라가서 문제
- 하지만 MAE는 성능이 너무 낮다

#### 
