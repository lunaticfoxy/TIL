- 사용자 공간의 애플리케이션이 커널과 통신하거나 커널에 의해 노출된 정보를 읽는 방법 소개


### 개요
- 내부 정보를 노출하는 인터페이스의 큰 분류
  #### 시스템 호출 (시스템 콜)
    - 애플리케이션 개발자에 의해 사용되는 인터페이스
  #### procfs (/proc 파일 시스템)
    - /proc 에 마운트되는 가상 파일 시스템
    - 내부 정보를 가상 공간에 파일 형태로 노출
      - 실제 파일과 동일한 접근 가능
      - cat, more, 권한 부여 등
    - 디렉토리 내 쓰기는 불가능
    - 관련 커널 설정 메뉴
      - Filesystems > Pseudo filesystems > /proc file system support
      - 대부분의 리눅스 배포판에 디폴트로 지정
  #### sysctl (/proc/sys 디렉토리)
    - 사용자 공간에서 커널 변수를 읽거나 변경할 수 있게 해줌
    - 커널이 명시적으로 보이도록 한 변수에 대해서만 설정 가능
    - 사용자 공간에서 접근하는 방법
      - sysctl 시스템 호출
        - sysctl 이 노출하는 변수를 설정하는데 사용
        - 실제로는 /proc/sys 에 정보를 기록하는 방식으로 동작
      - procfs 지원시 /proc/sys 디렉토리에서 파일 형태로 접근 가능
    - 관련 커널 설정 메뉴
      - General setup > Sysctl support
  #### sysfs (/sys 파일 시스템)
    - procfs, sysctl 의 오랜 남용으로 좀 더 깨끗한 형태의 정보 제공 필요
    - 많은양의 정보를 깨끗하고 규칙성 있게 제공
      - 커널 내 정보를 계층적으로 제공
      - 대략 다음 내용 포함
      ```
/sys
├── block
├── bus
├── class
├── dev
├── devices  
├── firmware
├── fs
├── kernel
├── module
└── power
      ```
      - sysctl 로 노출되는 정보중 sysfs 에서도 노출되는 정보 존재
    - 커널 2.6 이상에서 지원
    - 관련 커널 설정 메뉴
      - Filesystems > Pseudo filesystems > sysfs filesystem support(NEW)
      - General setup > Configure standard kernel features(for small systems) 도 활성화 필요
    - 자세한 내용은 17장 참조
  #### 
    
    
    
    
    
    
    
    
    
    
    
    
  
