from pymata4 import pymata4
import time

board = pymata4.Pymata4()

# Specify the LCD pins
rs = 5  # Register Select pin
enable = 6  # Enable pin
d4 = 7  # Data pin 4
d5 = 8  # Data pin 5
d6 = 9  # Data pin 6
d7 = 10  # Data pin 7

# Function to send commands to the LCD
def lcd_command(data):
    board.digital_write(rs, 0)  # Set RS pin LOW for command mode
    board.digital_write(enable, 0)  # Set enable pin LOW to prepare for data
    board.digital_write(d4, (data >> 4) & 1)
    board.digital_write(d5, (data >> 5) & 1)
    board.digital_write(d6, (data >> 6) & 1)
    board.digital_write(d7, (data >> 7) & 1)
    board.digital_write(enable, 1)  # Set enable pin HIGH to latch the data
    time.sleep(0.001)  # Delay to allow the data to be latched
    board.digital_write(enable, 0)  # Set enable pin LOW again

# Function to send characters to the LCD
def lcd_print(data):
    board.digital_write(rs, 1)  # Set RS pin HIGH for character mode
    board.digital_write(enable, 0)  # Set enable pin LOW to prepare for data
    board.digital_write(d4, data & 1)
    board.digital_write(d5, (data >> 1) & 1)
    board.digital_write(d6, (data >> 2) & 1)
    board.digital_write(d7, (data >> 3) & 1)
    board.digital_write(enable, 1)  # Set enable pin HIGH to latch the data
    time.sleep(0.001)  # Delay to allow the data to be latched
    board.digital_write(enable, 0)  # Set enable pin LOW again

# LCD initialization sequence
lcd_command(0x33)
lcd_command(0x32)
lcd_command(0x28)  # Set 4-bit mode, 2 lines, 5x8 font
lcd_command(0x0C)  # Display ON, cursor OFF, blink OFF
lcd_command(0x06)  # Entry mode: Increment, no shift

# Write a message on the LCD
message = "Hello, LCD!"
for char in message:
    lcd_print(ord(char))

# Close the connection to the Arduino board
board.shutdown()
