from PIL import Image

def main():
    
    ### Open an image
    kids = Image.open("box_big.jpg")
    
    print(kids.width)
    print(kids.height)
    
    ### What's the color at pixel (2000, 1600)?
    rgb = kids.getpixel((2000, 1600))
    print(rgb)
    
    ### This sets that pixel to black
    kids.putpixel((2000, 1600), (0, 0, 0))
    
    blue_filter(kids)
    kids.show()



def blue_filter(image):
    """Takes an image and makes it more blue.
    This is a good template for many image manipulating functions."""
    
    for x in range(image.width):
        print(x)
        
        for y in range(image.height):
            (r, g, b) = image.getpixel((x, y))
            
            image.putpixel((x, y), (r, g, b + 100))
            
    ### Note: don't have to return the image
    


if __name__ == "__main__":
    main()
    