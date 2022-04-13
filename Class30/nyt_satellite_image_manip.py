"""
Replicates some of the work of this NYT article.
https://www.nytimes.com/interactive/2020/09/02/upshot/america-political-spectrum.html

In particular, we can take an image, sort its pixels by luminance, and make the
new image.
"""

from PIL import Image

def main():
    
    ### This is a satellite image of Blue Ridge, VA
    va = Image.open("Hamilton_College.jpg")
    va.show()
    
#     print(va.width)
#     print(va.height)

    sorted_image = nyt(va)
    sorted_image.show()
    


def nyt(image):
    """Sketch of our algorithm:
    1. Go through all pixels and get the color of each. Put these in a list.
    2. Sort the list by luminance of each pixel.
    3. Make a new square image. Stick all the pixels in it, row by row.
    """
    
    ### Make a list to hold all the pixels:
    pixels = []
    
    for x in range(image.width):
        print("x =", x)
        
        for y in range(image.height):
            
            rgb = image.getpixel((x, y))
            pixels.append(rgb)
            
    ## Check what the first few elements of the list are:
#     print(pixels[:10])

    ## Now, we need to sort these pixels by luminance

#     pixels.sort() ### Sorts by red first, not what we want

    ### Make a new list where each element is a tuple containing the luminance value
    ### and the RGB tuple: Ex: (100, (80, 90, 130))
    
    pixels_with_luminance = []
    for pixel in pixels:
        lum = luminance(pixel)
        pwl = (lum, pixel)
        pixels_with_luminance.append(pwl)
        
    pixels_with_luminance.sort()
    
#     print(pixels_with_luminance[:1000])

    sorted_image = Image.new("RGB", (image.width, image.height))
    
    index = 0
    
    for y in range(sorted_image.height):
        print("putting new pixel at y =", y)
        
        for x in range(sorted_image.width):
            
            pixel = pixels_with_luminance[index][1]
            
            sorted_image.putpixel((x, y), pixel)
            
            index += 1
            
    return sorted_image
            
    
    
    
def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3



if __name__ == "__main__":
    main()
    