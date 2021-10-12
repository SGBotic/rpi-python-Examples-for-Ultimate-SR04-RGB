# example code for SGBotic Ultimate SR04 RGB
# this code is to change the I2C address of the above mentioned module
# Power cycle the unit for this change to take effect

# run on Raspberry Pi, Python3

from smbus import SMBus
import time

# Create a new I2C bus
i2cbus = SMBus(1)

#define I2C address
i2cAddr = 0x60
setI2cAddressRegister = 0xE0

#valid value from 0x08 to 0x71
newI2cAddr = 0x61

#start of main program
i2cbus.write_byte_data(i2cAddr, setI2cAddressRegister, newI2cAddr)
print("I2C address has been changed to %s" % newI2cAddr)
print("Power cycle the unit for this change to take effect")
print("")
  
