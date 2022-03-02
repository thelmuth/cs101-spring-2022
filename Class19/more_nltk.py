import nltk

def main():
    
    ### Open and read a file to a string
    filename = "PrideAndPrejudice.txt"
    file = open(filename, 'r')
    pap = file.read()
    
    print(pap[:200])
    
    words = nltk.word_tokenize(pap)
    pos_tags = nltk.pos_tag(words)
    
    for index in range(40):
        print(pos_tags[index])
    
    
    
    



if __name__ == "__main__":
    main()
