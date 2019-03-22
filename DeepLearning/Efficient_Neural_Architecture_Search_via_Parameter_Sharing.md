논문 제목: Efficient Neural Architecture Search via Parameter Sharing

명칭: NAS (Nerual Architecture Search)

목적: ImageNet 분류 모델의 자동 구성

기본 개념
- 강화학습을 통해 모델의 구성을 학습시키는 모델 구성 



NASNAsdddd기존 
- 컨트롤러를 RNN으로 구성
- 두가지 구성 방법 사용
  - 한 레이어 내 구조를 마음대로 결정
    - 한 RNN 노드가 한 레이어의 피쳐를 하나씩 결정
    - Layer의 개수는 사람이 고정
    - 한 레이어 내의 
  - 기본 구조
    - Normal Cell과 Reduction Cell을 나누어 구성
      - Normal Cell n개, Reduction Cell 1개의 구조를 반복
      - n은 사람이 결정, Cell 내부만 모델이 결정
    - Cell내 구성 방법
      - 레이어 1 구성
        - 레이어 인풋 지정 (RNN 블록 1)
        - 레이어 연산 지정 (RNN 블록 2)
      - 레이어 2 구성
        - 레이어 인풋 지정 (RNN 블록 3)
        - 레이어 연산 지정 (RNN 블록 4)
      - 두 레이어 합치는 방법 구성
- 동기
  - NASsms 800GPU를 28일동안 썼고, NASNetdms 450 GPU를 3,4일간 썼다.
  - 문제>
 f
