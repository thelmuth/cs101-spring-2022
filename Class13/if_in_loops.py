
### Have the user enter a word, and then turn it into Pig Latin
### If the word starts with a consonant, move that consonant to the
###   end and add "ay".   Ex: Tom => omTay
### If it starts with a vowel, just add "ay" to the end". Ex: apple => appleay

# word = input("Enter a word: ")
# if word[0] in "aeiouAEIOU":
#     pig_latin = word + "ay"
# else:
#     pig_latin = word[1:] + word[0] + "ay"
# 
# print(word, "in Pig Latin is", pig_latin)


### Turn a whole sentence into Pig Latin
### I took my dog on a walk.
sentence = input("Enter a sentence: ")
# sentence = sentence + " "

words = []
while " " in sentence:
    space_index = sentence.find(" ")
    words.append(sentence[:space_index])
    sentence = sentence[space_index + 1:]

words.append(sentence)

# print(words)
new_sentence = ""

for word in words:    
    if word[0] in "aeiouAEIOU":
        pig_latin = word + "ay"
    else:
        pig_latin = word[1:] + word[0] + "ay"
    
    new_sentence += pig_latin + " "

print(new_sentence)
    


