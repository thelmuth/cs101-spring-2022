import math
# from math import *

### Want: "Elsa, Anna, Olaf, Kristoff, Sven"
# names = ["Elsa", "Anna", "Olaf", "Kristoff", "Sven"]
# frozen = ""
# for name in names:
#     frozen = frozen + name + ", "
# print(frozen)


### Want: sum of all integers between 0 and 1 million
# the_sum = 0
# for number in range(1000001):
#     the_sum = the_sum + number
#     
# print("The sum of numbers 0 to 1000000 is:", the_sum)
### Recall: this is the accumulator pattern

### Accumulating values in a new list:
### Want: a new list containing the square of each of these numbers
# numbers = [16, 2999, 308, 0, 10000]
# squares = [] # empty list, to put all the squares in
# for num in numbers:
#     square = num * num
#     squares.append(square)
# print("squares:", squares)


### Want the user to enter list items
# number_elements = int(input("How many numbers do you want to enter? "))
# user_list = []
# for _ in range(number_elements):
#     num = int(input("Enter a number: "))
#     user_list.append(num)
# 
# print("The new list:", user_list)


### Can we just change the values in the original list?
# numbers = [16, 2999, 308, 0, 10000]
# for index in range(len(numbers)):
#     num = numbers[index]
#     square = num * num
#     numbers[index] = square
# 
# print("squares:", numbers)


### Accumulating over a string:
### Want to put a period after every character in the string.
# city = "NYC"
# new_city = ""
# for index in city:
#     new_city = new_city + index + "."
#     
# print(new_city)


# the_sum = 0
# for number in range(1000001):
# #     the_sum = the_sum + number
#     the_sum += number ### equivalent to the above line
#     
# print("The sum of numbers 0 to 1000000 is:", the_sum)


### Simple if statement:
### User enter a number, and print 1 divided by that number.
### If the user enters 0, we want to catch that
# divisor = float(input("Enter a number to divide 1 by: "))
# if divisor == 0.0:
#     # = is used for variable assignment
#     # == is used to check whether two things are equal or not
#     print("You can't divide by zero!")
# 
# else:
#     print("1 divided by", divisor, "equals", 1 / divisor)

### What if we want to check multiple conditions?
grade = int(input("Enter a grade: "))
### Want to print the letter grade for this numeric grade
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")





