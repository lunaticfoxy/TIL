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
