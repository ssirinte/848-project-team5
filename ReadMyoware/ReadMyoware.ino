#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>

const int MYOPIN = A5;
const int PULSEPIN = A0;
const int GSRPIN = A2;
const int MYO2 = A1;
const int LED13 = 13;

int myoVal; 
int myoVal2;
int pulseVal;
int gsrVal;

int index;
int gsrArray[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int pulseThreshold = 550;

PulseSensorPlayground pulseSensor;

void setup() {
  index = 0;
  pinMode(LED13,OUTPUT); //pin will blink with heartrate
  Serial.begin(9600);   // initialize serial communication at 9600 bits per second:
  //Serial.println("We are ready to start sensing !");
  pulseSensor.analogInput(PULSEPIN);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(pulseThreshold);

}

int average (int* arr, int len) {
  int sum = 0;
  for (int i = 0; i < len; i++) {
    sum += arr[i];
  }
  return (sum/len);
}


void loop() {
  // read the input on analog pin 0:
  myoVal = analogRead(MYOPIN);
  myoVal2 = analogRead(MYO2);
  //pulseVal = analogRead(PULSEPIN);
  gsrArray[index] = analogRead(GSRPIN);
  gsrVal = average(gsrArray, 10);
  index = (index + 1)%10;

  int myBPM = pulseSensor.getBeatsPerMinute();

  Serial.print(myoVal);
  Serial.print(",");
  Serial.println(myoVal2);
//  Serial.print(",");
//  Serial.println(gsrVal);

  delay(5);        // delay in between reads for stability
}
