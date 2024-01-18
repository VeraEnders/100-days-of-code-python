# Days in Month

# There is a function is_leap() that returns True if it is a leap year and return False if it is not a leap year.
# Create a function days_in_month() which will take a year and a month, then return the number of days in the month
# Example input: days_in_month(year=2022, month=2). Output: 28

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days = month_days[month - 1]

  if month == 2 and is_leap(year):
    return days + 1
  else:
    return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)