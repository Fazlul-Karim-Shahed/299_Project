from pyfirmata import Arduino, util, STRING_DATA
import time
import pyfirmata

board = Arduino('/dev/ttyACM0')
print(board)

pin = board.digital[2]
pin.mode = pyfirmata.SERVO

pin.write(0)
time.sleep(3)
pin.write(90)
time.sleep(1)
pin.write(180)
time.sleep(1)
time.sleep(1)
pin.write(0)
time.sleep(1)