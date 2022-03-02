import nltk
import random


def main():
    
    text = "I took my dog for a walk. It was very cold! But, he had a good time."
    nouns = []
    # replace_nouns(text, nouns)


    # sents = naive_sentence_tokenizer(text)

    # sents = nltk.sent_tokenize(text)
    # print(sents)

    movie = "I like the movie Mr. & Mrs. Smith! Brad Pitt, Angelina Jolie, etc. are in it."
    # movie_sents = naive_sentence_tokenizer(movie)

    # movie_sents = nltk.sent_tokenize(movie)
    # print(movie_sents)


    ### This creates a list of words/punctuation from text
    words = nltk.word_tokenize(movie)
    # print(words)


    ### NLTK can take a list of words, and find the parts of speech of those words
    ### This takes a tokenized list of words.
    ### Why not a single word?
    ### The surrounding words can help identify how the word is used in context

    pos = nltk.pos_tag(words)

    # print(pos)
    # for tup in pos:
    #     print(tup)
        
    ### We can print all of the part of speech tags:
    # nltk.help.upenn_tagset()


    buses = "I will book the bus ticket while I bus the table and read a book."

    # buses_words = nltk.word_tokenize(buses)
    # buses_pos = nltk.pos_tag(buses_words)
    # 
    # for tup in buses_pos:
    #     print(tup)


    breakfast = "I ate a bowl of cereal for breakfast."

    nouns = ["dog", "chair", "water", "car", "potato", "cheese", "soup", "nail",
             "tofu", "book", "mouse", "bread", "cloud", "computer", "snow"]


    new_sentence = replace_nouns(text, nouns)

    print(new_sentence)



def naive_sentence_tokenizer(text):
    """This tried to find all sentences in text."""
    
    sentences = []
    
    curr_sentence = ""
    for char in text:
        curr_sentence += char
        
        if char in ".!?":
            sentences.append(curr_sentence)
            curr_sentence = ""
            
    return sentences

def replace_nouns(text, nouns):
    """This will replace all nouns in the sentence with random nouns."""
    
    words = nltk.word_tokenize(text)
    words_pos = nltk.pos_tag(words)
    
#     print(words)
    
    ### This list will hold the words for the new sentence
    new_sentence_list = []
    
    ### This is a tuple assignment of the loop variable
    ### Will assign word to each first element of the tuple, and pos
    ### to the second element of each tuple
    for word, pos in words_pos:
        
#         print(pos, word)

        if pos == "NN":
            new_word = random.choice(nouns)
        else:
            new_word = word
            
        new_sentence_list.append(new_word)
        
#     print(new_sentence_list)

    #### This glues the words back together using correct spaces, etc.
    twd = nltk.tokenize.treebank.TreebankWordDetokenizer()
    new_sentence = twd.detokenize(new_sentence_list)
    
    return new_sentence
     
        


if __name__ == '__main__':
    main()

