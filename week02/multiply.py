# This programme multiplies 111 by 555
# author: Ruth McQuillan

print ("What is 111*555?")                  # Question to set the context of the answer
answer = 111 * 555                          # assigns the calculation to the variable
print (answer)                              # prints the value of the variable ( fix 1)
print (111*555)                             # directly prints the product of the calculation ( fix 2)
print ("The answer is " +str(answer))       # prints the product concatanated to a text string (fix 3)
print ("The answer is {}" .format(answer))  # prints a complete string with the answer using .format (fix 4)