#include <WiFi.h>
#include<Wire.h>
#define SSID "ALHN-77C6"
#define PASSWD "5420965120"

unsigned long int last_time = millis();

const uint16_t port = 123;
const char * host = "192.168.1.65";

//const int MPU=0x68;  // endereço I2C do MPU-6050
int16_t GyX,GyY,GyZ;
 
void setup(){
  
    Wire.begin();
    Wire.beginTransmission(0b1101000);
    Wire.write(0x6B);  // registro PWR_MGMT_1
    Wire.write(0b00000000);     // definido como zero (ativa o MPU-6050)
    Wire.endTransmission(true);
    Serial.begin(115200);;
 
    WiFi.begin(SSID,PASSWD);
    while (WiFi.status() != WL_CONNECTED){delay(100);}
 
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
}
 
void loop(){
    WiFiClient client;
 
    if (!client.connect(host, port)) {
        Serial.println("Falha de conexao");
        delay(1000);
        return;
    }   
    Serial.println("Conectado!");

    Wire.beginTransmission(0b1101000);
    Wire.write(0x43);  // começando com o registro 0x43 (GYRO_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(0b1101000,30);  // solicitar um total de 6 registros
    GyX=Wire.read()<<8|Wire.read();  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
    GyY=Wire.read()<<8|Wire.read();  // 0x45 (GYRO_YOUT_H) e 0x46 (GYRO_YOUT_L)
    GyZ=Wire.read()<<8|Wire.read();  // 0x47 (GYRO_ZOUT_H) e 0x48 (GYRO_ZOUT_L)
    Serial.print("Giroscópio: ");
    int Gix = GyX/82+2;
    int Giy = GyY/80;
    int Giz = GyZ/81+2;
    Serial.print("X = "); Serial.print(Gix);
    Serial.print(" | Y = "); Serial.print(Giy);
    Serial.print(" | Z = "); Serial.println(Giz);
    
    client.print(" "); client.print(Gix);
    client.print(" "); client.print(Giy);
    client.print(" "); client.println(Giz);
 
    //client.print("Hell low word");
 
    //Serial.println("Desconectando...");
    client.stop();
 
    //Serial.print("Aguardando 15 segundos para proximo envio:");
    while ((millis()-last_time) < 130){
      delay(4);}
    last_time = millis();
}
