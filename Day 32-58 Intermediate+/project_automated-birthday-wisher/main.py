import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "sender-name@gmail.com"
# Gmail app password 
PASSWORD = "qwerty"

def send_email(text, recipient_email):
  # SMTP = Simple Mail Transfer Protocol
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL, 
      to_addrs=f"{recipient_email}", 
      msg=f"Subject:Happy Birthday!\n\n{text}"
    )

def pick_quote():
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
  return quote

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
  # Person's actual info
  person_name = birthdays_dict[today]["name"]
  person_email = birthdays_dict[today]["email"]

  # Pick a random quote
  quote = pick_quote()

  # Pick a random letter from letter templates
  random_letter_template = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

  with open(random_letter_template) as template:
    text = template.read()
    # Replace the [NAME] with the person's actual name
    updated_text = text.replace("[NAME]", person_name)

    # Create a new letter with the name
    with open(f"letter_for_{person_name}.txt", mode="a") as letter:
      letter.write(updated_text)
      letter.write(f"\n\n{quote}")
    
    # Send the letter to that person's email address.
    send_email(updated_text, person_email)