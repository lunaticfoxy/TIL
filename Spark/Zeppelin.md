# 제플린과 관련된 정보들을 모으는 문서

### k8s 에서 제플린 돌리기
- 제플린은 k8s에서 별도의 팟을 생성하여 인터프리터를 실행시킬 수 있다
  - 그리고 이를 기본값으로 사용한다
- 하지만 이게 문제가 될 수 있다
  - k8s의 권한 지정이 복잡할때
  - 팟을 새로 띄우기 애매한 상황일때
- 이경우 zeppelin.run.mode 설정 값을 바꿔서 로컬에서 동작하게 가능하다
  - conf/zeppelin-site.xml 파일내 zeppelin.run.mode 값 변경
  - conf/zeppelin-site.xml 파일이 없다면 conf/zeppelin-site.xml.template 파일 이름을 변경 후 값 변경
  - 설정값 별 동작
    - auto : 알아서 동작
    - local : 로컬 환경에 프로세스만 새로 띄워서 동작 (가장 기본적이고 문제 없음)
    - k8s : 별도의 k8s 팟을 띄워서 동작
    - docker : 인터프리터용 도커를 띄어서 동작
