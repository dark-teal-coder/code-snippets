## GitHub: dark-teal-coder 
## First Published Date: 2022-03-23
## Program Input(s): 
### (1) N/A
## Program Process(es): 
### (1) N/A
## Program Output(s): 
### (1) N/A
## Program Description: This is a note to show the difference between break and continue statements. 

####################################################################################################

# break Statement and else Clauses on Loops
## The break statement breaks out of the innermost enclosing for or while loop.

# Loop statements may have an else clause. A loop's else runs when no break occurs.
# It is executed:
	# when the loop terminates through exhaustion of the list (with for) 
	# when the condition becomes false (with while) 
	# not when the loop is terminated by a break statement

# This is exemplified by the following loop, which searches for prime numbers:

for n in range(2, 21):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# Loop fell through without finding a factor
		print(n, 'is a prime number')

# continue Statement
## The continue statement continues with the next iteration of the loop.

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

####################################################################################################

## REFERENCES: 
### break and continue Statements, and else Clauses on Loops: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
