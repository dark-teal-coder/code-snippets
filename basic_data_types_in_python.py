## GitHub: dark-teal-coder 
## First Published Date: 2021-09-26

####################################################################################################
 
## OUTLINE:
### Integers
### Floating-point Numbers
### Complex Numbers
### Strings
### Booleans
### Built-in Functions
 
####################################################################################################
 
## Integers
## Def: whole numbers of any length up to memory limit of computer
### Default is decimal system (base 10)
## We use variables to store data
## Syntax: variable = data (= is an assignment operator)
a = 1
b = 2
c = 3
## print() function prints the specified message to the screen, or other output device
print(a, b, c)
## 7 arithmetic operators in Python:
### 01) Addition
print(a + b)
### 02) Subtraction
print(b - a)
### 03) Multiplication
print(b * c)
### 04) Division
print(c / b)
### 05) Modulus
print(c % b)
### 06) Exponentiation
print(b ** c)
### 07) Floor division
print(c // b)
## Number Systems
### Decimal/base 10 (default)
dec_num = 2021
print(dec_num)
### Binary/base 2
bin_num = 0b101010111
print(bin_num)
### Hexadecimal/base 16
hex_num = 0xac4d
print(hex_num)
### Octal/base 8
oct_num = 0o123456
print(oct_num)
num1 = 123
num2 = "123"
print(num1, num2)
## TypeError: num1 and num2 contain different types of data
# print(num1 + num2)
## To check the data type: type()
print(type(num1), type(num2))
## Type conversion:
num3 = int(num2)
num4 = bin(num1)
num5 = oct(num1)
num6 = hex(num1)
print(type(num3), type(num4), type(num5), type(num6))
 
####################################################################################################
 
## Floating-point Numbers
## Def: any number with a decimal point
flt1 = 2021.0
flt2 = 26.09
print(type(flt1), type(flt2))
## Float as the result of division
print(flt1 / flt2)
print(10 / 2)
## To turn an integer into a float
flt3 = float(100)
print(type(flt3))
## Be defined using scientific notation (powers of 10)
sci_no1 = 1e3
sci_no2 = 1e-2
print(sci_no1, sci_no2)
 
####################################################################################################
 
## Complex Numbers
## Def: a number in the form of a + bj, where a and b are real numbers and j satisfies j*j = -1
## Syntax: real part + imaginary part
com_num1 = 1 + 2j
com_num2 = 3 + 4j
print(type(com_num1), type(com_num2))
print(com_num1 + com_num2)
print(com_num1 - com_num2)
print(com_num1 * com_num2)
print(com_num1 / com_num2)
 
####################################################################################################
 
## Strings
## Def: a sequence of 0 or more characters enclosed in double quotes or single quotes
### Formats: raw and triple-quoted strings
str1 = "Hello,"
str2 = "Ree!"
print(str1, str2)
str3 = "I'm learning Python."
print(str3)
str4 = 'The full name of Bangkok is "Krung Thep Mahanakhon Amon Rattanakosin".'
print(str4)
## SyntaxError: the 2nd single quote signals end of string to Python
# print('I'm learning Python.')
## String conversion
print(type(str(2021)))
 
####################################################################################################
 
## Escape Sequences
## Escaping allows normal character interpretation to be suspended and that string to be defined as normal
## Escape character: backslash (\) + character to be escaped
### 01) Backslash
esc1 = "An escape character is made up of a \\ and an illegal character."
print(esc1)
### 02) Single quote
esc2 = 'She said, "I didn\'t know how to code before."'
print(esc2)
### 03) Double quote
esc3 = "The founder of Harvard University is called \"John Harvard\"."
print(esc3)
### 04) New line
esc4 = "This is line 1.\nThis is line 2."
print(esc4)
### 05) Tab
esc5 = "Platform: \t\tReal Python\nInstructor: \tDarren Jones"
print(esc5)
### 06) Carriage return
esc6 = "This is line 1.\rThis is line 2."
print(esc6)
### 07) Backspace
esc7 = "THA\b"
print(esc7)
### 08) Form feed
esc8 = "This is line 1.\fThis is line 2."
print(esc8)
### 09) Vertical tab
esc9 = "Word1\vWord2"
print(esc9)
### 10) Octal value
esc10 = "\110\141\162\166\141\162\144"
print(esc10)
### 11) Hexadecimal value
esc11 = "\x55\x6e\x69\x76\x65\x72\x73\x69\x74\x79"
print(esc11)
 
####################################################################################################
 
## Raw Strings
r_str = r"Type \\ when you want to type a backslash"
print(r_str)
## Useful in applications where escape sequence characters aren't interpreted normally
### E.g. regular expressions
 
####################################################################################################
 
## Triple-quoted Strings
print("""Her name is "Ree", isn't it?""")
print("""
Harvard University
Massachusetts Hall
Cambridge, MA 02138
""")
## Most commonly used in docstrings for functions
## Define a function
def my_function(value):
    """
    This is a docstring describing what the function does.
    E.g. This function takes a value and prints it out on the screen.
    """
    print("This value will be printed:", value)
    return
## Call the function
my_function("Ree")
 
####################################################################################################
 
## Booleans
truth = True
lie = False
print(truth, "or", lie)
## Numbers to Booleans
print(bool(0), bool(1))
## Equality comparison
## Syntax: double equal sign ==
print(1 == 1)
print(1 == "1")
print("Python" == "python")
## if Statements
if truth:
    print("It's true.")
else:
    print("It's false.")
## Be 0 or more elif parts; be 0 or 1 else statement
n = int(input("Please enter an integer: "))
if n > 0:
    print("It's a positive integer.")
elif n < 0:
    print("It's a negative integer.")
else:
    print("It's zero.")
 
####################################################################################################
 
## Composite Data Types
## Lists
### https://www.insider.com/the-20-most-popular-travel-destinations-in-the-world-2016-9#5-new-york-new-york-16
pop_travel_des = ['Bangkok', 'London', 'Paris', 'Dubai', 'New York']
### https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm
olympics_2020_gold = ["USA", "CHN", "JPN", "GBR", "RUS"]
### https://www.forbes.com/billionaires/
richest_ages_2021 = [57, 49, 72, 65, 36]
## Elements of a list can be accessed using square bracket notation
print(pop_travel_des[0], olympics_2020_gold[1], richest_ages_2021[-1])
print(pop_travel_des[0:3])
## Logic error: from the last to the first
# print(list1[-1:-5])
## Correct way: from the left to the right
print(olympics_2020_gold[-5:-1])
## Lists are mutable/changeable
olympics_2020_gold[-1] = "ROS"
print(olympics_2020_gold)
## Tuples
### https://www.norden.org/en/information/facts-about-nordic-countries
nordics = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden', 'Faroe Islands', 'Greenland', 'Aland')
## Last 3 are territories
territories = nordics[-3:]
print(territories)
## Tuples are immutable/unchangeable
## TypeError: 'tuple' object does not support item assignment
# nordics[0] = 'Germany'
## Sets
## Def: data structure containing only unique elements
num_shared = [1, 2, 2, 3, 3, 3]
num_set = set(num_shared)
num_unique = list(num_set)
print(num_shared, num_set, num_unique)
## Dictionary
## Syntax: {key1: value1, key2: value2, ...}
## To create an empty dictionary
empty_dict = {}
print(empty_dict)
## To create a dictionary with key-value pairs
harvard_dict = {'country': 'United States', 'state': 'Massachusetts'}
## To add a new value to the dictionary with reference to a new key
harvard_dict['city'] = 'Boston'
## To print the entire dictionary
print(harvard_dict)
## To print values in dictionary
print("Harvard is in", harvard_dict['city'], ",", harvard_dict['state'], ",", harvard_dict['country'])
## Using print() sep parameter to specify character(s) to separate the arguments
print("Harvard is in", harvard_dict['city'], ", ", harvard_dict['state'], ", ", harvard_dict['country'], sep='')
## Using f-string and placeholders {} to insert variables into the string
print(f"Harvard is in {harvard_dict['city']}, {harvard_dict['state']}, { harvard_dict['country']}")
## KeyError: the key 'district' does not exist in the dictionary
# print(harvard_dict['district'])
## Safer way to access values in dictionary
print(harvard_dict.get('district'))
 
####################################################################################################
 
## Functions: Math
print(abs(10), abs(-10), abs(0.1), abs(-0.1))
print(divmod(2021, 9))
print(max([1, 2, 3]))
print(max([-2, -1, 0]))
print(min([1, 2, 3]))
print(min([-2, -1, 0]))
print(pow(2, 3), 2 ** 3)
## pow() can take a third argument
print(pow(3, 2, 2), (3 ** 2) % 2)
print(round(1.5), round(1.6))
print(sum([2, 4, 6, 8, 10]))
 
####################################################################################################
 
## Functions: Type Conversion
## Text relies on the American Standard Code for Information Interchange (ASCII)
## Unicode has become more common as it represents more characters
## ASCII Table: https://ascii.cl/
print(ascii('Hello'))
print(ascii('สวัสดี'))
print(ascii('你好'))
print(ascii('こんにちは'))
print(chr(0x4f60), chr(0x597d))
print(ord('A'), ord('a'))
print(chr(65), chr(97))
print(int('123'))
print(int('123', base=16))
print(int('123', base=8))
print(int('0', base=2), int('1', base=2), int('10', base=2), int('11', base=2))
print(bin(10), oct(10), hex(10))
print(float(10))
print(complex(10))
print(str(10))
## Boolean value of 1 or more returns True
print(bool(0), bool(1), bool(2))
 
####################################################################################################
 
## Functions: Iterables and Iterators
## Built-in Functions working on iterables
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## len() returns the length of the iterable passed in
print(len(num_list))
## reversed() method returns an iterator that accesses the given sequence in the reverse order,
reversed_num = reversed(num_list)
print(reversed_num)
## list() creates a list object which is an ordered and changeable collection.
reversed_num_list = list(reversed_num)
print(reversed_num_list)
## sorted() returns a sorted list of the specified iterable object.
print(sorted([2, 0, 2, 1, 0, 9, 2, 6]))
## any() returns true if any of the items is True and returns False if empty or all are false.
### Any can be thought of as a sequence of OR operations on the provided iterables.
## all() returns True if all of the items are True, or if the iterable is empty.
### All can be thought of as a sequence of AND operations on the provided iterables.
boo_list1 = [True, True, True]
boo_list2 = [True, False, True]
boo_list3 = [False, False, False]
print(any(boo_list1), any(boo_list2), any(boo_list3))
print(all(boo_list1), all(boo_list2), all(boo_list3))
## range() returns a sequence of numbers, starting from 0 and increments by 1 (by default), and stops before a specified number.
print(range(10))
print(list(range(10)))
print(list(range(0, 10)))
print(list(range(0, 10, 2)))
## https://spectrum.ieee.org/top-programming-languages/
top_prog_lang_21 = ['Python', 'Java', 'C', 'C++', 'JavaScript', 'C#', 'R', 'Go', 'HTML', 'Swift']
for prog_lang in top_prog_lang_21:
    print(prog_lang)
## Add a counter
count = 0
for prog_lang in top_prog_lang_21:
    print(count, prog_lang)
    count += 1
## enumerate() adds a counter to an iterable and returns it in a form of enumerating object.
for count, prog_lang in enumerate(top_prog_lang_21):
    print(count, prog_lang)
## zip() returns an iterator of tuples where items at the same position of the iterators are paired together.
countries = ['Australia', 'Canada', 'New Zealand', 'United State of America', 'United Kingdom']
capitals = ['Canberra', 'Ottawa', 'Wellington', 'Washington, D.C.', 'London']
merged_list1 = []
for i in range(len(countries)):
    print(countries[i], capitals[i])
    merged_list1.append((countries[i], capitals[i]))
print(merged_list1)
merged_list2 = zip(countries, capitals)
print(merged_list2)
##
iterator = iter([1, 2, 3])
print(next(iterator))
print(next(iterator))
print(next(iterator))
## StopIteration: the list is exhausted
# print(next(iterator))
 
####################################################################################################
 
## Functions: Input and Output
for i in range(100):
    print(i)
## end()
for i in range(100):
    print(i, end=' ')
print()
## Opening a file in "write" mode
file = open('example.txt', 'w')
file.write("Hi, there!\n")
file.write("I'm a file.\n")
file.close()
## Opening a file in "read" mode
file = open('example.txt', 'r')
print(file.readlines())
file.close()
## More sophisticated way to write this:
with open('example.txt', 'r') as file:
    print(file.readlines())
 
####################################################################################################
 
## Functions: Variables, References, and Scope
## dir() returns list of the attributes and methods of any object
### E.g., functions, modules, strings, lists, dictionaries, etc.
name = "Ree"
print(dir(name))
## __function__ with double underscore called dunder methods
import datetime
print(dir(datetime))
print(dir(datetime.datetime))
## Scope
var = "global"
def function():
    var = "local"
    print(var)
print(var)
function()
print(var)
## vars() returns the __dict__ attribute for a module, class, instance, or any other object if the same has a __dict__ attribute.
## globals() returns the dictionary of current global symbol table.
var1 = "global variable"
var2 = "another global variable"
def function():
    var1 = "local"
    print(var1)
    print("1", vars(), globals())
    print(var2)
print(var1)
print("2", vars(), globals())
function()
print(var1)
print("3", vars(), globals())
 
####################################################################################################
 
## Functions: Miscellaneous
## exec() is used for the dynamic execution of Python program which can either be a string or object code.
### Taking a command from within a string
author = 'Ree'
command = """print("This program is written by", author)"""
exec(command)
### Taking a command from a command-line interpreter
#### Input a command, e.g., import os; os.system('dir'), when prompted
job = input("""Assign a simple task here: """)
exec(job)
## eval() parses the expression passed to it and runs python expression(code) within the program.
#### Input a math expression, e.g. 1 + 2, when prompted
calculate = input("""Solve a math problem here: """)
print(eval(calculate))
## eval() will also evaluates a command as exec()
## hash() returns the hash value of an object if it has one.
### The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary
print(hash(123))
print(hash("Hello!"))
print(hash('Hello.'))
## It can be used to check if two objects are the same
print(hash("Hello!") == hash('Hello.'))