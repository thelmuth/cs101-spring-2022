import csv

def main():
    
    ### Open the csv file to use as a grid
    room = csv_to_grid("room1.csv")
    
    ### Print out the grid one row at a time:
#     for row in room:
#         print(row)
        
    print_room(room)
    
    ### Find the location of the vacuum in the grid:
    location = find_in_grid(room, "vacuum")
    print(location)
    
    ### Let's move the vacuum down
    (room, location) = move_vacuum(room, location, "D")
    
    print_room(room)



def move_vacuum(room, location, direction):
    """Moves vacuum at current location in given direction in given room."""
    
    ### These are equivalent to the tuple assignment
#     row = location[0]
#     col = location[1]
    (row, col) = location
    
    if direction == "D":
        row = row + 1
    elif direction == "U":
        row = row - 1
    
    room[row][col] = "vacuum"
    
    return (room, (row, col))
        
    

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