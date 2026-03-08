"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 2: Turtle Basics - Draw a Cricket Pitch!
===============================================================================

In this session, you'll learn:
    ✅ The turtle module - Python's drawing tool
    ✅ Moving forward, backward, turning left and right
    ✅ Using penup() and pendown() to move without drawing
    ✅ Setting speed and colors
    ✅ Drawing your first real picture - a cricket pitch!

===============================================================================
"""

# =============================================================================
# GETTING STARTED WITH TURTLE
# =============================================================================

# import brings in extra tools (modules) that Python can use
# turtle is a drawing module - it creates a window and draws with a "turtle"
import turtle

# Think of the turtle as a pen held by a robot that follows your commands!

# =============================================================================
# ASCII FLOWCHART: How to Draw a Cricket Pitch
# =============================================================================
"""
    START
      │
      ▼
┌─────────────────────┐
│  Set up screen and  │
│  turtle settings    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Move to starting   │
│  position           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Draw the outer     │
│  pitch rectangle    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Draw crease lines  │
│  at both ends       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Draw wickets       │
│  (stumps) at ends   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Add labels and     │
│  finishing touches  │
└──────────┬──────────┘
           │
           ▼
         END
"""

# 🧠 LOGIC SEED: This step-by-step sequence is called an ALGORITHM
# Every program is just a list of steps executed in order
# This is EXACTLY how n8n workflows work - one node after another!

# =============================================================================
# PART 1: SETTING UP THE CANVAS
# =============================================================================

# Create the drawing window (called "screen")
screen = turtle.Screen()
screen.title("🏏 Cricket Pitch - My First Turtle Drawing!")
screen.bgcolor("forestgreen")  # Cricket fields are green!
screen.setup(width=800, height=600)  # Window size in pixels

# Create our turtle artist
pitch_artist = turtle.Turtle()
pitch_artist.speed(3)  # 1 = slowest, 10 = fast, 0 = instant

# 🔗 FUTURE TOOL: Setting up the screen is like configuring settings in n8n
# You set parameters BEFORE running the main workflow

# =============================================================================
# PART 2: UNDERSTANDING TURTLE MOVEMENTS
# =============================================================================

# BASIC TURTLE COMMANDS:
# forward(distance)  - Move forward by 'distance' pixels
# backward(distance) - Move backward by 'distance' pixels
# right(angle)       - Turn right by 'angle' degrees
# left(angle)        - Turn left by 'angle' degrees
# penup()            - Stop drawing (lift the pen)
# pendown()          - Start drawing (put pen down)
# goto(x, y)         - Jump to coordinates (x, y)

# 🧠 LOGIC SEED: Coordinates work like graph paper (CBSE Math!)
# Center of screen is (0, 0)
# x increases going RIGHT, decreases going LEFT
# y increases going UP, decreases going DOWN

# =============================================================================
# PART 3: DRAWING THE MAIN PITCH RECTANGLE
# =============================================================================

# Pitch dimensions (in pixels - scaled down from real pitch)
pitch_length = 400  # The long side
pitch_width = 80    # The narrow side

# Move to starting position (bottom-left corner of pitch)
pitch_artist.penup()                    # Don't draw while moving
pitch_artist.goto(-200, -40)            # Go to starting position
pitch_artist.pendown()                  # Ready to draw!

# Set the color for the pitch
pitch_artist.pencolor("sandybrown")     # Pitch color
pitch_artist.pensize(3)                 # Line thickness

# Drawing a rectangle requires 4 sides
# CBSE Geometry Connection: Rectangle has 4 right angles (90 degrees each)

# Draw the pitch rectangle
print("Drawing pitch rectangle...")

# Side 1: Bottom (going right)
pitch_artist.forward(pitch_length)      # Move 400 pixels →
print(f"  Drew bottom side: {pitch_length} pixels")

# Turn 90 degrees to face up
pitch_artist.left(90)                   # Turn left 90° ↑
print("  Turned left 90 degrees")

# Side 2: Right side (going up)
pitch_artist.forward(pitch_width)       # Move 80 pixels ↑
print(f"  Drew right side: {pitch_width} pixels")

# Turn 90 degrees to face left
pitch_artist.left(90)                   # Turn left 90° ←

# Side 3: Top (going left)
pitch_artist.forward(pitch_length)      # Move 400 pixels ←
print(f"  Drew top side: {pitch_length} pixels")

# Turn 90 degrees to face down
pitch_artist.left(90)                   # Turn left 90° ↓

# Side 4: Left side (going down)
pitch_artist.forward(pitch_width)       # Move 80 pixels ↓
print(f"  Drew left side: {pitch_width} pixels")

print("✅ Pitch rectangle complete!")
print()

# =============================================================================
# PART 4: DRAWING THE CREASE LINES
# =============================================================================

# In cricket, there are crease lines near each wicket
# Let's draw the batting crease (popping crease) at both ends

pitch_artist.pencolor("white")
pitch_artist.pensize(2)

# --- Left End Crease ---
print("Drawing left crease...")
pitch_artist.penup()
pitch_artist.goto(-150, -50)    # Position below pitch
pitch_artist.pendown()
pitch_artist.goto(-150, 50)     # Draw vertical line
print("  ✅ Left crease done")

# --- Right End Crease ---
print("Drawing right crease...")
pitch_artist.penup()
pitch_artist.goto(150, -50)     # Position below pitch on right
pitch_artist.pendown()
pitch_artist.goto(150, 50)      # Draw vertical line
print("  ✅ Right crease done")

print()

# =============================================================================
# PART 5: DRAWING THE WICKETS (STUMPS)
# =============================================================================

# Each wicket has 3 stumps (vertical lines)

pitch_artist.pencolor("peru")  # Wooden color for stumps
pitch_artist.pensize(4)        # Thicker lines for stumps

# --- Left End Wickets (3 stumps) ---
print("Drawing left wickets...")

# Stump positions: spread across 8 pixels total, centered at x = -180
stump_positions_left = [-184, -180, -176]

for stump_x in stump_positions_left:
    pitch_artist.penup()
    pitch_artist.goto(stump_x, -10)   # Bottom of stump
    pitch_artist.pendown()
    pitch_artist.goto(stump_x, 10)    # Top of stump (20 pixels tall)

print("  ✅ Left wickets done (3 stumps)")

# --- Right End Wickets (3 stumps) ---
print("Drawing right wickets...")

stump_positions_right = [176, 180, 184]

for stump_x in stump_positions_right:
    pitch_artist.penup()
    pitch_artist.goto(stump_x, -10)
    pitch_artist.pendown()
    pitch_artist.goto(stump_x, 10)

print("  ✅ Right wickets done (3 stumps)")

print()

# =============================================================================
# PART 6: ADDING LABELS
# =============================================================================

# Let's add text labels to our drawing

pitch_artist.penup()
pitch_artist.goto(0, 80)  # Position above the pitch
pitch_artist.pencolor("white")

# write() puts text on the canvas
pitch_artist.write("CRICKET PITCH", align="center", font=("Arial", 20, "bold"))

# Label the ends
pitch_artist.goto(-180, -80)
pitch_artist.write("Bowler's End", align="center", font=("Arial", 12, "normal"))

pitch_artist.goto(180, -80)
pitch_artist.write("Batsman's End", align="center", font=("Arial", 12, "normal"))

print("✅ Labels added!")

# =============================================================================
# PART 7: FINISHING UP
# =============================================================================

# Hide the turtle cursor when done
pitch_artist.hideturtle()

print()
print("═" * 50)
print("   🏏 YOUR CRICKET PITCH IS COMPLETE! 🏏")
print("═" * 50)
print()
print("You just gave Python exact step-by-step instructions!")
print("This is how ALL programming works.")
print()

# 🔗 FUTURE TOOL: This exact sequence of steps = an n8n workflow!
# Step 1: Setup → Step 2: Draw pitch → Step 3: Draw creases → etc.
# In n8n, each step would be a "node" connected to the next.

# Keep the window open until clicked
print("Click the drawing window to close it.")
screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CHANGE THE COLORS
    - Change screen.bgcolor() to "wheat" (dry pitch!)
    - Change the pitch rectangle color to "saddlebrown"
    - Predict: What color would "deepskyblue" make? (Try it!)

Challenge 2: ADD A CENTER LINE
    - Draw a thin dotted line from the left wicket to the right wicket
    - Hint: You can use a loop that alternates penup() and pendown()
    - This shows the path the ball travels!

Challenge 3: MAKE IT BIGGER
    - Change pitch_length from 400 to 500
    - Change pitch_width from 80 to 100
    - What else needs to change? (Hint: crease and stump positions!)
    - This teaches you about connected values in code

Challenge 4: ADD BAILS
    - Real wickets have 2 small bails on top of the stumps
    - Draw small horizontal lines connecting the tops of the stumps
    - Hint: The bail should go from stump_x of first stump to last stump at y=10
"""

# =============================================================================
# REFERENCE: Turtle Commands Cheat Sheet
# =============================================================================
"""
MOVEMENT:
    forward(distance)   or fd(distance)
    backward(distance)  or bk(distance)
    right(angle)        or rt(angle)
    left(angle)         or lt(angle)
    goto(x, y)
    
PEN CONTROL:
    penup()            or pu()
    pendown()          or pd()
    pensize(width)
    pencolor("color")
    
OTHER:
    speed(0-10)        # 0 = instant, 1 = slow, 10 = fast
    hideturtle()       # Hide the arrow
    showturtle()       # Show the arrow
    write("text")      # Write text at current position
    
COLORS YOU CAN USE:
    "red", "blue", "green", "yellow", "orange", "purple", "pink"
    "brown", "black", "white", "gray", "gold", "cyan", "magenta"
    "forestgreen", "sandybrown", "peru", "saddlebrown"
"""
