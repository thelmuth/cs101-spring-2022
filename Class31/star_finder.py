
from PIL import Image

def main():
    
    stars = Image.open("stars.jpg")
    
    # Create a black and white version with a threshold
    stars_bw = threshold_stars_image(stars, 30)
    
    stars_bw.show()
    
    
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
    