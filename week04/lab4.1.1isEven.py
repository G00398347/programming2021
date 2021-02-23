#This programme asks the user to enter an integer and outputs whether 
#the number is odd or even

#Author: Ruth McQuillan

number = int(input ("Please enter an integer: "))                 #required: the user must input an integer
if (number % 2) == 0:                                             #% checks for remainder - if number divide by 2 has no remainder it is even
    print ("{} is an even number ".format (number))               #what to do if number is even
else:                                                             #what to do if the number is not even
    print ("{} is an odd number " .format (number))