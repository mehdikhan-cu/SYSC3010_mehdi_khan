'''
    File name: lab2-hardware-step3.py
    Author: Mehdi Khan
    Date created: 27/09/2020
    Date last modified: 27/9/2020
    Python Version: 3.7.3
    Hardware: Raspberry Pi 4, SenseHAT
'''

# small animation of a slime walking,
# image of slime taken from: https://www.pinterest.ca/pin/74239093841257526/
# Credit for image goes to: Fred Bednarski

from sense_hat import SenseHat
import time

sense = SenseHat()

# Define some colours
bg = (124, 164, 49) # Background
dp = (164, 49, 64) # Dark Pink
p = (175, 92, 110) # Pink
i = (230, 228, 213) # White

# Set up where each colour will display
slime1 = [
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, dp, p, p, bg, bg,
	bg, bg, dp, p, p, i, p, bg,
	bg, dp, p, p, p, p, p, bg,
	dp, p, dp, dp, dp, p, dp, bg,
	bg, bg, bg, bg, bg, bg, bg, bg
]

slime2 = [
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, dp, dp, p, p, i, p,
	bg, dp, p, p, p, p, p, p,
	dp, p, dp, dp, dp, dp, p, dp,
	bg, bg, bg, bg, bg, bg, bg, bg
]

slime3 = [
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, bg, bg, bg, bg,
	bg, bg, bg, bg, dp, p, p, bg,
	bg, bg, bg, dp, p, p, i, p,
	bg, bg, dp, p, p, p, p, p,
	bg, dp, p, dp, dp, dp, p, dp,
	bg, bg, bg, bg, bg, bg, bg, bg
]

# Display an walking animation on LED matrix
def walking():
	for i in range(10):
		sense.set_pixels(slime1)
		time.sleep(0.25)
		sense.set_pixels(slime2)
		time.sleep(0.25)
		sense.set_pixels(slime3)
		time.sleep(0.25)

def walking2():
	for i in range(10):
		sense.flip_h()
		sense.set_pixels(slime1)
		sense.flip_h()
		time.sleep(0.25)
		sense.set_pixels(slime2)
		sense.flip_h()
		time.sleep(0.25)
		sense.set_pixels(slime3)
		sense.flip_h()
		time.sleep(0.25)

msg = "END"

while True:
	for event in sense.stick.get_events():
		if event.action == "pressed":
			if event.direction == "right":
				walking()
				sense.clear()
			elif event.direction == "left":
				walking2()
				sense.clear()
			else:
				sense.show_message(msg)
				quit()

