
#### 제목: SSD: Single Shot MultiBox Detector


#### 주소: https://arxiv.org/abs/1512.02325


#### 기존 연구
- Object Detection
  - 1-stage detector
    - 영역 검출 없이 전체 영역 (최소는 픽셀) 단위로 분류 
    - 속도 빠름
    - YOLO
      - Convolution으로 피쳐를 뽑고 FC Layer를 통해 영역으로 변환
      - 이 영역별로 Multiclass classification 수행
    - SSD가 여기 속함
  - 2-stage detector
    - 먼저 영역을 검출
    - 검출한 영역을 분류 수행
    - Faster RCNN
      - 먼저 Region을 추출
      - 이후 각각 classification 수행
      - 당시 제일 빠른 방법 (RCNN)


#### 내용 (장애 처리하느라 잘 못봄, 나중에 다시 한번 보자)
- 기존 모델에 feature 추출 과정 재활용
  - VGG-16의 conv5_3까지르 잘라서 사용
- Single-shot learning   
  - 사진 변형 없이 한장으로 훈련, 검출을 수행하는 detector
  - Bounding box를 여러 크기로 바꿔서 모든 픽셀에 적용
    - 그중에 해당 객체가 들어가 있는 곳을 다 포함하고 있으면 true, 아니면 false로 분류
- Hard Negative Mining
  - 어차피 학습할때 맞추기 어려우 값은 정해져있음
  - Negative를 Postive의 딱 3배만 뽑아서 학습


#### 결과
- 속도 향상을 위해 한 픽셀식 건너뛰면서 활용
- 빠르면서 좋은 성능
- 작은 객체에 대해서는 성능이 떨어짐
- 최대 속도 46프레임까지 나옴
