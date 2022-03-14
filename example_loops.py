def print_prime_factors(number):
	# Start with two, which is the first prime
	factor = 2
	# Keep going until the factor is larger than the number
	while factor <= number:
	# Check if factor is a divisor of number
	if number % factor == 0:
		# If it is, print it and divide the original number
		print(factor)
		number = number / factor
	else:
		# If it's not, increment the factor by one
		factor += 1
		return "Done"

print_prime_factors(100)

def is_power_of_two(n):
	# Check if the number can be divided by two without a remainder
	while n != 0 and n % 2 == 0:
		n = n / 2
	# If after dividing by two the number is 1, it's a power of two
	if n == 1:
		return True
	return False

print(is_power_of_two(0)) # Output: False
print(is_power_of_two(1)) # Output: True
print(is_power_of_two(8)) # Output: True
print(is_power_of_two(9)) # Output: False
