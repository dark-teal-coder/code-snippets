## GitHub: dark-teal-coder 
## First Published Date: 2021-11-15
## Program Input(s): 
### (1) taking an integer 
## Program Process(es): 
### (1) using for-loop to loop from 0 to the integer and find all numbers containing 3 
### (2) using list comprehension to loop from 0 to the integer and find all numbers containing 3 
## Program Output(s): 
### (1) returning a list of numbers containing 3 
### (2) returning a list of numbers containing 3 
## Program Description: This program is a part of Assignment 07 from the course CSCI-E-7 Introduction to Python at Harvard Extension School, Harvard University. 

####################################################################################################

from typing import List


def whozit_loop(n: int) -> List[int]:
	"""This function takes an integer, loop from 0 through to the integer, and returns a list of the numbers containing 3 using for-loop."""
	result = []
	for i in range(n):
		if '3' in str(i): 
			result.append(i)
	return result

def whozit_list(n):
	"""This function takes an integer, loop from 0 through to the integer, and returns a list of the numbers containing 3 using list comprehension."""
	return [i for i in range(n) if '3' in str(i)]


user = int(input())

print(whozit_loop(user))
print(whozit_list(user))