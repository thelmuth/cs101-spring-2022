
### num1 and num2 are the function's parameters
def average(num1, num2):
    """Averages 2 numbers (this is a docstring)"""
    result = (num1 + num2) / 2
    
    ## This tells what the function should return
    return result

time1 = 8
time2 = 13
avg_time = average(time1, time2)
print("Average of", time1, "and", time2, "is", avg_time)

apples = 52
oranges = 98
bananas = 102
avg_fruit = average(apples, oranges)
print("Average fruit is", avg_fruit)


def longer(string1, string2):
    """Returns the longer of 2 strings."""
    length1 = len(string1)
    length2 = len(string2)
    if length1 > length2:
        result = string1
    else:
        result = string2
        
    return result

def longer_shorter(string1, string2):
    """Same function, except less code."""
    if len(string1) > len(string2):
        return string1 ## Immediately returned if we get here
    else:
        return string2
    print("This will never print, because return immediately exits the function")
    
def starts_with_vowel(word):
    """Returns True if word starts with a vowel, and False otherwise."""
    if word[0] in "aeiou":
        return True
    else:
        return False
        
    

### Run longer funtion
big_animal = longer("lion", "elephant")
print(big_animal)
print(longer("giraffe", "dog"))

big_animal = longer_shorter("lion", "elephant")
print(big_animal)
print(longer_shorter("giraffe", "dog"))


### Test it out
print(starts_with_vowel("cat"))
print(starts_with_vowel("apple"))

