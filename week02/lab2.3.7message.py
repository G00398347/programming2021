#This is a deliberate error and the fix
#Author: Ruth McQuillan

#the deliberate error
message = "I have eaten " + 99 + "burritos."
print (message)
#error is that message contains str and int and python can only concatenate str to str

#fix
message = "I have eaten " + str(99) +   "burritos"            #converts int 99 to string
print (message)                                               #outputs message