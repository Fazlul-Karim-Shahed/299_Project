from pyfirmata import Arduino, util, STRING_DATA
from time import strftime, time
import time
port='/dev/ttyACM0'

board=Arduino(port)

data=" " + "Digital Clock"


while True:
    string=strftime('%H:%M:%S %p')
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))
    time.sleep(1)

# -------------------------------------------------------------------------------------------------
# from pymata4 import pymata4
# import time
# board = pymata4.Pymata4()

# # Specify the LCD pins
# rs = 5  # Register Select pin
# enable = 6  # Enable pin
# d4 = 7  # Data pin 4
# d5 = 8  # Data pin 5
# d6 = 9  # Data pin 6
# d7 = 10  # Data pin 7

# # Ultrasonic pin
# trigger_pin = 11
# eco_pin = 12

# # Initialize the LCD
# board.set_pin_mode_digital_output(rs)
# board.set_pin_mode_digital_output(enable)
# board.set_pin_mode_digital_output(d4)
# board.set_pin_mode_digital_output(d5)
# board.set_pin_mode_digital_output(d6)
# board.set_pin_mode_digital_output(d7)

# # Send commands to the LCD display
# board.digital_write(rs, 0)  # Set RS pin LOW for command mode

# # Function to send 4-bit data to the LCD


# def send_nibble(value):
#     board.digital_write(d4, (value >> 0) & 1)
#     board.digital_write(d5, (value >> 1) & 1)
#     board.digital_write(d6, (value >> 2) & 1)
#     board.digital_write(d7, (value >> 3) & 1)
#     board.digital_write(enable, 1)
#     board.digital_write(enable, 0)

# Function to send 8-bit data to the LCD


# def send_byte(value, mode):
#     board.digital_write(rs, mode)
#     send_nibble(value >> 4)
#     send_nibble(value)


# # Initialize the LCD in 4-bit mode
# send_nibble(0x03)
# time.sleep(5)  # Wait for initialization
# send_nibble(0x03)
# time.sleep(1)
# send_nibble(0x03)
# send_nibble(0x02)

# # Configure the LCD
# send_byte(0x28, 0)  # 4-bit mode, 2 lines, 5x8 font
# send_byte(0x0C, 0)  # Display on, cursor off, blinking off
# send_byte(0x06, 0)  # Entry mode set: increment mode, no shift


# def print_lcd(str):
#     # Write a message on the LCD
#     clear_line = ""
#     # message_line2 = ""
#     send_byte(0x80, 0)  # Set cursor at the beginning of the first line
#     for char in clear_line:
#         send_byte(ord(char), 1)
#     send_byte(0xC0, 0)  # Set cursor at the beginning of the second line
#     for char in clear_line:
#         send_byte(ord(char), 1)


# # Close the connection to the Arduino board

# print_lcd('Hello')

# board.shutdown()
# ---------------------------------------------------------------------------------

# from pymata4 import pymata4
# import time

# board = pymata4.Pymata4()

# rs = 12  # Register Select pin
# enable = 11  # Enable pin
# d4 = 5  # Data pin 4
# d5 = 4  # Data pin 5
# d6 = 3  # Data pin 6
# d7 = 2  # Data pin 7

# def lcd_command(data):
#     board.digital_write(rs, board.LOW)
#     board.digital_write(enable, board.LOW)
#     board.digital_write(d4, (data >> 4) & 0x01)
#     board.digital_write(d5, (data >> 5) & 0x01)
#     board.digital_write(d6, (data >> 6) & 0x01)
#     board.digital_write(d7, (data >> 7) & 0x01)
#     board.digital_write(enable, board.HIGH)
#     time.sleep(0.0001)
#     board.digital_write(enable, board.LOW)
#     time.sleep(0.0001)
#     board.digital_write(d4, (data >> 0) & 0x01)
#     board.digital_write(d5, (data >> 1) & 0x01)
#     board.digital_write(d6, (data >> 2) & 0x01)
#     board.digital_write(d7, (data >> 3) & 0x01)
#     board.digital_write(enable, board.HIGH)
#     time.sleep(0.0001)
#     board.digital_write(enable, 0)
#     time.sleep(0.0001)

# lcd_command(0x33)
# lcd_command(0x32)
# lcd_command(0x28)
# lcd_command(0x0C)
# lcd_command(0x06)

# message = "Hello, LCD!"
# for char in message:
#     lcd_command(ord(char) | 0x80)

# board.shutdown()
