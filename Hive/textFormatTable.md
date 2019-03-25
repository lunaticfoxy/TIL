Hive에서 텍스트 포맷으로 테이블 구성하기


'''sql
create table text_table_name
row format delimited fields terminated by ','
lines terminated by '\n'
stored as textfile
as
select * from source_table_name
;
'''

텍스트 포맷 테이블은 어떤 경우에 용이한가
- 내가 직접 테이블 파일을 볼 필요가 있을때
- 타 플랫폼에서 사용할 필요가 있을때
- 타 하둡으로 테이블을 이전할 가능성이 있을때
  - 하둡간 버전이나 설정 차이로 인해 포맷에 차이가 있을 경우가 있으므로 텍스트로 하는 방법이 확실
- 텍스트 데이터만 취급할경우 속도 향상
  
텍스트 포맷 테이블은 어떤 경우에 불리한가
- 미압축 -> 용량을 많이 차지함
- 텍스트 데이터가 아닌 경우 속도 하락
- 정확한 포맷을 지정하기 어려움
