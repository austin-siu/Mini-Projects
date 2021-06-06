board = [
    [0,0,0,0,1,0,5,0,0],
    [0,0,0,0,0,9,3,0,1],
    [0,0,5,0,0,8,0,0,6],
    [0,0,0,1,0,0,0,4,0],
    [7,8,0,0,0,0,0,2,5],
    [0,4,0,0,0,5,0,0,0],
    [4,0,0,8,0,0,1,0,0],
    [8,0,2,4,0,0,0,0,0],
    [0,0,6,0,3,0,0,0,0]
]

# Print the board
def print_board(bo):
    for i in range(len(bo)):
        # Every 3 rows, print horizontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        # Per row
        for j in range(len(bo[0])):
            # Every 3 columns, print separator w/o \n value 
            if j % 3 == 0 and j != 0:
                print ("| ", end = "")
            
            # Print each number
            if j == 8: 
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")
    

# Find an empty square and return the position
def find_empty(bo):
    for i in range(len(bo)):            # Row of the board 
        for j in range(len(bo[i])):     # Length of each row
            if bo[i][j] == 0:           # Empty space is denoted as 0 in board
                return (i,j)            # Row, Col
    
    # No empty values, board is complete!
    return None

# Validate guess
# pos is a tuple format of (row, col)
def validate(bo, num, pos):
    # Validate row
    for i in range(len(bo[0])):
        # num matches an existing value in row AND the existing value is not in the col value of input pos
        if bo[pos[0]][i] == num and pos[1] != i:    
            return False
    
    # Validate column
    for i in range(len(bo)):
        # num matches an existing value in column AND the existing value is not in the row value of input pos
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Divide board into 9 squares with top left box being 0,0
    col_box = pos[1] // 3
    row_box = pos[0] // 3

    # Validate 3x3 sector 
    for i in range(row_box * 3, row_box * 3 + 3):       # Locate which square, then multiply by 3 to get to row
        for j in range(col_box * 3, col_box * 3 + 3):   # Locate which square, then multiply by 3 to get to col
            if bo[i][j] == num and (i,j) != pos:        # num matches any of the values in square AND the existing value is not the input pos
                return False
    
    # None of the previous if cases genereated False
    return True


def solve(bo):
    # Base Case
    if not find_empty(bo):
        return True
    else:
        row, col = find_empty(bo)
    
    for i in range(1,10):
        if validate(bo, i , (row, col)):
            # Input into the board new value if value works!
            bo[row][col] = i

            # Recursively solve the board with the added new value and if it works all the way, return True!
            if solve(bo):
                return True

            # Backtrack if False and reset the value to 0
            bo[row][col] = 0
    
    # If the value didn't work, output False and returns the box back to 0
    return False

    

print_board(board)
solve(board)
print("\n New Board: ")
print_board(board)

