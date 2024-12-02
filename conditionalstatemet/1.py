
#1.Check a number
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



#2.Even or odd
num = 6
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#3.grader

percentage = 92
if percentage >= 90:
    print("Grade: A")
percentage = 75
if percentage >= 70 and percentage < 90:
    print("Grade: B")
percentage = 55
if percentage >= 50 and percentage < 70:
    print("Grade: C")
percentage = 40
if percentage < 50:
    print("Grade: F")



#4.divisibility
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")

num = 9
if num % 3 == 0:
    print("Divisible by 3")

num = 10
if num % 5 == 0:
    print("Divisible by 5")

num = 7
if num % 3 != 0 and num % 5 != 0:
    print("Not divisible by either 3 or 5")


#5.smallest number
num1 = 10
num2 = 20
if num1 < num2:
    print(num1)
else:
    print(num2)

num1 = 25
num2 = 15
if num1 < num2:
    print(num1)
else:
    print(num2)



#6.Find the largest of three numbers
num1 = 10
num2 = 20
num3 = 30

if num1 >= num2:
    if num1 >= num3:
        print(num1, "is the largest")
    else:
        print(num3, "is the largest")
else:
    if num2 >= num3:
        print(num2, "is the largest")
    else:
        print(num3, "is the largest")


 #7.Check leap year  
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")


#8.temperature check
temperature = 25
if temperature < 15:
    print("Temperature is Cold")
elif temperature >= 15 and temperature <= 30:
    print("Temperature is Warm")
else:
    print("Temperature is Hot")


#9.vowels
char = 'a'
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")



#10. Driving eligibility  
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You are eligible to drive")
    else:
        print("You need a valid license to drive")
else:
    print("You must be 18 or older to drive")




#11.Triangle 
    # Get user input
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Check if sides can form a triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")

#12.Calculate tax based on salary  
salary = 6000000
if salary <= 5000000:
    tax = salary * 0.05
    print("Tax:", tax)
elif salary > 5000000 and salary <= 10000000:
    tax = salary * 0.10
    print("Tax:", tax)
else:
    tax = salary * 0.20
    print("Tax:", tax)

#13. Categorize age  
age = 35
if age >= 0 and age <= 12:
    print("You are a Child")
elif age >= 13 and age <= 19:
    print("You are a Teen")
elif age >= 20 and age <= 59:
    print("You are an Adult")
else:
    print("You are a Senior")



#14.Logical AND check  
num = 20
if num > 10 and num % 2 == 0:
    print(num, "is greater than 10 and divisible by 2")
else:
    print(num, "does not meet the conditions")


#15.Logical OR check
num = 3
if num < 5 or num > 20:
    print(num, "meets the condition")
else:
    print(num, "does not meet the condition")


#16. Electricity bill  
units = 150
if units <= 100:
    bill = units * 5
    print("Electricity bill: ", bill)
elif units > 100 and units <= 200:
    bill = units * 10
    print("Electricity bill: ", bill)
else:
    bill = units * 15
    print("Electricity bill: ", bill)


#17.Season finder  
month = "June"
if month in ("December", "January", "February"):
    print("Season: Winter")
elif month in ("March", "April", "May"):
    print("Season: Spring")
elif month in ("June", "July", "August"):
    print("Season: Summer")
elif month in ("September", "October", "November"):
    print("Season: Autumn")
else:
    print("Invalid month")


#18.Password validation
password = "password@123"
if len(password) >= 8 and "@" in password:
    print("Password is valid")
else:
    print("Password is not valid. It should be at least 8 characters and contain '@'.")




#19.BMI
# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Categorize BMI
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You are normal.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are obese.")

#20.Character type checker  
char = "A"

if char.isalpha():
    print(char, "is an Alphabet")
elif char.isdigit():
    print(char, "is a Digit")
else:
    print(char, "is a Special character")