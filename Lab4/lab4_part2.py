# Done by: Mehdi Khan

from sense_hat import SenseHat
from time import sleep

s = SenseHat()

name = ['M', 'K']

def initial():
    s.show_letter(name[0])
    name.reverse()

x = 0

def count():
    x = x + 1
def count_minus():
    x = x - 1

while True:
    for event in s.stick.get_events():
        if event.action == "up":
            count()
            s.showmessage()
        if event.action == "down":
            count_minus
	    s.showmessage(x)
