
def main():
    
    ## Create a grid of color strings
    colors = [["green", "orange", "blue", "orange"],
              ["blue", "green", "green", "orange"],
              ["purple", "red", "blue", "red"],
              ["yellow", "blue", "green", "yellow"]]
    
#     print(colors)
    
    ### What happens if we index colors?
    mystery = colors[2]
#     print(mystery)
#     print(mystery[1])
#     print(mystery[0])
    
    ### Here's how we can access a single element:
#     print(colors[3][1])
    
    ### Write a function to make printing a grid nicer
#     print_grid(colors)

#     print(colors.index("green")) ### Won't work

    ### Write our own function that will find an element in a grid
    print("green", find_in_grid(colors, "green"))
    print("red", find_in_grid(colors, "red"))
    print("blue", find_in_grid(colors, "blue"))
    print("elephant", find_in_grid(colors, "elephant"))
    
#     row_and_col = find_in_grid(colors, "yellow")
#     row = row_and_col[0]
#     col = row_and_col[1]

    ### Tuple assignment allows us to assign multiple variables at once
    (row, col) = find_in_grid(colors, "yellow")
    
    print("yellow is at row", row, "and col", col)
    

    
    
    
def print_grid(grid):
    """A slightly nicer printing of a grid"""
    for row in grid:
        print(row)
    
def find_in_grid(grid, target):
    """Finds the row and column of an element in the grid."""
    
    ## len(grid) gives us the number of rows in the grid
    for row_index in range(len(grid)):
 
        ### len(grid[row_index]) will tell use how many elements are in
        ### this row, which is how many columns there are
        for col_index in range(len(grid[row_index])):
            
            ### First, print the row and col index
            #print(row_index, col_index)
            
            ### Prediction: - green
            ###             - 0 0
            ###   Second:   - 0 1
            
            if grid[row_index][col_index] == target:
                return (row_index, col_index)
            
        #print("Done with row")
    return (-1, -1)
        
    
    

if __name__ == "__main__":
    main()
