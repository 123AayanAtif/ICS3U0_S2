# Predict: I predict that the code will output "Please input a whole number:" then it will wait for a user input. 
# Once the user inputs a number I predict that it will output "Please input another nonzero whole number" and wait for the user input.
# My last prediction for this code will be that it will think if the second input is a factor of the first input and display if it is a factor, but it wont display if it isnt a factor because the code isnt capable to tell the user if it isnt a factor.

# Run: My prediction was correct, when I ran a number like 10 and 1, it was able to tell me that 1 is a factor of 10, but when I ran 3 and 10, it kept thinking and not showing any output. 
# Inspect: Yes, the output matched what I did on my calculator.

# Modify

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = 0
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)

# Modify 2
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
if(y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
    print("You cannot input 0 as it can not be divided")

# Modify 3
import math

x = input("Input a whole number between 1 and 20: ")
x = int(x) 
if ((x < 1 or x > 20)):
    print("The number must be between 1 and 20. Try again.")
else:
    y = input(" Input another non-zero whole number between 1 and 20:")
    y = int(y) 
    if ((y < 1 or y > 20)): 
        print("The number must be between 1 and 20.")
    else:
      print("Now deciding if", y, "is a factor of", x, "...")
      if y != 0:  
            rem = x % y
            if rem == 0:
                print("Yes!", y, "is a factor of", x)
            else:
                print("No,", y, "is not a factor of", x, "...")
