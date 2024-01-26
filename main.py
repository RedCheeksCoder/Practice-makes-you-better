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


answer = input("Do you want to continue? (Y/N)")

if answer == 'Y':
    print("We'll continue on playing!!!")
else:
    print("It's sad to say good bye my friend.")

