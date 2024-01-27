#greet = "Hello world!"
#print(type(greet))

#first_name = "Bryan"
#last_name = "Odina"
#full_name = first_name + " " + last_name

#print("Hello " + full_name)

#INTEGER

#age = 21
#age += 1

#print(age)
#print(type(age))


#isStudent = True
#print("Are you a student?: " + str(isStudent))



#MULTIPLE ASSIGNMENT
#Multiple variable assignment


""" is_student = True
from_taguig = False
stem_student = True



gpa = 3.5
grades = 2.75
height = 167.22


user_name = input("Enter your name: ")

print("Hello, " + user_name + "!")


#snake_case
student_name = "beatrice"
average_grade = 85
class_schedule = "Saturdays and Mondays"

#camelCase
studentName = "beatrice"
averageGrade = 85
classSchedule = "Saturdays and Mondays"

age = 15
number_of_apples = 23
subjects = 7

name = "John"
button = "Green"
coffee = "Is good" """


""" name = "Bryan"
school = "TUP-Taguig"
age = 20
height = 167.2
weight = 70
grades = 2.25
from_taguig = True;

print(f"Hi Im {name}, from {school}. And I am {age} with the height of {height} and weight of {weight}. Recently I got my grades and It's {grades}. Are you from TUP-Taguig too? {from_taguig}") """


""" user_name = input("Enter your name: ")

print(f"Hello, {user_name}") """

""" #BMI CALCULATOR
# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_meters = float(input("Enter your height in meters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

bmi = weight_kg / (height_meters ** 2)

print(f"Name: {name}")
print(f"Age: {age} years")
print(f"BMI: {bmi:.2f}") """


""" base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print(f"\nThe area of the triangle with base {base} and height {height} is: {area:.2f} square units")


# Initialize variables
total_price = 0

item = input("Enter the name of item 1: ")
price = float(input(f"Enter the price of {item}: $"))
quantity = int(input(f"Enter the quantity of {item}: "))
total_price += price * quantity

# Print shopping cart details
print("\nShopping Cart:")
print(f"{item}: {quantity} x ${price:.2f} each")

# Print total price
print(f"\nTotal Price: ${total_price:.2f}") """



""" #Augmented Assignment Operator
count = 0
#count = count + 1
count += 1

print(f"The count is {count}")
#NOTE this all the same to all operator (+, -, *, /)

number = int(input("Enter a number: "))

number = number ** 2
print(f"The square of the number is {number}")

#This can be written as
number **=2
print(f"The square of the number is {number}") """


""" number = int(input("Enter a number: "))
remainder = number % 2 
print(f"The remainder is: {remainder}")

#NOTE Popular in finding odd/even number
 """


""" x = 1.25
y = 2.75
z = 5.00

result = min(x, y, z)
print(f"Max: {result}")

result = round(x)
print(f"Rounded x: {result}") """

""" import math

print(math.pi)
print(math.e)

number = 9
print(math.sqrt(number))
print(math.ceil(number))
print(math.floor(number)) """


""" #Circumference of a circle 2pir
import math
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {circumference}") """

""" #Area of a circle 2pir
import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * radius**2
print(f"The area is {area}") """


""" age = int(input("Enter your age: "))

if age >= 18: 
    print("You are now an adult!")
#elif age <0:
    #print("Call your mama.")
else: 
    print("You need more experience!") """


""" raw_grade = int(input("Enter raw grades: "))

if raw_grade >= 50:
    print("You don't need to take the exam!")
elif raw_grade < 30:
    print("You definitely need to take the exam.")
else: 
    print("You need to take the exam.") """


""" answer = input("Do you want to continue? (Y/N)")

if answer == 'Y':
    print("We'll continue on playing!!!")
else:
    print("It's sad to say good bye my friend.") """

""" answer = True

if answer:
    print("ROCK AND ROLL!!!")
else:
    print("NAHH T_T")
 """

""" ##CALCULATOR
# Get user input for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the selected operation
result = 0

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

# Print the result
if operation in ['+', '-', '*', '/']:
    print(f"Result: {result}")
 """

#LOGICAL OPERATORS

""" temperature = 25

if temperature > 0 and temperature < 30:
    print("Temperature is within good range.")
else:
    print("The temperature is outside the range.") """

#len()
#find(“x”)
#rfind(“x”)
#capitalize()
#upper()
#lower()
#isdigit()
#isalpha()
#count(“x”)
#replace(“x”, “-“)

""" username = input("Enter your username: ")

if len(username) > 12:
    print("Usernames must not be more than 12 characters")
else:
    print(f"Welcome to TUP-Taguig {username}!")

if username.count(" ") >= 1: #find()
    print("Usernames must not contain spaces.")
else:
    print(f"Welcome to TUP-Taguig {username}!")

if not username.isalpha():
    print("Usernames must not contain numbers")
else:
    print(f"Welcome to TUP-Taguig {username}!") """



""" username = input("Enter your username: ")

if len(username) > 12:
    print("Usernames must not be more than 12 characters")
elif username.count(" ") >= 1: #find()
    print("Usernames must not contain spaces.")
elif not username.isalpha():
    print("Usernames must not contain numbers")
else:
    print(f"Welcome to TUP-Taguig {username}!") """

#Indexing
#[start : end : step]

""" credit_card = "5417-2351-6678-1124"

print(credit_card[0])
print(credit_card[0:4])
print(credit_card[5:9])
print(credit_card[5:])
print(credit_card[-3])
print(credit_card[::3])

#Last 4 digit
credit_card = input("Enter your credit card number: ")
last_four = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_four}") """

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

#format specifiers
price1 = 3.14159 
price2 = -987.65 
price3 = 12.34 
print(f"price1 is: ${price1:}") 
print(f"price2 is: ${price2:}") 
print(f"price3 is: ${price3:}")


###########WHILE LOOP############################

# ---------------- EXAMPLE 1 ----------------

name = input("Enter your name: ")

while name == "":
   print("You did not enter your name!")
   name = input("Enter your name: ")

print(f"Hello {name}")

# ---------------- EXAMPLE 2 ----------------

age = int(input("Enter your age: "))

while age < 0:
   print("Age can't be negative")
   age = int(input("Enter your age: "))

print(f"You are {age} years old")


# ---------------- EXAMPLE 3 ----------------

food = input("Enter a food you like (q to quit): ")

while not food == "q":
   print(f"You like {food}")
   food = input("Enter another food you like (q to quit): ")

print("bye")

# ---------------- EXAMPLE 4 ----------------

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")



###########FOR LOOPS#########################
# ---------------- EXAMPLE 1 ----------------

for x in range(1, 11):
   print(x)

# ---------------- EXAMPLE 2 ----------------

for x in reversed(range(1, 11)):
   print(x)

print("Happy New Year!")

# ---------------- EXAMPLE 3 ----------------

for x in range(1, 11, 2):
   print(x)

# ---------------- EXAMPLE 4 ----------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)

# ---------------- CONTINUE ----------------

for x in range(1, 21):
   if x == 13:
       continue
   else:
       print(x)

# ---------------- BREAK ----------------

for x in range(1, 21):
   if x == 13:
       break
   else:
       print(x)