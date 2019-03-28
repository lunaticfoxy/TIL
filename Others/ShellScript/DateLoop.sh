# 시작 날짜부터 종료 날짜까지 반복해서 출력하는 쉘 스크립트
#
# `date +"%Y-%m-%d" -d "07/02/2018"` 형태로 날짜 포맷 생성 가능
# `date +"%Y-%m-%d" -d "$NOW + 1 day"` 형태로 날짜에 덧셈 연산 가능
#
# 어려운 내용은 아니지만 띄어쓰기 주의할것


TARGET=`date +"%Y-%m-%d" -d "07/02/2018"`
END=`date +"%Y-%m-%d" -d "03/27/2019"`

echo $NOW
echo $END

echo $NOW
while [ "$NOW" != "$END" ];
do
    echo $NOW
    NOW=`date +"%Y-%m-%d" -d "$NOW + 1 day"`
done
