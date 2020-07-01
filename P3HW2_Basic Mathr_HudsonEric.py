# CTI-110
# P3HW2- Basic Math
# Eric Hudson
# 06/24/2020
#
print()
# Define the functions.
def add(x,y) :
    return x + y
def multiply(x,y) :
    return x * y
def subtract(x,y) :
    return x - y
print()    
# Create a menu
print("------MENU------")
print("1.Add Numbers")
print("2.Multiply Numbers")
print("3.Subtract Numbers")
print("4. Exit")
print("----------------")
choice = input("Enter choice(1/2/3/4/:")
print()
# Get two numbers.
value1 = int(input('Enter first number: '))
value2 = int(input('Enter second number: '))
print()
if choice == "1":
    print(value1, "+", value2,"=", add(value1,value2))
    
elif choice == "2":
    print(value1, "*", value2, "=", multiply(value1,value2))

elif choice == "3":
    print(value1, "-", value2, "=", subtract(value1,value2))

elif choice == "4":
    print("This program will now terminate.")

else:
    print("This input is invalid.")    
    
print()
# Define  the functions
# Explain the functions
# Print a menu of options
# Get two numbers from user
# Create if, elif, and else statements    
