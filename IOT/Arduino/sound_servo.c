#include <LCDIC2.h>



#include <Servo.h>
#include <Wire.h>

Servo my_servo;
LCDIC2  lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display

int sound_pin = A2;
int servo_pin = 6;

int state = 1;
int last = 0;
int changed = 0;

void setup() {
  my_servo.attach(servo_pin);
  
  Serial.begin(9600);
  Serial.println("Serial Connected");

}

void loop() {
  int sound_val = analogRead(sound_pin);
  char buf[64];
  sprintf(buf, "%3d", sound_val);
  Serial.println(buf);
  
  if(sound_val >= 70 && changed == 0) {
    //Serial.println(buf);
    if(last <= 0)
      state = 1;
    else if(last >= 180)
      state = -1;

    last += (state*30);
    my_servo.write(last);
    changed = 1;
  }
  else if(changed == 1 && sound_val < 70)
    changed = 0;

}
