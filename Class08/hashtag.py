
tweet = input("Enter a tweet: ")

first_hashtag_index = tweet.find("#")
rest_of_tweet = tweet[first_hashtag_index : ]

first_space = rest_of_tweet.find(" ")
hashtag = rest_of_tweet[ : first_space]

print()
print(hashtag)


### List of test cases
### input | expected output
# "Computer science #rules #python #cs101" | "#rules"
# "this#has#no#spaces" | "#has#no#spaces"
# "this has no hashtags" | ""   <-- empty string with no characters
# "#first thing is a hashtag" | "#first"
# "the last thing in this string is a #hashtag" | "#hashtag"
# "this has # a space after the hashtag" | "#"
# "" | ""