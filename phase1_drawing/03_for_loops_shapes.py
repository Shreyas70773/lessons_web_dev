"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 3: For Loops & Shapes
===============================================================================

In this session, you'll learn:
    ✅ How for loops work - doing something multiple times
    ✅ The range() function - generating sequences of numbers
    ✅ The geometry formula: exterior angle = 360° / number of sides
    ✅ Drawing triangles, squares, pentagons, hexagons, and circles

===============================================================================
"""

import turtle

# =============================================================================
# ASCII FLOWCHART: How a FOR LOOP Works
# =============================================================================
"""
                    START
                      │
                      ▼
         ┌────────────────────────┐
         │ i = first value        │
         │ (e.g., i = 0)          │
         └───────────┬────────────┘
                     │
          ┌──────────▼──────────┐
          │  Is i < end value?  │◄────────────────────┐
          └──────────┬──────────┘                     │
                     │                                │
           ┌─────────┴─────────┐                      │
           │                   │                      │
         YES                  NO                      │
           │                   │                      │
           ▼                   ▼                      │
    ┌──────────────┐     ┌──────────┐                 │
    │ Run the code │     │   END    │                 │
    │ inside loop  │     │   LOOP   │                 │
    └──────┬───────┘     └──────────┘                 │
           │                                          │
           ▼                                          │
    ┌──────────────┐                                  │
    │  i = i + 1   │──────────────────────────────────┘
    │ (go to next) │
    └──────────────┘

Example: for i in range(4):   # i goes 0, 1, 2, 3 then stops
             print(i)
"""

# 🧠 LOGIC SEED: A for loop is like telling n8n: "repeat this node X times"
# In n8n, you'd use a "Loop Over Items" node to do the same thing!

# =============================================================================
# SETUP THE DRAWING CANVAS
# =============================================================================

screen = turtle.Screen()
screen.title("🔷 Shape Gallery - For Loops & Geometry!")
screen.bgcolor("navy")
screen.setup(width=1000, height=700)

artist = turtle.Turtle()
artist.speed(3)
artist.pensize(3)

# =============================================================================
# THE MAGIC FORMULA: 360 / sides = exterior angle
# =============================================================================

# When you draw a polygon (closed shape with straight sides):
# - You make a full turn (360 degrees) around the shape
# - Each corner turns the same amount
# - So each turn = 360 / number_of_sides

# Triangle:  360 / 3 = 120 degrees
# Square:    360 / 4 = 90 degrees
# Pentagon:  360 / 5 = 72 degrees
# Hexagon:   360 / 6 = 60 degrees

# 🔗 FUTURE TOOL: This formula = a RULE that you apply consistently
# In n8n and SQL, you write rules once and they apply to all data

# =============================================================================
# SHAPE 1: TRIANGLE (3 sides)
# =============================================================================

def draw_triangle(x, y, size, color):
    """Draws a triangle at position (x, y) with given size and color"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    sides = 3
    angle = 360 / sides  # = 120 degrees
    
    print(f"Drawing TRIANGLE: {sides} sides, turning {angle}° each time")
    
    artist.begin_fill()
    for i in range(sides):
        artist.forward(size)
        artist.right(angle)  # Turn right 120 degrees
    artist.end_fill()

# Draw the triangle on the left side of screen
artist.penup()
artist.goto(-400, 250)
artist.pendown()
artist.pencolor("white")
artist.write("TRIANGLE (3 sides)", font=("Arial", 12, "bold"))

draw_triangle(-400, 200, 80, "red")

# =============================================================================
# SHAPE 2: SQUARE (4 sides)
# =============================================================================

def draw_square(x, y, size, color):
    """Draws a square at position (x, y)"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    sides = 4
    angle = 360 / sides  # = 90 degrees
    
    print(f"Drawing SQUARE: {sides} sides, turning {angle}° each time")
    
    artist.begin_fill()
    for i in range(sides):
        artist.forward(size)
        artist.right(angle)
    artist.end_fill()

# Draw square label and shape
artist.penup()
artist.goto(-200, 250)
artist.pendown()
artist.pencolor("white")
artist.write("SQUARE (4 sides)", font=("Arial", 12, "bold"))

draw_square(-200, 200, 80, "yellow")

# =============================================================================
# SHAPE 3: PENTAGON (5 sides)
# =============================================================================

def draw_pentagon(x, y, size, color):
    """Draws a pentagon at position (x, y)"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    sides = 5
    angle = 360 / sides  # = 72 degrees
    
    print(f"Drawing PENTAGON: {sides} sides, turning {angle}° each time")
    
    artist.begin_fill()
    for i in range(sides):
        artist.forward(size)
        artist.right(angle)
    artist.end_fill()

# Draw pentagon label and shape
artist.penup()
artist.goto(0, 250)
artist.pendown()
artist.pencolor("white")
artist.write("PENTAGON (5 sides)", font=("Arial", 12, "bold"))

draw_pentagon(0, 200, 70, "lime")

# =============================================================================
# SHAPE 4: HEXAGON (6 sides)
# =============================================================================

def draw_hexagon(x, y, size, color):
    """Draws a hexagon at position (x, y)"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    sides = 6
    angle = 360 / sides  # = 60 degrees
    
    print(f"Drawing HEXAGON: {sides} sides, turning {angle}° each time")
    
    artist.begin_fill()
    for i in range(sides):
        artist.forward(size)
        artist.right(angle)
    artist.end_fill()

# Draw hexagon label and shape
artist.penup()
artist.goto(200, 250)
artist.pendown()
artist.pencolor("white")
artist.write("HEXAGON (6 sides)", font=("Arial", 12, "bold"))

draw_hexagon(200, 200, 60, "cyan")

# =============================================================================
# SHAPE 5: CIRCLE (using small steps with many tiny turns)
# =============================================================================

def draw_circle_manual(x, y, radius, color):
    """Draws a circle by making many tiny moves and turns"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    # A circle = polygon with LOTS of sides (360 tiny sides!)
    sides = 60  # 60 sides looks smooth enough
    angle = 360 / sides  # = 6 degrees per turn
    
    # Circumference = 2 * pi * radius (we'll approximate)
    circumference = 2 * 3.14159 * radius
    side_length = circumference / sides
    
    print(f"Drawing CIRCLE: {sides} tiny sides, turning {angle}° each time")
    
    artist.begin_fill()
    for i in range(sides):
        artist.forward(side_length)
        artist.right(angle)
    artist.end_fill()

# Draw circle label and shape
artist.penup()
artist.goto(380, 250)
artist.pendown()
artist.pencolor("white")
artist.write("CIRCLE (360°)", font=("Arial", 12, "bold"))

draw_circle_manual(380, 170, 40, "magenta")

# =============================================================================
# DEMONSTRATION: THE PATTERN WITH INCREASING SIDES
# =============================================================================

# Now let's show the pattern more clearly in one row

print("\n" + "=" * 50)
print("        GEOMETRY PATTERN DEMONSTRATION")
print("=" * 50)

artist.penup()
artist.goto(-350, -50)
artist.pendown()
artist.pencolor("white")
artist.write("Watch the pattern: more sides = smaller turns!", font=("Arial", 14, "bold"))

# Draw shapes with 3, 4, 5, 6, 7, 8 sides in a row
colors = ["red", "orange", "yellow", "lime", "cyan", "violet"]
positions = [-350, -200, -50, 100, 250, 380]

for i, num_sides in enumerate(range(3, 9)):  # 3 to 8 sides
    angle = 360 / num_sides
    
    artist.penup()
    artist.goto(positions[i], -100)
    artist.pendown()
    artist.pencolor(colors[i])
    artist.fillcolor(colors[i])
    
    artist.begin_fill()
    for _ in range(num_sides):
        artist.forward(40)
        artist.right(angle)
    artist.end_fill()
    
    # Label below each shape
    artist.penup()
    artist.goto(positions[i], -160)
    artist.pencolor("white")
    artist.write(f"{num_sides} sides\n{angle:.1f}°", font=("Arial", 10, "normal"))
    
    print(f"Shape with {num_sides} sides: exterior angle = {angle:.1f}°")

# =============================================================================
# CONNECTING TO YOUR MATH CLASS
# =============================================================================

artist.penup()
artist.goto(-350, -220)
artist.pencolor("gold")
artist.write("📐 CBSE GEOMETRY CONNECTION:", font=("Arial", 14, "bold"))

artist.goto(-350, -250)
artist.pencolor("white")
artist.write("Sum of exterior angles of ANY polygon = 360°", font=("Arial", 12, "normal"))

artist.goto(-350, -280)
artist.write("Each exterior angle = 360° ÷ number of sides", font=("Arial", 12, "normal"))

# =============================================================================
# FINAL MESSAGE
# =============================================================================

artist.penup()
artist.goto(0, -320)
artist.pencolor("gold")
artist.write("🎉 You drew 6 different shapes using the SAME pattern!", 
             align="center", font=("Arial", 14, "bold"))

artist.hideturtle()

print("\n" + "=" * 50)
print("   🎉 SHAPE GALLERY COMPLETE! 🎉")
print("=" * 50)
print("\nKey Learning:")
print("  • A for loop repeats code a specific number of times")
print("  • range(n) generates numbers from 0 to n-1")
print("  • The formula 360/sides works for ANY regular polygon!")
print()

# 🔗 FUTURE TOOL: When you use n8n's "Loop Over Items" node,
# it works exactly like this for loop - processing each item one by one!

screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: DRAW A HEPTAGON (7 sides)
    - Calculate: what's 360 / 7?
    - Create a new function draw_heptagon(x, y, size, color)
    - Draw it in a new position
    - Predict: will it look more like a hexagon or more like a circle?

Challenge 2: CHANGE LOOP VARIABLE
    - In the for loop, we used 'i' and '_' as variable names
    - Change one loop to use 'side_number' instead:
        for side_number in range(sides):
            print(f"Drawing side {side_number + 1}")
            artist.forward(size)
            artist.right(angle)
    - Now it tells you which side it's drawing!

Challenge 3: ROTATING SQUARES
    - Use a for loop to draw 36 overlapping squares
    - After each square, turn 10 degrees
        for i in range(36):
            draw_square(0, 0, 100, "white")
            artist.right(10)
    - This creates a beautiful circular pattern!
    - Hint: Make color change with each square for extra cool effect

Challenge 4: PREDICT THE OUTPUT
    - What does range(5) actually give you?
    - Test it: for x in range(5): print(x)
    - Answer: It prints 0, 1, 2, 3, 4 (NOT 5!)
    - Why? range(n) goes from 0 to n-1
"""
