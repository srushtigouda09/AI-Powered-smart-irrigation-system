#include <DHT.h>

#define DHTPIN 2         // DHT11 data pin connected to pin 2
#define DHTTYPE DHT11    // Using DHT11 sensor

DHT dht(DHTPIN, DHTTYPE);

int soilPin = A0;        // Soil moisture sensor analog pin
int pumpLed = 8;         // Pump indicator LED
int threshold = 600;     // Adjust after testing

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(pumpLed, OUTPUT);
  digitalWrite(pumpLed, LOW);
}

void loop() {
  int moistureValue = analogRead(soilPin);  // Read soil moisture
  float temperature = dht.readTemperature(); // Read temperature only

  if (isnan(temperature)) {
    Serial.println("Error reading DHT11 temp!");
    delay(2000);
    return;
  }

  bool pumpOn = false;
  if (moistureValue > threshold) {
    pumpOn = true;
    digitalWrite(pumpLed, HIGH); // LED ON = pump ON
  } else {
    pumpOn = false;
    digitalWrite(pumpLed, LOW);  // LED OFF = pump OFF
  }

  Serial.print("moisture=");
  Serial.print(moistureValue);
  Serial.print(";temp=");
  Serial.print(temperature);
  Serial.print(";pump=");
  Serial.println(pumpOn ? "ON" : "OFF");

  delay(1000);
}
