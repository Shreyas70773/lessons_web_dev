"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 15: Functions Calling Functions - Building Scenes!
===============================================================================

In this session, you'll learn:
    ✅ How functions can call other functions
    ✅ Building complex things from simple pieces
    ✅ The power of composition
    ✅ Creating a complete turtle scene from reusable parts

===============================================================================
"""

import turtle
import random

# =============================================================================
# THE BIG IDEA: COMPOSITION
# =============================================================================

print("=" * 60)
print("       🏗️ BUILDING COMPLEXITY FROM SIMPLICITY 🏗️")
print("=" * 60)
print()

"""
COMPOSITION = Building big things from small things

Just like LEGO:
    • Small bricks → Medium structures → Big creations
    
In code:
    • draw_line() → draw_rectangle() → draw_house() → draw_village()

🔗 FUTURE TOOL: n8n workflows call sub-workflows.
A complex automation is just simple nodes composed together!
"""

print("""
How our scene will be built:

                    ┌─────────────────────┐
                    │    draw_scene()     │ ◄── Main function
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │ draw_sun()  │     │draw_ground()│     │ draw_tree() │
    └─────────────┘     └─────────────┘     └──────┬──────┘
                                                    │
                                         ┌──────────┴──────────┐
                                         │                     │
                                         ▼                     ▼
                                  ┌─────────────┐       ┌─────────────┐
                                  │draw_trunk() │       │draw_leaves()│
                                  └─────────────┘       └─────────────┘

Each box is a function. They build on each other!
""")

# =============================================================================
# SETUP TURTLE
# =============================================================================

screen = turtle.Screen()
screen.title("🎨 Scene Builder - Functions Calling Functions")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=900, height=700)

artist = turtle.Turtle()
artist.speed(0)  # Fastest
artist.hideturtle()

# =============================================================================
# LEVEL 1: BASIC SHAPE FUNCTIONS
# =============================================================================

def draw_filled_circle(x, y, radius, color):
    """Draws a filled circle at position (x, y)"""
    artist.penup()
    artist.goto(x, y - radius)  # Start at bottom of circle
    artist.pendown()
    artist.fillcolor(color)
    artist.pencolor(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()


def draw_filled_rectangle(x, y, width, height, color):
    """Draws a filled rectangle starting at (x, y) bottom-left"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.fillcolor(color)
    artist.pencolor(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()


def draw_triangle(x, y, size, color):
    """Draws a filled triangle (roof shape)"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.fillcolor(color)
    artist.pencolor(color)
    artist.begin_fill()
    for _ in range(3):
        artist.forward(size)
        artist.left(120)
    artist.end_fill()

# =============================================================================
# LEVEL 2: OBJECT FUNCTIONS (use Level 1 functions)
# =============================================================================

def draw_sun(x, y, size):
    """
    Draws a sun with rays.
    CALLS: draw_filled_circle
    """
    # Main sun body
    draw_filled_circle(x, y, size, "yellow")
    
    # Draw rays
    artist.pencolor("orange")
    artist.pensize(3)
    
    for angle in range(0, 360, 45):
        artist.penup()
        artist.goto(x, y)
        artist.setheading(angle)
        artist.forward(size)
        artist.pendown()
        artist.forward(size * 0.5)
    
    artist.pensize(1)


def draw_cloud(x, y, size):
    """
    Draws a fluffy cloud.
    CALLS: draw_filled_circle (multiple times!)
    """
    # A cloud is just overlapping circles
    draw_filled_circle(x, y, size, "white")
    draw_filled_circle(x - size * 0.8, y - size * 0.3, size * 0.7, "white")
    draw_filled_circle(x + size * 0.8, y - size * 0.3, size * 0.7, "white")
    draw_filled_circle(x - size * 0.4, y + size * 0.4, size * 0.6, "white")
    draw_filled_circle(x + size * 0.4, y + size * 0.4, size * 0.6, "white")


def draw_tree(x, y, trunk_height, leaf_radius):
    """
    Draws a tree with trunk and leaves.
    CALLS: draw_filled_rectangle (trunk), draw_filled_circle (leaves)
    """
    trunk_width = trunk_height * 0.2
    
    # Draw trunk (calls Level 1 function)
    draw_filled_rectangle(x - trunk_width/2, y, trunk_width, trunk_height, "#8B4513")
    
    # Draw leaves (calls Level 1 function)
    draw_filled_circle(x, y + trunk_height, leaf_radius, "#228B22")
    draw_filled_circle(x - leaf_radius * 0.6, y + trunk_height - leaf_radius * 0.3, 
                       leaf_radius * 0.8, "#32CD32")
    draw_filled_circle(x + leaf_radius * 0.6, y + trunk_height - leaf_radius * 0.3, 
                       leaf_radius * 0.8, "#32CD32")


def draw_house(x, y, width, height):
    """
    Draws a house with walls, roof, door, window.
    CALLS: draw_filled_rectangle, draw_triangle
    """
    # Main building (walls)
    draw_filled_rectangle(x, y, width, height, "#DEB887")
    
    # Roof
    artist.penup()
    roof_start_x = x - width * 0.1
    roof_start_y = y + height
    artist.goto(roof_start_x, roof_start_y)
    
    # Manual triangle for roof (angled)
    artist.fillcolor("#8B0000")
    artist.pencolor("#8B0000")
    artist.begin_fill()
    artist.goto(x + width * 1.1, roof_start_y)
    artist.goto(x + width/2, roof_start_y + height * 0.6)
    artist.goto(roof_start_x, roof_start_y)
    artist.end_fill()
    
    # Door
    door_width = width * 0.25
    door_height = height * 0.5
    door_x = x + width/2 - door_width/2
    draw_filled_rectangle(door_x, y, door_width, door_height, "#654321")
    
    # Window
    window_size = width * 0.2
    window_x = x + width * 0.15
    window_y = y + height * 0.5
    draw_filled_rectangle(window_x, window_y, window_size, window_size, "#87CEEB")
    
    # Window 2
    window_x2 = x + width * 0.65
    draw_filled_rectangle(window_x2, window_y, window_size, window_size, "#87CEEB")


def draw_ground():
    """
    Draws the grass ground.
    CALLS: draw_filled_rectangle
    """
    ground_color = "#228B22"  # Forest green
    draw_filled_rectangle(-450, -350, 900, 150, ground_color)


def draw_flowers(x, y):
    """
    Draws a simple flower.
    CALLS: draw_filled_circle
    """
    # Petals
    colors = ["red", "pink", "yellow", "orange", "purple"]
    petal_color = random.choice(colors)
    
    for angle in range(0, 360, 72):
        petal_x = x + 8 * turtle.math.cos(turtle.math.radians(angle))
        petal_y = y + 8 * turtle.math.sin(turtle.math.radians(angle))
        draw_filled_circle(petal_x, petal_y, 5, petal_color)
    
    # Center
    draw_filled_circle(x, y, 4, "yellow")

# =============================================================================
# LEVEL 3: SCENE FUNCTION (uses Level 2 functions)
# =============================================================================

def draw_scene():
    """
    Draws a complete scene.
    CALLS: draw_ground, draw_sun, draw_cloud, draw_house, draw_tree, draw_flowers
    """
    print("🎨 Building the scene...")
    print()
    
    # 1. Ground (foundation)
    print("  Drawing ground...")
    draw_ground()
    
    # 2. Sun
    print("  Drawing sun...")
    draw_sun(300, 250, 40)
    
    # 3. Clouds
    print("  Drawing clouds...")
    draw_cloud(-250, 250, 30)
    draw_cloud(0, 280, 35)
    draw_cloud(150, 230, 25)
    
    # 4. House
    print("  Drawing house...")
    draw_house(-100, -200, 150, 120)
    
    # 5. Trees
    print("  Drawing trees...")
    draw_tree(-350, -200, 100, 50)
    draw_tree(200, -200, 80, 40)
    draw_tree(320, -200, 120, 60)
    
    # 6. Flowers
    print("  Drawing flowers...")
    for _ in range(10):
        fx = random.randint(-400, 400)
        fy = random.randint(-330, -220)
        draw_flowers(fx, fy)
    
    # 7. Title
    artist.penup()
    artist.goto(0, 310)
    artist.pencolor("navy")
    artist.write("🏡 My Scene - Built with Composed Functions!", 
                 align="center", font=("Arial", 16, "bold"))
    
    print()
    print("✅ Scene complete!")

# =============================================================================
# BUILD THE SCENE!
# =============================================================================

draw_scene()  # This one call triggers everything!

print()
print("=" * 60)
print("       🏗️ FUNCTION CALL HIERARCHY 🏗️")
print("=" * 60)
print()

print("""
When you called draw_scene(), here's what happened:

draw_scene()
    ├── draw_ground()
    │       └── draw_filled_rectangle()
    ├── draw_sun()
    │       └── draw_filled_circle()
    ├── draw_cloud() [×3]
    │       └── draw_filled_circle() [×5 each]
    ├── draw_house()
    │       ├── draw_filled_rectangle() [×2]
    │       └── draw_triangle()
    ├── draw_tree() [×3]
    │       ├── draw_filled_rectangle()
    │       └── draw_filled_circle() [×3 each]
    └── draw_flowers() [×10]
            └── draw_filled_circle() [×6 each]

One function call created ~100+ shapes!
That's the power of composition!
""")

# 🔗 FUTURE TOOL: n8n workflows work EXACTLY like this.
# Your main workflow calls sub-workflows, which call actions.
# A complex automation = simple pieces composed together.

print("Click the turtle window to close.")
screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A BIRD FUNCTION
    def draw_bird(x, y, size):
        # Draw a simple V-shape bird
        # Hint: Just two lines at an angle
    
    Call it multiple times in draw_scene() to add birds to the sky!

Challenge 2: ADD A FENCE
    def draw_fence(x, y, posts, post_width, post_height):
        # Draw multiple fence posts in a row
        # Hint: Use a for loop and draw_filled_rectangle()
    
    Add a fence in front of the house!

Challenge 3: CREATE draw_village()
    def draw_village():
        # Call draw_house() multiple times at different positions
        # Call draw_tree() between houses
        # This function calls draw_scene-level functions!

Challenge 4: ADD FUNCTION PARAMETERS
    Modify draw_scene() to accept parameters:
    def draw_scene(num_clouds=3, num_trees=3, num_flowers=10):
        # Use these parameters to control how many of each to draw
    
    Now you can create different scenes:
    draw_scene(num_clouds=5, num_trees=1, num_flowers=20)

Challenge 5: TRACE THE CALLS
    If draw_cloud() draws 5 circles, and draw_scene() draws 3 clouds,
    how many times is draw_filled_circle() called just for clouds?
    
    Answer: 3 clouds × 5 circles = 15 calls!
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
COMPOSITION PATTERN:
    def complex_task():
        simple_task_1()
        simple_task_2()
        simple_task_3()
    
    # Calling complex_task() runs all three simple tasks

BENEFITS:
    1. MODULARITY: Change one piece without affecting others
    2. REUSABILITY: Use the same function in multiple places
    3. TESTABILITY: Test each function independently
    4. READABILITY: High-level code reads like English

CALL STACK:
    When function A calls function B:
    1. A pauses
    2. B runs completely
    3. A continues from where it paused
    
    This can go many levels deep!

REAL-WORLD CONNECTION:
    This is how ALL software is built:
    - Web pages call components that call elements
    - Games call scenes that call objects that call sprites
    - Apps call screens that call widgets that call renderers
    
    And in n8n: Workflows call sub-workflows that call nodes!
"""
