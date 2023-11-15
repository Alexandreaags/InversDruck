from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from scales import Scales

balanca = Scales(d_out=3, pd_sck=2)

p_up = Pin(16, Pin.OUT)       # 1 for on / 0 for off
p_down = Pin(17,Pin.OUT) # 1 for up / 0 for down

p_up.value(0)
p_down.value(0)
sleep(5)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

p_up.value(1)
p_down.value(0)
sleep(.5)
p_up.value(0)
p_down.value(0)

balanca.tare()
threshold = 0.10

while True:
    #az = 0
    #for i in range(50):
    balanca.measure_force()
    az = imu.accel.z
    az = abs(az)#/50
    az = az - 1.13

    """ if balanca.force != 50.0:
        set_point = 50.0 - balanca.force
        if az < - threshold and  set_point > 0:
            p_up.value(0)
            p_down.value(1)
        if az > threshold and set_point < 0:
            p_up.value(1)
            p_down.value(0) """

    if az > threshold or balanca.force > 35:
        p_up.value(1)
        p_down.value(0)  
    if az < - threshold or  balanca.force < 25:
        p_up.value(0)
        p_down.value(1) 


    print(az, balanca.force, p_down.value(), p_up.value())
