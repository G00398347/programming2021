#how to get character position
#remember the first character is at positon 0
#square brackets used to access elements of the string

a= "Hello, World!"
print (a[1])

#loop through a string using for
#note indent before print
for x in "banana" :
 print(x)    

#to get the lenght of a string
print (len (a)) 

#to check if a phrase or character is in a string
txt = "The best things in life are free!"
print("free" in txt)
#in the above case the answer will be true as free is in the string- bool

#to check if a phrase or character is present in a string using an if statement
#print only if free is present
if "note" in txt:                      #I changed free to note to get different result - see terminal
    print ("Yes, 'free' is present")

#to check if a phrase or character is not present in a string using not in
print ("expensive" not in txt)
#in the above case the answer will be true as expensive is not in the string-bool

#to check if a phrase or character is not present in a string using an if statement
if "expensive" not in txt:
    print ("Yes, 'expensive' is NOT present.")

#slicing is used to return a range of characters
#specify the start index and the end index, separated by a colon, to return a part of the string.
print (a[2:5])   

#get the characters from the start to position 5 ( this will not include position 5)
#REMEMBER THE FIRST CHARACTER IS POSITION 0
print(txt[:5])

#get the characters from position 5 all the way to the end
print (txt[5:])

#use negative indexing to start the slice from the end of the string
#example : to get the characters in text from i in life to but not including e in are
#include spaces and note- when counting from the end the first character is -1
#the character indexed after the : is excluded, the character indexed before the : is included
print (txt [-13:-7])                                              
     
