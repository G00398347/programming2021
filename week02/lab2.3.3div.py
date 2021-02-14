#This programme reads in two numbers, #divides the first one by the second 
#and gives the integer result and the remainder
#Author: Ruth McQuillan

x = int (input ("Please enter first number:  "))                                      #this is asking for the numerator
y = int (input ("Please enter the number you wish to divide by: "))                   #this is asking for the denominator
answer = x//y                                                                         #this gives the answer as an integer ( without the remainder)
remainder = x % y                                                                     #this gives the remainder

print ("{} divided by {} is {} with remainder {}" .format (x, y,answer,remainder))    #output command and format