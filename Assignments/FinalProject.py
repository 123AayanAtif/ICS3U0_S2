"""
Author : Aayan Atif
Student number: 760754
Course code: ICS3U
Revision date : June 12, 2025
Program : Credit Card Expiry Checker
Description:
This program reads credit card data from a file and checks each card for validity using the Luhn algorithm.  
It identifies cards that are either expired or about to expire (as of a specified cutoff date), sorts them by expiry date, and displays a color-coded report in the console.

"""




# ANSI color codes for output formatting
CLR_RED = "\033[91m"        # Red for expired cards
CLR_YELLOW = "\033[93m"     # Yellow for soon-to-expire cards
CLR_RESET = "\033[0m"       # Reset to default color


def validate_luhn(num_str):
  
    """
    Validates a credit card number string using the Luhn algorithm.
    Returns True if valid, False otherwise.
    
    Variable Dictionary:
    num_str (str) = credit card number string passed into validate_luhn()
    checksum (int) = sum of digits used in Luhn checksum calculation
    rev_str (str) = reversed string of num_str for Luhn processing
    idx (int) = loop index for iterating over digits in reversed credit card number
    digit (int) = integer digit currently processed in Luhn algorithm
    """
    checksum = 0
    rev_str = num_str[::-1]  # Reverse card number string

    for idx in range(len(rev_str)):
        digit = int(rev_str[idx])  # Convert character to digit
        if idx % 2 == 1:  # Every second digit from right
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit  # Accumulate total

    return checksum % 10 == 0  # Must be divisible by 10


def sort_by_expiry(data_list):
    """
    Sorts the list of credit card records in place by expiry date (YYYYMM format) using merge sort.
    
    Variable Dictionary:
    data_list (list) = list of card records being sorted in sort_by_expiry()
    mid_idx (int) = midpoint index to split records into left and right halves
    left_part (list) = left half of data_list
    right_part (list) = right half of data_list
    a (int) = index for iterating over left_part
    b (int) = index for iterating over right_part
    c (int) = index for placing merged elements into data_list
    """
  
    if len(data_list) > 1:
        mid_idx = len(data_list) // 2  # Find midpoint
        left_part = data_list[:mid_idx]  # Split into left half
        right_part = data_list[mid_idx:]  # Split into right half

        sort_by_expiry(left_part)   # Recursively sort left
        sort_by_expiry(right_part)  # Recursively sort right

        a = b = c = 0  # Indices for merge operation

        # Merge sorted halves into main list
        while a < len(left_part) and b < len(right_part):
            if left_part[a][-1] < right_part[b][-1]:  # Compare expiry
                data_list[c] = left_part[a]
                a += 1
            else:
                data_list[c] = right_part[b]
                b += 1
            c += 1

        # Append leftovers from left half
        while a < len(left_part):
            data_list[c] = left_part[a]
            a += 1
            c += 1

        # Append leftovers from right half
        while b < len(right_part):
            data_list[c] = right_part[b]
            b += 1
            c += 1


def process_line(text):
    """
    Parses a single line of input data into its components,
    validates, and returns a record if valid.
    
    Variable Dictionary:
    text (str) = current line read from file during processing
    fields (list) = list of fields parsed from a line by splitting on commas
    first (str) = first name extracted from line data
    last (str) = last name extracted from line data
    type_id (str) = credit card type extracted from line data
    number (str) = credit card number extracted from line data
    mm (str) = raw month from file
    yy (str) = raw year from file
    m (int) = expiry month converted to integer
    y (int) = expiry year converted to integer
    date_num (int) = combined integer YYYYMM format of expiry date
    """
  
    fields = text.strip().split(",")  # Split line by commas

    if len(fields) != 6:  # Ensure correct field count
        return None

    first, last, type_id, number, mm, yy = fields

    if not number.isdigit():  # Must be all digits
        return None

    try:
        m = int(mm)
        y = int(yy)
    except ValueError:  # Invalid month/year values
        return None

    if not (1 <= m <= 12):  # Check valid month
        return None

    date_num = y * 100 + m  # Convert to YYYYMM format
    return [first, last, type_id, number, m, y, date_num]


def print_expired(data_expired):
    """
    Prints the expired cards report to the console with colors.
    
    Variable Dictionary:
    data_expired (list) = list of records containing expired or soon-to-expire cards
    head (str) = report column titles
    bar (str) = line to separate header and entries
    rec (list) = single record from data_expired used during output
    clr (str) = chosen ANSI color code string depending on status
    line (str) = formatted output line
    summary (str) = summary line showing count
    """
  
    if not data_expired:
        print(CLR_RED + "No expired or soon-to-expire credit cards found." + CLR_RESET)
        return

    # Report header
    head = "{:<20} {:<12} {:<20} {:<6} {}".format("Name", "Card Type", "Number", "Expiry", "Status")
    bar = "-" * 70

    print(head)
    print(bar)

    # Output each card with color formatting
    for rec in data_expired:
        clr = CLR_RED if rec[4] == "EXPIRED" else CLR_YELLOW
        entry = "{:<20} {:<12} {:<20} {:<6} {}".format(rec[0], rec[1], rec[2], rec[3], rec[4])
        print(clr + entry + CLR_RESET)

    # Output summary
    final_line = "\nTotal expired/renew immediately cards: {}".format(len(data_expired))
    print(final_line)


def launch():
    """
    Main function to process credit card data and output the expiry report.
    
    Variable Dictionary:
    file_path (str) = file path for input data of credit cards
    cutoff (int) = integer YYYYMM format representing the expiry cutoff date
    results (list) = list of records containing expired or soon-to-expire cards
    data_lines (list) = list of all lines read from the input file
    entry (list) = parsed credit card record
    first (str) = first name
    last (str) = last name
    type_id (str) = credit card type
    number (str) = credit card number
    m (int) = expiry month
    y (int) = expiry year
    date_num (int) = expiry date in YYYYMM format
    status (str) = "EXPIRED" or "RENEW IMMEDIATELY"
    full_name (str) = formatted full name padded for alignment
    formatted_exp (str) = formatted expiry date in YYYYMM string format
    """
    path = "/workspaces/ICS3U_S2/ICS3U/Data/cardnumbers.dat"  # Input file
    cutoff = 202506  # June 2025 (YYYYMM)
    found = []  # Store expired or soon-expiring records

    try:
        with open(path, "r") as handle:
            lineset = handle.readlines()  # Read all lines

        for line in lineset[1:]:  # Skip header
            row = process_line(line)
            if row is None:
                continue  # Skip invalid lines

            first, last, type_id, number, m, y, date_num = row

            # Check if expired and valid
            if date_num <= cutoff and validate_luhn(number):
                stat = "EXPIRED" if date_num < cutoff else "RENEW IMMEDIATELY"
                label = (first + " " + last + ":").ljust(20)
                type_id = type_id.ljust(12)
                number = "#" + number
                formatted = str(y) + str(m).zfill(2)  # Pad month
                found.append([label, type_id, number, formatted, stat, date_num])

        sort_by_expiry(found)  # Sort results
        print_expired(found)   # Print report

    except FileNotFoundError:
        print(CLR_RED + "Error: CARDNUMBERS.dat not found at the given path." + CLR_RESET)

    except Exception as err:
        print(CLR_RED + "An unexpected error occurred: " + str(err) + CLR_RESET)


# Program entry point
if __name__ == "__main__":
    launch()
