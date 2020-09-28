# Done by: Mehdi Khan

from sense_hat import SenseHat
from time import sleep

s = SenseHat()

name = ['M', 'K']

def initial():
    s.show_letter(name[0])
    name.reverse()

while True:
    for event in s.stick.get_events():
        if event.action == "pressed":
            initial()
            sleep(.5)
            s.clear()
