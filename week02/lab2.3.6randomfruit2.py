#This is a modified version of randomfruit using tuples

import random

fruits = ('apple', 'banana', 'cherry','pear', 'kiwi', 'orange')   #required:a list of items

#lab solution using indexing and tuple () instead of list []
index = random.randint (0, len (fruits) -1)                        #specifying the index from which to select a random int
fruit = fruits [index]                                             #creates the variable fruit indexed  
print ("A Random Fruit: {} " .format(fruit))                       #output a random fruit
