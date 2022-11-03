// C++ code
//

int inputPin0 = A0;
int inputPin1 = A1;
int outputPin0 = 13;
int outputPin1 = 12;

int buttonPin = 7;
int buttonLedPin = 11;


int sensorValue0 = 0;
int sensorValue1 = 0;

int buttonValue = 0;

void setup()
{
  pinMode(outputPin0, OUTPUT);
  pinMode(outputPin1, OUTPUT);
  
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buttonLedPin, OUTPUT);
}

void loop()
{
  // Read from sensor
  sensorValue0 = analogRead(inputPin0);
  sensorValue1 = analogRead(inputPin1);
  
  // Read from button
  buttonValue = digitalRead(buttonPin);
  
  // Just for temp sensor, convert to readable celsius
  sensorValue0 = sensorValue0 * 0.248;
  sensorValue1 = sensorValue1 * 0.248;
  
  // Conditionals
  if (sensorValue0 > 50)
  {
	digitalWrite(outputPin0, HIGH);
    delay(500);
  }
  
  else {
    digitalWrite(outputPin0, LOW);
    delay(500);
  }
  
  
  if (sensorValue1 > 50)
  {
	digitalWrite(outputPin1, HIGH);
    delay(500);
  }
  
  else {
    digitalWrite(outputPin1, LOW);
    delay(500);
  }
  
  // For button
  if (buttonValue == HIGH)
  {
	digitalWrite(buttonLedPin, LOW);
  }

  else {
    digitalWrite(buttonLedPin, HIGH);
  }
}
