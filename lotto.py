from random import shuffle
from time import sleep

while True:
    nummers = [1,2,3,4,5,6,7,8,9,10]
    shuffle(nummers)
    print(nummers)
    sleep(5)