import time  # For adding a delay between lines
import random  # For picking random ASCII art

# List of cute ASCII art designs to display with each line
ascii_art = [
    "   ~*~  ",
    "   ^_^  ",
    "   <3   ",
    "  =^.^= ",
    "   *+*  "
]

# Your poem (replace this with your own poem!)
poem_lines = [
    "The moon above, so soft and bright,      ",
    "Casts dreams upon the world tonight,     ",
    "With stars that twinkle, small and sweet,",
    "The night is where our hearts will meet. "
]

def print_poem_with_art():
    # Print a header with some cute art
    print("\n" + "="*40)
    print("  ~ A Cute Poem for You ~  ")
    print("="*40 + "\n")
    
    # Loop through each line of the poem
    for line in poem_lines:
        # Pick a random ASCII art
        art = random.choice(ascii_art)
        # Print the art, the line, and some padding
        print(f"{art} {line} {art}")
 #       print(f"{art} {line}\t{art}")
        # Add a short delay for effect (0.5 seconds)
        time.sleep(0.5)
    
    # Print a footer with more cute art
    print("\n" + "="*40)
    print("  ~ The End ~  ")
    print("="*40)

# Run the program
if __name__ == "__main__":
    print_poem_with_art()