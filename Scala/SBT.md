### 스칼라에서 빌드시 사용하는 SBT (Simple Build Tool) 에 관한 내용 정리

#### 명령어
- tasks : 해당 프로젝트에서 사용하는 주요 명령어들을 파악할 수 있다.
- console : 줄 단위로 실행가능한 콘솔을 통해서 프로젝트 내에서 컴파일된 클래스들을 사용해 볼 수 있다.
- clean : target에 컴파일된 모든 파일들을 삭제
- settings : build.sbt에서 지정가능한 목록들과 설명을 보여준다.
- reload : buils.sbt나 소스코드 등 프로젝트 내 변경사항이 있을 때 다시 로드해준다.
- ~ compile : 관리하는 소스코드가 추가되거나 변경될 때 자동으로 컴파일하도록 한다.
- compile : 소스코드를 컴파일한다.
- run : test/src/ 소스코드를 실행한다.
- test : 소스코드를 컴파일하고 실행한다. (compile + run)
