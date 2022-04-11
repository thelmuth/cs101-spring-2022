from PIL import Image

def main():
    
#     greet("Hi", "Aaron", "How are you doing today?")
#     
#     greet("Hello")
#     
#     greet("Howdy", question="What is the weather?")
#     
#     greet("Howdy", question="What?", name="Elizabeth")
    
    ### Open an image
    kids = Image.open("box.jpg")
    
#     kids_shrunk = resize(kids, 200, 400)
    kids_shrunk = resize(kids, 200)
    
    kids.show()
    kids_shrunk.show()


def greet(greeting, name="person", question="How are you?"):
    """ greeting is required. name and question are optional parameters and have default values."""

    print(greeting, name, ".", question)



def resize(image, new_width, new_height=None):
    """Resizes the image to have the new_width and new_height"""
    
    ## Goal: new_height be optional: if you provide it, it is used. If not, function figures
    ## out the correct new_height to maintain the correct proportions
    
    old_width = image.width
    old_height = image.height

    if new_height == None:
        new_height = new_width * old_height // old_width
        print("new_height = ", new_height)
        

    new_image = Image.new("RGB", (new_width, new_height))

    
    for new_x in range(new_image.width):
        for new_y in range(new_image.height):
            
            old_x = new_x * old_width // new_width
            old_y = new_y * old_height // new_height
            
            pixel = image.getpixel((old_x, old_y))
            new_image.putpixel((new_x, new_y), pixel)
            
    return new_image
    
    

if __name__ == "__main__":
    main()
    