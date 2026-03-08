"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    PROJECT: Your Personal Turtle Drawing Library!
===============================================================================

🎨 WHAT THIS PROJECT DOES:
    Create a library of reusable drawing functions, then use them
    to build a beautiful space-themed scene!

🧠 CONCEPTS YOU'LL USE:
    ✅ Defining functions with parameters
    ✅ Functions calling functions
    ✅ Return values
    ✅ Building complex scenes from simple parts

===============================================================================
"""

import turtle
import random
import math

# =============================================================================
# SETUP
# =============================================================================

screen = turtle.Screen()
screen.title("🌌 Space Scene - Personal Turtle Library")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.colormode(255)

artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

print("=" * 60)
print("       🌌 SPACE SCENE CREATOR 🌌")
print("=" * 60)
print()
print("Using your personal turtle library to create a space scene!")
print()

# =============================================================================
# YOUR TURTLE LIBRARY - BASIC SHAPES
# =============================================================================

def draw_star(x, y, size, color):
    """
    Draws a 5-pointed star at position (x, y).
    
    Parameters:
        x, y: Position (center of star)
        size: Size of the star (length of each point)
        color: Color of the star (string or RGB tuple)
        
    Usage:
        draw_star(0, 0, 50, "yellow")
        draw_star(100, 100, 30, (255, 215, 0))
    """
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.fillcolor(color)
    
    # Move to starting point
    artist.penup()
    artist.goto(x, y + size)
    artist.pendown()
    artist.setheading(252)  # Point downward-right
    
    artist.begin_fill()
    for _ in range(5):
        artist.forward(size * 2)
        artist.right(144)  # 144 degrees for 5-pointed star
    artist.end_fill()


def draw_hexagon(x, y, size, color):
    """
    Draws a filled hexagon at position (x, y).
    
    Parameters:
        x, y: Position (bottom-left of first side)
        size: Length of each side
        color: Fill and line color
        
    Usage:
        draw_hexagon(0, 0, 50, "cyan")
    """
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.setheading(0)
    artist.pencolor(color)
    artist.fillcolor(color)
    
    artist.begin_fill()
    for _ in range(6):
        artist.forward(size)
        artist.left(60)  # 360/6 = 60 degrees
    artist.end_fill()


def draw_spiral(x, y, turns, color, line_width=1):
    """
    Draws a spiral pattern at position (x, y).
    
    Parameters:
        x, y: Center position of spiral
        turns: Number of complete turns
        color: Line color
        line_width: Thickness of line
        
    Usage:
        draw_spiral(0, 0, 5, "magenta", 2)
    """
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    artist.pensize(line_width)
    artist.setheading(0)
    
    # Spiral: gradually increasing forward distance
    for i in range(turns * 36):
        artist.forward(i * 0.3)
        artist.right(10)
    
    artist.pensize(1)  # Reset pen size


def draw_text(x, y, message, color="white", size=16, align="center"):
    """
    Writes text at position (x, y).
    
    Parameters:
        x, y: Position
        message: Text to display
        color: Text color
        size: Font size
        align: "left", "center", or "right"
        
    Usage:
        draw_text(0, 100, "Hello Space!", "yellow", 24)
    """
    artist.penup()
    artist.goto(x, y)
    artist.pencolor(color)
    artist.write(message, align=align, font=("Arial", size, "bold"))


def draw_circle(x, y, radius, color, filled=True):
    """
    Draws a circle at position (x, y).
    
    Parameters:
        x, y: Center position
        radius: Circle radius
        color: Line/fill color
        filled: True for filled, False for outline only
        
    Usage:
        draw_circle(0, 0, 50, "blue")
        draw_circle(0, 0, 50, "red", filled=False)
    """
    artist.penup()
    artist.goto(x, y - radius)  # Start at bottom
    artist.pendown()
    artist.pencolor(color)
    
    if filled:
        artist.fillcolor(color)
        artist.begin_fill()
        artist.circle(radius)
        artist.end_fill()
    else:
        artist.circle(radius)


def draw_ring(x, y, radius, color, thickness=3):
    """
    Draws a ring (planet ring style) at position (x, y).
    
    Parameters:
        x, y: Center position
        radius: Ring radius
        color: Ring color
        thickness: Line thickness
    """
    artist.penup()
    artist.goto(x, y - radius)
    artist.pendown()
    artist.pencolor(color)
    artist.pensize(thickness)
    artist.circle(radius)
    artist.pensize(1)

# =============================================================================
# YOUR TURTLE LIBRARY - COMPLEX OBJECTS
# =============================================================================

def draw_planet(x, y, radius, base_color, ring=False, ring_color=None):
    """
    Draws a planet with optional ring.
    CALLS: draw_circle, draw_ring
    
    Parameters:
        x, y: Position
        radius: Planet radius
        base_color: Planet color
        ring: True to add a ring (like Saturn)
        ring_color: Color of the ring
        
    Usage:
        draw_planet(0, 0, 50, "red")
        draw_planet(100, 0, 40, "orange", ring=True, ring_color="gold")
    """
    # Draw the planet body
    draw_circle(x, y, radius, base_color)
    
    # Add ring if requested
    if ring:
        if ring_color is None:
            ring_color = base_color
        # Draw tilted ellipse (approximated with stretched circle)
        draw_ring(x, y, radius * 1.5, ring_color, thickness=3)


def draw_starfield(num_stars, x_range=(-450, 450), y_range=(-350, 350)):
    """
    Draws a field of random stars.
    CALLS: draw_star (or simple dots for small stars)
    
    Parameters:
        num_stars: How many stars to draw
        x_range: (min_x, max_x) for star positions
        y_range: (min_y, max_y) for star positions
        
    Usage:
        draw_starfield(100)  # 100 random stars
    """
    star_colors = ["white", "yellow", (255, 255, 200), (200, 200, 255)]
    
    for _ in range(num_stars):
        sx = random.randint(x_range[0], x_range[1])
        sy = random.randint(y_range[0], y_range[1])
        scolor = random.choice(star_colors)
        ssize = random.choice([2, 3, 4, 5])
        
        if ssize <= 3:
            # Small dot for tiny stars
            artist.penup()
            artist.goto(sx, sy)
            artist.pendown()
            artist.dot(ssize, scolor)
        else:
            # Actual star shape for bigger stars
            draw_star(sx, sy, ssize, scolor)


def draw_shooting_star(start_x, start_y, length, angle):
    """
    Draws a shooting star streak.
    
    Parameters:
        start_x, start_y: Starting position
        length: Length of the trail
        angle: Direction angle (0 = right, 90 = up)
    """
    artist.penup()
    artist.goto(start_x, start_y)
    artist.setheading(angle)
    artist.pendown()
    
    # Fade effect - brighter at the start
    for i in range(10):
        brightness = 255 - (i * 20)
        artist.pencolor(brightness, brightness, brightness)
        artist.pensize(5 - i * 0.4)
        artist.forward(length / 10)
    
    artist.pensize(1)


def draw_galaxy_spiral(x, y, arms, size):
    """
    Draws a spiral galaxy.
    
    Parameters:
        x, y: Center position
        arms: Number of spiral arms
        size: Size of galaxy
    """
    # Draw core
    draw_circle(x, y, size * 0.1, "white")
    
    # Draw spiral arms
    for arm in range(arms):
        start_angle = (360 / arms) * arm
        artist.penup()
        artist.goto(x, y)
        artist.setheading(start_angle)
        artist.pendown()
        
        for i in range(40):
            # Spiral outward
            distance = i * (size / 40)
            angle = start_angle + i * 15
            
            px = x + distance * math.cos(math.radians(angle))
            py = y + distance * math.sin(math.radians(angle))
            
            brightness = 255 - int(i * 5)
            artist.pencolor(brightness, brightness, min(255, brightness + 50))
            artist.pensize(3 - i * 0.05)
            
            artist.penup()
            artist.goto(px, py)
            artist.pendown()
            artist.dot(3)

# =============================================================================
# THE MAIN SCENE FUNCTION
# =============================================================================

def draw_space_scene():
    """
    Draws a complete space scene using all library functions.
    
    This function demonstrates function composition - 
    building complex visuals from simple, reusable parts!
    """
    print("🌌 Creating space scene...")
    print()
    
    # 1. Draw background starfield
    print("  ⭐ Drawing starfield...")
    draw_starfield(150)
    
    # 2. Draw a distant galaxy
    print("  🌀 Drawing galaxy...")
    draw_galaxy_spiral(-300, 250, 4, 80)
    
    # 3. Draw shooting stars
    print("  💫 Drawing shooting stars...")
    draw_shooting_star(350, 300, 100, 220)
    draw_shooting_star(-200, 250, 80, 250)
    
    # 4. Draw planets
    print("  🪐 Drawing planets...")
    
    # Large red planet
    draw_planet(-200, 0, 80, "#FF6B6B")
    
    # Saturn-like planet with ring
    draw_planet(200, 50, 60, "#FFB347", ring=True, ring_color="#FFD700")
    
    # Small blue planet
    draw_planet(350, -150, 30, "#4ECDC4")
    
    # Purple planet
    draw_planet(-350, -200, 45, "#9B59B6")
    
    # 5. Draw some special stars
    print("  ✨ Drawing feature stars...")
    draw_star(0, 280, 15, "yellow")
    draw_star(-100, 200, 10, (255, 215, 0))
    draw_star(150, 180, 12, "white")
    
    # 6. Draw a spiral nebula
    print("  🌀 Drawing spiral nebula...")
    draw_spiral(100, -200, 3, "#FF69B4", line_width=2)
    
    # 7. Add title
    print("  📝 Adding title...")
    draw_text(0, 340, "🌌 MY SPACE SCENE 🌌", "white", 24)
    draw_text(0, -350, "Created with my Personal Turtle Library!", "gray", 12)
    
    print()
    print("✅ Space scene complete!")

# =============================================================================
# CREATE THE SCENE!
# =============================================================================

draw_space_scene()

print()
print("=" * 60)
print("       📚 YOUR FUNCTION LIBRARY 📚")
print("=" * 60)
print()

print("Functions you created:")
print("  📦 Basic Shapes:")
print("     • draw_star(x, y, size, color)")
print("     • draw_hexagon(x, y, size, color)")
print("     • draw_spiral(x, y, turns, color)")
print("     • draw_text(x, y, message, color, size)")
print("     • draw_circle(x, y, radius, color)")
print("     • draw_ring(x, y, radius, color)")
print()
print("  🎨 Complex Objects:")
print("     • draw_planet(x, y, radius, color, ring, ring_color)")
print("     • draw_starfield(num_stars)")
print("     • draw_shooting_star(start_x, start_y, length, angle)")
print("     • draw_galaxy_spiral(x, y, arms, size)")
print()
print("  🖼️ Scene Builder:")
print("     • draw_space_scene()")
print()
print("Click the window to close.")

screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD YOUR OWN FUNCTION
    Create a new function and add it to the library:
    
    def draw_asteroid(x, y, size, color):
        '''Draw an irregular asteroid shape'''
        # Hint: Draw a circle with some bumps or an irregular polygon
        
    Add it to the space scene!

Challenge 2: CREATE A MOON
    def draw_moon(x, y, radius, planet_x, planet_y):
        '''Draw a moon near a planet'''
        # Draw a small circle near the planet
        # Maybe add craters (smaller dark circles)?

Challenge 3: CREATE A SPACESHIP
    def draw_spaceship(x, y, size, direction):
        '''Draw a simple spaceship'''
        # Triangular body pointing in direction
        # Add flames coming out the back
        # Add windows

Challenge 4: CREATE A DIFFERENT SCENE
    def draw_underwater_scene():
        '''Use your shapes to make an underwater world'''
        # Use draw_circle for bubbles
        # Create draw_fish() function
        # Create draw_seaweed() function

Challenge 5: MAKE IT INTERACTIVE
    - Ask the user how many planets to draw
    - Ask what color they want the main planet
    - Use their input to customize the scene!

Challenge 6: CREATE A CONSTELLATION
    def draw_constellation(points, color="white"):
        '''Draw a constellation from a list of points'''
        # points = [(x1,y1), (x2,y2), (x3,y3), ...]
        # Draw stars at each point
        # Connect them with thin lines
    
    # Example constellation:
    orion = [(0,0), (20,40), (40,80), (60,40), (80,0), (40,50)]
"""

# =============================================================================
# LIBRARY DESIGN TIPS
# =============================================================================
"""
DESIGNING GOOD FUNCTIONS:

1. SINGLE PURPOSE
   Each function should do ONE thing well.
   ✅ draw_circle() - draws a circle
   ❌ draw_circle_and_square() - does too much!

2. CLEAR PARAMETERS
   Use descriptive parameter names.
   ✅ draw_star(x, y, size, color)
   ❌ draw_star(a, b, c, d)

3. SENSIBLE DEFAULTS
   Make functions easy to use with defaults.
   ✅ draw_text(x, y, msg, color="white", size=16)
   
4. GOOD DOCSTRINGS
   Explain what the function does, its parameters, and usage.
   This helps YOU remember later!

5. COMPOSABILITY
   Design functions to work well together.
   ✅ draw_planet() calls draw_circle() and draw_ring()
   
This is how professional libraries are created!
"""
