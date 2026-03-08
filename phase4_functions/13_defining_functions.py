"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 13: Defining Functions - Stop Repeating Yourself!
===============================================================================

In this session, you'll learn:
    ✅ What functions are and why they're essential
    ✅ How to define functions with def
    ✅ How to call (use) functions
    ✅ The DRY principle: Don't Repeat Yourself!

===============================================================================
"""

import turtle

# =============================================================================
# THE PROBLEM: REPEATING CODE
# =============================================================================

print("=" * 60)
print("       ❌ THE PROBLEM: COPY-PASTE CODE ❌")
print("=" * 60)
print()

# Let's say we want to draw 3 squares at different positions
# WITHOUT functions, we'd have to copy-paste the code:

print("""
BEFORE FUNCTIONS (messy, repetitive code):

# Draw square 1
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)
    
# Move to new position
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

# Draw square 2 (same code again!)
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)

# Move again
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

# Draw square 3 (same code AGAIN!)
for _ in range(4):
    turtle.forward(50)
    turtle.right(90)
    
Notice how the same 4 lines appear THREE times?
That's 12 lines that could be just 1!
""")

# =============================================================================
# THE SOLUTION: FUNCTIONS!
# =============================================================================

print("=" * 60)
print("       ✅ THE SOLUTION: FUNCTIONS! ✅")
print("=" * 60)
print()

"""
A FUNCTION packages code into a reusable block.

You DEFINE it once, then CALL it whenever you need it.

def function_name():
    # Code goes here
    # This code runs when you call the function

🔗 FUTURE TOOL: A function = an n8n sub-workflow!
You build it once, then trigger it many times from different places.
"""

# =============================================================================
# DEFINING YOUR FIRST FUNCTION
# =============================================================================

print("Defining a simple function:")
print()

# DEFINING a function (creating it)
def say_hello():
    """This function prints a greeting"""
    print("🏏 Hello, Cricket Fan!")
    print("Welcome to Python Power User Course!")
    print("-" * 40)

# The function is now defined, but it hasn't run yet!
print("Function 'say_hello' is defined.")
print("Now let's CALL it:")
print()

# CALLING a function (using it)
say_hello()

print()
print("Let's call it again:")
say_hello()

print()
print("And again:")
say_hello()

print()
print("See? Three greetings, but we only wrote the code ONCE!")
print()

# =============================================================================
# VISUAL: BEFORE vs AFTER FUNCTIONS
# =============================================================================

print("=" * 60)
print("       📊 BEFORE vs AFTER COMPARISON 📊")
print("=" * 60)
print()

print("""
╔════════════════════════════════════════════════════════════════╗
║                    ❌ WITHOUT FUNCTIONS                        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║   # Print player 1 stats                                       ║
║   print("=" * 40)                                              ║
║   print("Player: Virat Kohli")                                 ║
║   print("Team: RCB")                                           ║
║   print("Average: 52.3")                                       ║
║   print("=" * 40)                                              ║
║                                                                ║
║   # Print player 2 stats (same code!)                          ║
║   print("=" * 40)                                              ║
║   print("Player: Rohit Sharma")                                ║
║   print("Team: MI")                                            ║
║   print("Average: 45.2")                                       ║
║   print("=" * 40)                                              ║
║                                                                ║
║   # Print player 3 stats (same code AGAIN!)                    ║
║   print("=" * 40)                                              ║
║   print("Player: MS Dhoni")                                    ║
║   print("Team: CSK")                                           ║
║   print("Average: 38.7")                                       ║
║   print("=" * 40)                                              ║
║                                                                ║
║   25+ lines of repetitive code!                                ║
╚════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════╗
║                    ✅ WITH FUNCTIONS                           ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║   def print_player(name, team, average):                       ║
║       print("=" * 40)                                          ║
║       print(f"Player: {name}")                                 ║
║       print(f"Team: {team}")                                   ║
║       print(f"Average: {average}")                             ║
║       print("=" * 40)                                          ║
║                                                                ║
║   # Use the function - 3 simple calls!                         ║
║   print_player("Virat Kohli", "RCB", 52.3)                     ║
║   print_player("Rohit Sharma", "MI", 45.2)                     ║
║   print_player("MS Dhoni", "CSK", 38.7)                        ║
║                                                                ║
║   9 lines total! Clean and reusable!                           ║
╚════════════════════════════════════════════════════════════════╝
""")

# =============================================================================
# LIVE DEMO: TURTLE WITHOUT FUNCTIONS
# =============================================================================

# Setup turtle
screen = turtle.Screen()
screen.title("🔷 Functions Demo - Before & After")
screen.bgcolor("navy")
screen.setup(width=800, height=600)

artist = turtle.Turtle()
artist.speed(3)
artist.pensize(2)

# Draw label
artist.penup()
artist.goto(0, 250)
artist.pencolor("white")
artist.write("WITHOUT FUNCTIONS (left) vs WITH FUNCTIONS (right)", 
             align="center", font=("Arial", 14, "bold"))

# =============================================================================
# LEFT SIDE: Without Functions (copied code)
# =============================================================================

artist.penup()
artist.goto(-250, 150)
artist.pencolor("gray")
artist.write("❌ Copied Code", align="center", font=("Arial", 12, "normal"))

# Draw 3 squares manually (copying code 3 times)
artist.pencolor("red")

# Square 1
artist.penup()
artist.goto(-300, 100)
artist.pendown()
for _ in range(4):
    artist.forward(50)
    artist.right(90)

# Square 2 (same code again)
artist.penup()
artist.goto(-250, 100)
artist.pendown()
for _ in range(4):
    artist.forward(50)
    artist.right(90)

# Square 3 (same code again)
artist.penup()
artist.goto(-200, 100)
artist.pendown()
for _ in range(4):
    artist.forward(50)
    artist.right(90)

# =============================================================================
# RIGHT SIDE: With Functions (define once, use many times)
# =============================================================================

artist.penup()
artist.goto(200, 150)
artist.pencolor("white")
artist.write("✅ Using Function", align="center", font=("Arial", 12, "normal"))

# DEFINE the function
def draw_square(x, y, size, color):
    """Draws a square at position (x, y) with given size and color"""
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.pencolor(color)
    
    for _ in range(4):
        artist.forward(size)
        artist.right(90)

# CALL the function 3 times!
draw_square(100, 100, 50, "lime")
draw_square(160, 100, 50, "cyan")
draw_square(220, 100, 50, "yellow")

# Now let's show we can easily draw MORE with minimal code
draw_square(100, 30, 50, "magenta")
draw_square(160, 30, 50, "orange")
draw_square(220, 30, 50, "white")

# =============================================================================
# SHOW THE CODE COMPARISON
# =============================================================================

artist.penup()
artist.goto(-250, -50)
artist.pencolor("red")
artist.write("12+ lines of repeated code", align="center", font=("Arial", 10, "normal"))

artist.goto(200, -50)
artist.pencolor("lime")
artist.write("6 lines total (function + calls)", align="center", font=("Arial", 10, "normal"))

# Additional benefit message
artist.goto(0, -150)
artist.pencolor("gold")
artist.write("Functions: Write once, use forever!", align="center", font=("Arial", 16, "bold"))

artist.goto(0, -180)
artist.pencolor("white")
artist.write("Need to change the square code? Just update the function!", 
             align="center", font=("Arial", 11, "normal"))

artist.hideturtle()

# =============================================================================
# CONSOLE OUTPUT
# =============================================================================

print("=" * 60)
print("       🎯 KEY BENEFITS OF FUNCTIONS 🎯")
print("=" * 60)
print()

print("1. ♻️  REUSABILITY")
print("   Write code once, use it anywhere, as many times as needed.")
print()

print("2. 🔧 MAINTAINABILITY")
print("   Need to fix or improve something? Change it in ONE place!")
print()

print("3. 📖 READABILITY")
print("   draw_square(100, 100, 50, 'red') is clearer than 10 lines of code")
print()

print("4. 🧪 TESTABILITY")
print("   Test the function once, trust it everywhere")
print()

print("5. 🧠 ORGANIZATION")
print("   Break big problems into small, manageable pieces")
print()

# 🔗 FUTURE TOOL: Functions = n8n Sub-workflows = SQL Stored Procedures
# The concept of "package it up and reuse it" appears EVERYWHERE in tech!

print("Click the turtle window to close it.")
screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CREATE A GREETING FUNCTION
    def greet_player(name):
        print(f"Welcome, {name}!")
        print("Ready to play some cricket?")
    
    Then call it:
    greet_player("Virat")
    greet_player("Rohit")
    greet_player("Dhoni")

Challenge 2: CREATE A TRIANGLE FUNCTION
    def draw_triangle(x, y, size, color):
        # Move to position
        # Draw 3 sides with angle 120
        
    Call it 5 times with different positions and colors!

Challenge 3: CREATE A STAR FUNCTION
    def print_star_rating(stars):
        print("⭐" * stars)
    
    Call it: print_star_rating(5) → ⭐⭐⭐⭐⭐

Challenge 4: SPOT THE ERROR
    What's wrong with this code?
    
    def hello()     # Missing colon!
        print("Hi")
    
    Python requires a colon : after the function definition!

Challenge 5: FUNCTION NAMING
    Which function names are good? Why?
    
    a) def x():              # Bad - unclear
    b) def calculate():      # Okay - but calculate what?
    c) def calculateBattingAverage():  # Good - descriptive!
    d) def calc_batting_avg():  # Good - Python style (snake_case)
    
    Rule: Names should describe WHAT the function does!
"""

# =============================================================================
# FUNCTION REFERENCE
# =============================================================================
"""
DEFINING A FUNCTION:
    def function_name():
        # code inside the function
        # this code runs when function is called

CALLING A FUNCTION:
    function_name()

NAMING RULES:
    - Use lowercase with underscores: calculate_average
    - Start with a verb: get_score, calculate_total, print_stats
    - Be descriptive: draw_square is better than ds

THE DRY PRINCIPLE:
    DRY = Don't Repeat Yourself
    
    If you copy-paste code more than twice,
    make it a function instead!
    
🔗 FUTURE TOOL CONNECTIONS:
    Python function = n8n Sub-workflow
    Python function = SQL Stored Procedure
    Python function = API Endpoint
    
    The concept is universal!
"""
