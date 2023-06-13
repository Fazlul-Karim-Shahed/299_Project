


board = Arduino('/dev/ttyACM0')
print(board)
z
board.digital[13].write(1)
pin = board.digital[10]
pin.mode = pyfirmata.SERVO
pin.write(0)