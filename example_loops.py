## Break & Continue
### break statement: to skip the current iteration 
### continue statement: to continue with the next one



## While Loops 
### A while loop executes the body of the loop while the condition remains True.
### While loops are mostly used when there is an unknown number of operations to be performed and a condition needs to be checked at each iteration.
### Common pitfalls: 
#### 01) Unintended infinite loops 
#### 02) Failures to initialize all the variables used in the condition before the loop

### Prime Factors 
def print_prime_factors(num):
	## 2 is the first prime
	factor = 2
	## Keep going until the factor is larger than the number
	while factor <= num:
	## Check if factor is a divisor of the number
		if num % factor == 0:
			## If it is, print it and divide the original number
			print(factor)
			num = num / factor
		else: 
		## If it's not, increment the factor by 1
			factor += 1
			return "Done"

print_prime_factors(100)

### Power of 2 
def is_power_of_two(num):
    '''This function checks if the number at parameter 1 can be divided by 2 without a remainder.'''
    while num != 0 and num % 2 == 0:
        num = num / 2
    ## If after dividing by 2 the number is 1, it's a power of 2
    if num == 1:
        return True
    return False

print(is_power_of_two(0)) # Output: False
print(is_power_of_two(1)) # Output: True
print(is_power_of_two(8)) # Output: True
print(is_power_of_two(9)) # Output: False

### Sum of Divisors 
def sum_divisors(num):
	'''This function returns the sum of all divisors of the number at parameter 1, exclusive of itself.'''	
	sum = 0
	divisor = 1 
	while divisor < num: 
		if num % divisor == 0: 
			sum += divisor
			divisor += 1
	return sum

print(sum_divisors(0)) # Output: 0 
print(sum_divisors(3)) # Output: 1 
print(sum_divisors(36)) # Output: 55 (1 + 2 + 3 + 4 + 6 + 9 + 12 + 18) 
print(sum_divisors(102)) # Output: 114 (2 + 3 + 6 + 17 + 34 + 51) 

## Counting Up or Down
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Output: "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Output: "Counting down: 2,1"
print(counter(5, 5)) # Output: "Counting up: 5"

## Multiplication Table
def multiplication_table(start, stop):
	for x in range(start, stop + 1):
		for y in range(1, stop + 1):
			print(str(x * y), end=" ")
		print()

## This will output the following multiplication table: 
### 1 2 3 
### 2 4 6
### 3 6 9
multiplication_table(1, 3)



## For Loops 
### A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence. 
### For loops are mostly used when there is a pre-defined sequence or range of numbers to iterate.
### Common pitfalls: 
#### 01) Forgetting that the upper limit of a range() isn't included 
#### 02) Iterating over non-iterables

### Factorial
def get_factorial(num):
	'''This function returns the factorial of the number at parameter 1.'''
	if n == 0: 
		return 1
    result = 1
	for i in range(1, num + 1):
		result *= i
	return result

print(get_factorial(4)) # Output: 24
print(get_factorial(5)) # Output: 120



## For-loops VS. While-loops 
### Use for-loops when there is a sequence of elements to interate 
### Use while-loops when you want to repeat an action until a condition changes 



## Nested For Loops

### Domino Tiles
for left in range(7): 
	for right in range(left, 7): 
		print("[" + str(left) + "|" + str(right) + "]", end=" ")
	print()

### Home Team VS. Away Team 
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
	for away_team in teams:
		if home_team != away_team:
			print(home_team + " vs. " + away_team)
