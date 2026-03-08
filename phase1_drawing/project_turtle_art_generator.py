"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    PROJECT: Turtle Art Generator - Create Your Mandala!
===============================================================================

🎨 WHAT THIS PROJECT DOES:
    You type a number (3 to 10), and Python creates a beautiful 
    mandala-style pattern with that many shapes spiraling outward!

🧠 CONCEPTS YOU'LL USE:
    ✅ input() - Getting information from the user
    ✅ while loops - Validation (keep asking until answer is valid)
    ✅ for loops - Drawing shapes and repeating patterns
    ✅ Modulo (%) - Cycling through colors
    ✅ Functions - Organizing code into reusable pieces

===============================================================================
"""

import turtle
import random

# =============================================================================
# SETUP THE DRAWING CANVAS
# =============================================================================

screen = turtle.Screen()
screen.title("🎨 Mandala Art Generator - Your Creation!")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.colormode(255)

artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing
artist.hideturtle()

# =============================================================================
# BEAUTIFUL COLOR PALETTES
# =============================================================================

# Each palette is a list of RGB colors
# 🧠 LOGIC SEED: Lists store multiple values in order
# We'll use modulo (%) to cycle through these colors endlessly!

PALETTES = {
    "sunset": [
        (255, 94, 77),    # Coral
        (255, 154, 0),    # Orange
        (255, 206, 84),   # Gold
        (255, 89, 94),    # Salmon
        (255, 128, 0),    # Deep orange
    ],
    "ocean": [
        (0, 119, 182),    # Ocean blue
        (0, 180, 216),    # Sky blue
        (144, 224, 239),  # Light cyan
        (72, 202, 228),   # Turquoise
        (0, 150, 199),    # Deep blue
    ],
    "forest": [
        (34, 139, 34),    # Forest green
        (0, 128, 0),      # Green
        (107, 142, 35),   # Olive
        (85, 107, 47),    # Dark olive
        (124, 252, 0),    # Lawn green
    ],
    "neon": [
        (255, 0, 255),    # Magenta
        (0, 255, 255),    # Cyan
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Lime
        (255, 0, 128),    # Hot pink
    ],
    "ipl": [
        (0, 102, 178),    # MI Blue
        (255, 204, 0),    # CSK Yellow
        (204, 0, 0),      # RCB Red
        (59, 42, 107),    # KKR Purple
        (255, 130, 0),    # SRH Orange
        (255, 55, 148),   # RR Pink
    ]
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def draw_polygon(sides, size, color):
    """
    Draws a regular polygon with the given number of sides.
    
    Parameters:
        sides - number of sides (3=triangle, 4=square, etc.)
        size  - length of each side in pixels
        color - RGB tuple or color name
    """
    angle = 360 / sides
    artist.pencolor(color)
    artist.pensize(2)
    
    for _ in range(sides):
        artist.forward(size)
        artist.right(angle)


def draw_spiral_shape(sides, start_size, growth, rotations, palette):
    """
    Draws a spiraling mandala pattern.
    
    Parameters:
        sides      - number of sides for each shape
        start_size - initial size of the first shape
        growth     - how much bigger each shape gets
        rotations  - how many shapes to draw
        palette    - list of colors to cycle through
    """
    current_size = start_size
    
    for i in range(rotations):
        # 🧠 LOGIC SEED: MODULO (%) - The Remainder Trick!
        # When i goes 0, 1, 2, 3, 4, 5, 6, 7...
        # i % 5 gives us: 0, 1, 2, 3, 4, 0, 1, 2... (cycles 0-4 forever!)
        # This is how we cycle through colors without running out!
        
        color_index = i % len(palette)  # Cycles through palette indices
        current_color = palette[color_index]
        
        # Draw one polygon
        draw_polygon(sides, current_size, current_color)
        
        # Rotate slightly for the spiral effect
        artist.right(360 / rotations)
        
        # Grow the size for next shape
        current_size += growth


def display_title(num_shapes):
    """Shows the title and info at the top of the screen."""
    artist.penup()
    artist.goto(0, 380)
    artist.pencolor("white")
    artist.write(f"🎨 MANDALA ART - {num_shapes}-Sided Shapes", 
                 align="center", font=("Arial", 24, "bold"))
    artist.goto(0, 350)
    artist.write("Created with Python by YOU!", 
                 align="center", font=("Arial", 14, "normal"))
    artist.goto(0, 0)  # Return to center


# =============================================================================
# MAIN PROGRAM: GET USER INPUT WITH VALIDATION
# =============================================================================

print("=" * 60)
print("       🎨 WELCOME TO THE MANDALA ART GENERATOR! 🎨")
print("=" * 60)
print()
print("You'll create a beautiful spiraling mandala pattern!")
print("Choose how many sides each shape should have (3-10).")
print()

# --- Input Validation Loop ---
# We use a WHILE loop to keep asking until we get a valid answer

# 🔗 FUTURE TOOL: Input validation is EVERYWHERE in real software!
# Every web form, every n8n webhook, every database entry needs validation.
# "Is this data in the correct format?" is a question asked billions of times daily.

valid_input = False

while not valid_input:
    user_input = input("Enter number of sides (3-10): ")
    
    # Check if user typed a number
    if user_input.isdigit():
        num_sides = int(user_input)
        
        # Check if the number is in our valid range
        if 3 <= num_sides <= 10:
            valid_input = True
            print(f"✅ Great choice! Creating {num_sides}-sided mandala...")
        else:
            print("❌ Oops! Please enter a number between 3 and 10.")
            print("   (3 = triangle, 4 = square, 5 = pentagon, etc.)")
    else:
        print("❌ That's not a number! Please type a digit like 5 or 7.")

print()

# --- Choose a color palette ---
print("Choose a color palette:")
print("  1. sunset  - Warm orange and coral tones")
print("  2. ocean   - Cool blue and cyan tones")
print("  3. forest  - Natural green tones")
print("  4. neon    - Bright vibrant colors")
print("  5. ipl     - IPL team colors!")
print()

palette_choice = input("Enter palette name (or press Enter for 'ipl'): ").lower().strip()

if palette_choice in PALETTES:
    chosen_palette = PALETTES[palette_choice]
    print(f"✅ Using '{palette_choice}' palette!")
else:
    chosen_palette = PALETTES["ipl"]
    print("✅ Using 'ipl' palette (default)!")

print()
print("🎨 Drawing your mandala... Watch the magic happen!")
print()

# =============================================================================
# DRAW THE MANDALA
# =============================================================================

# Display title
display_title(num_sides)

# Move to center
artist.penup()
artist.goto(0, 0)
artist.pendown()

# Set parameters for the spiral
start_size = 5           # Initial shape size
growth = 3               # How much each shape grows
num_rotations = 60       # How many shapes to draw (more = denser pattern)

# Draw the mandala!
draw_spiral_shape(num_sides, start_size, growth, num_rotations, chosen_palette)

# Add center decoration
artist.penup()
artist.goto(0, -20)
artist.pendown()
artist.pencolor("white")
artist.pensize(3)
artist.circle(30)

# =============================================================================
# COMPLETION MESSAGE
# =============================================================================

artist.penup()
artist.goto(0, -400)
artist.pencolor((100, 100, 100))
artist.write("Click the window to close", 
             align="center", font=("Arial", 12, "normal"))

print("=" * 60)
print("         🎨 YOUR MANDALA IS COMPLETE! 🎨")
print("=" * 60)
print()
print(f"Shape type: {num_sides}-sided polygon")
print(f"{'  3=Triangle' if num_sides==3 else '  4=Square' if num_sides==4 else '  5=Pentagon' if num_sides==5 else '  6=Hexagon' if num_sides==6 else f'  {num_sides}-gon'}")
print(f"Colors used: {len(chosen_palette)} colors cycling with modulo (%)")
print(f"Total shapes drawn: {num_rotations}")
print()
print("🧠 KEY CONCEPT YOU USED:")
print("  The MODULO operator (%) gives us the remainder after division.")
print("  Example: 7 % 5 = 2 (because 7 ÷ 5 = 1 remainder 2)")
print("  This lets us cycle through 5 colors forever: 0,1,2,3,4,0,1,2...")
print()
print("🔗 FUTURE TOOL CONNECTION:")
print("  This pattern (get input → validate → process → output) is")
print("  exactly how n8n workflows operate: Trigger → IF Node → Action!")
print()

screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A NEW PALETTE
    - Add a "rainbow" palette to the PALETTES dictionary
    - Use these colors: red, orange, yellow, green, blue, purple
    - Find the RGB values online or guess!
    - Test it by choosing "rainbow" when running the program

Challenge 2: CHANGE THE GROWTH PATTERN
    - Currently, `growth = 3` makes each shape 3 pixels bigger
    - What happens if you set growth = 7? (faster expansion)
    - What happens if you set growth = 1? (very tight spiral)
    - Try setting growth = 0. What do you get? (concentric shapes!)

Challenge 3: REVERSE SPIRAL DIRECTION
    - Find the line: artist.right(360 / rotations)
    - Change it to: artist.left(360 / rotations)
    - The spiral now turns the other way!

Challenge 4: ADD MORE INPUT VALIDATION
    - Currently, entering "abc" shows an error and asks again
    - Can you add validation for these cases too?
        - What if they type a negative number? (-5)
        - What if they type a decimal? (4.5)
    - Hint: int("4.5") causes an error! Use try/except

Challenge 5: RANDOMIZE EVERYTHING
    - Import random at the top: import random
    - Set num_sides = random.randint(3, 10)
    - Set palette randomly: 
        palette_name = random.choice(list(PALETTES.keys()))
    - Now each run creates a surprise!

Challenge 6: MODULO DEEP DIVE
    Run this code and study the output:
    
    for i in range(20):
        print(f"i = {i}, i % 5 = {i % 5}")
    
    Notice how i % 5 ALWAYS stays between 0 and 4!
    That's the magic of modulo - it loops back around.
"""

# =============================================================================
# BONUS: Understanding the Math
# =============================================================================
"""
WHY 360 / ROTATIONS?

If we want 60 shapes to form a complete circle (360 degrees):
    Each shape needs to be rotated by: 360 / 60 = 6 degrees

So after drawing 60 shapes, each rotated 6 degrees:
    60 × 6 = 360 degrees (full circle!)

This is the same math you learned in the shapes lesson:
    360 / 4 = 90 degrees for a square
    360 / 6 = 60 degrees for a hexagon
    360 / 60 = 6 degrees for 60 rotations

Math is everywhere in programming! 📐
"""
