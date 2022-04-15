
from PIL import Image

def main():
    
    kids = Image.open("box.jpg")
#     kids.show()
    
    ## How many possible colors are there in RGB?
    print("There are 256^3 possible colors =", 256 ** 3)

    ## How many pixels are in this image?
    print("There are", kids.width * kids.height, "pixels in this image.")
    
    ## How many unique colors are in this image?
    
#     colors = []

    colors = {}
    
    for y in range(kids.height):
        print("y = ", y, "and number of colors so far is", len(colors))
        for x in range(kids.width):
            pixel = kids.getpixel((x, y))
            
            if pixel not in colors:
                #colors.append(pixel)
                
                colors[pixel] = 1

    print("There are", len(colors), "unique colors in this image.")

if __name__ == "__main__":
    main()
    