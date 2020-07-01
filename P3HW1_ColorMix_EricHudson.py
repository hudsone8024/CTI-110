# CTI-110
# P3HW1- Color Mixer
# Eric Hudson
# 29 June 2020
#
# Get the user to enter two primary colors.
color1 = input("Enter primary color 1: ")
color2 = input("Enter primary color 2: ")
if (color1== "red" and color2== "blue") or \
   (color1== "blue" and color2== "red"):
    print(color1 + "mixed with" + color2 + "is purple")
elif (color1== "red" and color2== "yellow") or \
     (color1== "yellow" and color2== "red"):
    print(color1 + "mixed with" + color2 + "is orange")    
elif (color1== "blue" and color2== "yellow") or \
     (color1== "yellow" and color2== "blue"):
    print(color1 + "mixed with" + color2 + "is green") 
else:
   print("At least one of your colors are not a primary color.")
   