# Usage / command-line options:
#  - --path / -p {1,2}    Force which path to display (1 or 2). If omitted a random path is chosen.
#
# Examples:
#  python3 tactile_force.py           # choose path randomly
#  python3 tactile_force.py --path 1  # force path 1 (prints path1 and a 🎣 line)
#  python3 tactile_force.py -p 2      # force path 2 (prints path2 and a 🎻 line)
#
# Notes:
#  - The script sleeps for 3 seconds before choosing a path.
#  - The script prints a short emoji separator (🎣 or 🎻) and a long hyphen line representing
#    a string when the chosen path finishes.

import random
import time
import argparse
import shutil

# Parse CLI early so invalid values fail before any output or sleep.
# --path / -p accepts only "1" or "2"; argparse will print usage and exit on invalid input.
parser = argparse.ArgumentParser(description="Tactile Force demo")
parser.add_argument("--path", "-p", choices=["1", "2"],
                    help="Force which path to display (1 or 2). If omitted, a random choice is used.")
args = parser.parse_args()

intro = """
There is a tactile force between us—
a fine violin string pulled taut,
humming with the weight of what we withhold.
If I pluck it, gently,
it reverberates through the quiet,
a chord that drips sweet injury,
and I am, at once, undone.
"""

path1 = """
If I could pull that tensile line
and draw you close—
wrap you in my arms, I would.
But the taut strand is delicate, brittle,
its hold a tenuous strain, the test too shy.
I dare not risk the snap, the loss of you—
your soft resistance pulsing through the wire,
alive, exciting, unreeled.
"""

path2 = """
Yet in that unraveling, your fingers find the bow—
draw it slow across the frayed edge,
coaxing fierce discord from the wound. 
It rounds as fingertips coax
into unity at last—
vibrations building to symphony,
beauty forged from healed pain,
trembling into silence, spent and whole.
"""

print("\nTactile Force — Live Demo\n")
print(intro)
print("\nPath choice incoming...")
time.sleep(3)

# Determine which path to use (CLI overrides random choice)
if args.path:
    choice = args.path
    chosen_random = False
else:
    choice = random.choice(["1", "2"])  # Replace with poll winner: input("Poll says (1/2): ")
    chosen_random = True
if choice == "1":
    print("\n" + "="*30)
    # Use different wording depending on whether the choice was random or forced
    if chosen_random:
        print("Randomly chose the tease 🎻")
    else:
        print("Audience chose the tease 🎻")
    print(path1)
# Ensure the alternate path prints when '2' is chosen (the '1' branch is above)
if choice == "2":
    print("\n" + "="*30)
    if chosen_random:
        print("Randomly chose the bow 🎶")
    else:
        print("Audience chose the bow 🎶")
    print(path2)

# Print a long "violin string" line across the terminal width.
# Use hyphens which display reliably in most terminals; fall back to 80 columns.
try:
    term_width = shutil.get_terminal_size((80, 20)).columns
except Exception:
    term_width = 80

# Single emoji line (visual separator) placed before the long string.
# Show a fishing-pole 🎣 for path 1, and a violin 🎻 for path 2.
if choice == "1":
    print("🎣")
elif choice == "2":
    print("🎻")

print("-" * term_width)