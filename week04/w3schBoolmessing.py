#This file is for messing with Booleans from w3schools

#when you compare two values the expression is evaulated and returns the Boolean answer
print (10 > 9)       #returns True
print (10 == 9)      #returns False
print (10 < 9)       #returns False

#when you run a condition in an if statement python returns True or False
a = 200
b = 33
if b > a : 
    print ("b is greater than a ")
else :
    print ("b is not greater than a")    

#most values are evaluated as true if there is some content
print (bool("abc"))    
print (bool (123))
print (bool (["apple", "cherry", "banana"]))

#there are not many values that evaluate to False but see below
print (bool (False))
print (bool (None))
print (bool (0))
print (bool (""))
print (bool (()))
print (bool ([]))
print (bool ({}))

def myFunction() :
  return 0

if myFunction():
  print("YES!")
else:
  print("NO!")
