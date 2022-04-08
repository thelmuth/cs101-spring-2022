from PIL import Image

def main():
    
    ### Open an image
    kids = Image.open("box.jpg")
    
#     kids_rotated = rotate(kids)
    
#     kids_rotated.show()

#     gradient = make_gradient()
    
#     gradient.show()

#     print(kids.width, kids.height)

    kids_shrunk = resize(kids, 2000, 2667)
    
    kids_test = resize(kids_shrunk, 500, 667)
    
    kids.show()
    kids_shrunk.show()
    kids_test.show()



def resize(image, new_width, new_height):
    """Resizes the image to have the new_width and new_height"""
    
    new_image = Image.new("RGB", (new_width, new_height))
    
    old_width = image.width
    old_height = image.height
    
    for new_x in range(new_image.width):
        for new_y in range(new_image.height):
            
            old_x = new_x * old_width // new_width
            old_y = new_y * old_height // new_height
            
            pixel = image.getpixel((old_x, old_y))
            new_image.putpixel((new_x, new_y), pixel)
            
    return new_image
    


def rotate(image):
    """Creates and returns a new image rotated 90 degrees clockwise"""
    
    old_width = image.width
    old_height = image.height
    
    ### Create a new image, with swapped width and height:
    new_image = Image.new("RGB", (old_height, old_width))
    
    for x in range(old_width):
        for y in range(old_height):
            
            pixel = image.getpixel((x, y))
            
            new_x = old_height - y - 1
            new_y = x
            
            new_image.putpixel((new_x, new_y), pixel)
            
    return new_image
    
    
def make_gradient():
    """Makes a new image with a gradient. We'll test this out with different gradients."""
    
    image = Image.new("RGB", (256, 256))
    
    for x in range(image.width):
        for y in range(image.height):
            
#             image.putpixel((x, y), (20, 200, 170))

            ## Makes a black to white gradient going to the right
#             image.putpixel((x, y), (x, x, x))
            
            ## Green to purple, top to bottom
#             image.putpixel((x, y), (y, 128, y))
            
            ## Diagonal gradient
#             image.putpixel((x, y), (y, x, x))
            
            
            image.putpixel((x, y), (y, 128, x))
            
    return image
    


if __name__ == "__main__":
    main()
    