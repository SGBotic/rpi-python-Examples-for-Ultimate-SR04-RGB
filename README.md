# Python examples for SGBotic Ultimate SR04 RGB Ultrasonic Sensor

Python example for [Ultimate SR04 RGB Ultrasonic Sensor](https://www.sgbotic.com/index.php?dispatch=products.view&product_id=3248), an I2C ultrasonic sensor with illuminate transceiver.

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