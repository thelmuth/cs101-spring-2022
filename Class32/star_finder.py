
from PIL import Image

def main():
    
    stars = Image.open("stars.jpg")
#     stars.show()
    
    # Create a black and white version with a threshold
    stars_bw = threshold_stars_image(stars, 30)
    
    stars_bw.show()
    
    number_of_stars = count_the_stars(stars_bw)
    
    stars_bw.show()
    
    print("The number of stars is:", number_of_stars)
    
    
def turn_all_neighbors_black(image, x, y):
    """Turns all neighboring pixels black repeatedly for an entire star."""
    
    white_neighbors = []
    white_neighbors.append((x, y))
    image.putpixel((x, y), (0, 255, 0))
    
    while white_neighbors != []:
        
        (x, y) = white_neighbors.pop(0)
        
#         print("In the loop", x, y)
        
        # Right pixel:
        if x + 1 < image.width and image.getpixel((x + 1, y)) == (255, 255, 255):
            white_neighbors.append((x + 1, y))
            image.putpixel((x + 1, y), (0, 255, 0))
            
        # Left pixel:
        if x - 1 >= 0 and image.getpixel((x - 1, y)) == (255, 255, 255):
            white_neighbors.append((x - 1, y))
            image.putpixel((x - 1, y), (0, 255, 0))
                
        # Down pixel:
        if y + 1 < image.height and image.getpixel((x, y + 1)) == (255, 255, 255):
            white_neighbors.append((x, y + 1))
            image.putpixel((x, y + 1), (0, 255, 0))
            
        # Up pixel:
        if y - 1 >= 0 and image.getpixel((x, y - 1)) == (255, 255, 255):
            white_neighbors.append((x, y - 1))
            image.putpixel((x, y - 1), (0, 255, 0))
            
        
    
    
    
def count_the_stars(image):
    
    count = 0
    
    for x in range(image.width):
        print(x)
        for y in range(image.height):
            
            color = image.getpixel((x, y))
            
            ## If true, we've found a white pixel
            if color == (255, 255, 255):
                turn_all_neighbors_black(image, x, y)
                count += 1
                
    return count
    
    
def threshold_stars_image(image, threshold):
    
    bw = Image.new("RGB", (image.width, image.height))
    
    for x in range(image.width):
        for y in range(image.height):
            
            pixel = image.getpixel((x, y))
            lum = luminance(pixel)
            
            if lum > threshold:
                bw.putpixel((x, y), (255, 255, 255))
                
            else:
                bw.putpixel((x, y), (0, 0, 0))
                
    return bw
            
            
            

def luminance(rgb):
    """Finds the average of r, g, and b components to determine how
    bright a pixel is."""
    
    (r, g, b) = rgb
    return (r + g + b) // 3




if __name__ == "__main__":
    main()
    