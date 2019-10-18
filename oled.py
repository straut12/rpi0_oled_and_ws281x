"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64     # Change to 64 if needed
BORDER = 0    # default was 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)

# Use for SPI
#spi = board.SPI()
#oled_cs = digitalio.DigitalInOut(board.D5)
#oled_dc = digitalio.DigitalInOut(board.D6)
#oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
#oled.invert(1)
oled.fill(0)
oled.show()
image = Image.open('/home/pi/Desktop/python.png').resize((oled.width, oled.height), Image.ANTIALIAS).convert('1')
draw = ImageDraw.Draw(image)
oled.image(image)
oled.show()
time.sleep(1)

#oled.invert(0)

# Clear display.
oled.fill(0)
oled.show()
image = Image.open('/home/pi/Desktop/bronco.png').resize((oled.width, oled.height), Image.ANTIALIAS).convert('1')
draw = ImageDraw.Draw(image)
oled.image(image)
oled.show()
time.sleep(1)


# Clear display.
oled.fill(0)
oled.show()
image = Image.open('/home/pi/Desktop/iron man.png').resize((oled.width, oled.height), Image.ANTIALIAS).convert('1')
draw = ImageDraw.Draw(image)
oled.image(image)
oled.show()
time.sleep(1)

# Clear display.
oled.fill(0)
oled.show()
image = Image.open('/home/pi/Desktop/iron man.pbm').resize((oled.width, oled.height), Image.ANTIALIAS).convert('1')
draw = ImageDraw.Draw(image)
oled.image(image)
oled.show()
time.sleep(1)

# Clear display.
oled.fill(0)
oled.show()
image = Image.open('/home/pi/Desktop/oled-iron-man-flying-front.png').resize((oled.width, oled.height), Image.ANTIALIAS).convert('1')
draw = ImageDraw.Draw(image)
oled.image(image)
oled.show()
time.sleep(1)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
               outline=0, fill=0)

# Load default font.
#font = ImageFont.load_default()
font = ImageFont.truetype('/home/pi/Desktop/Retron2000.ttf', 13)

# Draw Some Text
x = 0
top = -2
spacing_incr = 15
text1 = "My Media Hits"
text2 = "YouTube = 412"
text3 = "Twitter = 124"
text4 = "Instagram = 100"

draw.text((x, top), text1, font=font, fill=255)
draw.text((x, top+spacing_incr), text2, font=font, fill=255)
spacing = spacing_incr * 2
draw.text((x, top+spacing), text3, font=font, fill=255)
spacing = spacing_incr * 3
draw.text((x, top+spacing), text4, font=font, fill=255)


#(font_width, font_height) = font.getsize(text)
#draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
#          text, font=font, fill=255)



# Display image
oled.image(image)
oled.show()

