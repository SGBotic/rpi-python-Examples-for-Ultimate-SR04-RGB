# Python examples for SGBotic Ultimate SR04 RGB Ultrasonic Sensor

![03248_github](https://user-images.githubusercontent.com/2862935/136160932-7d405714-955f-415a-843e-dcd4038eb9ee.jpg)

Python examples for [Ultimate SR04 RGB Ultrasonic Sensor](https://www.sgbotic.com/index.php?dispatch=products.view&product_id=3248), an I2C ultrasonic sensor with illuminate transceiver.

These examples to be run on Python3.

## Setup I2C in Raspberry Pi

* go to Menu >> Preferences >> Raspberry Pi Configuration to enable I2C interface

* Install “python-smbus” and “i2c-tools”
```blocks
sudo apt-get update
sudo apt-get install -y python-smbus i2c-tools
```

* Scan the connected I2C devices
```blocks
i2cdetect -y 1
```