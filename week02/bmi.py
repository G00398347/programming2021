# This is a programme that calculates somebody's Body Mass Index (BMI)
# author: Ruth McQuillan

strweight = input ('Enter your weight in kilograms: ')           # this line asks for the persons weight in kgs
strheight = input ('Enter your height in centimetres: ')         # ditto for height in cms
heightinmeters= float(strheight)/100                             # converts input string height to float and calculates height in metres
weight = float(strweight)                                        # converts input string weight to float
bmi = round( weight/(heightinmeters ** 2 ),2)                    # performs bmi calculation and rounds to 2 decimal places
print ('Your BMI is: {}. ' .format (bmi) )                       # outputs calculation to screen