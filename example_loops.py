## Use for-loops when there is a sequence of elements to interate 
## Use while-loops when you want to repeat an action until a condition changes 

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


def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  divisor = 1 
  while divisor < n: 
    if n % divisor == 0: 
      sum += divisor
    divisor += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120



## Domino Tiles
for left in range(7): 
	for right in range(left, 7): 
		print("[" + str(left) + "|" + str(right) + "]", end=" ")
	print()
