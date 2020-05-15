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
    - 첫번째 계층에는 대략 다음 내용 포함
      - block, bus, class, dev, devices, firmware, fs, kernel, module, power
      - 이외 리눅스 배포판에 따라 추가되거나 빠질 수 있음 
    - sysctl 로 노출되는 정보중 sysfs 에서도 노출되는 정보 존재
  - 커널 2.6 이상에서 지원
  - 관련 커널 설정 메뉴
    - Filesystems > Pseudo filesystems > sysfs filesystem support(NEW)
    - General setup > Configure standard kernel features(for small systems) 도 활성화 필요
  - 자세한 내용은 17장 참조
  #### ioctl 시스템 호출
  - 표준 시스템 호출에서 제공되지 않는 특수한 장치의 입출력 제어를 위한 시스템 호출
    - read(), write() 만으로 해결되지 않는 경우 사용
    - 디바이스에 직접 32비트 명령어를 전달
      - 명령어 형태는 디바이스마다 다름
  - 디바이스 파일에 적용되는 형태
  - 네트워크에 사용되는 부분
    - 소켓 디스크립터에서 소켓 시스템 호출의 반환 값 형태로 사용
    - ifconfig, route 등
  #### Netlink 소켓
  - 네트워크 애플리케이션이 커널과 통신하는 방식
  - IPROUTE2 패키지에서 사용
  - 소켓 형태로 커널 모듈과 사용자 애플리케이션이 통신하는 방식
    
### procfs와 sysctl
- 모두 커널 내부 정보 노출
- procfs는 주로 읽기 전용 데이터 노출
  - 복잡하거나 특별한 데이터 형식이 필요한 경우는 거의 procfs로 노출
  - 캐시나 통계정보도 포함
- sysctl은 대부분 쓰기도 가능한 정보 노출
  - 읽기 전용 데이터중 간단한 커널 변수나 데이터 스트럭쳐는 sysctl 로 노출
    
  #### procfs
  - 
    
    
    
    
    
    
    
    
    
    
  
