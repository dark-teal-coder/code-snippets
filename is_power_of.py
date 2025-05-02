# Recursion
def is_power_of(number, base):
    """This function returns whether the number is a power of the given base"""
    if number < base: 
        return base**0 == number
    return is_power_of(number/base, base)

print(is_power_of(8, 2)) # True
print(is_power_of(70, 10)) # False
