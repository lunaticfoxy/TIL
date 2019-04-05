#### Language Models are Unsupervised Multitask Learners
#### A.K.A GPT-2


##### 주소
- 논문: https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf
- Github repo: https://github.com/openai/gpt-2

##### 개요
- 너무 생성 잘한다고 밝혀서 이슈가 된 논문
- 사실 모델은 Transformer와 별 차이 없음
- 어떤식으로 탐색해 봤는가에 대한 가치

##### 관련 연구
- Transformer 모델
- 


##### 논문 내용
- 데이터 수집
  - Common Crawl을 사용할까 하였으나 여러가지 면에서 맞지 않음
    - 정형화되지 않은 데이터를 수집하고 싶었음
  - 본인들이 직접 데이터를 크롤하여 사용
    - Reddit에서 Karma > 3인 데이터 수집
    - 4.5B Links 수집

- 데이터 전처리: Byte Pair Encoding 사용 (Subword model)

- 내부 모델
  - Transformer와 거의 동일
  - Layer normalization만 서브 블록의 앞쪽으로 이동하고 출력 전에 norm 추가
    - 기존 인코더: {attention -> norm -> mlp -> norm}xN
    - 변경 인코더: {norm -> attention -> norm -> mlp}xN -> norm
    - 디코더도 동일, 단 입력 값이 들어가기 전에 norm이 들어감
    
- 결과
  - Zero-shot 러닝만 사용: fine tuning, pre-training 이런거 전혀 신경쓰지 않고 Language-Model로만 학습
  - 각 문제별 결과
    - Children`s Book test
      - 동화책을 그대로 넣고 다음 단어 예측 (?)
    - LAMBADA
      - 50토큰 이상 앞의 데이터를 알아야 다음 예측이 가능한 문제
      - Very long sequence 문제
    - Winoigrad Schema Challenge
      - Commonsense를 이용해서 체크하는 방식
      - ex) 사과를 믹서기에 넣는다 -> 사과를 간다
    - Summerization
      - 요약문제
      - 기존 Language Model을 그대로 학습하되 출력 직전에 "TL;DR" 토큰늘 넣어주고 생성하라고 함
      - 요약을 따로 학습시키지 않아도 요약문 생성
      - 높은 성능은 아니지만 적당히 좋은 결과
    - Translation
      - "english sentence = 값 french sentence =" 를 넣어주고 생성하게 함
      - 어느정도 번역 가능
      - 기존에 있던 걸러지지 않은 일부 프랑스어로 학습한듯
    - Question Answering
      - ACC 1% 매우 안좋음
      - 다만 확률정답은 1%가 안되니 불가능하긴 할거다
  - Generailization vs Memorization
    - 학습된게 아니라 기억된게 아닐까?
    - Test데이터에서 원본 데이터셋과 겹치는 비율이 0.08%니 아닐거다
    - Training 데이터에서 겹치는 비율이 높으면 오히려 성능이 낮아진다
    
-
