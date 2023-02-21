import board
from adafruit_ht16k33.segments import BigSeg7x4

i2c = board.I2C()
display = BigSeg7x4(i2c)
display.fill(1)
