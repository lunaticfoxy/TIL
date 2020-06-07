#### 다루는 내용
- 코어 네트워크 초기화 루틴
- NIC 초기화 루틴
- NIC가 인터럽트를 사용하는 방법과 IRQ 핸들러를 할당/해제하는 방법
  - IRQ를 드라이버들이 공유하는 방법
- 장치 초기화/설정 시 사용자 공간과 커널 공간 간의 상호작용
  - 커널이 사용자 공간에 있는 디바이스 드라이버와 설정을 적용하기 위해 사용자 공간 헬퍼를 수행하는 방법
  - 핫 플러그 기능
- 커널과의 상호작용과 설정에서 가상 장치와 실제 장치와의 차이점


### 시스템 초기화 개요
- 주의: 네트워킹과 관련된 초기화만 다룰것임

#### 이 책에서 다루는 시스템 초기화의 주 과정
- Boot-time 옵션
  - parse_args 호출을 통해 LILO나 GRUB이 전달한 커널 설졍 변수 처리
- 인터럽트와 타이머
  - IRQ에 대한 핸들러를 디바이스 드라이버가 어떻게 등록
- 초기화 루틴
  - 커널 서브시스템과 빌트인 디바이스 드라이버의 최기화

#### run_init_process를 통한 최초 프로세스 생성
- run_init_process에서 모든 프로세스의 부모가 될 첫 프로세스 생성
  - PID 1
  - 시스템 종료시까지 멈추지 않음
- 일반적으로는 SysVinit 패키지에 포함된 init 으로 수행 
  - 사용자가 부팅 옵션으로 init= 을 줌으로서 원하는 프로세스 지정 가능


### 장치 등록과 초기화
- 네트워크 장치가 사용 가능하려면 커널에 의해 인식되고 적절한 드라이버와 연결되어야 함
- 드라이버는 장치를 필요로 하는 커널 컴포넌트와 연결하기 위한 정보를 내부 데이터 스트럭쳐에 저장
- 이 과정은 코어 커널과 디바이스 드라이버에 의해 나누어 진행

#### 하드웨어 초기화
- 디바이스 드라이버가 포괄적 버스계층 (PCI, USB 등) 의 도움을 받아 수행됨
- 각 장치의 IRQ와 I/O 주소를 설정하여 커널에서 사용할 수 있게 함
#### 소프트웨어 초기화
- 장치가 사용되기 전 어떤 네트워크 프로토콜이 활성화되었는지에 따라 추가 정보 필요
  - ex) IP주소
- 다른 장에서 상세히 다룸
#### 기능 초기화
- 장치 부트 초기 단계에 신경을 써줘야 하는 옵션 설정
  - ex) 전송량 조절 시스템의 큐


### NIC(Network Interface Card = 이더넷 랜 카드) 초기화의 기본 목적
- 네트워크 장치는 커널 내 net_device_data 스트럭쳐의 인스턴스로 표현
- 이 과정에서 드라이버가 장치/커널 간 통신에 필요한 리소스 할당

#### IRQ 라인
- NIC는 IRQ를 할당받고 필요한경우 커널에 인터럽트를 검
  - 단, 가상 장치의 경우 IRQ를 지정받을 수 없음
    - ex) 루프백 장치
- /proc/interrupts 파일에서 현재 IRQ 할당 현환 확인 가능
#### I/O 포트와 메모리 등록
- 자신의 메모리 영역을 시스템 메모리로 매핑하여 사용
- request_region, release_region 함수에 의해 등록/해제


### 장치와 커널 간 통신
#### 폴링
- 커널측에서 수행
- 장치의 상태를 주기적으로 체크하여 변경사항 확인
#### 인터럽트
- 장치 측에서 수행
- 장치가 커널의 주의를 끌기위해 하드웨어 신호 발생

### 하드웨어 인터럽트
- 모든 인터럽트는 인터럽트 핸들러 함수를 실행하는 형태로 동작
  - 장치별로 다른 핸들러를 지님
  - 디바이스 드라이버에 의해 설치
- NIC 등록 단계에서 IRQ를 할당받고 이에 대한 핸들러를 등록
  - 관련 함수들
    - kernel/irq/manage.c 에 정의
    #### int request_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char *name, void *dev) (= request_threaded_irq)
    - 핸들러 등록
    - IRQ의 유효성 확인 후 타 장치에 할당되지 않았는지 확인 후 등록
    #### void free_irq(unsigned_int irq, void* dev_id)
    - 핸들러 제거
    - 다른 장치가 더 없다면 IRQ 라인 비활성
- 커널은 IRQ 번호를 사용해 드라이버 핸들러 탐색 및 수행
  - IRQ 번호와 핸들러 사이의 매핑을 전역 테이블에 저장
  - IRQ 번호:핸들러 = 1:N 관계
    - 여러개의 장치가 같은 IRQ 번호 사용 가능
    
 #### 인터럽트 종류
 ##### 프레임 수신
 - 가장 흔하고 표준적인 상황
 ##### 전송 실패
 - 이더넷 장치가 지연 전송까지 실패한 뒤에 발생
 - 상위 계층으로는 전달하지 않음
   - 상위 계층에서는 다른 방법으로 실패를 체크해야 함
     - 타이머 타임아웃, 음수 ACK 등
 ##### DMA 전송 성공적 완료
 - 보내야 할 프레임을 저장하는 버퍼 영역은 NIC의 전송단 메모리로 옮겨진 뒤 해제
 - 동기 전송 (DMA 미사용) 의 경우 프레임이 NIC로 옮겨지는 순간 인지
 - DMA 사용시 (비동기 전송) 명확한 인터럽트가 있어야 드라이버가 인지 가능
   - ex) DMA 사용시 - drivers/net/ethernet/3com/3c59x.c 에서 dev_kfree_skb 호출
   - ex) DMA 미사용시 - drivers/net/ethernet/3com/3c509.c
     - 책에서는 dev_kfree_skb 호출 부분을 비교해본다고 하면 되는데 해당 파일에 dev_kfree_skb 호출이 존재하지 않음
     - 다른 곳으로 옮겨졌거나 다른 함수를 사용하는것으로 보임
 ##### 장치가 새 전송을 위한 충분한 메모리 있음
 - NIC 장치가 프레임 크기 만큼의 공간을 가지고있지 않아 송신 측 큐를 중단하는 경우가 있음
 - 이 경우 정상상태로 돌아오면 인터럽트를 발생시키고, 인터럽트를 수신하면 전송 재시작

```c
static netdev_tx_t el3_start_xmit(struct sk_buff *skb, struct net_device *dev)
{
	struct el3_private *lp = netdev_priv(dev);
	int ioaddr = dev->base_addr;
	unsigned long flags;

	netif_stop_queue (dev);

  ...

	if (inw(ioaddr + TX_FREE) > 1536)
		netif_start_queue(dev);
	else
		/* Interrupt us when the FIFO has room for max-sized packet. */
		outw(SetTxThreshold + 1536, ioaddr + EL3_CMD);
  ...
}
```
- 상세 동작은 11장에서 설명


#### 인터럽트 공유
- IRQ라인은 제한된 리소스
  - 많은 장치가 공유할수록 IRQ를 사용할 수 있는 장치가 늘어남
- 장치들이 동일한 IRQ를 사용하되 자기가 필요 없는 호출은 핸들러 내부에서 걸러내도록 함
- 이를 위해 장치가 IRQ에 등록될 때 인터럽트 공유 지원 여부를 명시적으로 알려줘야 함
  - 첫번째로 해당 IRQ에 등록되는 장치가 인터럽트 공유를 허용했을 때만 새로운 장치가 해당 IRQ 공유 가능
  - 이 때 새로운 장치도 인터럽트 공유를 허용해야 함

#### IRQ와 핸들러 매핑 구조
- IRQ-핸들러 매핑 구조는 벡터의 리스트에 저장됨
  - IRQ별로 별개의 리스트 존재
- irqaction 데이터 스트럭쳐에 매핑 정의
  - request_irq 함수에서 irqaction 스트럭쳐를 받아 전역 irq_desc 벡터에 집어넣음
  - irq_desc는 kernel/irq/irqdesc.c 에 정의
    - 아키텍쳐마다 arch/XXX/kernel/irq.c 에 재정의 될 수 있다고 하는데 찾진 못함
  - irq_desc는 맵 형태이며 각각의 원소는 해당 IRQ마다 할당된 irqaction의 리스트를 가리키고 있음
- irqactionn 구조체 주요 데이터 필드
  - void (*handler)(int irq, void *dev_id, struct pt_regs *regs)
    - 인터럽트 처리 핸들러
    - 파라미터
      - irq: IRQ 번호 (보통 사용하지 않고 dev_id로 구분)
      - dev_id: 장치 식별자
      - regs: 프로세스의 레지스터 정보 (보통 사용되지 않음)
  - unsigned long flags
    - 플래그 세트로 include/asm-XXX/signal.h 에 정의된 값 입력
    - 주요 플래그
      - SA_SHIRO: 공유 IRQ 처리 여부
      - SA_SIMPLE_RANDOM: 자기 자신을 무작위 이벤트의 소스로 사용 가능 (커널 내부 난수 발생에 사용 - 추후 상세 설명)
      - SA_INTERRUPT: 핸들러 내부에서 발생하는 인터럽트를 무시한채로 수행 = 핸들러 내 타 인터럽트 호출 방지
    - void *dev_id
      - 해당 장치 net_device 의 포인터
    - struct irqaction *net
      - 같은 IRQ 번호를 사용하는 다음 irqaction과 연결
    - const char *name
      - 장치 이름
      - /proc/interrrupts 에 표현되기 위한 값


### 초기화 옵션
- 컴파일시 들어간 디폴트를 재정의하거나 변경하기 위한 옵션
#### 모듈 옵션
- module_param 계열의 매크로들
- 모듈 로드시 옵션 값 입력
- 컴포넌트가 커널에 빌트인 되어있는경우 사용 불가
  - 이후 필요한경우 /sys 파일 시스템을 사용하여 값 변경
#### 부팅 시 커널 옵션
- __setup 계열의 매크로들
- 부팅시 부트로더를 통해 옵션값 입력
- 커널에 빌트인된 컴포넌트가 사용
- 모듈의 경우에도 사용은 가능하나 혼란스러울 경우도 있음

### 모듈 옵션
- module_param 계열 매크로를 통해 정의
  - module_param(변수명, 변수타입, /sys 내 접근권한) 형태로 사용
```c
module_param(multicast_filter_limit, int 0444);
moudle_param(max_interrupt_work, int 0444);
moudle_param(debug, int 04444);
```
- module_param 으로 등록한 변수는 /sys/module 아래에 변수명으로 디렉터리를 할당받음
- 주의사항
  - 읽기권한을 주지 않으면 등록할 이유가 없음
  - 쓰기권한을 줄 경우 값이 변경되었을때 알림을 받고 처리할 수 있도록 모듈을 만들어야 함


### 장치 처리 계층 초기화: net_dev_init
- 트래픽 컨트롤, CPU별 수신 큐 등의 네트워킹 코드 초기화는 net_dev_init 에서 부팅시 이루어짐
  - net/core/dev.c 에 정의
- 일어나는 초기화 - 초기화 함수
  - CPU별 인터럽트 데이터 스트럭쳐 초기화
  - /proc 내 파일 생성 - dev_proc_init, dev_mcast_init
  - /sys/class/net 내 장치별로 디렉토리 생성 - netdev_sysfs_init
  - 난수에 사용되는 초기값을 CPU별로 초기화 - net_random_init
    - 난수는 여러 컨텍스트에서 여러 목적으로 사용
      - ex) 타이머의 딜레이에 난수를 넣어 여러 타이머의 동시 동작 방지
    - 커널 내 숫자의 난수화 정도를 시스템 엔트로피 라고 부름
      - 엔트로피가 클수록 행동이 비 결정적
    - 네트워크 디바이스는 몇개의 NIC 드라이버만 이에 기여
  - 프로토콜에 의존성 없는 방향 캐시 초기화 (33장) - dst_init
  - 프로토콜 핸들러의 역 다중화를 위한 핸들러 벡터 초기화 (13장)
  - 큐 길이의 주기적 수집을 위한 타이머 생성 (10장) - net_dev_init
  - CPU 핫 플러그 이벤트 발생 알림 체인에 콜백 핸들러 등록 - dev_cpu_callback


### 사용자 공간 헬퍼
- 커널이 이벤트를 처리하기 위해 사용자 공간 프로그램을 호출하는 경우에 사용
- 헬퍼 종류
  #### /sbin/modprobe
  - 커널이 모듈을 로드해야 할 때 사용
  - module-init-tools 패키지에 포함
  #### /sbin/hotplug
  - 커널이 새로운 장치가 꽂히거나 뽑히는것을 감지했을 때 수행
  - 장치 식별자에 따라 정확한 디바이스 드라이버 로드
    - 꽂혀진 버스에 따라 식별
    - 버스에서 정한 규격에 따라 ID 부여
  - hotplug 패키지에 포함
- 커널에서는 call_usermodehelper 함수를 통해 사용자 공간 헬퍼 호출
  - 변수 리스트 arg[], 환경 변수 리스트 env[] 를 헬퍼 프로그램에 전달 가능
    - arg[0]: 호출할 함수의 이름
    - arg[1]: 호출할 설정 스크립트의 이름

#### kmod (kernel/kmod.c)
- 커널 컴포넌트가 모듈을 로드할 수 있게 해주는 커널 모듈 로더
- 여러개의 루틴을 제공
  - 여기서는 request_module만 설명하겠음
- eth0 모듈 로드시 request_module 을 통해 모듈이 로드되는 과정
  - kmod 내 request_module 호출
  - kmod가 arg[0]에 /sbin/modprobe, arg[1]에 eth0 를 넣어 call_usermodehelper 호출
  - call_usermodehelper가 /sbin/modprobe 실행
  - /sbin/modprobe 가 /etc/modprobe.conf 파일을 참조하여 모듈 이름 체크
    - 이 경우 eth0는 실제로 3c59x의 별칭임이 /etc/modprobe.conf 내에 'alias eth0 3c59x' 형태로 표시되어 있음
    - 따라서 실제로는 3c59x 를 호출
  - /sbin/modprobe 가 3c59x.ko 로드 시도
- 사용자가 IPROUTE2 패키지의 tc 명령어로 트래픽 컨트롤 설정 시도시 커널에 없는 분류기를 참고하기도 함
  - 이때도 /sbin/modprobe가 필요한 모듈 로드 시도

#### 핫 플러그
- 플러그앤플레이를 제공하기 위한 기능
- 핫 플러그 가능 장치의 삽입/제거 감지시 사용자 프로그램에 알려주는 역할
  - 필요한 경우 드라이버와 설정 로드
- 개념상 핫 플러그 기능이 없거나, 부팅시에 이미 장착되어 있는 장치에 대해서도 알림 발생
  - 실제로 조치를 취할지는 사용자 공간 애플리케이션이 결정
- 장치 초기화를 위해 스크립트 세트 실행
  - 리눅스 배포판별로 스크립트 이름, 위치는 다를 수 있음
  - 부팅시에 존재하는 장치 알림은 이 단계에서 무시 (스크립트 세트가 없으므로)
- 커널 모듈 컴파일 시 객체 파일은 /lib/modules/{커널_버전} 아래에 생성
  - 해당 디렉토리 내 modules.pcimap, modules.usbmap 도 함께 존재
    - 해당 파일은 커널에서 지원하는 장치의 pci id와 usb id, 그리고 그 장치들에서 참조해야 하는 모듈을 포함
    - 이 파일들을 통해 정확한 장치 탐색
    - 6장에 예시
##### /sbin/hotplug
- 핫 플러그를 위한 사용자 공간 헬퍼
- /etc/hotplug, /etc/hotplug.d 에 포함된 파일을 통해 설정 가능
##### kobject_hotplug (lib/kobject_uevent.c)
- 커널에서 장치의 삽입과 제거 이벤트에 응답하기 위해 호출되는 함수
- NIC 추가 혹은 제거시 일어나는 동작
  - 커널에서 kobject_hotplug 호출
  - kobject_hotplug가 arg[0]에는 /sbin/hotplug, arg[1]에는 net.agent(스크립트 명)를 넣고, env에는 관련 환경 변수들을 넣음
    - env[0]=HOME, env[1]=PATH, env[2]=ACTION, ... , env[i]=INTERFACE (여기서는 eth0)
  - 설정된 arg와 env를 인자로 call_usermodehelper 호출
  - call_usermodehelper가 /sbin/hotplug 호출하며 인자로 arg[1]에 있는 net.agent 전달
  - /sbin/hotplug 에서는 net.agent 스크립트 실행
  - net.agent는 env[i] 에 포함된 INTERFACE 정보 (여기서는 eth0) 에 따라 장치에 관련된 설정 적용

#### 실제 PCMCIA 이더넷 카드 추가시
- 먼저 /sbin/modprobe 가 수행되어 드라이버 모듈 로딩
- 이후 /sbin/hotplug 가 수행되어 장치 설정 수행



### 가상 장치
- 하나 이상의 실제 장치 위에 추가된 추상화
- N:N 관계로 구성
  - 1:1, 1:N, N:1 가능
  - 단 모든 관계가 커널에서 동작하지는 않음
#### 가상 장치 예
- 리눅스가 지원하는 가상 장치 예시
  ##### 본딩 (Bonding) - N:1
  - 물리 장치를 그룹핑해서 하나처럼 사용하기 위한 가상 장치
  ##### 802.1Q - N:1
  - 802.3/이더넷 헤더 IEEE 규칙을 확장한 것
  - VLAN 헤더라고 불리는 가상 LAN 생성 가능
  ##### 브리징 - N:1
  - 브리지의 가상 표현 (4부)
  ##### 인터페이스 에일리어싱 - 1:N
  - 원래 하나의 이더넷 인터페이스를 여러개의 가상 인터페이스로 설정하고 IP를 설정하기 위한 것
  - 현재는 다중 IP 설정을 위해 가상 인터페이스 설정은 필요 없음
  - 몇몇 경우에 NIC 가상 인터페이스를 갖는 것이 편할 수 있어 사용 (30장)
  ##### True Equalizer (TEQL)
  - 트래픽 컨트롤에서 사용할 수 있는 큐잉 정책
  - 본딩과 유사한 형태로 동작
  ##### 터널 인터페이스
  - IPIP (IP over IP) 터널링 구현, GRE (Genneralized Routing Encapsulation) 프로토콜에 사용
  
#### 커널 네트워크 스택과 통신
- 가상 장치와 실제 장치의 커널과의 통신 차이
##### 초기화
- 기본적으로는 실제와 동일하게 net_device_data 스트럭쳐 할당
  - 대부분 내부에 실제 장치에서 사용되는 함수 포인터를 감싸는 래퍼 함수 포함
- 에일러이싱 같은 경우는 net_device를 할당받지 않음
  - 실제 장치에 레이블을 붙이는 형태로 개발 (30장)
##### 설정
- 해당 가상 장치에만 사용되는 상위 필드 설정시 별도의 사용자 공간 도구 사용
##### 외부 인터페이스
- /proc 를 통해 외부에 정보 노출 가능
- 원래 물리 장치 파일의 대체는 불가능
- 자신의 net_device 인스턴스가 없는 장치는 /proc 접근 불가
##### 전송
- 가상 장치와 실제 장치가 1:1이 아닐경우 장치 선택 루틴 필요 (11장)
##### 수신
- 가상장치는 소프트웨어 이므로 IRQ 핸들러 등록, 포트 할당, 메모리 할당 등의 실제 시스템 자원 통신 불필요
- 실제 장치에서 위 과정을 거친 뒤 간접적으로 트래픽 전달
- 실제 동작은 장치마다 다르게 수행
  - 802.1Q 인터페이스는 이더타입을 등록하고 정확한 프로토콜ID를 가진 패킷만 전달받음 (13장)
  - 브리지 인터페이스는 연결된 실제 장치의 모든 패킷 수신
##### 외부 알림
- 다른 컴포넌트가 생성한 알림 수신을 위해 알림 체인에 별도 등록 필요
  - 트래픽은 실제 장치가 전달해주지만 알림은 로직이기 때문에 실제 장치가 전달하지 못함
- 단, 하드웨어 알림은 가상 장치에 바로 전달 불가


### /proc 파일 시스템을 통한 튜닝
#### /proc/sys/kernel
- modprobe, hotplug 존재
#### /proc/moduels
- 현재 로드된 모듈 리스트 보여줌
- lsmod 가 이 정보를 사용
#### /proc/net/dev
- 커널에서 등록한 장치의 전송 관련 통계 표시 (ex. 송수신 바이트 패킷수)
#### /proc/net/dev_mcast
- 커널에서 등록한 각 네트워크 장치의 IP 멀티캐스트와 관련된 변수 표시
#### /proc/net/wireless
- 무선 장치별로 관련 통계값 출력
  - 실제로는 dev->get_wireless_stats 결과의 값을 출력 (net/wireless/wext-core.c 에 정의)
- 무선 장치는 통계정보를 보관하기 위한 데이터 스트럭쳐를 별도로 할당받기 때문에 따로 표시
#### /proc/net/softnet_stat
- 네트워크 코드에 의해 사용된 소프트웨어 인터럽트 통계 표시 (12장)



### 5장 정리
#### 함수, 매크로
- request_irq, free_irq : IRQ라인에 콜백 핸들러 등록, 해제
- request_region, release_region : I/O 포트와 메모리 할당, 해제
- call_usermodehelper : 사용자 공간 헬퍼 애플리케이션 호출
- module_param : 모듈을 위한 설정 매개변수 정의
- net_dev_init : 부팅시 네트워크 코드 초기화
#### 전역 변수
- dev_boot_phase : 레거시 코드에서 NIC 디바이스 등록시전 net_dev_init 의 수행을 강제하기 위한 플래그 (정리에서는 생략했었음)
- irq_desc : IRQ 표현자 벡터의 포인터
#### 데이터 스트럭쳐
- struct irq_action : IRQ 라인을 정의하기 위한 스트럭쳐
- net_device : 네트워크 장치를 표현하기 위한 스트럭쳐
