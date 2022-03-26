#include <Servo.h>

Servo rod;
Servo base;
Servo arm1;
Servo arm2;
Servo rotate;

const int reset=12;

float positionX;
float baseAngle;
float arm1Angle;
float arm2Angle;
float rotateAngle;




void setup() {
  // put your setup code here, to run once:
  base.attach(9);
  arm1.attach(6);
  arm2.attach(5);
  rotate.attach(11);
  rod.attach(10);

  pinMode(reset, INPUT);
  rotate.write(rotateAngle);

  Serial.begin(9600);

}

void loop() {
  float baseAngle=90;
  float arm1Angle=90;
  float arm2Angle=90;
  float rotateAngle=0;
  int testTime=10000; //How long should robot stay in position(in ms)

  Serial.println("Begin");

  Serial.println("Enter Base Angle:");
  delay(5000);
  
    while (Serial.available()==0){
    }
    if (Serial.available() > 0){
      baseAngle=Serial.parseFloat();
      base.write(baseAngle);
      Serial.flush();
    }

    Serial.println("Enter Arm 1 Angle:");
    while (Serial.available()==0){
    }
    if (Serial.available() > 0){
      arm1Angle=Serial.parseFloat();
      arm1.write(arm1Angle);
      Serial.flush();
    }

    Serial.println("Enter Arm 2 Angle:");
    while (Serial.available()==0){
    }
    
    if (Serial.available() > 0){
      arm2Angle=Serial.parseFloat();
      arm2.write(arm2Angle);
      Serial.flush();
      delay(1000);
    }
    
    Serial.println("Enter Rotate Angle:");
    while (Serial.available()==0){
    }
    if (Serial.available() > 0){
      rotateAngle=Serial.parseFloat();
      rotate.write(rotateAngle);
      Serial.flush();
    }
    
  
  delay(testTime);

  Serial.println("Moving to Origin");
  base.write(90);
  arm1.write(90);
  arm2.write(90);
  rotate.write(0);
  
}
