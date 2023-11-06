from imu import MPU6050
from time import sleep
from machine import Pin, I2C

p_up = Pin(16, Pin.OUT)       # 1 for on / 0 for off
p_down = Pin(17,Pin.OUT) # 1 for up / 0 for down

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

threshold = 0.10

while True:
    #az = 0
    #for i in range(50):
    az = imu.accel.z
    az = abs(az)#/50
    az = az - 1.13
    if az < - threshold:
        p_up.value(0)
        p_down.value(1)
    elif az > threshold:
        p_up.value(1)
        p_down.value(0)
    else:
        p_up.value(0)
        p_down.value(0)

    #print("az",az, "g\t  ", p_up.value(), p_down.value(),"  ,end="\r")
    
