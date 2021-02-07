#this programme rounds a number
#Author: Ruth McQuillan

numberToRound = float (input ("Enter a float number:"))              # This asks for a number with a decimal point
roundedNumber = round(numberToRound)                                 # This uses the round built in function to round the float number entered at input


#The soloution rounds to the nearest EVEN number- Be careful of round
print ( '{} rounded is {}'.format (numberToRound,roundedNumber))     
