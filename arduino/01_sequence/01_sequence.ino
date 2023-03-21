const int lampAPin = 3;
const int lampBPin = 5;
const int lampCPin = 6;
const int lampDPin = 10;

const int lampPins[] = {lampAPin, lampBPin, lampCPin, lampDPin};

void setup() {
  pinMode(lampAPin, OUTPUT);
  pinMode(lampBPin, OUTPUT);
  pinMode(lampCPin, OUTPUT);
  pinMode(lampDPin, OUTPUT);
}

void loop() {
    for (int i = 0; i < 4; i++) {
      digitalWrite(lampPins[i], HIGH);
      delay(500);
    }
    for (int i = 0; i < 4; i++) {
      digitalWrite(lampPins[i], LOW);
      delay(500);
    }
}
