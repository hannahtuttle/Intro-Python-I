"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


y = input("Input the year: ")
m = input("Input the month: ")

def check_calendar(year, month):
    try:
      if year== '' and month=="":
        print(f'current calendar: {calendar.month(datetime.now().year, datetime.now().month)}')
      elif len(month) == 1 and year == '':
        # print(month)
        print(f"{calendar.month(datetime.now().year, int(month))}")
      elif year and month:
        print(f'the month and year you selected: {calendar.month(int(year), int(month))}')
    except :
      print('expected year format to look like 1990 and month format to look like 1')    
    # print(calendar.month(year, month))


check_calendar(y,m)
