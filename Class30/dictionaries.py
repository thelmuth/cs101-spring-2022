
from PIL import Image

def main():
    
    text = input("Enter some text: ")
    
    ## Create a dictionary of frequencies of how often each character appears
    ## Letters will be the keys, and the values will be how often each letter appears
    
    frequencies = {}
    
    for char in text:
        
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
            
        print(frequencies)
            
#     print(frequencies)
#     
#     for char in frequencies:
#         print(char, "=>", frequencies[char])
    




if __name__ == "__main__":
    main()
    