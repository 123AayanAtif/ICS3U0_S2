# Predict: I predict that the code will output "Please input a length:" and waits for the user to enter a length
# I then predict it will output "The area of a square of side length (length the user entered) is: (result of entered number to the power of 2)"

# Run: The output showed that my prediction was correct.

# Inspect: It stopped in execution because it was waiting for a user input
# For example, I input 10, and it output "The area of a square of side length 10.0 is: 100.0", which matched the answer of my calculator (except for the .0 part which is because of the value being a float)
# Modify:
import math
radius = input("Input the circle's radius: ")
radius = float(radius)
area = 0.5*math.pi*math.pow(radius, 2) + 4*math.pow(radius, 2)
print("Area is:", area)
# The reason why the radius has to be multiplied by 2 in part of the formula is because you need the diameter/length where radius is only half of it
