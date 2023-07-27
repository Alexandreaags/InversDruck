#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()

from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x,2)
    gy=round(imu.gyro.y,2)
    gz=round(imu.gyro.z,2)
    tem=round(imu.temperature,2)
    print("ax",ax,"g\t","ay",ay,"g\t","az",az,"g\t","gx",gx,"°/s\t","gy",gy,"°/s\t","gz",gz,"°/s\t","Temperature",tem,"        ",end="\r")
    sleep(0.1) 
    

        
