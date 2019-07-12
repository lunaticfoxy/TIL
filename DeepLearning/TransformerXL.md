#### Transformer의 개선 버전인 Transformer XL에 대한 내용

#### 주소: https://arxiv.org/abs/1901.02860

#### 기존 연구
- Transformer의 최대 길이는 고정
  - 주어진 길이의 데이터밖에 처리하지 못함
  - 최대 길이만큼 잘라서 사용
- abosulte positional encoding 의 한계
  - 절대적인 위치만 가지고있으므로 상대적인 위치에 대한 파악이 어려움
    - 가능은 하겠지만 제대로 반영되지 않음


#### 내용
- 장기간의 데이터를 볼 수 있도록 개선
  - Q, K, V 계산시 계속해서 누적하는 mem에다가 concat 해서 활용
    - 그럼 Q, K, V가 각각 벡터가 아니라 매트릭스가 됨
    - 따라서 매트릭스 곱을 한다음 이걸 다시 합쳐서 벡터로 변환
    - 이후에 계속해서 mem에 결과를 누적
  - 그 결과로 모델의 길이에 상관 없이 계속해서 데이터를 누적해 볼 수 있음
- relational positional encoding 추가
  - K 계산시 두개로 나누어 처리
    - K_h: 기존 (absoulte positional encoding) 방식으로 계산된 K
    - K_r: relational positional encoding 방식으로 계산된 L
  - 각각 나누어 연산해서 두 어텐션 스코어를 합산
  - 실제 수식은 직관적이지 않음 (긴 수식을 간소화해서 사용)
