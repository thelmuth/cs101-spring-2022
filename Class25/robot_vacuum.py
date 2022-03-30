import csv, random

def main():
    
    ### Open the csv file to use as a grid
    room = csv_to_grid("room1.csv")
        
    print_room(room)
    
    ### Find the location of the vacuum in the grid:
    location = find_in_grid(room, "vacuum")
    print(location)
    
    ### Let's move the vacuum down
#     (room, location) = move_vacuum(room, location, "R")
#     (room, location) = move_vacuum(room, location, "R")
# 
#     commands = ["D", "R", "R", "R", "R", "U", "L", "L"]
#     
#     for direction in commands:
#         (room, location) = move_vacuum(room, location, direction)
#     
#         print_room(room)
#         print(location)

    clean_room(room, location)


def clean_room(room, location):
    """Automatically has vacuum clean the room."""
    
    ## Ideas:
    ##   3  - while loop to check if there's still dirt in room, keep moving in one direction until obstacle
    ##   14 - find location of closest dirt, and move in that direction
    ##   14 - for a long time, move randomly
    ##   7  - move randomly, but ensure you don't enter locations where you haven't been

    while still_dirty(room):
        direction = random.choice(["R", "L", "U", "D"])
        (room, location) = move_vacuum(room, location, direction)
        print_room(room)


def still_dirty(room):
    """Returns True if room still has dirt, and False if it is all clean."""
    
    return True


def move_vacuum(room, location, direction):
    """Moves vacuum at current location in given direction in given room."""
    
    (row, col) = location
    new_row = row
    new_col = col
    
    if direction == "D":
        new_row = row + 1
        
    elif direction == "U":
        new_row = row - 1
        
    elif direction == "L":
        new_col = col - 1
        
    elif direction == "R":
        new_col = col + 1
        
    if room[new_row][new_col] != "obstacle":
        room[new_row][new_col] = "vacuum"
        
        room[row][col] = "clean"
        return (room, (new_row, new_col))
    
    else:
        print("Sorry, you ran into an obstacle")
        return (room, location)
        
    

def print_room(room):
    """Prints a room, with one character per cell.
       Ex:  OOOOOOOOOO
            O  O     O
            O  O     O
            O VO*    O
            O     *  O
            OOOOOOOOOO  """
    
    for row in room:
        
        row_string = ""
        for cell in row:
            
            if cell == "obstacle":
                row_string += "O"
            elif cell == "vacuum":
                row_string += "V"
            elif cell == "clean":
                row_string += " "
            elif cell == "dirt":
                row_string += "*"
        
        print(row_string)
    
    
    


def csv_to_grid(filename):
    """Turns the csv file given by filename into a grid and returns it."""
    
    file = open(filename, "r")
    reader = csv.reader(file)
    
    grid = []
    for row in reader:
        grid.append(row)
        
    return grid


def find_in_grid(grid, target):
    """Finds the row and column of an element in the grid."""
    
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            
            if grid[row_index][col_index] == target:
                return (row_index, col_index)

    return (-1, -1)

if __name__ == "__main__":
    main()