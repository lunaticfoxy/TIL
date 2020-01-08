### 스칼라에서 빌드시 사용하는 SBT (Simple Build Tool) 에 관한 내용 정리

#### 프로젝트 구조
- project: 프로젝트 정의 파일들
  - project/build/.scala: 주 프로젝트 정의 파일
  - project/build/.properties: 프로젝트, sbt, 스칼라 버전 정의
- src: 소스코드
  - src/main: 앱 코드가 이 디렉터리 아래 들어감. 
    - src/main/scala : 코드가 스칼라일 경우
    - src/main/java : 코드가 자바일 경우
    - src/main/resources – jar에 추가하고픈 정적 파일들(예: 로그 설정 파일 등)
  - src/test: 앱 코드는 src/main에, 테스트 코드는 여기에 넣는다
- lib_managed: 프로젝트에서 사용하는(의존하는) jar 파일들. sbt update를 하면 여기에 jar들이 다운로드됨.
- target: 빌드시 만들어지는 것들이 들어가는 곳(예: generated thrift code, class files, jars)

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


#### Dependency 추가
- 기본적으로는 Maven과 유사
- build.sbt에 정의
- libraryDependencies 시퀀스에 라이브러리 추가
- resolvers 시퀀스에 리포지토리 추가 가능
```scala
libraryDependencies ++= Seq(
  groupID % artifactID % revision,
  groupID % otherID % otherRevision
)

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.0" % "provided",
  "org.apache.spark" %% "spark-sql" % "1.6.0" % "provided",
  "org.apache.spark" %% "spark-hive" % "1.6.0" % "provided"
)

resolvers += name at location

#ex> resolvers += "Sonatype OSS Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots"
```


#### Packaging
- maven에서 dependency libraries를 함께 packaging 하는 것과 동일한 개념
- build.sbt에 다음 내용을 추가
  - assemblyJarName in assembly :=  artifact.value.name + "-" + version.value + "." + artifact.value.extension

```scala
assemblyMergeStrategy in assembly := {
  case PathList("javax", "servlet", xs @ _*)         => MergeStrategy.first
  case PathList(ps @ _*) if ps.last endsWith ".html" => MergeStrategy.first
  case "application.conf"                            => MergeStrategy.concat
  case "unwanted.txt"                                => MergeStrategy.discard
  case x =>
    val oldStrategy = (assemblyMergeStrategy in assembly).value
    oldStrategy(x)
}
```

```scala
assemblyMergeStrategy in assembly := {
  case PathList("com","payco",xs @ _*) => MergeStrategy.last
  case _ => MergeStrategy.discard
}
```
- 다음 명령어로 패키지 생성
  - sbt clean assembly
