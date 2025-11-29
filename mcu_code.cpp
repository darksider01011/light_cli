#include <Wire.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80); // Web server on port 80

const int green = D3;

const char* ssid = "timer";
const char* password = "33771610mA-";

void setup() {
  WiFi.softAP(ssid, password);
  Serial.begin(9600);
  pinMode(green, OUTPUT);


  // on
  server.on("/off", HTTP_GET, []() {
    server.send(200, "text/html", getHTML());
    digitalWrite(green, LOW);
    Serial.println("ON");
  });

  // off
  server.on("/on", HTTP_GET, []() {
    server.send(200, "text/html", getHTML());
    digitalWrite(green, HIGH);
    Serial.println("off");
  });
  
  // Start the server
  server.begin();
}

String getHTML() {
  String ptr = "<!DOCTYPE html> <html>\n";
  return ptr;
}

void loop() {
    server.handleClient();
}
