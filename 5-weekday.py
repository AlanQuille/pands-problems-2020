# This imports the datetime class for
# class with functions handling dates and times
import datetime

# This uses the today and weekday functions
# in the datetime class to get the current
# date (today) and then get the number of
# the current day, where 0 is Monday and
# 6 is Sunday (weekday) and sets the variable
# dayno to this number
dayno = datetime.datetime.today().weekday()

# This is to test whether the correct statement will 
# be printed if dayno = 6 (weekend) or 3 (weekday)
# dayno = 6
# dayno = 3

# This if statement prints out the appropriate 
# statement if the current day is a weekday
# i.e. dayno is between 0 and 4
if dayno <= 4:
    print("Yes, unfortunately today is a weekday.")
# This else statement prints out the
# appropriate statement if the current day is
# not a weekday i.e. dayno is between 5 and 6
else:
    print("It is the weekend, yay!")

