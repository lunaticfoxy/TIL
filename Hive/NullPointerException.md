## Hive에서 나타나는 NullPointerException 케이스들

### Tez 기반 환경에서 UNION ALL 사용시
- 원인: 테이블 조건중 하나라도 데이터가 없다면 에러 발생
  - 실제로는 데이터가 있어도 발생하는 경우 확인
- 해결 방법: set hive.vectorized.execution.enabled = false;
