#this is a programme to convert a float amount entered in dollars to cents
#Author: Ruth McQuillan

amount = float (input ('Enter amount in dollars e.g. 4.55:'))  #this invites the user to input the amount in dollars 
absoluteValue = abs (amount)                                   #this removes minus if negative float entered in amount
absoluteConvertCents = absoluteValue * 100                     #this multipies the absolute value of dollars by 100 to convert to cents
amountCents =  int (absoluteConvertCents)                      #this ensures that the decimal point is removed from the output by converting the float to integer
print ('That amount in cents is {}'.format(amountCents))       #this is the instruction to output the amount in cents as an integer


