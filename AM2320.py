import time
import smbus

i2c = smbus.SMBus(1)
address = 0x5c

def GetTemp():
    loop = True
    block = []
    while loop:
        try:
            i2c.write_i2c_block_data(address, 0x00,[])
            i2c.write_i2c_block_data(address, 0x03,[0x02, 0x02])

            time.sleep(0.05)

            block = i2c.read_i2c_block_data(address, 0, 4)
            loop = False
        except IOError:
            pass
    temp =  block[2] << 8 | block[3]
    return format(temp / 10)

def GetHum():
    loop = True
    block = []
    while loop:
        try:
            i2c.write_i2c_block_data(address, 0x00,[])
            i2c.write_i2c_block_data(address, 0x03,[0x00, 0x02])

            time.sleep(0.05)

            block = i2c.read_i2c_block_data(address, 0, 4)
            loop = False
        except IOError:
            pass
    hum =  block[2] << 8 | block[3]
    return format(hum / 10)

