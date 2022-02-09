import time

### What if we want to print the numbers 0, 1, 2, ..., 5

# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

### Same thing, with a loop:
# for number in range(1000):
#     # number is the loop variable of this loop
#     print(number)
# print("The loop ended!")

### If 2 arguments, tells the start and end
# for x in range(5, 10):
#     print(x)
#     print("squaring", x, "gives", x * x)
#     print()

### If 3 arguments, tells the start, end, and step size:
# for x in range(5, 20, 4):
#     print(x)
# print("At end:", x)

# for x in range(100000000000000000):
#     print(x)

### You can work backward in loops:
# for countdown in range(10, -1, -1):
#     print("T-minus", countdown, "seconds")
#     time.sleep(1)
    

### We have a string, and we want to go through each character individually
# animal = "panda"
# for index in range(len(animal)):
#     char = animal[index]
#     print("The character at index", index, "is", char)

### We can instead loop over the string itself:
# animal = "panda"
# for char in animal:
#     print("The character is", char)
# print("We don't have access to the indices if we do it this way.")


### We can also iterate over the elements of a list
# numbers = [16, 2999, 308, 0, 10000]
# for num in numbers:
#     print("num is", num)
# 
# for index in range(0, len(numbers), 2):
#     print("every other", numbers[index])


### Want to sum all of the numbers in our list:
# numbers = [16, 2999, 308, 0, 10000]
# the_sum = 0
# for num in numbers:
#     the_sum = the_sum + num
# print(the_sum)


### Want: "Elsa, Anna, Olaf, Kristoff, Sven"
names = ["Elsa", "Anna", "Olaf", "Kristoff", "Sven"]
frozen = ""
for name in names:
    frozen = frozen + name + ", "
print(frozen)







