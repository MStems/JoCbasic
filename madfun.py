# Merrilee S
# Create program asking user for decimal number output absolute, 
# rounded and sq.root of number

import math
dec = float(input("Please give me a decimal number: "))
# print("The absolute value of", dec ,("=") (abs(dec)))
print("The absolute value of", dec ,"= ", abs(dec))
print("The rounded value of", dec ,"=", round(dec, 0))
print("The rounded square root of the absolute value of", dec,"=", math.sqrt(abs(round(dec, 0))))
