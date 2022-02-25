from cs101audio import *
import math
import matplotlib.pyplot as plt


# def this_function_returns_nothing(x, y):
#     z = x + y
#     print(z)
#     
# 
# answer = this_function_returns_nothing(5, 10)
# print(answer)
# cat = answer + 20


### Let's say we want to plot the predicted high temperatures for the week
days = ["Wed", "Thurs", "Fri", "Sat", "Sun", "Mon", "Tues"]
highs = [47,     30,     29,   28,     32,    22,    31]

### Make a bar chart:
# plt.bar(days, highs)
# plt.show()


### Make a line chart that also includes the low temperatures as well
lows = [13,     21,      8,     19,    5,     11,     14]

# plt.plot(days, highs)
# plt.plot(days, lows)
# 
# ### This adds a legend
# plt.legend(("High Temp", "Low Temp"))
# plt.show()



### Plot x-y pairs of the funtion y = 2^x
### Maybe we're modeling a disease where every person who gets
### sick infects 2 new people
x_values = []
y_values = []
for x in range(15):
    x_values.append(x)
    y = 2 ** x
    y_values.append(y)

# print(x_values)
# print(y_values)

### Make the line green and put circles at the data points
# plt.plot(x_values, y_values, color="green")
# 
# plt.plot(x_values, y_values, color="orange", marker="o", linestyle="none")
# plt.show()





#### Plot audio
### Start with a song from NES -- uses square waves to generate music
# zelda = Audio()
# zelda.open_audio_file("zelda.wav")
# # zelda.play()
# 
# five_ms = zelda[100:105]
# # five_ms.play()
# 
# sample_list = five_ms.get_sample_list()
# print(len(sample_list))
# 
# plt.plot(sample_list)
# plt.show()


### Same thing using generated audio
# noise = generate_music_note("c4", 500, "sawtooth")
# noise.play()
# 
# noise_samples = noise.get_sample_list()
# plt.plot(noise_samples)
# plt.show()
# 
# noise_short = noise_samples[5000:5500]
# plt.plot(noise_short)
# plt.show()

#### Visualize the snare sample
# snare = Audio()
# snare.open_audio_file("Snare.wav")
# snare.play()
# 
# sample_snare = snare.get_sample_list()
# print(len(sample_snare))
# 
# plt.plot(sample_snare[2000:3000])
# plt.show()


x = 0
### Loop until x cubed > 1000
while x ** 3 > -10000:
    print(x, x ** 3)
    x += 1







