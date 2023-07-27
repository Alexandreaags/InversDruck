#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()

from imu import MPU6050
from time import sleep
from machine import Pin, I2C

p_on = Pin(16, Pin.OUT)       # 1 for on / 0 for off
p_direction = Pin(17,Pin.OUT) # 1 for up / 0 for down

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

p_on.value(0)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)

    az = abs(az)

    p_on.value(0)

    if az < 0.8:
        p_on.value(1)
        p_direction.value(1)
    if az > 1.3:
        p_on.value(1)
        p_direction.value(0)
       

    print("ax",ax,"g\t","ay",ay,"g\t","az",az, "g\t  ", p_on.value(),"        ",end="\r")
