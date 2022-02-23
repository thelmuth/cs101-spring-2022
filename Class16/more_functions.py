### TODO
### - Quiz 4 today on Gradescope
### - Project 1 due Feb. 28

from cs101audio import *

### Write a function that is given a list of words and returns the
### longest word in that list.

def longest_word(word_list):
    """Given a list of words, returns the longest word in the list."""
    
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    
    return longest

names = ["Charlie", "Caroline", "Cat", "Charlotte", "Cathy", "Carol", "Chad"]
longest_name = longest_word(names)
print("The longest name was:", longest_name)


### Test out functions with audio

def roll_audio(audio, times, length):
    """Rolls the given audio object the given number of times."""
    
#     new_audio = Audio()
#     for _ in range(times):
#         chunk = audio[:40]
#         new_audio += chunk
        
    new_audio = audio[:length] * times
    
    return new_audio


def bounce_audio(audio, times, length):
    """Makes sound of a bouncing ball that gets closer together the longer
    it plays."""
    
    new_audio = Audio()
    for rep in range(times + 1, 0, -1):
        chunk = audio[:rep * length + 20]
        chunk.change_speed((times - rep) * 0.1 + 1)
        new_audio += chunk

    return new_audio




snare = Audio()
snare.open_audio_file("Snare.wav")
snare_roll = roll_audio(snare, 10, 50)
# snare_roll.play()

bass = Audio()
bass.open_audio_file("Bass-Drum.wav")
bass_roll = roll_audio(bass, 20, 100)
# bass_roll.play()

bounce_bass = bounce_audio(bass, 10, 40)
# bounce_bass.play()



def doubled_letters(text):
    """Finds any letters in string that are doubled -- in other words, the
    same letter twice in a row. So, doubled_letters('bookkeeper Molly')
    should return 'okel'. """

    doubled = ""
    for letter_index in range(len(text) - 1):
        if text[letter_index] == text[letter_index + 1]:
            doubled += text[letter_index]
            
    return doubled

print(doubled_letters('bookkeeper Molly'))

            










