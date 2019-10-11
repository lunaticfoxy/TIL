#### Hive에서 메모리가 부족하진 않은데 할당 실패가 뜨는경우
- 메모리 제한의 70% 정도로 자바 최대 메모리 옵션을 준다
- 정확한 이유는 알수없으나 jvm 자체 공간 할당에 이슈가 있는듯 함
```hql
SET mapreduce.map.memory.mb=1024;
SET mapreduce.map.java.opts=-Xmx717m;
SET mapreduce.reduce.memory.mb=1024;
SET mapreduce.reduce.java.opts=-Xmx717m;
```
