from cs101audio import *

# Creates a new empty audio object
song = Audio()
song.open_audio_file("Flashing Lights.wav")

# song.play()
print("The length of this song in milliseconds is", len(song))

### Audio objects can be used like lists, storing information in
### 1 millisecond increments. We can use things like indexing, slicing, and concatenation
### to work with aaudio objects.

### Ex: break song into 3 parts:
intro = song[:20500] # start up to 20.5 seconds
flashing_lights = song[20500 : 42500]
kanye = song[42500:]

### Speed up the intro and flashing_lights because they're slow
intro.change_speed(2)
flashing_lights.change_speed(1.5)

### Can use + to concatenate audio objects back together
new_song = intro + flashing_lights + kanye
# new_song.play()
# new_song.save_to_file("fast_lights.wav")


### Use a for loop to break the song into second-long chunks:
# for index in range(0, len(song), 1000):
#     print(index)
#     chunk = song[index : index + 1000]
#     chunk.play()
    
## Speed up the song 1% each time through the loop
## Want: 1.0 first time through, 1.01 second time through, etc.
# for index in range(0, len(song), 1000):
#     speed = 1 + index / 100000
#     print(index, "speed =", speed)
#     chunk = song[index : index + 1000]
#     chunk.change_speed(speed)
#     chunk.play()


## Same thing, except we'll create a new audio object that contains the whole song
new_song = Audio()
for index in range(0, len(song), 1000):
    speed = 1 + index / 100000
    print(index, "speed =", speed)
    chunk = song[index : index + 1000]
    chunk.change_speed(speed)
    new_song = new_song + chunk
    
new_song.play()






