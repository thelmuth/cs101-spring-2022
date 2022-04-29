from PIL import Image

def main():
    
#     image = Image.open("eliza.jpg")
#     image.show()


    ### my_pixel is an object
    ### Pixel is a class that creates pixel objects
    my_pixel = Pixel((40, 100, 254))
    
    tup = my_pixel.get_tuple()
    
    print(tup)
    print(my_pixel.r)
    
    
class Pixel:
    """Represents a pixel in an image."""
    
    ### Using def indented within a class creates a method for that class
    def __init__(self, rgb):
        """This is called the Constructor for the class.
        This is called when we create a new Pixel object."""
        
        ### Let's store the r, g, and b components as attributes:
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

        
    def get_tuple(self):
        """Returns a tuple representation of this pixel."""
        return (self.r, self.g, self.b)
        
        
        
        
        
    
    
    
    
if __name__ == "__main__":
    main()
    