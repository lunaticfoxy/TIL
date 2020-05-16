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
  - 대부분의 네트워킹 기능에서 부팅시나 모듈 적재시 /proc 아래에 파일 등록
    - /proc/net 아래에 네트워크 관련 코드 적재
  - /proc 아래 파일 로드시 커널에서 함수를 호출하고 그 결과를 출력하는 식으로 동작
  - proc_mkdir 을 통해 /proc 내 디렉토리 생성
    - /proc/net 내부 파일은 include/linux/proc_fs.h 에서 정의한 proc_net_fops_create와 proc_net_remove 함수에 의해 등록되고 해제
      - create_proc_entry, remove_proc_entry 함수에 으해 래핑
      - proc_net_fops_create 는 내부에서 proc_net_create를 호출하여 파일을 생성하고 파일 작동 핸들러를 초기화
        - ex) ARP 프로토콜이 /proc/net 아래에 arp 파일을 등록하는 방법
```c
static struct file_operations arp_seq_fops = {
  .owner  = THIS_MODULE,
  .open   = arp_seq_open,      // 초기화 - procfs가 사용자에게 정보를 전달하기 위한 함수 포인터 등록 발생
  .read   = seq_read,
  .llseek = seq_lseek,
  .releae = seq_relase_private
};

static int __init arp_proc_init(void)
{
  if(!proc_net_fops_create("arp", S_IRUGO, &arp_seq_fops))  // "arp": 파일명, S_IRUGO: 읽기권한만 가짐, &arp_seq_fops: 호출 함수들
    return -ENOMEM;
  return 0;
}

static struct seq_operations arp_seq_ops = {
  .start = clip_seq_start,    // 하나의 아이템에 대한 내용 출력 시작
  .next = neigh_seq_next,     // 다음 아이템으로 이동
  .stop = neigh_seq_stop,
  .show = clip_seq_show       // 아이템 내용 출력
}

static int arp_seq_open(struct inode *inode, struct file *file)
{
  ...
  rc = seq_open(file, &arp_seq_ops); // /proc/net/arp 파일 open시 연결될 함수 포인터들 등록
  ...
}
```

  #### sysctl: /proc/sys 디렉토리
  - /proc/sys에 등록되는 커널 변수에 대해 다음 사항 정의 필요
    - /proc/sys 아래 디렉토리 위치
      - 동일한 커널 컴포턴트나 기능과 연관된 변수는 같은 디렉토리에 위치
      - ex) /proc/sys/net/ipv4 아레에는 IPv4와 관련된 파일 저장
    - 파일 이름
    - 파일 권한
  - /proc/sys에 노출된 변수 내용은 파일 접근 혹은 sysctl 시스템 콜을 통해 읽기-쓰기 가능
  - /proc/sys내 디렉토리나 파일이 생성되는 이벤트
    - 커널 모듈에 새로운 기능 등록
    - 새로운 네트워크 장비가 등록되거나 제거
      - 장치별로 하나씩 매개변수를 가지게 됨
      - ex) /proc/sysnet/ipv4/conf, /proc/sys/net/ipv4/neigh 디렉토리는 네트워크 장치별로 하나의 하위 디렉토리를 가짐 (36장, 29장 설명)
  - /proc/sys 안의 파일과 디렉토리는 ctl_table 스트럭쳐에 의해 정의
    - kernel/sysctl.c에 정의된 register_sysctl_table, unregister_sysctl_table 함수로 등록, 제거
    - ctl_table의 주요 필드
      - const char *procname : /proc/sys 내 파일명
      - int maxlen : 커널 변수의 크기
      - mode_t mode : 파일과 디렉토리에 설정된 권한
      - clt_table *child : 부모자식 관계 설정시 자식배열의 첫번째 원소 주소
      - proc_handler : 파일 읽기와 쓰기를 담당하는 함수
      - strategy : 데이터를 보여주거나 저장하기 전 추가적인 포매팅 수행 루틴
      - extra1, extra2 : 변수에 최소값/최대값을 정의할때 사용
    - proc_handler와 strategy는 변수의 특성에 따라 다르게 초기화됨
      - proc__handler 초기화 함수
        - proc_dostring: 문자열 읽기/쓰기
        - proc_dointvec: 정수 배열 읽기/쓰기
        - proc_dointvec_min_max: 범위 내의 정수 배열을 읽기/쓰기 (범위 밖이면 받아들이지 않음)
        - proc_dointvec_jiffies: 지피스로 기록된 커널 변수를 초로 변환하여 사용자에게 읽기/쓰기 제공
        - proc_dointvec_ms_jiffies: 지피스로 기록된 커널 변수를 밀리초로 변환하여 사용자에게 읽기/쓰기 제공
        - proc_doulongvec_minmax: 범위 내의 long 배열을 읽기/쓰기 (unsigned long 같은데 확인 필요)
        - proc_doulongvec_ms_jiffies_minmax: 지피스로 기록된 커널 변수중 범위 내의 long 배열을 밀리초 로 변환하여 사용자에게 읽기/쓰기 제공
      - strategy 초기화 함수
        - sysctl_string: 문자열 읽기/쓰기
        - sysctl_intvec: 범위 내의 정수 배열 읽기/쓰기
        - sysctl_jiffies: 지피스 값 초 단위로 변환하여 읽기/쓰기
        - sysctl_ms_jiffies: 지피스 값을 밀리초 단위로 변환하여 읽기/쓰기
      - ctl_table 초기화 예시 - drivers/scsi/scsi_sysctl.c 에 정의된 /proc/sys/dev/scsci/logging_level 파일 생성
```c
static ctl_table scsi_table[] = { 
  {
    .ctl_name     = DEV_SCSI_LOGGING_LEVEL,
    .procname     = "logging_level",            // 파일명
    .data         = &scsi_logging_level,        // 등록될 변수
    .maxlen       = sizeof(scsi_logging_level), // 정수 변수
    .mode         = 0644,                       // 권한 644 (모든 사람이 읽을수 있고 소유자만 쓸수 있음)
    .proc_handler = &dproc_dointvec             // 정수 배열 읽기/쓰기
  },
  { }
};

static ctl_table scsi_dir_table[] = {
  {
    .ctl_name     = DEV_SCSI,
    .procname     = "scsi",         // 디렉토리 명
    .mode         = 0555,
    .child        = scsi_table      // 하위에 scsi_table에 있는 파일/디렉토리 들을 가짐
  },
  { }
};

static ctl_table scsi_root_table[] = {
  {
    .ctl_name     = CTL_DEV,
    .procname     = "dev",
    .mode         = 0555,
    .child        = scsi_dir_table  // 하위에 scsi_dir_table에 있는 파일/디렉토리 들을 가짐
  },
  { }
};

int __init scsi_init_sysctl(void)
{
  scsi_table_header = register_sysctl_table(scsi_root_table, 1); // /proc/sys 아래 scsi_root_table 과 하위 노드를 계층으로 삽입
                                                                 // ctl_table 관리 리스트의 맨 앞에 삽입 (0이면 맨 뒤)
}

// 매번 위와 같은 구조를 작성하여 삽입하기 불편하므로 템플릿을 정의하고 새 파일을 추가할때 사용
// ex) 인접 서브시스템은 net/core/neightbour.c 에 있는 neigh_sysctl_register를 사용
```

    - 주요 네트워크 파일과 디렉토리
      - /proc/sys/net/bridge
      - /proc/sys/net/core
      - /proc/sys/net/ipv4/route, neigh, conf

### ioctl
- ifconfig로 보는 예시
  - 시스템 관리자가 "ifconfig eth0 mtu 1250" 입력
    - MTU 값을 변경하기 위해
  - ifconifg 가 소켓을 오픈
  - 관리자에게 받은 정보로 로컬 데이터 스트럭쳐 초기화
  - ioctl 호출을 통해 초기화된 데이터 스트럭쳐를 커널로 전달
```c
struct ifreq data;
fd = socket(PF_INET, SOCK_DGRAM, 0);
// data 초기화 시작
...
// data 초기화 끝
err = icotl(fd, SIOCIFMTU, &data) // SIOCIFMTU 는 어떤 명령을 처리할지에 대한 커맨드 변수
```
  - sock_ioctl에 단계에서 커맨드 변수 (여기서는 SIOCIFMTU) 에 따라 루틴 변경
    - sock_ioctl 단계에서 바로 처리 가능한 변수는 바로 처리
      - br_ioctl_hook (17장), br_vlan_hook : 브릿징 관련 처리
      - divert_ioctl, dlci_ioctl_hook
    - SIOCIFMTU 는 sock_ioctl 단계에서 처리가 불가능
  - sock_ioctl에서 처리가 불가능한 명령어는 Socket 을 통해 넘어온 데이터를 수신하여 inet_ioctl 단계에서 루틴 변경
    - devinet_ioctl
    - arp_ioctl (29장)
    - ip_rt_ioctl (36장)
    - SIOCIFMTU 는 inet_ioctl 단계에서 처리가 불가능
  - inet_ioctl에서 처리가 불가능한 명령어는 TCP/UDP 여부에 따라 tcp_ioctl, udp_ioctl 단계로 이동
    - tcp_ioctl / udp_ioctl 에서 처리가 가능한 명령어라면 처리
    - inet_ioctl 은 tcp_ioctl / udp_ioctl 에서 처리가 불가능
  - tcp_ioctl / udp_ioctl 단계에서 처리가 불가능한 명령어는 dev_ioctl로 전달
- 네트워크용 ioctl 명령어는 include/linux/socket.h 에 정의되어 있음
  - 디바이스 드라이버에서 새로운 명령어를 SIOCDEVPRIVATE와 SIOCDEVPRIVATE+15 사이 값으로 새로 정의 가능
    
### 넷링크
- 사용자 공간과 커널 사이에 IP 네트워크 설정시 선호하는 인터페이스
- 커널 내부 메시징 시스템으로도 사용됨
- 표준 소켓 API를 사용해서 접근 가능
  - domain: PF_NETLINK
  - type: SOCK_DGRAM
  - protocol
    - 네트워킹 스택의 컴포넌트나 컴포넌트 세트에 따라 여러개 정의 가능
    - NETLINK_ROUTE, NETLINK_FIREWALL 등
    - include/linux/netlink.h 에 NETLINK_XXX 이름으로 정의
- 넷링크 소켓의 endpoint는 PID를 통해 식별 가능
  - PID가 0인 경우는 커널 프로세스
- 유니캐스트, 멀티캐스트 사용 가능
  - 엔드포인트의 주소는 PID나 멀티캐스트의 그룹 아이디, 혹은 이 둘의 조합
    - 커널에서 특별한 이벤트의 알림을 사용할 때 넷링크 멀티캐스트 그룹 정의
      - ex) RTMGRP_IPV4_ROUTE, RTMGRP_NEIGH : 라우팅 테이블의 변경, L3-L2 주소 매핑 변경시 알림
    - 멀티캐스트 그룹은 include/linux/rtnetlink.h 내에 RTMGRT_XXX 형태로 정의
    - 그룹 관련된 내용은 6부, 7부에서 상세히 다룸
- acknowledgement (ACK) 값에 음수, 양수 모두 포함 가능
- ioctl 등에 비한 장점: 커널이 수동적으로 동작하는게 아니고 적극적인 전송의 초기화가 가능함
  - 소켓을 열어두고 있으면 커널이 정보를 먼저 전송하는게 가능하다는 이야기로 보임

### 설정 변경의 직렬화
- 사용자가 설정 변경시마다 커널 내부의 핸들러가 세마포어 (rtnl_sem)을 획득하여 네트워크 설정 정보에 접근하여 변경
- ioctl, netlink 모두 동일하게 동작
