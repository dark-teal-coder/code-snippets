## Use for-loops when there is a sequence of elements to interate 
## Use while-loops when you want to repeat an action until a condition changes 



## While Loops 

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



## For Loops 

### Factorial
def get_factorial(num):
	'''This function returns the factorial of the number at parameter 1.'''
	result = 1
	for i in range(1, num + 1):
		result *= i
	return result

print(get_factorial(4)) # Output: 24
print(get_factorial(5)) # Output: 120



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
