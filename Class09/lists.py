
fruit = ["apples", "bananas", "cherries"]
numbers = [16, 2999, -97]

# Indexing is the same syntax as we would for a string:
print(fruit[1])
print(fruit[:2])

# We can change the element at an index:
fruit[2] = "cantaloupe"
print(fruit)

### This throws an error because we cannot change the characters in a string.
# name = "Tom Helmuth"
# name[2] = "d"
# print(name)

## Don't use the variable name list -- there's a function called list

## We can add elements to the end of a list:
fruit.append("kiwi")
print(fruit)

## We can remove an element at a specific location using the pop method:
fruit.pop(1)
print(fruit)

## We can concatenate two lists using +
new_list = [1, 2, 3] + fruit
print(new_list)

## We can find the length of a list using the len function
print(len(new_list))


### New example of list aliasing
x = [1, 2, 3]
y = x
y[0] = 500
print("y = ", y) #expect [500, 2, 3]
print("x = ", x) #expect [1, 2, 3]

## When we assign a variable equal to another variable, those objects end up
## referencing the same object.
## y = x  => y and x refer to the same list.

## How can you make an actual copy?
x = [1, 2, 3]
y = x[:]
y[0] = 500
print("NEW y = ", y) #expect [500, 2, 3]
print("NEW x = ", x) #expect [1, 2, 3]


