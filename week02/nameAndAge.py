#This programme reads in a name and age and outputs Hello 'Name', your age is "age"
#Author: Ruth McQuillan

name = input ("Please enter your name: ")                #asks for the persons name
age =  input ("Please enter your age: " )                #asks for the persons age

age2 =int(age)                                           #converts age string to intger
print ("Hello {}, your age is {}." .format (name,age2))  #prints greeting, name and age

#modified version
print ("Hello {} \tyour age is {}" .format (name, age2)) #uses tab to space the output


