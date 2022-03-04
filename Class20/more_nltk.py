import nltk

def main():
    
    ### Open and read a file to a string
    filename = "PrideAndPrejudice.txt"
    file = open(filename, 'r')
    pap = file.read()
    
#     print(pap[:200])
#     
#     words = nltk.word_tokenize(pap)
#     pos_tags = nltk.pos_tag(words)
#     
#     for index in range(40):
#         print(pos_tags[index])
    
    sentence = "I went to to the school for a lunch lunch meeting."
    
#     print_repeated_words(sentence)
#     print_repeated_words(pap)
    
    
    ### Find sentences with 2 characters in them
#     elizabeth_and_darcy = sentences_containing_both_characters(pap, "Elizabeth", "Darcy")
#     
#     print(len(elizabeth_and_darcy))
#     
#     for sent in elizabeth_and_darcy:
#         print(sent)

    bingley_and_jane = sentences_containing_both_characters(pap, "Bingley", "Jane")
    
    for sent in bingley_and_jane:
        print(sent)
    
    
    
    
def sentences_containing_both_characters(text, character1, character2):
    """Returns a list of sentences that contain both character1 and character2."""
    
    sentences = nltk.sent_tokenize(text)
    found_sentences = []
    
    for sentence in sentences:
        if character1 in sentence and character2 in sentence:
            found_sentences.append(sentence)
            
    return found_sentences
    
    
    
def print_repeated_words(text):
    """Prints any words in text that are repeated."""
    
    words = nltk.word_tokenize(text)
    
    for index in range(len(words) - 1):
        if words[index] == words[index + 1]:
            print(words[index])
     
#     string = ""
#     for word in words:
#         if word == string:
#             print(word)
#             
#         string = word
    
    
    



if __name__ == "__main__":
    main()
