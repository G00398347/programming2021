#This programme rounds a number
#Author: Ruth McQuillan

numberToRound = float (input ("Enter a float number:"))               #this asks for a number with a decimal point
roundedNumber = round(numberToRound)                                  #this uses the round built in function to round the float number entered at input


#I have found inconsitency in whether a float gets rounded up or down
#it does not seem to round to the nearest even number as stated in the lab
#for example 7.1 rounded to 7 while 7.5 rounded to 8 when I ran this
#it appears to be more to do with wheter you are above at or below .5
#be careful of round if accuracy is NB.

print ( '{} rounded is {}'.format (numberToRound,roundedNumber))     
