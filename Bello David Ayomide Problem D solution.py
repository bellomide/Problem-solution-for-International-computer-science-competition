import string
import sys
import random

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE
    grid_size = 10
    # Create empty grid filled with dots
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Directions: 8 possible (horizontal, vertical, diagonal)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (-1, -1), # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)   # diagonal up-right
    ]
    
    for word in words:
        word = word.upper().strip()
        
        # Skip empty words
        if not word:
            continue
            
        # Skip words that are too long for the grid
        if len(word) > grid_size:
            print(f"Warning: Word '{word}' is too long for {grid_size}x{grid_size} grid, skipping.", file=sys.stderr)
            continue
            
        placed = False
        attempts = 0
        
        while not placed and attempts < 1000:
            attempts += 1
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            dr, dc = random.choice(directions)
            
            # Check if word fits within grid boundaries
            end_row = row + dr * (len(word) - 1)
            end_col = col + dc * (len(word) - 1)
            
            if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
                can_place = True
                # Check if we can place the word (empty spots or matching letters)
                for i in range(len(word)):
                    r = row + dr * i
                    c = col + dc * i
                    if grid[r][c] != "." and grid[r][c] != word[i]:
                        can_place = False
                        break
                
                if can_place:
                    # Place the word
                    for i in range(len(word)):
                        r = row + dr * i
                        c = col + dc * i
                        grid[r][c] = word[i]
                    placed = True
        
        if not placed:
            print(f"Warning: Could not place word '{word}' after 1000 attempts.", file=sys.stderr)
    
    # Fill empty spaces with random letters
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == ".":
                grid[r][c] = random.choice(string.ascii_uppercase)
    
    return grid


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
    
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)