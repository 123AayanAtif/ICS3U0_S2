#  Author : Aayan Atif
#  Revison date : 28 Feburary 2025
#  Program : Even or Odd
#  Description : A program that checks if two numbers multiplied together are even or odd
#  VARIABLE DICTIONARY:
#  a (int) = user-inputted number, used for calculations in multiple parts of the program  
#  b (int) = second user-inputted number, used for multiplication in even/odd detection  
#  d (float) = calculated inner diagonal of a cube  
#  quarters (int) = number of quarters in the change  
#  dimes (int) = number of dimes in the change  
#  nickles (int) = number of nickels in the change  
#  pennies (int) = number of pennies in the change  
#  change (int) = remaining amount of change in cents during calculation  
#  total (int) = original amount of change input by the user  

# Part 1: 

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")
# Prints out description of what the program will do

a = int(input("Please enter your first number: "))
# Asks and waits for the users input for the first number
b = int(input("Please enter your second number: "))
# Ask and waits for the unders input for the seecond number

if (a % 2 == 1 and b % 2 == 1):
  # Checks if both the first number and second number is odd
  print("The product ", a, "x", b, " will be odd.")
  # Prints out the result of the 2 numbers will be odd since both the first and second numbers are odd
  
elif (a % 2 == 0 and b % 2 == 0):
  # Checks if both the first number and second number is odd
  print("The product ", a, "x", b, " will be even.")
  # Prints out the result of the 2 numbers will be even since both the first and second numbers are even

elif (a % 2 == 1 and b % 2 == 0):
  # Checks if the first number is odd and if the second number is even
  print("The product ", a, "x", b, " will be even.")
  # Prints out the result of the 2 numbers will be even since one of the numbers is even and one of the numbers is odd
  
else:
  print("The product ", a, "x", b, " will be even.")
  # This will run when the first number is even and the second number is off

# Part 2: The inner (or body) diagonal of a cube

#  Program : Calculate the inner (or body) diagonal of a cube
#  Description : This program calculates the inner or body diagonal of a cube

import math

print("I can calculate the cube's inner diagonal for any edge length.")
# Prints out description of what the program will do

a = int(input("Enter the edge length of your cube:"))
# Asks user for a number as an edge length of the cube
d = a * math.sqrt(3)
# Calculates the diagonal of the cube (variable d) by using the number the user inputted 
d = round(d, 2)
# Rounds the value of the diagonal for the cube to 2 decimal places

print("The length of the inner diagonal of a cube with the side length %.f will be: %.2f" % (a,d))
# Prints out the length of the inner diagonal of the cube with the side length the user inputted

# Part 3: Making change in coins

#  Program : Making change in coins
#  Description : A program that checks if two numbers multiplied together are even or odd

# Initialize coin counters
quarters = 0
dimes = 0
nickles = 0
pennies = 0

# Get user input for change in cents
change = int(input("Please enter the amount of change in cents: "))
total = change

# Calculate quarters
if change >= 25:
    quarters = int(change / 25)
    change = change % 25

# Calculate dimes
if change >= 10:
    dimes = int(change / 10)
    change = change % 10

# Calculate nickels
if change >= 5:
    nickles = int(change / 5)
    change = change % 5

# Calculate pennies
if change >= 1:
    pennies = int(change / 1)

# Handle special case for 1 cent
if change == 1:
    print("1 cent can be 1 penny.")

# Print total cents and start building the output
else:
    print(total, "cents can be ", end="")

# Add quarters to the output
if quarters > 0:
    if quarters > 1:
        print(quarters, "quarters", end="")
    else:
        print("1 quarter", end="")
    if dimes >= 1 or nickles >= 1 or pennies >= 1:
        print(", ", end="")
    if (dimes >= 1 and nickles == 0 and pennies == 0) or (dimes == 0 and nickles >= 1 and pennies == 0) or (dimes == 0 and nickles == 0 and pennies >= 1):
        print("and ", end="")
    if dimes == 0 and nickles == 0 and pennies == 0:
        print(".")

# Add dimes to the output
if dimes > 0:
    if dimes > 1:
        print(dimes, "dimes", end="")
    else:
        print("1 dime", end="")
    if nickles >= 1 or pennies >= 1:
        print(", ", end="")
    if (nickles >= 1 and pennies == 0) or (nickles >= 0 and pennies == 1):
        print("and ", end="")
    if nickles == 0 and pennies == 0:
        print(".")

# Add nickels to the output
if nickles > 0:
    if nickles > 1:
        print(nickles, "nickles", end="")
    else:
        print("1 nickle", end="")
    if pennies >= 1:
        print(" and ", end="")
    if pennies == 0:
        print(".")

# Add pennies to the output
if pennies > 0:
    if pennies > 1:
        print(pennies, "pennies.")
    else:
        print("1 penny.")
