# Code used to display some Raspberry Pi Pico data on PC

import serial
import time

import numpy as np
import matplotlib.pyplot as plt

az = []

samples = 2000

### open a serial connection
pico = serial.Serial("COM5", 115200)

### get Acceleration array
for i in range(0,samples):
    inst_acc_z = str(pico.readline())
    inst_acc_z = int(inst_acc_z[2:-3])
    az.append(inst_acc_z)

np_az = np.array(az)

samples_array = [range(0, samples)]

plt.plot(np_az, samples_array)
plt.xlabel('Acceleretion on Z [g]')
plt.ylabel('Samples')

plt.show()