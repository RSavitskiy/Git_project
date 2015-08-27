# -*- coding: utf-8 -*-
import random

number = random.randint(1, 10)
a = 0
while a < 10:
    player = raw_input("you namber ")
    if int(number) == int(player):
        print "bingo you win"
        break
    elif player != number:
        a += 1
        print "you not win, Try again, you have " + str(10 - a) + " chance "
        if a == 10:
            print " you lose  number = " + str(number)
