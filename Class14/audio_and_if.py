from cs101audio import *
import sys

song = Audio()

# print("Press 1 for All To Well")
# print("Press 2 for Flashing Lights")
# choice = input("Please select a song: ")
choice = "1"

if choice == "1":
    song.open_audio_file("All To Well (2 minute version).wav")
elif choice == "2":
    song.open_audio_file("Flashing Lights.wav")
else:
    print("You didn't choose 1 or 2.")
    ### This exits the program immediately:
    sys.exit()
    
# song.play()

#### Let's experiment with some drum samples:

bass = Audio()
bass.open_audio_file("Bass-Drum.wav")

snare = Audio()
snare.open_audio_file("Snare.wav")

# bass.play()
# snare.play()

### Let's make a beat by looping the bass drum
# num_beats = 8
# drums = Audio()
# for _ in range(num_beats):
#     drums += bass
    
# drums = bass * 8
    
# drums.play()

#### Let's make this last for a specific beats-per-minute
beats_per_minute = 94
ms_per_beat = 60 * 1000 / beats_per_minute

print("ms per beat:", ms_per_beat)
print("ms in the bass sample:", len(bass))
print("ms in the snare sample:", len(snare))

### Trim the bass sample to be the right length:
bass = bass[:ms_per_beat]

# x = len(bass) / ms_per_beat
# bass.change_speed(x)


# num_beats = 8
# drums = Audio()
# for _ in range(num_beats):
#     drums += bass
# 
# drums.play()


### Now, let's add the snare drum every 4th beat

# num_beats = 16
# drums = Audio()
# for index in range(num_beats):
#     if index % 4 == 3:
#         drums += snare
#     else:
#         drums += bass
# 
# drums.play()


### Let's change the snare length to make it the right lenth

### This creates a silent audio object that's ms_per_beat long
snare_full = Audio(ms_per_beat)
snare_full.overlay(snare)

num_beats = 16
drums = Audio()
for index in range(num_beats):
    if index % 4 == 3:
        drums += snare_full
    else:
        drums += bass

# drums.play()

### We want to overlay these drums on All To Well
### We want to start 23.61 seconds into the song
padded_drums = Audio(23610)
padded_drums += drums


### Note: if overlay makes the audio sound bad, first lower it's gain
song.apply_gain(-15)

song.overlay(padded_drums)
song.play()






