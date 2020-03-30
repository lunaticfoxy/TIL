# Seq2Seq 란?

- Sequence to Sequence의 줄임말
    - 시퀀스란?
        - 연속되어 들어오는 모든 데이터
        - 타임시리즈 센서 로그, 텍스트, 음성 등등
- 입력 시퀀스로부터 출력 시퀀스를 생성하는 모델의 총칭

# 1:1 시퀀스 생성

## 개요

- Alex Graves 2013 ([https://arxiv.org/abs/1308.0850](https://arxiv.org/abs/1308.0850))
- 최초의 유명해진 시퀀스 생성 모델
- 입력 시퀀스를 유사하지만 새로운 출력 시퀀스로 1:1로 변환해주는 모델
    - 손글씨 생성 ⇒ 잘됨
    - 위키피디아 문서 생성 ⇒ 잘 안됨

## 아키텍쳐

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cda1c2c0-9e75-4cc3-bd4d-718687847dbb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cda1c2c0-9e75-4cc3-bd4d-718687847dbb/Untitled.png)

- 첫번째 히든 레이어 연산
    - 다음 값들의 합을 계산
        - t시점 입력값 * Weight
        - t-1시점, 첫번째 히든 레이어 출력값 * Weight
        - 바이어스
    - RNNFunction은 일반 RNN or LSTM

$$h_t^1=RNNFunction(W_{ih^1}x_t+W_{h^1h^1}h_{t-1}^1+b_h^n1)$$

- n번째 히든 레이어 연산
    - 다음 값들의 합을 계산
        - t시점 입력값 * Weight
        - t시점, n-1번째 히든 레이어 출력값 * Weight
        - t-1시점, n번째 히든 레이어 출력값 * Weight
        - 바이어스
    - 첫번째 히든 레이어보다 더할 요소가 하나 증가

$$h_t^n=RNNFunction(W_{ih^n}x_t+W_{h^{n-1}h^n}h_t^{n-1}+W_{h^nh^n}h_{t-1}^n+b_h^n)$$

- 히든 레이어 조합
    - 1~n번 레이어들의 출력값에 Weight를 곱해서 합

$$\widehat{y_{t}}=\Sigma^N_{n=1}W_{h^ny}h_t^n$$

- 출력 값 계산
    - OutFunction은 Weight만 존재하는 1레벨 레이어

$$y_{t}=OutFunction(\widehat{y_{t}})$$

- 학습 방법
    - t-1 시점의 y 출력시 t시점의 x가 나타날 조건부 확률 계산

    $$Loss(x)=-\Sigma_{t=1}^TlogPr(x_{t+1}|y_t)$$

    - 예시
        - 손글씨: t 시점 좌표의 위치와 t+1시점 좌표 위치 사이의 등장 조건부 확률
        - 텍스트 생성: t 시점의 단어와 t+1 시점 단어 사이의 등장 조건부 확률

## 장단점

- 장점
    - 1:1 시퀀스 생성에 강력
        - 손글씨 생성
        - 목소리 변조
    - 손글씨 생성 예시 ⇒ 맨 위의 시퀀스 입력시 생성된 손글씨 샘플들

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e459668-12a3-4e4a-8b20-943a11a71810/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e459668-12a3-4e4a-8b20-943a11a71810/Untitled.png)

- 단점
    - 1:1 시퀀스 이외에는 성능 낮음
        - 번역에도 사용하기 어려움

# 입력-출력 시퀀스 분리

## 개요

- Sutskever 2014 ([https://arxiv.org/abs/1409.3215](https://arxiv.org/abs/1409.3215))
- 입력 부분과 출력 부분을 분리한 시퀀스 생성 모델
- 1:1이 아니라도 시퀀스 생성 가능

## 아키텍쳐

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f84693f-8f68-4add-9542-37597ba90812/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f84693f-8f68-4add-9542-37597ba90812/Untitled.png)

- 입력이 ABC 일때 WXYZ 를 출력하는 모델 예시
    - 하나의 RNN으로 입력, 출력이 모두 진행된다고 생각하면 됨
    - 모델 동작 과정
        - ABC 를 각각 입력 후 입력 시퀀스의 종료를 뜻하는 <EOS> 입력
            - EOS ⇒ End Of Sequence
        - 이후에는 이전 시점의 출력값을 입력
        - <EOS> 입력 시점부터 나타나는 출력값을 출력 시퀀스로 사용
            - <EOS> 입력 전까지 나타나는 출력값은 버림
        - 출력 시퀀스에 <EOS>가 나타나면 시퀀스 생성 종료

- 히든 레이어 계산
    - 입력값*Weight + 이전 히든 레이어*Weight
    - 기본적으론 1레벨 히든 레이어
        - 원한다면 더 쌓는건 가능

$$h_t=sigmoid(W^{hx}x_t+W^{hh}h_{t-1})$$

- 출력값 계산
    - 히든 레이어에 Weight를 곱한 값을 출력

$$y_t=W^{yt}h_t$$

- 학습
    - 최초부터 t-1 시점까지 출력과 t시점 출력 사이의 조건부 확률 계산
        - 순서 고려 X
    - 위에서 구한 조건부 확률을 시퀀스 생성 종료시점까지 계산한뒤 이들의 곱을 전체 조건부 확률로 사용

    $$p(y_1, y_2,....,y_{T'}|x_1,x_2,...x_T)=\prod_{t=1}^{T'}p(y_t|v,p_1,p_2,...,p_{t-1})$$

    - 조건부 확률을 최대화 하는 방향으로 학습

## 장단점

- 장점
    - 1:1이 아닌 시퀀스에 대해서도 생성 가능
- 단점
    - 성능 보단 이런식으로도 시퀀스 생성이 가능하다는걸 보여준 모델

# Encoder-Decoder 분리

## 개요

- Kyunghyun Cho **2014 (**[https://arxiv.org/abs/1406.1078](https://arxiv.org/abs/1406.1078))
- 기존 Seq2Seq는  Encoding 단계과 Decoding 단계의 특성을 하나의 RNN이 모두 가지고 있어야 함
    - 당연히 성능 하락 발생
- Encoder와 Decoder를 분할하여 사용
    - Encoding 단계가 끝난 뒤의 출력을 Context 라 부르며, 이 Context를 기반으로 Decoding 수행
    - 나머지 부분은 Sustskever의 모델과 거의 동일
- 사족 - GRU가 나온 논문

## 아키텍쳐

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0e7cb7f-fb08-47e0-aaa2-997282c3887d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0e7cb7f-fb08-47e0-aaa2-997282c3887d/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/54d59ada-ed51-439d-94d0-88ed938e37d7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/54d59ada-ed51-439d-94d0-88ed938e37d7/Untitled.png)

- Encoder 부분은 Sutskever의 모델과 동일
- Decoder RNN이 따로 존재하며, Context C 를 추가 입력으로 받는다는 점만 차이
    - Sutskever의 모델: Context 가 존재하나 첫번재 Decoder의 입력으로만 사용됨
    - Cho의 모델: Context가 별개의 입력으로 존재하며, 모든 Decoding 단계에 입력됨

## 장단점

- 장점: Sutskever의 모델에 비해 성능 향상
- 단점: Context 벡터의 영향력이 너무 커짐

# Attention 적용

## 개요

- Yonghui Wu 2016 ([https://arxiv.org/abs/1609.08144](https://arxiv.org/abs/1609.08144))
- Cho의 논문에서 Context 부분을 강화하기 위해 Attention 이라는 개념 도입
- Attention이란?
    - Decoding 단계의 출력마다 참조해야 하는 Encoding 단계의 입력이 다를것이라는 생각에서 시작
        - "How is he? ⇒ He is fine"  VS  "Who is he? ⇒ He is Oscar"
            - 3번째 Decoding 단계의 출력은 How와 Who에 영향을 받음
            - He, is를 출력할때와 fine, Oscar를 출력할때의 context 를 동일하게 넣는건 찝찝하다
            - 저부분을 더 중요하게 볼 수 없을까?
    - Encoder 의 출력 결과를 매번 저장하고 있다가 Decoding시에 필요한걸 뽑아쓰자
        - 어떤걸 얼마나 뽑아쓸까? → 매 출력단계마다 어떤 입력에 집중할지 Weight로 계산하자

           ⇒ Attention의 개념

- 그리고 이 모델을 기반으로 기계번역에 적용해보자
    - 이 논문이 나오고 한달뒤에 구글 번역기 성능 급 상승

## 아키텍쳐

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9dd1e5a-203d-43b1-af3a-61fef1c7bc06/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9dd1e5a-203d-43b1-af3a-61fef1c7bc06/Untitled.png)

- Context가 단일값이 아닌 매 단계마다 Attention 메커니즘에 의해 계산되는 값이란 점만 기존과 다름
- Encoder의 출력 결과를 모두 저장하고 있음
    - 이 출력 결과를 Attention 단계에서 활용

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3eb35d06-8c07-4972-bfb6-c72255a6eb7a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3eb35d06-8c07-4972-bfb6-c72255a6eb7a/Untitled.png)

    - AttentionFunction은 1개의 feed-forward ayer
        - s = x*W1+y*W2+b
    - s_t 는 i 번째 출력에서의 "t 번째 인코딩 값의 중요도" 라고 생각하면 됨
        - 이전 출력값을 기반으로 1-n 번째 인코딩의 중요도를 각각 계산해서 s_1, s_2, ..., s_n에 저장
    - p_t 는 "t 번째 인코딩 값이 반영될 비율" 이라고 생각
    - 이후 p_t를 가중치로 하는 인코딩값 들의 가중 평균을 계산하여 i 번째 Context 로 활용

### 장단점

- 장점: 매우 높은 성능 향상
- 단점
    - 매우 큰 연산량
    - 모든 Encoding 결과를 저장하려면 매우 큰 메모리 필요
    - 학습뿐만 아니라 Evaluation 단계에서도 연산속도와 메모리의 이슈가 커짐
    - 사실상 이때부터 구글 머니게임 시작

# Attention의 추가 활용

## 개요

- Attention이라는게 좋다더라
- 이걸 Seq2Seq 말고 다른데 활용해볼수는 없을까?
- 실제로 여러가지 시도가 존재하였고, 대부분 기존 모델보다 성능 향상

## Hierarchical Attention Network

- 개념
    - Zichao Yang 2018 ([https://arxiv.org/abs/1810.06033](https://arxiv.org/abs/1810.06033))
    - 문서 분류에 Attention을 사용해보자
    - 문서는 문장의 집합이고, 문장은 단어의 집합
    - 두 단계의 Attention 사용
        - 문장 내에서 어떤 단어가 중요한지를 결정하는 Attention
        - 문서 내에서 어떤 문장이 중요한지를 결정하는 Attention

- 아키텍쳐

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/416f1d75-e943-40dc-a9fd-4594848c4e1f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/416f1d75-e943-40dc-a9fd-4594848c4e1f/Untitled.png)

    - Seq2Seq 모델의 Encoder + Attention 부분을 2단계로 구성
        - 첫단계는 word encoder + attention을 통한 word context를 생성하고, 이를 합하여 문장마다 하나의 벡터 생성
        - 두번째 단계는 sentence encoder + attention을 통해 sentence context를 생성하고, 이를 합하여 문서마다 하나의 벡터 생성
        - 이 벡터에 softmax를 적용하여 문서 분류에 사용

## 장단점

- 장점: 당연히 성능 향상
- 단점
    - 어마어마한 연산량
    - 매 문장마다 encoding 필요
    - 이 문장 encoding을 모아서 다시 문서 encoding 필요

# 정리

- Seq2Seq 모델: 입력 시퀀스로부터 출력 시퀀스를 생성하기 위한 모델
- 입력 시퀀스 중에 중요한부분을 찾아내기 위한 방법으로 Attention 도입
- 성능 향상은 있으나 무지막지한 연산량으로 모델 확장 어려움
