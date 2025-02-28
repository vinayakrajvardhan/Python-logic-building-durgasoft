from datetime import datetime

def find_day(date, month, year):
    dt = datetime(year, month, date)
    return dt.strftime("%A")

# Test the function
date = 28
month = 2
year = 2024
day = find_day(date, month, year)
print(f"The day of the week is: {day}")