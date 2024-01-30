"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Define a disctionary to map month names to month numbers
    month_dict={'January':1,'February':2,'March':3, 'April':4,'May':5, 'June':6, 'July':7,'August':8, 
                'September':9,'October':10,'November':11,'December':12}
     
     # Extract day and month from the provided dates
    today_day,today_month= todays_date.split()
    scheduled_day, scheduled_month= scheduled_date.split()

     # Remove the 'th', 'st', 'nd', or 'rd' from the day
    today_day =int(today_day[:-2])
    scheduled_day =int(scheduled_day[:-2])
     # Get today's date and the scheduled date
    today = datetime(datetime.now().year, month_dict[today_month],today_day)
    scheduled =datetime (datetime.now().year, month_dict[scheduled_month],scheduled_day)
     # Compare the dates
    if scheduled < today:
        print("The scheduled date has passed.")
    
    elif scheduled == today:
        print("The scheduled date is today.")
    else:
        print("The sheduled date is yet to pass.")

   


# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
