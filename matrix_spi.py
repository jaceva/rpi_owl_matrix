import spidev
import time
# import numpy as np

spi = spidev.SpiDev()
bus = 0
device = 0
spi.open(bus, device)
spi.max_speed_hz = 10000000

m1 = [0xab] * (1944 * 6) # ((6 strands * 24 bits/led * 108 leds) / 8 bits/byte) * 6 controllers
m2 = [0xcd] * (1944 * 6) 
t = 0.5
while True:
  
  # start = time.time()
  spi.xfer3(m1)
  # print(time.time()-start)
  time.sleep(t)

  # start = time.time()
  spi.xfer3(m2)
  # print(time.time()-start)
  time.sleep(t)
  
