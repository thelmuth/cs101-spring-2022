from PIL import Image

def main():
    
    ### Open an image
    kids = Image.open("box.jpg")
    
#     blue_filter(kids)

#     grayscale(kids)

    edge_detect(kids, 30)
    
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
    
    
def luminance(rgb):
    """Finds the average of the r, g, and b components to determine how bright
    a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3
    

def grayscale(image):
    """Makes the image grayscale"""
    
    for x in range(image.width):
        print(x)
        
        for y in range(image.height):
            rgb = image.getpixel((x, y))
            
            avg = luminance(rgb)
            
#             if avg < 128:
#                 image.putpixel((x,y), (0,0,0))
#             elif avg == 128:
#                 image.putpixel((x,y), (128, 128, 128))
#             else:
#                 image.putpixel((x,y), (255, 255, 255))
            
            image.putpixel((x,y), (avg, avg, avg))

def edge_detect(image, luminance_threshold):
    """Finds the edges of objects in an image, and returns a B&W version
    where the edge pixels are black and non-edges are white.
    luminance_threshold gives the threshold for determining if there is an edge."""
    
    for x in range(image.width - 1):
        print(x)
        
        for y in range(image.height - 1):
            
            pixel = image.getpixel((x,y))
            pixel_right = image.getpixel((x+1, y))
            pixel_down = image.getpixel((x, y+1))
            
            ### Get luminance of each
            lum_pixel = luminance(pixel)
            lum_right = luminance(pixel_right)
            lum_down = luminance(pixel_down)
            
            if abs(lum_pixel - lum_right) > luminance_threshold:
                image.putpixel((x,y), (0,0,0))
            
            elif abs(lum_pixel - lum_down) > luminance_threshold:
                image.putpixel((x,y), (0,0,0))
                
            else:
                image.putpixel((x,y), (255, 255, 255))
            
def rotate(image):
    """Creates and returns a new image rotated 90 degrees clockwise"""
    
    old_width = image.width
    old_height = image.height
    
    ### Create a new image, with swapped width and height:
    new_image = Image.new("RGB", (old_height, old_width))
    
    
    
    


if __name__ == "__main__":
    main()
    