from PIL import Image

def main():
    
    image = Image.open("eliza.jpg")
    image.show()
    
    ### Should detect grayscale pixels in the image
    detect_grayscale(image)
    
    image.show()


    ### my_pixel is an object
    ### Pixel is a class that creates pixel objects
    my_pixel = Pixel((40, 100, 254))
    
    tup = my_pixel.get_tuple()
    
    print(tup)
    print(my_pixel.r)
    print("Should be not gray:", my_pixel.is_grayscale())
    
    my_pixel.set_rgb(23, 93, 70)
    print(my_pixel.get_tuple())
    
    print("Luminance:", my_pixel.luminance())
    
    my_pixel.make_grayscale()
    print(my_pixel.get_tuple())
    print("Is it now grayscale?", my_pixel.is_grayscale())
    
    print(my_pixel)
    
    
    gray_pixel = Pixel((92, 92, 92))
    print("Should be gray:", gray_pixel.is_grayscale())
    
    
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
        
    ### Almost all methods are of 1 of 2 types:
    ###  1. Accessor - access information about an object and return it
    ###      - Ex: get_pixel - returns the RGB of a pixel
    ###      - Ex: Turtle.get_heading(), BS.find, Audio.get_samples(), str.strip()
    ###  2. Mutator - changes something about the object, typically doesn't return anything
    ###      - Ex: put_pixel - changing the value of a pixel in the image
    ###      - Ex: Audio.apply_gain(), turtle.forward()
    
    def is_grayscale(self):
        """Return True if this pixel is grayscale, and False otherwise."""
        return self.r == self.g == self.b
        
    def set_rgb(self, red, green, blue):
        """Sets the r, g, and b values of this pixel."""
        
        self.r = red
        self.g = green
        self.b = blue
        
    def make_grayscale(self):
        """Changes a pixel's components to be grayscale based on its luminance."""
        
        # Use self. to use another method within the same class
        lum = self.luminance()
        self.set_rgb(lum, lum, lum)
        
        
    def luminance(self):
        """Calculate and return the luminance of this pixel."""
        
        return (self.r + self.g + self.b) // 3
    

    ### A special method to return a string representation of the object:
    def __str__(self):
        """Must return a string representation of the object."""
        
        return "(R: " + str(self.r) + ", G: " + str(self.g) + ", B: " + str(self.b) + ")"


        
def detect_grayscale(image):
    """Detects grayscale pixels in an image, making them bright red.
    All other pixels are turned into grayscale, to make it easier to see
    the red pixels."""
    
    for x in range(image.width):
        for y in range(image.height):
            
            pixel = Pixel(image.getpixel((x, y)))
        
            if pixel.is_grayscale():
                ### Make this pixel bright red
                pixel.set_rgb(255, 0, 0)
                
            else:
                pixel.make_grayscale()
                
            image.putpixel((x, y), pixel.get_tuple())
        
    
    
    
    
if __name__ == "__main__":
    main()
    