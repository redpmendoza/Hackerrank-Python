import calendar

# Get month, date, and year
month, date, year = map(int, input().split(" "))

# Output day
print(calendar.day_name[calendar.weekday(year,month,date)].upper())