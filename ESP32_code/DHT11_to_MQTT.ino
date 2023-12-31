// #include <WiFi.h>
// #include <PubSubClient.h>
// #include <DHT.h>

// #define DHT_PIN 25

// DHT dht(DHT_PIN, DHT11);

// #ifdef __cplusplus
// extern "C" {
// #endif
// uint8_t temprature_sens_read();
// #ifdef __cplusplus
// }
// #endif

// uint8_t temprature_sens_read();

// const char *ssid = "keripikUdang";      // Enter your WiFi name
// const char *password = "keripikMbote";  // Enter WiFi password

// const char *mqtt_broker = "broker.emqx.io";
// const char *topic = "esp32/data_dht";
// const char *mqtt_username = "emqx";
// const char *mqtt_password = "public";
// const int mqtt_port = 1883;

// WiFiClient espClient;
// PubSubClient client(espClient);

// void setup() {
//   delay(3000);
//   // Set software serial baud to 115200;
//   Serial.begin(115200);

//   // Connecting to a WiFi network
//   WiFi.begin(ssid, password);
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.println("Connecting to WiFi..");
//   }
//   Serial.println("Connected to the WiFi network");

//   // Connecting to a MQTT broker
//   client.setServer(mqtt_broker, mqtt_port);
//   while (!client.connected()) {
//     String client_id = "esp32testClient-";
//     client_id += String(WiFi.macAddress());
//     Serial.printf("The client %s connects to the public MQTT broker\n", client_id.c_str());
//     if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
//       Serial.println("Public EMQX MQTT broker connected");
//     } else {
//       Serial.print("Failed with state ");
//       Serial.print(client.state());
//       delay(2000);
//     }
//   }

//   dht.begin();
// }

// void loop() {
//   float temp = dht.readTemperature();
//   char temps[10];
//   sprintf(temps, "%3.2f", temp);
//   client.publish(topic, temps);
//   client.loop();
//   delay(1000);
// }
