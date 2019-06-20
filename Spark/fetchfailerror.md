#### Fetch failed 에러
- 의미
  - 말그대로 노드에 작업 할당 과정 자체에서 에러발생
  - 기본 할당 자체가 불가능하면 Meta Fetch failed가 발생하기도 함
- 발생원인
  - 노드 메모리 부족
    - 처리할 데이터를 가져와야되는데 메모리 부족
    - 혹은 어떤 작업을 해야하는지 메타 정보 자체를 저장하기도 메모리가 부족할때
  - 네트워크 장애
    - 현실적으로 생기기 어려움
    - 웬만한 네트워크 장애라면 해당 노드에 아예 잡이 배치도 안될것
    - 데이터 배치하는 순간만 장애가 날경우 발생 가능성은 있음
  - 저장공간 문제
    - 가상메모리 할당도 불가능할 정도의 저장공간만 남으면 발생가능
    - 드라이버 노드에서 생길 가능성 높음
- 메모리부족 해결방법
  - 중간테이블 생성
    - 2개 테이블 조인하다 생기는 문제면 답없음
  - 데이터 분할처리
    - 수동처리
      - 코드로 직접 데이터를 나눠서 받아 처리하고 이후 합치도록 구성
        - union 보다 join이 훨씬 큰 자원을 먹는다는 점을 이용
        - repartition은 꼭 할필요는 없지만 성능 향상에 도움이 될 가능성이 존재
      - 예시 방법
```scala
val df1 = spark.sql("select * from tb1")
val df2 = spark.sql("select * from tb2")

val cutSize = 5
val dfSeq = (0 until 5).map{i =>
                        df1.filter(df1("key")%5==i).repartition("key")
                          .join(df2.filter(df("key")%5==i).repartition("key"), df1("key")===df2("key"), "full outer")
             }

def unionAll(df, dfs:Seq[Dataframe]) : Dataframe = {
  if(dfs.length == 0)
    df
  else if(df==null)
    unionAll(dfs(0), dfs.drop(1))
  else
    unionAll(df.union(dfs(0), dfs.drop(1))
}

val dfAll = unionAll(null, dfSeq)
```
      - 주의사항: 나눌 Key가 일정한 비율로 나뉜다는걸 가정해야 한다
        - 꼭 일정하지는 않아도 한 df로 너무 많이 들어가면 문제가 된다
    - 자동처리
      - 노드를 늘리면 알아서 데이터가 분할된다!
      - 머니 이즈 파워!
- 유사한 문제
  - java heap overflow
  - out of memory
- 주의사항
  - executer 메모리를 할당하는 과정에서 노드 메모리를 풀로 먹는것
  - 따라서 executer 메모리 크기를 늘려서의 해결은 불가능
