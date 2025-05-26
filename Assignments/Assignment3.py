"""
   Author : Aayan Atif
   Student Number : 760754
   Revision Date : 24 April 2025
   Course Code : ICS3U
   Program : Is it a Palindrome?
   Description : A program that checks if each word in a list to see if it is a palindrome or not

VARIABLE DICTIONARY:
    words_list (list) = List of words to check if they are palindromes or not
    word (str) = Current word being checked in the outer loop
    is_palindrome (bool) = Boolean flag to track if the current word is a palindrome
    length (int) = Length of the current word
    max_index (int) = Half of the word length, used to loop to the middle of the word
    i (int) = Loop index for comparing characters from start and end of the word
    
"""

# List of up to 10 words
words_list = ["racecar", "noon", "desk", "civic", "store", 
         "level", "rotor", "school", "kayak", "madam"]

print("Palindrome program!")
# outputs the text provided in the print statement. 

# starts a loop to go through each word in the list
for word in words:
    # assumes the word is a palindrome at the start
    is_palindrome = True

   # gets the current length of the word 
    length = len(word)
  
   # calculate the halfway point of the word
    max_index = length // 2

  # loop from the start to the middle of the word
    for i in range(max_index):
      # compare the letter from the front and the letter at the end
        if word[i] != word[length - 1 - i]:
          # if none of the numbers match, assume its not a palindrome
            is_palindrome = False
            # no break used but sets the flag and let the loop finish

  # after the loop, checks the result and prints the appropriate message.
    if is_palindrome:
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")

# print the message to end the program
print("Goodbye!")
