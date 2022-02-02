
tweet = input("Enter a tweet: ")

first_hashtag_index = tweet.find("#")
rest_of_tweet = tweet[first_hashtag_index : ]

first_space = rest_of_tweet.find(" ")
hashtag = rest_of_tweet[ : first_space]

print()
print(hashtag)
