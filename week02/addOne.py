#This programme reads in a number, increments the number by 1 and prints the answer
#Author: Ruth McQuillan

str1 = input ("Enter a number here: ")              #input returns a string
number = int (str1)                                 #int converts the string to an integer
newNumber = number +  1                             #increment number by 1
print (" {} + one = {}" .format(number,newNumber))  #print the incremented number
