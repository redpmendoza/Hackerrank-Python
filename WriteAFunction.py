# Function is leap
def is_leap(year):

    # Set leap to false
    leap = False

    # Check if year is leap year
    if (year % 400 == 0):
        leap = True
    elif (year % 4 == 0 and year % 100 != 0):
        leap = True
    return leap

# Get year
year = int(input())

# Output result
print(is_leap(year))