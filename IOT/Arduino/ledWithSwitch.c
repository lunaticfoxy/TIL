/*
주의사항
- 단순히 스위치와 전원만 연결하면 값이 튀게 된다
  - 값이 들어가는쪽에서도 전류가 나오니 이 전류를 읽을수도 있다
  - 이를 플로팅 현상 (값이 뜬다) 이라고 함
- 이를 막기 위해서는 값이 들어가는쪽을 미리 저항 + 그라운드로 연결해놓는다
  - 미리 초기값을 0으로 확실히 고정
- 이후 반대쪽에 전원을 연결하면 스위치가 눌릴때만 1값이 들어오게 된다
*/

int led_r = 6;
int led_g = 5;
int led_b = 7;
int btn = 8;

int state = 0;
int changed = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(led_b, OUTPUT);
  pinMode(btn, INPUT);
  Serial.begin(9600);
  Serial.println("Serial Connected");
}

void loop() {
  // put your main code here, to run repeatedly:
  switch(state){
    case 0:
      digitalWrite(led_r, LOW);
      digitalWrite(led_g, LOW);
      digitalWrite(led_b, LOW);
      break;
    case 1:
      digitalWrite(led_r, HIGH);
      digitalWrite(led_g, LOW);
      digitalWrite(led_b, LOW);
      break;
    case 2:
      digitalWrite(led_r, LOW);
      digitalWrite(led_g, HIGH);
      digitalWrite(led_b, LOW);
      break;
    case 3:
      digitalWrite(led_r, LOW);
      digitalWrite(led_g, LOW);
      digitalWrite(led_b, HIGH);
      break;
  }

  char buf[64];
  int btn_state = digitalRead(btn);
  sprintf(buf, "%d", btn_state);
  Serial.println(buf);
  if(changed == 0 && btn_state == 1) {
    state = (state + 1)%4;
    changed = 1;
  }
  else if(changed == 1 && btn_state == 0)
    changed = 0;

}
