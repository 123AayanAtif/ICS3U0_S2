"""

Author : Aayan Atif
   Student Number : 760754
   Revision Date : 15 May 2025
   Course Code : ICS3U
   Program : Wordle Searcher
   Description : This program lets the user search a Wordle solution file 
   either by entering a word or by entering a specific date.

VARIABLE DICTIONARY:



"""

# Function to convert month abbreviation to 2-digit number
def monthToNumber(mon):
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
              "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
              "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    return months.get(mon, "00")  # Return "00" if invalid month

# Function to merge day, month, and year into a single integer (YYYYMMDD)
def merge(day, month_abbr, year):
    month_num = monthToNumber(month_abbr)
    return int(year + month_num + day)

# Function to find the date for a given word
def isMatch(word_list, date_list, search_word):
    search_word = search_word.upper()
    for i in range(len(word_list)):
        if word_list[i] == search_word:
            return date_list[i]
    return 0  # Word not found

# Function to get the word on a specific date
def getWordByDate(date_list, word_list, search_date):
    if search_date < 20210619:
        return "too early"
    elif search_date > 20240421:
        return "too late"
    elif search_date in date_list:
        index = date_list.index(search_date)
        return word_list[index]
    else:
        return "not found"

# Read the file and store data into two lists
date_list = []  # List for integer dates
word_list = []  # List for words

# Open the wordle.dat file and read data
with open("wordle.dat", "r") as file:
    for line in file:
        parts = line.strip().split()
        month = parts[0]
        day = parts[1]
        year = parts[2]
        word = parts[3]
        date = merge(day, month, year)
        date_list.append(date)
        word_list.append(word)

# Start interactive session
print("Welcome to the Wordle Database!")
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ")

if choice.lower() == "w":
    search_word = input("What word are you looking for? ")
    result_date = isMatch(word_list, date_list, search_word)
    if result_date != 0:
        print("The word " + search_word.upper() + " was the solution to the puzzle on " + str(result_date))
    else:
        print(search_word.upper() + " was not found in the database.")

elif choice.lower() == "d":
    year = input("Enter the year: ")
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    day = input("Enter the day: ")
    day = day.zfill(2)  # Ensure day is 2 digits
    search_date = merge(day, month, year)
    result = getWordByDate(date_list, word_list, search_date)

    if result == "too early":
        print(str(search_date) + " is too early. No wordles occurred before 20210619. Enter a later date.")
    elif result == "too late":
        print(str(search_date) + " is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
    elif result == "not found":
        print("No word was found for the date " + str(search_date) + ".")
    else:
        print("The word entered on " + str(search_date) + " was " + result + ".")
else:
    print("Invalid option. Please enter either 'w' or 'd'.")
