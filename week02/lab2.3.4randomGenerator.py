#This programme prints out a random number between 1 and 10
#Author: Ruth McQuillan

import random                         #imports the module random
print (random.randrange (1,10))       #asks for output of a random number between one and 10

#modification so that the user inputs the range
start = int (input (" Please enter the first number of your number range: ")) #required - an integer specifying start of range
stop  = int (input (" Please eneter the last number of your number range: ")) #required - and integer specifying end of range

print (random.randint (start,stop))                                           #returns an integer selected from a specified range                   
