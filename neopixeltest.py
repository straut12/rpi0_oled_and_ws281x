import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.D18, 6)

time.sleep(3)

for x in range(0,3):
	pixels[x] = (255, 30, 0)
	time.sleep(1)

for x in range(0,3):
	pixels[x] = (255, 60, 0)

for x in range(3,6):
	pixels[x] = (0, 0, 255)
	time.sleep(1)

for x in range(0,30):
	for x in range(0,3):
		pixels[x] = (255, 30, 0)
	time.sleep(1)
	for x in range(0,3):
		pixels[x] = (255, 60, 0)
	for x in range(3,6):
		pixels[x] = (0, 0, 255)
	time.sleep(1)
	pixels.fill((0,0,0))

for x in range(0,3):
	pixels[x] = (255, 60, 0)
for x in range(3,6):
	pixels[x] = (0, 0, 255)

time.sleep(5)
pixels.fill((0, 0, 0))
