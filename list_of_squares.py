## GitHub: dark-teal-coder 
## First Published Date: 2021-11-15
## Program Input(s): 
### (1) taking an integer  
## Program Process(es): 
### (1) using for-loop to find squares from 0 to N*N
### (2) using list comprehension to find squares from 0 to N*N 
## Program Output(s): 
### (1) returning a list of squares from 0 to N*N 
### (2) returning a list of squares from 0 to N*N
## Program Description: This program is a part of Assignment 07 from the course CSCI-E-7 Introduction to Python at Harvard Extension School, Harvard University. 

####################################################################################################

from typing import List


def squares_loop(N: int) -> List[int]: 
    """This function takes an integer N, and returns a list of the squares from 0 up to (N*N) using for-loop."""
    result = []
    for i in range(N + 1): 
        result.append(i * i)
    return result 

def squares_list(N):
    """This function takes an integer N, and returns a list of the squares from 0 up to (N*N) using list comprehension."""
    return [i * i for i in range(N + 1)]


user = int(input())

print(squares_loop(user))
print(squares_list(user))
