#### Hive Query에서 distinct와 group by 비교
##### (주의 - 당연히 다른 쿼리지만 단순 카운트를 하고싶을때 동일하게 사용할 수 있는 경우에 대한 비교)

#### 성능 비교시
- node의 수가 적을 경우: distinct가 유리
- node의 수가 많을 경우: group by 가 유리

#### 원인
- count(distinct key) 동작 원리
  - mapper가 각자 카운트를 한다
  - reducer가 이걸 모아서 중복을 제거한다 <- 여기가 병목
- count(*) group by key 동작 원리
  - mapper가 그룹을 묶은 뒤 그룹 내에서 count를 한다
  - reducer가 이를 종합한다
- distinct의 중복 제거와 group by의 그룹을 묶는 행위가 사실상 동일한 동작
  - reducer가 혼자 하냐, mapper가 나눠서 하냐의 차이뿐
  - 따라서 보다 많은 노드에서 일어나는 group by 의 성능이 좋음
  
  
#### 주의사항
- 이건 쌩 hive 쿼리에서만 일어나는 일임
- 내부적으로 최적화를 해주는 임팔라나 스파크에서는 의미 
  
