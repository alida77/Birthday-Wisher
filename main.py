# Extra Hard Starting Project
import pandas
import random
import datetime as dt
import smtplib

my_email = "Your Email Here"
my_password = "Your Password Here"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# birthdays_dict = {(month, day): data_row}
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        contents = letter_file.read()
    final_letter = contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{final_letter}")
