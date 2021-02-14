#This programme reads in a string, strips any leading or trailing spaces,
#converts the string to lowercase
#and outputs length for the input and output strings

string1 = input (str( " Please enter a string: " ))                                               #required - a string 
normalisedString1 = string1.strip () .lower ()                                                    #strips out spaces and coverts string to all lower case 

lenString1 = len(string1)                                                                         #counts the number of characters in the input string
lenNormString1 = len (normalisedString1)                                                          #counts the number of characters in the normalised string


print ("That String normalised is :{}".format (normalisedString1))                                #prints normalised string
print ("We reduced the input string from {} to {} characters".format(lenString1,lenNormString1))  #outputs the reduction in the length of 
                                                                                                  #characters due to normalisation
