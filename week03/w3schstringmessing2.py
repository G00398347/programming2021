#remove whitespace

a = " Hello World!  "
print (a.strip())

#replace a string with another string
b = a.strip ()                         #this is my own attempt to remove the white space before replacing
                                       #this step was not in the w3schools example
print (b.replace("H", "J"))

#split a string
a = " If in doubt, say nothing"
b = a.split (",")
print (b)

#to concatenate strings 
a = "Hello"
b = "World"
c = a + b
print (c)

#to add a space to concatenated strings
c = a + " " + b
print (c)

#using the format method to combine numbers and strings
#just checking the placement of the numbers in this exercise from w3schools

quantity = 3
itemNo = 567
price = 49.95
myOrder = ( "I want to pay  {} dollars each for {} of item  {} ")
print (myOrder.format (price, quantity,itemNo,))

#rather than ordering the variables after the .format, you can index number the arguments (variables in this case)
myOrder2 = ( "I want to pay  {2} dollars each for {0} of item  {1} ")
print (myOrder2.format  (quantity,itemNo,price)) 
#note that the order of the variables in the print command is not the order in which they are printed 


#escape characters allow you to insert characters that are illegal
#the \ is used to fix this problem followed by the illegal character
                                           
txt2 = "We are the so called \"Vikings\" from the north"
print (txt2)




