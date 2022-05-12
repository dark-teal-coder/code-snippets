## GitHub: dark-teal-coder 
## First Published Date: 2022-04-16
## Program Input(s): 
### (1) starting hour and minute and duration as integers
## Program Process(es): 
### (1) basic time calculation
## Program Output(s): 
### (1) ending time in 24-hour format as a string
## Program Description: This program contains solutions to more advanced problems in Python Essentials - Part 1 (Basics) at https://edube.org/study/pe1. 

####################################################################################################

## 2.6.1.11 LAB: Operators and expressions
## Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
# Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.
# Test your code carefully. Hint: using the % operator may be the key to success.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

dur_hr_min = divmod(dura, 60)
total_min = mins + dur_hr_min[1]
total_hr = (hour + dur_hr_min[0] + (total_min // 60))
end_hr = total_hr % 24
end_min = (total_min % 60)

print(f"{end_hr}:{end_min}")
