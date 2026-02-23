int redled1 = 8;
int redled2 = 9;
int redled3 = 10;


void setup() {
  Serial.begin(9600);
  pinMode(redled1, OUTPUT);
  pinMode(redled2, OUTPUT);
  pinMode(redled3, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') {
      red_half();
    } 
  }
}


void red_half() {
  on(redled1);
  on(redled2);
  on(redled3);
  off(redled1);
  off(redled2);
  off(redled3);
}

void on(int led) {
  digitalWrite(led, HIGH);
}

void off(int led) {
  digitalWrite(led, LOW);
}
