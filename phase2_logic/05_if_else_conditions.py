"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 5: If/Else Conditions - Cricket Match Scorer!
===============================================================================

In this session, you'll learn:
    ✅ if statements - checking if something is true
    ✅ elif - checking multiple conditions in order
    ✅ else - what happens when nothing else matches
    ✅ Comparison operators: ==, !=, <, >, <=, >=
    ✅ Making decisions based on cricket performance!

===============================================================================
"""

import turtle

# =============================================================================
# ASCII FLOWCHART: How If/Elif/Else Works
# =============================================================================
"""
                        START
                          │
                          ▼
               ┌─────────────────────┐
               │   Get runs scored   │
               └──────────┬──────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   Is runs == 0?       │──── YES ──▶ "Duck! 🦆"
              └───────────┬───────────┘
                         NO
                          │
                          ▼
              ┌───────────────────────┐
              │   Is runs < 20?       │──── YES ──▶ "Poor innings"
              └───────────┬───────────┘
                         NO
                          │
                          ▼
              ┌───────────────────────┐
              │   Is runs <= 50?      │──── YES ──▶ "Good innings"
              └───────────┬───────────┘
                         NO
                          │
                          ▼
              ┌───────────────────────┐
              │   Is runs < 100?      │──── YES ──▶ "Excellent!"
              └───────────┬───────────┘
                         NO
                          │
                          ▼
              ┌───────────────────────┐
              │   Is runs == 100?     │──── YES ──▶ "CENTURY! 💯"
              └───────────┬───────────┘
                         NO
                          │
                          ▼
                 "SUPER CENTURY! 🔥"
                          │
                          ▼
                         END

🔗 FUTURE TOOL: This if/elif chain is LITERALLY the n8n IF node.
In SQL, you use the same logic in a WHERE clause to filter data:
    SELECT * FROM scores WHERE runs >= 100  -- gives you all centuries!
"""

# =============================================================================
# COMPARISON OPERATORS - YOUR DECISION-MAKING TOOLS
# =============================================================================

"""
COMPARISON OPERATORS (return True or False):

    ==    Equals (is it exactly the same?)
    !=    Not equals (is it different?)
    <     Less than
    >     Greater than
    <=    Less than or equal to
    >=    Greater than or equal to

Examples:
    50 == 50     → True
    50 == 49     → False
    100 > 50     → True
    30 < 50      → True
    50 <= 50     → True (50 equals 50)
    50 >= 100    → False

🧠 LOGIC SEED: These same operators exist in SQL!
    WHERE runs > 50    (same as Python's runs > 50)
    WHERE team = 'MI'  (same as Python's team == 'MI')
"""

# =============================================================================
# THE CRICKET SCORER PROGRAM
# =============================================================================

print("=" * 60)
print("       🏏 CRICKET PERFORMANCE RATING SYSTEM 🏏")
print("=" * 60)
print()

# Get the batsman's name
batsman_name = input("Enter batsman name: ")

# Get runs scored
runs_input = input(f"How many runs did {batsman_name} score? ")
runs = int(runs_input)

print()
print(f"📊 Analyzing {batsman_name}'s performance...")
print()

# =============================================================================
# THE IF/ELIF/ELSE CHAIN - Making Decisions
# =============================================================================

# Note: Python checks conditions from TOP to BOTTOM
# It STOPS at the first condition that is True!

if runs == 0:
    # The batsman got out without scoring
    rating = "Duck 🦆"
    color = "red"
    message = "Oh no! Out for zero. Better luck next time!"
    
elif runs < 20:
    # Scored something, but not enough
    rating = "Poor"
    color = "orange"
    message = "Needs improvement. Practice those shots!"
    
elif runs <= 50:
    # Decent contribution
    rating = "Good"
    color = "yellow"
    message = "Solid performance! Every run counts for the team."
    
elif runs < 100:
    # Great innings, just missed the century
    rating = "Excellent ⭐"
    color = "lime"
    message = "Fantastic batting! So close to a century!"
    
elif runs == 100:
    # Perfect century!
    rating = "CENTURY! 💯"
    color = "gold"
    message = "WHAT A PLAYER! A perfect hundred!"
    
else:
    # More than 100 - super century!
    rating = "SUPER CENTURY! 🔥"
    color = "cyan"
    message = "ABSOLUTELY INCREDIBLE! A century plus!"

# =============================================================================
# DISPLAY THE RESULTS
# =============================================================================

print("┌" + "─" * 50 + "┐")
print(f"│ Player: {batsman_name:<40} │")
print(f"│ Runs:   {runs:<40} │")
print(f"│ Rating: {rating:<40} │")
print("├" + "─" * 50 + "┤")
print(f"│ {message:<50} │")
print("└" + "─" * 50 + "┘")

# =============================================================================
# VISUAL FEEDBACK WITH TURTLE
# =============================================================================

# Let's draw a performance indicator!
screen = turtle.Screen()
screen.title(f"🏏 {batsman_name}'s Performance")
screen.bgcolor("navy")
screen.setup(width=600, height=400)

artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# Draw the rating display
artist.penup()
artist.goto(0, 100)
artist.pencolor("white")
artist.write(f"Player: {batsman_name}", align="center", font=("Arial", 20, "bold"))

artist.goto(0, 50)
artist.write(f"Runs: {runs}", align="center", font=("Arial", 18, "normal"))

artist.goto(0, -20)
artist.pencolor(color)
artist.write(rating, align="center", font=("Arial", 36, "bold"))

artist.goto(0, -80)
artist.pencolor("white")
artist.write(message, align="center", font=("Arial", 12, "normal"))

# Draw a colored performance bar
bar_width = min(runs * 2, 400)  # Scale the bar, max 400 pixels

artist.penup()
artist.goto(-200, -130)
artist.pendown()
artist.pencolor(color)
artist.fillcolor(color)
artist.begin_fill()
for _ in range(2):
    artist.forward(bar_width)
    artist.left(90)
    artist.forward(30)
    artist.left(90)
artist.end_fill()

# Bar labels
artist.penup()
artist.goto(-200, -180)
artist.pencolor("white")
artist.write("0", font=("Arial", 10, "normal"))
artist.goto(0, -180)
artist.write("100", font=("Arial", 10, "normal"))
artist.goto(200, -180)
artist.write("200", font=("Arial", 10, "normal"))

print()
print("✅ Visual display shown! Click the window to close.")

screen.exitonclick()


# =============================================================================
# BONUS: MULTIPLE PLAYERS
# =============================================================================

"""
Here's how you could rate multiple players:

players = [
    ("Rohit Sharma", 45),
    ("Virat Kohli", 100),
    ("MS Dhoni", 0),
    ("KL Rahul", 88),
]

for name, runs in players:
    if runs == 0:
        print(f"{name}: Duck 🦆")
    elif runs < 20:
        print(f"{name}: Poor")
    elif runs <= 50:
        print(f"{name}: Good")
    elif runs < 100:
        print(f"{name}: Excellent ⭐")
    elif runs == 100:
        print(f"{name}: CENTURY! 💯")
    else:
        print(f"{name}: SUPER CENTURY! 🔥")
"""


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A NEW RATING
    - Add a "Half Century" rating for exactly 50 runs
    - It should come BEFORE the <= 50 check
    - Give it a special message and color

Challenge 2: NEGATIVE NUMBERS
    - What happens if someone enters -10?
    - Add a check at the very top:
        if runs < 0:
            print("Invalid! Runs can't be negative.")
    - Make sure this comes BEFORE all other checks

Challenge 3: BOWLING RATING
    - Create a similar system for bowlers:
        - 0 wickets = "Unlucky"
        - 1-2 wickets = "Good"
        - 3-4 wickets = "Excellent"
        - 5+ wickets = "FIVE-FOR! 🎳"
    - Use the same if/elif/else pattern

Challenge 4: PREDICT THE OUTPUT
    What does this print?
    
    runs = 50
    if runs >= 50:
        print("A")
    elif runs == 50:
        print("B")
    else:
        print("C")
    
    Answer: Just "A"! Even though runs == 50 is also true,
    Python STOPS after the first matching condition!

Challenge 5: ORDER MATTERS
    Switch these two lines and run again:
        elif runs < 20:     (this one)
        elif runs <= 50:    (and this one)
    
    Now what happens when you enter 15?
    (It should still say "Poor" but does the order matter for 45?)
"""

# =============================================================================
# REFERENCE: If/Elif/Else Patterns
# =============================================================================
"""
BASIC PATTERN:
    if condition:
        # do this if condition is True
    else:
        # do this if condition is False

WITH MULTIPLE CONDITIONS:
    if condition1:
        # do this
    elif condition2:
        # or do this
    elif condition3:
        # or do this
    else:
        # do this if nothing above matched

NESTED CONDITIONS:
    if runs > 0:
        if runs >= 100:
            print("Century!")
        else:
            print("Not a century")
    else:
        print("Duck!")

REMEMBER:
    - elif means "else if"
    - Python checks from TOP to BOTTOM
    - Only ONE block runs (the first match)
    - else is optional (catches everything else)
"""
