#This programme prints out a random fruit from a list
#Author: Ruth McQuillan

import random                                                     #required:import the random module

fruits = ['apple', 'banana', 'cherry','pear', 'kiwi', 'orange']   #required:a list of items

#my solution after research and before looking at solution provided!
print ("A Random Fruit:" , (random.choice(fruits)))               #output a random fruit using random.choice


#lab solution using indexing
index = random.randint (0, len (fruits) -1)                        #specifying the index from which to select a random int
fruit = fruits [index]                                             #creates the variable fruit indexed  
print ("A Random Fruit: {} " .format(fruit))                       #output a random fruit




