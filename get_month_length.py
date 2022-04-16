## GitHub: dark-teal-coder 
## First Published Date: 2021-12-22
## Program Input(s): 
### (1) Year and month as integers
### (2) Year and month as integers
## Program Process(es): 
### (1) Go to the last day of the month and subtract one day
### (2) Use pre-defined function from calendar module to get number of days in month
## Program Output(s): 
### (1) Last data of the month
### (2) Number of days in the month
## Program Description: We usually need to get the date range of a particular month (and year) when we try to generate reports in Python. This code will help us get the start and end dates of a particular month and year. It is based on the official Python documentation of the "datetime" and "calendar" libraries.

####################################################################################################

from datetime import date
from datetime import timedelta
from calendar import monthrange


def get_month_date_range(y: int, m: int) -> date: 
	"""This function takes year with century as a decimal number and month as a decimal number, and returns the last date of the month."""
	start_date = date(y, m, 1) 
	## Initialize with any value 
	end_date = date.today()
	if start_date.month == 12: 
		## If it's Dec, the last day should be 31. 
		end_date = start_date.replace(day=31)
		return start_date, end_date 
	## For all other months, go to next month and go back a day. 
	end_date = start_date.replace(month=start_date.month+1) - timedelta(days=1)
	return start_date, end_date


def get_month_range(y: int, m: int) -> int: 
	"""This function take year with century as a decimal number and month as a decimal number, and returns number of days in month."""
	month_range = monthrange(y, m)
	return month_range[1]


## Unit test 
start_date, end_date = get_month_date_range(2024, 2)
print(f"Getting date range from {start_date} to {end_date}")
## Unit test 
days_of_month = get_month_range(2024, 2)
print(days_of_month)

####################################################################################################

## REFERENCES: 
### strftime() and strptime() format codes: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior 
