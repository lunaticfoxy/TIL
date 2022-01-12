
### Local ( 로컬 ) ----> Remote (원격지)
- 단일 파일을 원격지로 보낼 때.
  - 구문 : # scp [옵션] [파일명] [원격지_id]@[원격지_ip]:[받는 위치]
    - scp testfile2 root@192.168.159.129:/tmp/testclient  

- 복수의 파일을 원격지로 보낼 때.
  - 구문 : # scp [옵션] [파일명 1] [파일명 2] [원격지_id]@[원격지_ip]:[받는 위치]
    - scp tesfile1 testfile2 root@192.168.159.129:/tmp/testclient

- 여러 파일을 포함하고 있는 디렉터리를 원격지로 보낼 때. ( -r 옵션을 사용합니다 )
  - 구문 : # scp [옵션] [디렉터리 이름] [원격지_id]@[원격지_ip]:[보낼 경로]
    - scp -r testgogo root@192.168.159.129:/tmp/testclient


### Remote ( 원격지 ) ---> Local ( 로컬 )
- 단일 파일을 원격지에서 로컬로 가져올 때
  - 구문 : # scp [옵션] [원격지_id]@[원격지_ip]:[원본 위치] [받는 위치]
    - scp root@192.168.159.129:/tmp/testclient/testfile2 /tmp
 
- 복수의 파일을 원격지에서 로컬로 가져올 때
  - 구문 : # scp [옵션] [원격지_id]@[원격지_ip]:[원본 위치 파일][원본 위치 파일] [받는 위치]
    - scp root@192.168.159.129:"/tmp/testclient/testfile2 /tmp/testclient/testfile3" /tmp

- 여러 개의 파일을 포함하는 디렉터리 원격지에서 로컬로 가져올 때
  - 구문: scp [옵션] [원격지_id]@[원격지_ip]:[디렉터리 위치] [받을 경로]
    - scp -r root@192.168.159.129:/tmp/testclient/testgogo /tmp

