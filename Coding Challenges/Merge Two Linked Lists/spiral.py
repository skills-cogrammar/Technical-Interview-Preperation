"""
https://leetcode.com/problems/spiral-matrix-ii/

    Constraints 
        - Create nxn grid
        - output should be a 2D array that represents the spiral
        - Count from 1 - n^2

    Steps 
        - Generate the grid 
            - Fill each index with None initially 
        - Determine the starting direction 
        - Add numbers to each cell until:
            - Run out of bound
            - Next position already filled
        - If next move is not possible 
            - Check next direction 
        - The operations are complete once we reach nxn for our loop
"""

"""
0 - Right
1 - Down
2 - left
3 - Up
"""

def generate_matrix(n):
    matrix = [[None for i in range(n)] for x in range(n)]
    current_direction = 0
    offset = get_offset(current_direction)

    current_position = [0,0]

    for i in range(1, (n*n) + 1):        
        if (is_in_bound(current_position, n)):            
            matrix[current_position[0]][current_position[1]] = i

        next_position = [current_position[0] + offset[0], current_position[1] + offset[1]]

        if (not is_in_bound(next_position, n) or next_position_taken(matrix, next_position)):
            current_direction = change_direction(current_direction)
            offset = get_offset(current_direction)
            next_position = [current_position[0] + offset[0], current_position[1] + offset[1]]

        current_position = next_position                   

    return matrix

def next_position_taken(matrix, next_position):
    return matrix[next_position[0]][next_position[1]]

def is_in_bound(current_position, n):
    # The issue was using AND instead of OR 😞
    if (current_position[0] >= n or current_position[0] < 0):
        return False
    if (current_position[1] >= n  or current_position[1] < 0):
        return False
    
    return True

def print_matrix(matrix):
    for x, row in enumerate(matrix):
        print()
        for y, col in enumerate(matrix[x]):
            print(col, end=" ")


def change_direction(current_direction: int):
    return (current_direction + 1) % 4

def get_offset(current_direction: int):
    
    match current_direction:
        case 0: return (0, 1)
        case 1: return (1, 0)
        case 2: return (0, -1)
        case 3: return (-1, 0)



if __name__ == '__main__':
    print_matrix(generate_matrix(6))