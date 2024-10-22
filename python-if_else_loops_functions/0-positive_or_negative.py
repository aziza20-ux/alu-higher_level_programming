#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if (number < 0):
    print("number {} is negative".format(number))
elif (number > 0):
    print("nunber {} is positive".format(number))
else:
    print("nunber {} is zero".format(number))
    
    
