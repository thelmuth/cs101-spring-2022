
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
#     print("green", find_in_grid(colors, "green"))
#     print("red", find_in_grid(colors, "red"))
#     print("blue", find_in_grid(colors, "blue"))
#     print("elephant", find_in_grid(colors, "elephant"))
    
#     row_and_col = find_in_grid(colors, "yellow")
#     row = row_and_col[0]
#     col = row_and_col[1]

    ### Tuple assignment allows us to assign multiple variables at once
#     (row, col) = find_in_grid(colors, "yellow")
#     
#     print("yellow is at row", row, "and col", col)
    
    
    ### Here's a rectangular grid of numbers:
    num_grid = [[1,0,3,4,5,6],
                [5,3,8,3,5,1],
                [4,18,3,2,1,0],
                [7,7,7,7,7,7]]
    
#     print_grid(num_grid)
#     
#     ### We can use our find_in_grid function on this grid as well
#     print(find_in_grid(num_grid, 8))
#     print(find_in_grid(num_grid, 7))
# 
#     print(sum_grid(num_grid))
#     
#     print("These are the indices of elements divisible by 3:")
#     print(indices_of_all_numbers_divisible_by_3(num_grid))

#     print(find_all(num_grid, 3))

#     print(find_all(colors, "orange"))

    print(find_adjaced_same_elements(num_grid))
    print(find_adjaced_same_elements(colors))


def find_adjaced_same_elements(grid):
    """Finds two elements that are adjacent in the same row of the grid.
    Returns the (row, col) of the first one."""
    
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0]) - 1):
            
            element = grid[row_num][col_num]
            neighbor = grid[row_num][col_num + 1]
            
            if element == neighbor:
                return ((row_num, col_num), (row_num, col_num + 1))
                


def find_all(grid, target):
    """Finds all occurences of target in grid, and returns a list of their
    (row, col)"""
    
    locations = []
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            if grid[row_num][col_num] == target:
                locations.append((row_num, col_num))
                
    return locations
            



### Two primary ways of iterating through a grid:
### 1. Looking at the elements only
### 2. Using the indices of the elements (row and col)
    
def sum_grid(grid):
    """Sums all of the elements in the grid."""
    
    total = 0
    for row in grid:
        ### The elements in grid are the rows of the grid
        
        for element in row:
            ### The elements in row are the actual elements of the grid
            
            total += element
#             total = total + element
            
#             print(total)
            
#         print("-----")
        
    return total
        
        
def indices_of_all_numbers_divisible_by_3(grid):
    """Find all indices of numbers in the grid that are divisible by 3.
    Return a list of those (row, col) tuples."""
    
    print("The number of rows in the grid is:", len(grid))
    print("The number of columns in the grid is:", len(grid[0]))
    
    div_by_3 = []
    
    for row_num in range(len(grid)):
        ### row_num will be 0, 1, 2, ..., number of rows - 1
        
        for col_num in range(len(grid[0])):
            ### col_num will be 0, 1, 2, ..., number of columns - 1
        
            element = grid[row_num][col_num]
            if element % 3 == 0:
                div_by_3.append((row_num, col_num))
                
    return div_by_3
            
    
    
    
    
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
            
            if grid[row_index][col_index] == target:
                return (row_index, col_index)

    return (-1, -1)
        
    
    

if __name__ == "__main__":
    main()
