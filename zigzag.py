def zigzag_visual(n):
    # This defines a function named zigzag_visual that takes one argument n. The purpose of this function is to generate a zigzag pattern.
    lines = [''] * n 
    # This creates a list called lines with n empty strings. For example, if n = 3, lines will be ['', '', '']. This list will eventually hold each line of the zigzag pattern.
    row, step = 0, 1
    # row is set to 0. This will be used to keep track of the current row in the zigzag pattern.# step is set to 1. This will determine the direction of movement (up or down) in the zigzag pattern.
    for row in range(1, n*n+1):
        # This starts a loop that iterates from 1 to n*n (inclusive). The idea is to fill the lines list with characters in a zigzag manner.
        lines[row] += ''
        if row % 2 == 0:
            step = 1
        else:
            for row in range(n):
                step =-1
    return lines
n = 3
lines = zigzag_visual(n)
for row in lines:
    print(row)                
    