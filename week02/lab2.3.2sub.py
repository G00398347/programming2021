#This programme reads in two numbers and subtracts the second one from the first one
#Author: Ruth McQuillan

x = int (input ("Enter first number: "))            #asks for 1st number in integer format
y = int (input ("Enter second number:"))            #asks for 2nd number in integer format
answer = x-y                                        #subraction operation
print ("{} minus {} is {}" .format (x,y,answer))    #output command and format

#when something other than an integer is entered for first or second number a ValueError invalid literal for int() with base 10:
