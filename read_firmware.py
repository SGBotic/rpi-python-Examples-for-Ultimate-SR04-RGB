# python code for SGBotic Ultimate SR04 RGB
# this code is to read the firmware version

# run on Raspberry Pi, Python3

from smbus import SMBus

i2cAddr = 0x60
versionRegister = 0xF0

# Create a new I2C bus
i2cbus = SMBus(1)  

#start of main program
version = i2cbus.read_byte_data(i2cAddr, versionRegister)
print("firmware version: %s" % version)
print("")
print("")
  
