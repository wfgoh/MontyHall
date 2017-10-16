# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:09:31 2017

@author: Christopher
"""

import numpy as np

samplesize = 100
countwin = 0
countlose = 0
countswitch = 0
countrandomguess = 0

for i in range(samplesize):
    door = [1,2,3]
    car = np.random.choice(door)
    guess = np.random.choice(door)
    goat = [1,2,3]
    goat.remove(car)
    if guess == car:
        countwin += 1
        opn = np.random.choice(goat)
        door.remove(opn)
        randomguess = np.random.choice(door)
        door.remove(guess)
        switch = door[0]
        if switch == car:
            countswitch += 1
            print('I\'ll be surprised if you win!')
    if guess != car:
        countlose += 1
        goat.remove(guess)
        opn = goat[0]
        door.remove(opn)
        randomguess = np.random.choice(door) 
        door.remove(guess)
        change = door[0]
        if change == car:
            countswitch += 1 #I bet you always win
    if randomguess == car:
        countrandomguess += 1
    
print('No swtich after door opened:',countwin,'wins over',samplesize,'times')
print('Probability =',float(countwin)/float(samplesize))
print('Switch after door opened:',countswitch,'wins over',samplesize,'times')
print('Probability =',float(countswitch)/float(samplesize))
print('Random guess after door opened:',countrandomguess,'wins over',samplesize,'times')
print('Probability =',float(countrandomguess)/float(samplesize))
#print(countlose,countlose/samplesize)
