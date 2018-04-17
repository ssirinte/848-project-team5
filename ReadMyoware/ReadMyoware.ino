const int MYOPIN = A1;
const int PULSEPIN = A0;
const int GSRPIN = A2;
const int LED13 = 13;

int myoVal; 
int pulseVal;
int gsrVal;

int index;
int gsrArray[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int pulseThreshold = 550;



void setup() {
  index = 0;
  pinMode(LED13,OUTPUT); //pin will blink with heartrate
  Serial.begin(9600);   // initialize serial communication at 9600 bits per second:
  Serial.println("We are ready to start sensing !");

}

int average (int* arr, int len) {
  int sum = 0;
  for (int i = 0; i < len; i++) {
    sum += arr[i];
  }
  return (sum/len);
}

//void keyPressed(){
//    output.flush();
//    output.close();
//    exit(); 
//  }

void loop() {
  // read the input on analog pin 0:
  myoVal = analogRead(MYOPIN);
  pulseVal = analogRead(PULSEPIN);
  gsrArray[index] = analogRead(GSRPIN);
  gsrVal = average(gsrArray, 10);
  index = (index + 1)%10;
  
  if(pulseVal > pulseThreshold){                        
     digitalWrite(LED13,HIGH);
  } else {
     digitalWrite(LED13,LOW);
  }

  Serial.println(myoVal);
//  Serial.print(",");
//  Serial.print(pulseVal);
//  Serial.print(",");
//  Serial.println(gsrVal);

  delay(5);        // delay in between reads for stability
}
