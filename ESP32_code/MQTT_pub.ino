// #include <WiFi.h>
// #include <PubSubClient.h>

// #ifdef __cplusplus
// extern "C" {
// #endif
// uint8_t temprature_sens_read();
// #ifdef __cplusplus
// }
// #endif
// uint8_t temprature_sens_read();

// // WiFi
// const char *ssid = "keripikUdang"; // Enter your WiFi name
// const char *password = "keripikMbote"; // Enter WiFi password

// // MQTT Broker
// const char *mqtt_broker = "broker.emqx.io";
// const char *topic = "esp32/data_dht";
// const char *mqtt_username = "emqx";
// const char *mqtt_password = "public";
// const int mqtt_port = 1883;

// WiFiClient espClient;
// PubSubClient client(espClient);

// void setup() {
//   // Set software serial baud to 115200;
//   Serial.begin(115200);
//   // connecting to a WiFi network
//   WiFi.begin(ssid, password);
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.println("Connecting to WiFi..");
//   }
//   Serial.println("Connected to the WiFi network");

//   //connecting to a mqtt broker
//   client.setServer(mqtt_broker, mqtt_port);

//   while (!client.connected()) {
//     String client_id = "esp32testClient-";
//     client_id += String(WiFi.macAddress());
//     Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
//     if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
//       Serial.println("Public emqx mqtt broker connected");
//     } else {
//       Serial.print("failed with state ");
//       Serial.print(client.state());
//       delay(2000);
//     }
//   }
// }

// void loop() {
//   // float temp = (temprature_sens_read() - 32) / 1.8;
//   float temp = random(20, 40);
//   char temps[10];
//   sprintf(temps,"%3.2f", temp);
//   client.publish(topic, temps);
//   client.loop();
//   delay(1000);
// }