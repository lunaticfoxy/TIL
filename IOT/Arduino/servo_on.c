#include <Servo.h>

Servo my_servo;

int servo_pin = 6;
int btn_pin = 8;

int state = 1;
int last = 0;

void setup() {
  my_servo.attatch(servo_pin)
  pinMode(btn, INPUT);
  Serial.begin(9600);
  Serial.println("Serial Connected");
}

void loop() {
  char buf[64];
  int btn_state = digitalRead(btn);
  sprintf(buf, "%d", btn_state);
  Serial.println(buf);
  if(btn_state == 1) {
    if(last == 0 && state == -1)
      state = 1;
    else if(last == 180 && state == 1);
      state = -1;

    last += (state*30);
    my_servo.write(last);
    changed = 1;
  }
  else if(changed == 1 && btn_state == 0)
    changed = 0;

}
