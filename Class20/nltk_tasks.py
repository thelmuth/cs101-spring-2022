import nltk
import matplotlib.pyplot as plt

def main():
    
    filename = "PrideAndPrejudice.txt"
    file = open(filename, "r")
    pap = file.read()

    ### Find all proper nouns:
    proper_nouns = find_proper_nouns_in_text(pap)
    
    ### How often does Elizabeth appear?
    elizabeth = count_occurences(proper_nouns, "Elizabeth")
#     print("Elizabeth appears", elizabeth, "times.")
# 
#     darcy = count_occurences(proper_nouns, "Darcy")
#     print("Darcy appears", darcy, "times")

    unique_proper_nouns = remove_duplicates(proper_nouns)
    
    print("number of all proper nouns", len(proper_nouns))
    print("number of unique proper nouns", len(unique_proper_nouns))
    print(unique_proper_nouns[:10])
    
    proper_noun_counts = get_counts(proper_nouns)
    
    plt.bar(proper_noun_counts)
    plt.show()



######################################
## Functions below here written in lab

def find_proper_nouns_in_text(text):
    """Finds and returns a list of all proper nouns in text."""
    
    words = nltk.word_tokenize(text)
    words_with_pos = nltk.pos_tag(words)
    
    all_proper_nouns = []
    for word, pos in words_with_pos:
        if pos == "NNP":
            all_proper_nouns.append(word)
            
    return all_proper_nouns

def remove_duplicates(list_with_dupes):
    """ Returns the given list with all duplicates removed. """
    
    clean_list = []
    
    for entry in list_with_dupes:
        if entry not in clean_list:
            clean_list.append(entry)
            
    return clean_list

def count_occurences(list_to_count, target):
    """Returns the number of times that target appears in list_to_count."""
    count = 0
    for thing in list_to_count:
        if target == thing:
            count += 1
    return count

def get_counts(list_to_count):
    """ Returns a frequency list corresponding to the given list. """
    
    freq_list = []
    clean_list = remove_duplicates(list_to_count)
    
    for word in clean_list:
        count = count_occurences(list_to_count, word)
        freq_list.append(count)
    
    return freq_list


if __name__ == "__main__":
    main()