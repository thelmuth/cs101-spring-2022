
### Turn a whole sentence into Pig Latin
### I took my dog on a walk.
sentence = input("Enter a sentence: ")

### This code splits a sentence into the words in a list:
# words = []
# while " " in sentence:
#     space_index = sentence.find(" ")
#     words.append(sentence[:space_index])
#     sentence = sentence[space_index + 1:]
# 
# words.append(sentence)

words = sentence.split() ## This takes a string and splits it into a list of words on spaces.



new_sentence = ""

for word in words:    
    if word[0] in "aeiouAEIOU":
        pig_latin = word + "ay"
    else:
        pig_latin = word[1:] + word[0] + "ay"
    
    new_sentence += pig_latin + " "

print(new_sentence)
    


