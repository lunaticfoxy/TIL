### Attention Is All You Need
#### (A.K.A. Transformer Model, Attention Model)

- 주소: Attention Is All You Need

- 목적: Seq2Seq를 CNN, RNN 없이 구성하여 병렬화를 최대화하자

- 요약
  - Seq2Seq 모델을 MLP + Attention 만으로 제작
  - 병렬화를 통해 연산량 감소
  - 새로운 Attention 제안
  
- 기존 연구
  - RNN
    - 유동적인 길이의 시퀀스에서 좋은 성능
    - Seq2Seq의 핵심 모델
    - LSTM, GRU 등을 이용해서 Vanishing Gradient 완화
    - 문제점
      - 순차 연산 필요 (병렬성 감소로 연산 시간 증가)
      - Vanishing Gradient 여전함
      - 계층 데이터 처리 어려움
  - CNN
    - 한 연산마다 처리할 영역이 정해져있음 => 병렬화 유리
    - RNN 대신 CNN을 써서 시퀀스를 처리해보려는 연구 
    - 문제점
      - 양쪽 끝의 정보를 합치기 위해서만 최소 log(n) 이상의 레이어 필요 (트리 구조로 좁혀지니깐)
      - 완벽한 병렬화는 되지 않음... 결국 영역마다 Convolution 해야되니 순차 연산 들어갈수밖에 없음
        - 메모리가 무한하다면 가능하려나?
  - Attention
    - 자연어 기계 번역 분야에서 encoder-decoder를 연결하는 핵심 이슈
    - Representation 단계부터 (self-)attention을 사용하면 안될까?

- 핵심 내용
  - self-attention
    - intra-attention이라고도 부름
    - 한 시퀀스 내의 요소가 다른 요소와 가지는 관계 정보
    - 시퀀스 내 모든 요소 사이의 pair를 만들어 계산
      - 본인 -> 본인 포함
    - 계산된 attention을 weight로 사용하여 가중평균을 구하여 해당 위치의 출력값으로 사용
    - 장점
      - 한 레이어당 계산 복잡도가 O(1) (vs O(n) in RNN)
      - 시퀀셜 오퍼레이션이 거의 없어 병렬화 용이
        - Convolution에 비해 메모리도 매우 적게 먹으므로 확실한 병렬화 가능
        - 모든 시퀀스가 한 레이어 안에서 연결됨
        - 모델 자체의 표현력도 더 높다(는 주장)
        
  - 논문 내 사용되는 attention 종류
    - encoder-decoder attention
      - encoder에서 decoder로 전달
      - encoder의 값을 decoder로 얼마나 반영할 것인가
    - encoder self-attention
      - encoder의 한 레이어 내에서 일어나는 self-attention
    - masked decoder self-attention
      - decoder에서만 사용되는 attention
      - mask를 줘서 이전 출력값만 사용하게 함
      
  - Dot-Product Attention
    - 용어 정리
      - Q: query vector (입력된 벡터)
      - K: key memory (키 벡터 => 입력된 벡터와 유사도 계산)
      - V: value memory (해당 키에 저장된 값)
    - Attention을 들어온 Query와 가장 유사한 Key를 찾아 여기 저장된 Value를 리턴하는 Map이라고 생각하자
    - 중간과정 생략하고 대충 A(Q,K,V) = softmax(QK^T)V 가 됨 => 여기까지가 Dot-Product Attention의 개념
    - 근데 QK^T가 너무 커져버리면 softmax 값이 튀겠지?
      - 벡터 크기의 루트로 softmax 내부의 절대값을 줄여주자
      - 이를 Scaled Dot-Product Attention이라 부름
    - 기존 Attention이랑 차이점?
      - 기존의 각 값마다 Attention을 계산하기 위해 별개의 레이어를 만드는 방식을 Additive Attention 이라 부름
      - 당연히 표현력은 기존 방식이 좋음 (레이어 하나를 더 거치니깐)
      - 근데 현실적으로 자연어는 sparse해서 저 레이어 학습시키는거만해도 일
      - 그리고 속도도 당연히 dot-product가 빠르지
    - 그림에 있는 Mask는 Decoder에서만 사용되는 것으로 자기보다 뒤쪽에 나타나는 Attention은 통과시키지 않는다 대충 이런 구조
    
  - Multi-Head Attention
    - Self-Attention과 Convolution을 비교해보자
      - convolution은 채널에 따라 다른 정보가 매핑됨
      - self-attention은 사실 그냥 가중합이라 그런거 없음
      - 당연히 표현력이 떨어지겠지
    - 그럼 self-attention도 쪼개자
      - 한 벡터를 쪼개서 각각 attention 한다음 concat
      - 각각의 조각이 convolution의 채널과 유사한 형태가 될것이라 기대
    - 개념상으로는 쪼개는 내용 없이 여러번 attention을 준 뒤 이를 (어떻게든) 합치는 방식이지만 실제로 구현시에는 모두 쪼개서 구현
    
  - Positional Embedding
    - 시퀀스 위치 정보가 없으니깐 강제로 넣자
    - 대충 sin-cos 그래프 비슷한 형태로 넣어서 포지션별로 다른 값이 들어가게 하자
    - 첨언 - 이후에 추가된 모델들은 그냥 정수로 1,2,3,4 식으로 증가시켜줌
    
  - Transformer 모델
    - 사실상 전체 모델이라 생각하면 됨
    - Encoder-Decoder 구조
      - 두 부분이 다른점은 Decoder에는 Encoder의 값을 받기 위한 Attention 부분이 하나 더 들어간다 정도
      - 각각 6개 레이어 사용
    - Residual Connection이 들어가는 경우도 있음 (선택사항)
    - Encoder 동작
      - 입력 문장 전체를 인코더에 입력
      - 입력된 값을 복사해서 Q, K, V에 할당
      - Q, K, V로 attention
      - attention 결과를 feed-forward
      - 위 과정을 레이어 수만큼 반복
      - 리턴값을 embedding vector로 사용
    - Decoder 동작
      - start 시그널을 디코더에 입력
      - 마스크된 값을 Q, K, V로 주고 1차 attention 수행
      - embedding vector를 q, k, 1차 attention 값을 v로 주고 2차 attention 수행
      - 2차 attention 결과를 feed-forward
      - 위의 과정을 레이어 수만큼 반복
      - 출력값을 사용
      - 이후 다음 출력값부터는 start 시그널 대신 이전 출력값 입력 + 

  - Multi-Head Attentio
