### Jenkins의 Lockable Resource Plugin에 대한 설명

#### 주소: https://wiki.jenkins.io/display/JENKINS/Lockable+Resources+Plugin

#### 설명
- Jenkins의 잡들이 각각 필요한 자원이 겹치는 경우 이를 동시에 활용할 수 없도록 lock을 걸기 위한 플러그인

#### 사용법
- 리소스 세팅
  - 1. Jenkins 설정 -> 시스템 설정 -> Lockable Resource Manager로 이동
  - 2. Add Lockable Resource 선택
  - 3. 리소스의 이름, 설명, 라벨, Reserved by 설정
    - 이름: 리소스 전체 관리 이름
    - 라벨: 사용될 세부 자원 (스페이스로 분리)
    - Reserved by: 해당 잡에 대해서만 할당 가능한 리소스임을 표시
- 잡 세팅
  - 1. 잡 설정 -> General로 이동
  - 2. Resources나 Label에 자원 입력
    - Resources에는 위에 등록한 리소스의 이름을 입력
    - Label에는 위에 등록한 리소스의 세부 자원을 입력
    - 한 자원에 대해서는 둘 중 하나만 입력 해야 함

#### 용도
- 동시에 도는 잡 개수 제한
- 동일한 데이터베이스에 동시 접근 방지
    
