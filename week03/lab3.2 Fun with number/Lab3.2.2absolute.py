#this programme displays the absolute value of the number input by the user
#the given answer has a decimal point
#therfore I use float as the input data type
number = float (input ("Enter a number:"))
absoluteValue = abs(number)
print ('The absolute value of {} is {}'.format (number, absoluteValue))