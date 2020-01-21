# 1. program to find the square root
print('Program to find the square root of a number')
num = int(input('Enter the number for finding the square root:'))
print(f'The square root of {num} is : {num ** 0.5}')

# 2. program to calculate the area of a triangle
print('Program to find the area of a triangle')
a, b, c = tuple(map(lambda x: int(x), (input('Enter the 3 sides of triangle comma separated:').split(','))))
print(f'Sides of the triangle entered are: {a},{b},{c}')
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('Area of the triangle is: %4.2f' % area)

# 3. program to solve quadratic equation
print('Program to solve the quadratic equation, ax**2 + b*x + c')
a, b, c = tuple(map(lambda x: int(x), (input('Enter the variables a,b,c of quadratic equation, comma separated:').split(','))))
print(f'The variables entered are: {a},{b},{c}')
d = (b ** 2) - 4*a*c
sol1 = (-b + (d ** 0.5)) / (2 * a)
sol2 = (-b - (d ** 0.5)) / (2 * a)
print('The solutions for quadratic equations are: {0:4.2f} and {1:4.2f}'.format(sol1, sol2))

# 4. Swap two variables
print('Program for swapping two variables in Python')
a = 10
b = 20
print(f"Before swap, value of a = {a} and b = {b}")
a,b = b,a
print(f"After swap, value of a = {a} and b = {b}")

# 5. Program to generate a random number
print('Program to generate a random number')
import random
print('Generate random number between 1-10:')
print(random.randint(1,10)) 

# 6. Program to convert kilometers to miles (1 km= 0.621371 miles)
print('Program to convert kilometers into miles')
in_kilo_meters = float(input('Enter in kilometers to convert into miles:'))
in_miles = round((in_kilo_meters * 0.621371) , 3)
print(f"{in_kilo_meters} Kms is {in_miles} Miles")

# 7. Program to convert Celsius into Fahrenheit
print('Program to convert Celsius into  Fahrenheit')
in_celsius = int(input('Enter the value in celsius:'))
in_fahrenheit = round((float(in_celsius * 1.8) + 32) , 1)
print(f"{in_celsius} celsius is {in_fahrenheit} Fahrenheit")

# 8. Program to check a number is +ve,-ve or 0
print('Program to find a number is positive, negative or zero')
num = int(input('Enter the number:'))
if num < 0:
    print(f'{num} is negative')
elif num > 0:
    print(f'{num} is positive')
else:
    print(f'{num} is zero')

# 9 . Program to check a number is even or odd
print('Program to check a number is even or odd')
num = int(input('Enter the number:'))
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

# 10 . Program to check leap year -leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.
print('Program to check leap year')
years = [2017,1900,2000,2012]
for year in years:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is leap year')
            else:
                print(f'{year} is not a leap year')
        else:
            print(f'{year} is leap year')
    else:
        print(f'{year} is not a leap year')

# 11 . Program to find the largest among the three numbers
print('Program to find the largest among the 3 numbers')
a, b, c = tuple(map(lambda x: int(x),(input('Enter comma separated 3 numbers:').split(','))))
print(f'Maximum of {a} ,{b} and {c} is: {max(a,b,c)}')

# 12 . Program to check prime number
print('Program to check prime number')
num = int(input('Enter the number:'))
for i in range(2,num-1):
    if num % i == 0:
        print(f'{num} is not a prime number')
        break
else:
    print(f'{num} is a prime number')

# 13 . Print all the prime numbers in the interval
print('Program to find the prime numbers in a given interval:')
lower_range, upper_range = tuple(map(lambda x: int(x),input('Enter the range,comma separated').split(',')))
for num in range(lower_range,upper_range+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,end=' ')

# 14. Find the factorial of a number
print('Program to find the factorial of a number')
a = int(input('Enter the number:'))
result = 1
if a < 1:
    print('Enter a +ve value')
elif a == 0:
    result = 1
else:
    for x in range(1, a+1):
        result *= x
print(f"Factorial of {a} is {result}")

# 15. Program to display the multiplication table
print('Program to display the multiplication table')
num = int(input('Enter the number:'))
for i in range (1,11):
    mul = num * i
    print(f'{num} * {i} = {mul}')

# 16. Program to print the Fibonacci series
print('Program to print the Fibonacci series')
count = int(input('Enter the count of numbers:'))
num1 = 0
num2 = 1
if count < 0:
    print('Enter +ve number')
elif count == 0:
    print(num1)
elif count == 1:
    print(num1)
else:
    print(num1, end=' ')
    print(num2,end=' ')
    for i in range(1, count-1):
        sum = num1 + num2
        print(sum,end=' ')
        num1, num2 = num2, sum

# 17. Program for Armstrong number xyz = x^3+ y^3 + z^3
print('Program for identify the Armstrong number')
data = input('Enter the number:')
num = int(data)
digits = []

for i in range(0,len(data)):
    digits.append(num % 10)
    num = num // 10
result = sum(list(map(lambda x : pow(x,len(digits)),digits)))
if result == int(data):
    print(f"{int(data)} is an Armstrong number")
else:
    print(f"{int(data)} is not an Armstrong number")


# 18. Program to find the Armstrong number in an interval
print('Program to find the Armstrong number in an interval')
lower_range, higher_range = tuple(map(lambda x: int(x), input('Enter the interval,comma separated:').split(',')))
armstrong_num = []
for num in range(lower_range, higher_range+ 1):
    length = len(str(num))
    digits = []
    temp = num
    for i in range(length):
        digits.append(temp % 10)
        temp = temp // 10
    if num == sum(list(map(lambda x: pow(x, length), digits))) :
        armstrong_num.append(num)
print("The Armstrong number's are:", armstrong_num)

# 19. Program to find the sum of natural numbers
print('Program to find the sum of natural numbers')
length = int(input('Enter the number of natural numbers to find the sum:'))
result = length * (length + 1) // 2
print(f"Sum of {length} Natural numbers is:{result}")
