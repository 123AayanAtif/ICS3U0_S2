# Predict: I predict that the code will likely display "Please input a whole number: and wait for the user to input something into the console"
# It will then print "When (the number entered by the user)  is divided by 6 the result is: (result of the number divided by 6)"

# For example, if I put put in the number 18, it will output:
# Please input a whole number:  18
# When 18  is divided by 6 the result is: 3.0

# Run: When I ran the code, I found my prediction to be correct.

# Inspect: When the code stopped execution, it paused specifically because of the input() function in the code, and waits until the user inputs something into the console.
# Modify:
num = input("Please input a whole number: ")
num3 = input("Use any whole number except zero: ")
num = int(num)
num3 = int(num3)
num2 = num / num3
print("When", num, "is divided by", num3, "the result is:", num2)

# The instruction "Use any whole number except zero" is needed because you can't divide by 0, or python will crash. 
