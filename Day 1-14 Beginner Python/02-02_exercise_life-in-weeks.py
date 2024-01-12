# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old.
# Let's assume in 1 year = 365 days = 52 weeks = 12 months
# Example: age = 56 -> You have 12410 days, 1768 weeks, and 408 months left.

current_age = int(input("What is your current age? "))
years_until_90 = 90 - current_age
days = years_until_90 * 365
weeks = years_until_90 * 52
months = years_until_90 * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)