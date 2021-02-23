#This is for trying out python operators

#assignment operator example
x = 5
x += 3
print (x)     #this prints x as 8

#in and not in- membership operators example
x = "Just for fun"
y = {1:"a", 2:"b"}

print ("J"in x)
print ("just" not in x)
print (1 in y)
print ("a" in y)

#identity operators is and is not example 1
a = True
b = False

print ("a and b is ", a and b)
print ("a or b is  ", a or b )
print ("not b is ", not b)

#identity operators is and is not example 2
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print (x is not z)
print (x is not y)        #returns true because x is not the same object as y
print (x != y)            #demonstratest the difference between is not equal to and is not- 
                          #the above line returns false becaue x has the same conted as y so they are equal

#logical operators- and/or/not
a = 5
print (a > 3 and a < 10)       #returns true because both conditions are met
print (a > 3 or a < 10)        #returns true because one of the conditions is true
print (not(a > 3 and a < 10))  #returns false because not reverses the result i.e. returns false if the result is true
print (not(a > 3 or a < 10))   #returns false because not reverses the result i.e. returns false if the result is true
