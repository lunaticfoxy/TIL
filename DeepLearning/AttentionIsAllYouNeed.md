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
      - mask를
