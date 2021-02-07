#this programme takes a float, converts it to an integer and rounds it down 
#Author : Ruth McQuillan

#the term give to rounding down is floored
import math
numberToFloor = float (input('Enter a float number:'))                 #this is where the user enters the decimalised number they wish to round down
flooredNumber = math.floor (numberToFloor)                             #this is the floor command to round down to the nearest integer
print ('{} floored is {}' .format(numberToFloor,flooredNumber))        #this is the printed output