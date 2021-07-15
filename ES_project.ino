#include <time.h>
#include <ESP8266WiFi.h>
int val;
int LEDPin = 4;
int tempPin = A0;
boolean temperature_flag = false;
boolean pulse_flag = false;
boolean BP_flag = false;
boolean BO_flag = false;
const char* ssid = "MmM";
const char* password = "091907143411";
void setup()
{
  pinMode(LEDPin, OUTPUT);
  //  digitalWrite(LEDPin, LOW);
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
}
void loop()
{

    srand(time(0));

  // pulse //

    int pulse = (rand() % (120 - 50 + 1)) + 50;
    if (pulse < 60 || pulse > 100) {
      pulse_flag = true;
    }
    Serial.print("pulse:");
    Serial.println(pulse);
  
    // blood pressure //
  
    int SBP = (rand() % (145 - 110 + 1)) + 110; // Systolic Blood Pressure
    int DBP = (rand() % (95 - 70 + 1)) + 70; // Diastolic Blood Pressure
  
    if (SBP > 120 || DBP > 80) {
      BP_flag = true;
    }
    Serial.print("SBP:");
    Serial.println(SBP);
    Serial.print("DBP:");
    Serial.println(DBP);
  
    // blood oxygen //
  
    int BO = (rand() % (100 - 80 + 1)) + 80;
    if (BO < 95) {
      BO_flag = true;
    }
    Serial.print("BO:");
    Serial.println(BO);
  
    // temperature //
  
    val = analogRead(tempPin);
    // Convert the reading into voltage:
    float voltage = val * (3200 / 1024.0);
    // Convert the voltage into the temperature in degree Celsius:
    float temperature = voltage / 10;
    if (temperature < 36.5 || temperature > 37.5) {
      temperature_flag = true;
    }
    Serial.print("temp:");
    Serial.println(temperature);
  
    if (temperature_flag || BO_flag || BP_flag || pulse_flag) {
      digitalWrite(LEDPin, HIGH);
    }
    delay(1000 * 60); // delay one minute
    temperature_flag = false;
    pulse_flag = false;
    BP_flag = false;
    BO_flag = false;
}
