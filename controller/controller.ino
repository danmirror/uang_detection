#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>

SoftwareSerial mySerial(9, 8);

void setup () {
  Serial.begin (115200);
  mySerial.begin (9600);
  mp3_set_serial (mySerial);
  delay(10);
  mp3_set_volume (15);
}

void loop () {

  if (Serial.available() > 0) 
  {
   char data = Serial.read();
    
   if(data='1'){
    mp3_play(2);

    delay(5000);
   }
   
   else{
    mp3_play(1);
  
    delay(5000);
   }
   Serial.println('1');
 
    
  }

}
