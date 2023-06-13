import cv2
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA
import time

board = Arduino('/dev/ttyACM0')
print(board)

board.digital[13].write(1)
pin = board.digital[2]
pin.mode = pyfirmata.SERVO
pin.write(0)

DATABASE = ['A5998', '2BE']

photo_url = "https://192.168.0.104.8080/picture"
# stream_url = "http://192.168.52.240/stream"


# image_bytearray = urllib.request.urlopen(photo_url)

# img_nparray = np.array(bytearray(image_bytearray.read()), dtype=np.uint8)

# img = cv2.imdecode(img_nparray, -1)

# plt.imshow(img)
# plt.show()

# Save the image to a file
# cv2.imwrite('image.jpg', img)
# ------------------------------------------------------------------------------------------------

img = cv2.imread('./Car3.jpg')


def img_process(img):
    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to separate the foreground from the background
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get the contour with the largest area, which is likely to be the license plate
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for contour in contours:
        # Get the perimeter of the contour
        perimeter = cv2.arcLength(contour, True)

        # Approximate the contour to a polygon to simplify its shape
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # If the polygon has 4 vertices, it is likely the license plate
        if len(approx) == 4:
            # Get the bounding box of the polygon
            x, y, w, h = cv2.boundingRect(approx)

            # Crop the license plate from the image
            plate = gray[y:y+h, x:x+w]

            # Apply thresholding to the license plate
            plate_thresh = cv2.threshold(
                plate, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

            # Apply morphological transformations to further clean up the image
            plate_thresh = cv2.morphologyEx(
                plate_thresh, cv2.MORPH_CLOSE, (3, 3))

            # Apply OCR to recognize the text on the license plate
            # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
            text = pytesseract.image_to_string(plate_thresh, config='--psm 11')

            # Remove any non-alphanumeric characters from the text
            text = ''.join(e for e in text if e.isalnum())

            # Print the recognized text
            print("License plate number: " + text)

            break
    return text


# text = img_process(img)

text = img_process(img)
count = 0


def print_lcd(data):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data))


for i in DATABASE:
    if i == text:
        print_lcd('Car found')
        print_lcd('')
        time.sleep(2)
        print_lcd('Gate opening')
        print_lcd('')
        pin.write(90)
        time.sleep(2)
        print_lcd('Waiting for car entry.')
        print_lcd('')
        time.sleep(5)
        print_lcd('Gate closing')
        print_lcd('')
        pin.write(0)
        time.sleep(2)

        print_lcd('Thank you')
        print_lcd('')
        count = 0
        print('ok')
        break
    else:
        pin.write(0)
        count += 1

if count != 0:
    print_lcd('Car not found')
    print_lcd('')
    time.sleep(2)
    print_lcd('Permission Denied')
    print_lcd('')
    time.sleep(2)
    print_lcd('Thank you')
    print_lcd('')
    print('not ok')


plt.imshow(img)
plt.show()
