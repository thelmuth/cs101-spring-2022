from PIL import Image, ImageDraw

def main():

    leo = MyTurtle()
    
    leo.forward(100)
    leo.right()
    leo.pen_color((250, 0, 220))
    leo.width(20)
    
    leo.forward(200)
    leo.left()
    leo.pen_color("orange")
    
    leo.forward(50)
    
    
    leo.show()
    
    
    
class MyTurtle:
    """ Implementing a class to replicate some of the Turtle class."""
    
    def __init__(self):
        
        ### Attributes:
        self.image = Image.new("RGB", (600, 600), (255, 255, 255))
        self.image_draw = ImageDraw.Draw(self.image)
        
        self.x = 300  ## Starting location
        self.y = 300
        
        self.dx = 1
        self.dy = 0
        
        self.color = (0, 0, 0)
        
        self.color_names = {"red": (255, 0, 0),
                            "green": (0, 255, 0),
                            "blue": (0, 0, 255),
                            "yellow": (255, 255, 0),
                            "orange": (255, 128, 0),
                            "purple": (200, 0, 200)}
        
        self.pen_size = 1
        
        
    def show(self):
        """ Displays current image."""
        self.image.show()
        
        
    def forward(self, distance):
        
        for _ in range(distance):
            
            if self.pen_size == 1:
                self.image.putpixel((self.x, self.y), self.color)
            else:
                radius = self.pen_size // 2
                self.image_draw.ellipse((self.x - radius, self.y - radius,
                                         self.x + radius, self.y + radius),
                                        fill = self.color)
            
            
            self.x += self.dx
            self.y += self.dy
        
    def right(self):
        """Turns the turtle 90 degrees to the right"""
        
        if self.dx == 1:
            self.dx = 0
            self.dy = 1
            
        elif self.dx == -1:
            self.dx = 0
            self.dy = -1
            
        elif self.dy == 1:
            self.dx = -1
            self.dy = 0
            
        else:
            self.dx = 1
            self.dy = 0
            
    def left(self):
        """Turns turtle 90 degrees left"""
        for _ in range(3):
            self.right()
            
    def pen_color(self, color):
        """ Sets the turtle's color. Can be a tuple or a string color name."""
        
        if type(color) == str:
            self.color = self.color_names[color]
        else:
            self.color = color
            
    def width(self, new_width):
        
        self.pen_size = new_width
            

if __name__ == "__main__":
    main()
    