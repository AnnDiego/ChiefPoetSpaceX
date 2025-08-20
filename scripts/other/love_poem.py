# Define the first principle of love using simple arithmetic
one = 1
two = one + one

# Assert that two is greater than one, print error if not (should never happen)
assert two > one, print("Love's First Principle has failed")

# Confirm the principle with a celebratory message
print("\nLove's First Principle is confirmed! 👼💘\n")

# Set the title of the poem
poem_title = "Two, a Love Poem in Python"

# List of lines in the poem, each line is a string
poem_lines = [
    "One stands alone,                  ",
    "    Two souls unite,               ",
    "        Our love affirms,          ",
    "Together, greater than one--we two."
]

# Print the title of the poem
print(poem_title)

# Print a decorative line of "=" matching the longest line in the poem plus extra for hearts
print("=" * (max(len(line) for line in poem_lines) + 4))

# Print each line of the poem, wrapped with heart emojis for cuteness
for line in poem_lines:
    print(f"❤️ {line} ❤️")

# Print a blank line, a happy ending message with heart eyes emoji, and another blank line
print("\nHappy Ending 😍\n")
