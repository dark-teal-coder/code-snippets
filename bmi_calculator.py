## GitHub: dark-teal-coder 
## First Published Date: 2021-11-15
## Program Input(s): 
### (1) taking a user's weight in kilograms and height in meters
## Program Process(es): 
### (1) calculating the BMI of that user  
## Program Output(s): 
### (1) informing the user what his/her BMI indicates 
## Program Description: This program contains logic that calculates the BMI of a user.

####################################################################################################

print("Input your weight in kilograms:", end=' ')
w = float(input())
print(str(w))
print("Input your height in meters:", end=' ')
h = float(input())
print(str(h))
bmi = w / (h ** 2)
print(f"Your BMI is {bmi}")

if bmi < 18.5: 
	print("Underweight")
elif 18.5 <= bmi and bmi < 25: 
	print("Normal")
elif 25 <= bmi and bmi < 30: 
	print("Overweight")
else: # (bmi >= 30) 
	print("Obesity ")
