# 함수와 관련된 내용 정리

### 스크립트 내의 함수를 입력받아 실행하는 코드

```sh
## test.sh 파일

function TestFunction() {
    TARGET_DATE=$1
    PARAM1=$2
    PARAM2=$3
    echo "TestFunction ${TARGET_DATE} ${PARAM1} ${PARAM2}"
}


CMD=$1
shift
if [ "x$1" == "x" ] ; then
    TARGET_DATE=`date --date='yesterday' +'%Y-%m-%d' `
else
    TARGET_DATE=$1
fi
shift || true
$CMD $TARGET_DATE $*
```

```sh
## 실행법
bash -e test.sh TestFunction param1 param2
```
