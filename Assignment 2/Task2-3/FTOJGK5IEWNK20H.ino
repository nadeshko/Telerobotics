// Magetometer offsets:
#define MPU9150addr 0x68
#define MXOFFSET 0
#define MYOFFSET 0
#define MZOFFSET 0

#include "Wire.h"

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include <I2Cdev.h>
#include "MPU6050.h"
#include "math.h"

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro(MPU9150addr);

float hdg, fax, fay, faz, fgx, fgy, fgz, fmx, fmy, fmz;
boolean AccelWkg; // Accelerometer present and working?

#define LED_PIN 13
bool blinkState = false;
uint8_t LED13count= 0;

void setup() {
  // put your setup code here, to run once:
    Wire.begin();

    // initialize serial communication
    // (38400 chosen because it works as well at 8MHz as it does at 16MHz, but
    // it's really up to you depending on your project)
    Serial.begin(38400);

    // initialize device
    Serial.println("Initializing I2C devices...");
    accelgyro.initialize();

    // verify connection
    Serial.println("Testing device connections...");
    AccelWkg = accelgyro.testConnection();
    Serial.println(AccelWkg ? "MPU6050 connection successful" : "MPU6050 connection failed");

    // configure Arduino LED for
    pinMode(LED_PIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
    float delta, motion;
    float fLLed, fRLed;
    uint8_t LColour, RColour;
    uint32_t colour32;
    int deltaColour;
    char line[256];
    
    if (AccelWkg) {
      readAccel();
      readMag();

      // display tab-separated accel/gyro x/y/z values
      sprintf(line, "a: %4d %4d %4d\tg: %4d %4d %4d\tm: %6d %6d %6d\thdg: %3d\n",
          int(fax*100), int(fay*100), int(faz*100),
          int(fgx), int(fgy), int(fgz), int(fmx), int(fmy), int(fmz), int(hdg));
          Serial.write(line);
          Serial.flush();
      delay(250);
    }
}

void readAccel() {
    int16_t ax, ay, az;
    int16_t gx, gy, gz;
    char line[256];
    // read raw accel/gyro measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    // these methods (and a few others) are also available
    //accelgyro.getAcceleration(&ax, &ay, &az);
    //accelgyro.getRotation(&gx, &gy, &gz);
    // Convert accel to G
    fax = float(ax)/16384; fay = float(ay)/16384; faz = float(az)/16384;
    
    // Convert gyro to float deg/sec
    fgx = float(gx)/131.072; fgy = float(gy)/131.072; fgz = float(gz)/131.072;
    
}

void readMag() {
  int16_t mx, my, mz;
  accelgyro.getMag(&mx, &my, &mz);
  // Apply offets to magnetometer
  mx -= MXOFFSET; my -= MYOFFSET; mz -= MZOFFSET;
  fmx = float(mx); fmy = float(my); fmz = float(mz);
  
  hdg = atan2(-fmy, fmx) * 180 / 3.14159;
  if (hdg < 0) hdg += 360;
}

