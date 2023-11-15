from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from scales import Scales
from mcp4725 import MCP4725, BUS_ADDRESS

balanca = Scales(d_out=3, pd_sck=2)

#p_up = Pin(16, Pin.OUT)       # 1 for on / 0 for off
#p_down = Pin(17,Pin.OUT) # 1 for up / 0 for down

#p_up.value(0)
#p_down.value(0)
sleep(5)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

dac=MCP4725(i2c,BUS_ADDRESS[0])

dac.write(0)

""" p_up.value(1)
p_down.value(0)
sleep(.5)
p_up.value(0)
p_down.value(0) """

#0 - 4095
#0 - 50
#51 - 1799
#1800 - 1899
#1900 - 4095 // 5 - 1900 // >50 - 4095

balanca.tare()
threshold = 0.10

while True:
    #az = 0
    #for i in range(50):
    balanca.measure_force()
    """ az = imu.accel.z
    az = abs(az)#/50
    az = az - 1.13 """

    """ if balanca.force != 50.0:
        set_point = 50.0 - balanca.force
        if az < - threshold and  set_point > 0:
            p_up.value(0)
            p_down.value(1)
        if az > threshold and set_point < 0:
            p_up.value(1)
            p_down.value(0) """

    if balanca.force < 45 or balanca.force > 55:
        set_point = balanca.force - 50
        if set_point > 0 and <= 50:
            x = set_point / 50:
            dac.write(x*(4095-1900)+1900)
        elif set_point < 0 and >= -50:
            x = -1*set_point / 50:
            dac.write(1799-x*(1799-50))
        elif set_point < -50:
            dac.write(51) 
        elif set_point > 50:
            dac.write(4095)

                
"""         p_up.value(1)
        p_down.value(0)  
    if az < - threshold or  balanca.force < 25:
        p_up.value(0)
        p_down.value(1)  """


    print(az, balanca.force, p_down.value(), p_up.value())
