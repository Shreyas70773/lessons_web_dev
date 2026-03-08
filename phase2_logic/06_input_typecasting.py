"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 6: Input & Type Casting - Batting Average Calculator
===============================================================================

In this session, you'll learn:
    ✅ input() - Getting text from the user
    ✅ Type casting - Converting between str, int, and float
    ✅ Why type casting matters (the bug you'll definitely encounter!)
    ✅ type() - Checking what type a value is

===============================================================================
"""

# =============================================================================
# THE BUG THAT GETS EVERYONE!
# =============================================================================

print("=" * 60)
print("       🐛 LET'S SEE A COMMON BUG FIRST! 🐛")
print("=" * 60)
print()

# When you use input(), Python ALWAYS gives you TEXT (a string)
# Even if the user types "42", Python sees it as text, not a number!

print("🔍 Watch what happens when we DON'T convert types:")
print()

# This is what input() actually returns
runs_text = "50"  # Simulating input("Enter runs: ") where user typed "50"
innings_text = "10"  # Simulating input("Enter innings: ") where user typed "10"

print(f"runs_text = '{runs_text}'")
print(f"innings_text = '{innings_text}'")
print(f"type of runs_text: {type(runs_text)}")  # <class 'str'>
print()

# Now watch the bug!
print("❌ WRONG: What happens with 'runs_text / innings_text'?")
print("   Python says: TypeError! You can't divide strings!")
print("   (We'll skip this line to avoid crashing)")
print()

# Let's show what string "addition" does (concatenation, not math!)
print("❌ ANOTHER BUG: What does runs_text + innings_text give us?")
result_wrong = runs_text + innings_text
print(f"   '{runs_text}' + '{innings_text}' = '{result_wrong}'")
print("   It JOINED the text instead of adding numbers! 5010 ≠ 60")
print()

# =============================================================================
# THE FIX: TYPE CASTING
# =============================================================================

print("=" * 60)
print("       ✅ THE FIX: TYPE CASTING! ✅")
print("=" * 60)
print()

# Convert strings to numbers using int() or float()
runs_number = int(runs_text)      # "50" → 50
innings_number = int(innings_text)  # "10" → 10

print(f"✅ int('{runs_text}') = {runs_number}")
print(f"✅ int('{innings_text}') = {innings_number}")
print(f"   type of runs_number: {type(runs_number)}")  # <class 'int'>
print()

# Now math works!
total = runs_number + innings_number
average = runs_number / innings_number

print(f"✅ {runs_number} + {innings_number} = {total} (correct!)")
print(f"✅ {runs_number} / {innings_number} = {average} (correct!)")
print()

# 🧠 LOGIC SEED: Data types are how DATABASES store information too!
# SQL has INTEGER, TEXT, REAL (float) for the exact same reason.
# You can't add a TEXT column to a NUMBER column in SQL either!

# =============================================================================
# THE THREE MAIN TYPE CONVERSIONS
# =============================================================================

print("=" * 60)
print("       📚 TYPE CONVERSION REFERENCE 📚")
print("=" * 60)
print()

# 1. str() - Convert anything to text
number = 42
text_version = str(number)
print(f"str(42)     → '{text_version}' (type: {type(text_version).__name__})")

# 2. int() - Convert to whole number
text = "100"
int_version = int(text)
print(f"int('100')  → {int_version} (type: {type(int_version).__name__})")

# NOTE: int() truncates (cuts off) decimals!
decimal = 45.99
int_decimal = int(decimal)
print(f"int(45.99)  → {int_decimal} (cuts off .99!)")

# 3. float() - Convert to decimal number
text_decimal = "52.73"
float_version = float(text_decimal)
print(f"float('52.73') → {float_version} (type: {type(float_version).__name__})")

print()

# =============================================================================
# REAL PROGRAM: CRICKET BATTING AVERAGE CALCULATOR
# =============================================================================

print("=" * 60)
print("   🏏 CRICKET BATTING AVERAGE CALCULATOR 🏏")
print("=" * 60)
print()

# Get player information
player_name = input("Enter player name: ")

# Get numeric data - MUST convert from string to number!
runs_input = input(f"Total runs scored by {player_name}: ")
runs = int(runs_input)  # Convert string to integer

innings_input = input("Innings played: ")
innings = int(innings_input)

not_outs_input = input("How many times NOT OUT: ")
not_outs = int(not_outs_input)

# Calculate batting average
# Formula: Average = Runs / (Innings - Not Outs)
# We need to handle division by zero!

dismissals = innings - not_outs

if dismissals == 0:
    print()
    print("⚠️ Cannot calculate average - player was never dismissed!")
    average = 0.0
else:
    average = runs / dismissals  # This gives us a float automatically
    
# Calculate strike rate (let's ask for balls faced)
balls_input = input("Total balls faced: ")
balls = int(balls_input)

if balls == 0:
    strike_rate = 0.0
else:
    strike_rate = (runs / balls) * 100

print()

# =============================================================================
# DISPLAY RESULTS WITH NICE FORMATTING
# =============================================================================

print("┌" + "─" * 45 + "┐")
print(f"│{'PLAYER STATISTICS':^45}│")
print("├" + "─" * 45 + "┤")
print(f"│  Player:       {player_name:<28}│")
print(f"│  Total Runs:   {runs:<28}│")
print(f"│  Innings:      {innings:<28}│")
print(f"│  Not Outs:     {not_outs:<28}│")
print(f"│  Balls Faced:  {balls:<28}│")
print("├" + "─" * 45 + "┤")
print(f"│  Batting Avg:  {average:<28.2f}│")  # .2f = 2 decimal places
print(f"│  Strike Rate:  {strike_rate:<28.2f}│")
print("└" + "─" * 45 + "┘")

print()

# =============================================================================
# PERFORMANCE VERDICT
# =============================================================================

if average >= 50:
    print("🏆 VERDICT: World-class batsman!")
elif average >= 40:
    print("⭐ VERDICT: Excellent player!")
elif average >= 30:
    print("👍 VERDICT: Good solid batsman!")
elif average >= 20:
    print("😐 VERDICT: Average player, room for improvement.")
else:
    print("📚 VERDICT: Needs more practice!")

if strike_rate >= 150:
    print("⚡ STRIKE RATE: Explosive T20 player!")
elif strike_rate >= 100:
    print("🏃 STRIKE RATE: Quick scorer!")
elif strike_rate >= 80:
    print("🎯 STRIKE RATE: Steady and reliable.")
else:
    print("🐢 STRIKE RATE: Defensive player.")

print()
print("=" * 60)

# 🔗 FUTURE TOOL: Every database column has a TYPE
# In SQL:
#   CREATE TABLE players (
#       name TEXT,           -- like Python's str
#       runs INTEGER,        -- like Python's int
#       average REAL         -- like Python's float
#   )
# Getting types wrong causes bugs in SQL too!


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: WHAT HAPPENS WITH BAD INPUT?
    - Run the program and type "abc" instead of a number
    - You'll see: ValueError: invalid literal for int()
    - This is what happens when int() gets non-numeric text!
    - Challenge: Add a try/except to handle this (preview of error handling)
    
    try:
        runs = int(runs_input)
    except ValueError:
        print("That's not a valid number!")
        runs = 0

Challenge 2: BOWLING CALCULATOR
    - Create a bowling average calculator:
        - Inputs: wickets (int), runs_conceded (int)
        - Formula: Bowling Avg = runs_conceded / wickets
        - Lower bowling average = better bowler!
    - Don't forget to handle wickets = 0!

Challenge 3: TYPE EXPERIMENT
    Run these lines and observe:
    
    print(int(3.9))      # What happens to the .9?
    print(int("3.9"))    # Does this work? Why not?
    print(float("3.9"))  # This works!
    print(int(float("3.9")))  # Two-step conversion!

Challenge 4: STRING TO INT EDGES
    Which of these will work? Predict, then test:
    
    int("42")       # ?
    int(" 42 ")     # ? (has spaces)
    int("42.0")     # ?
    int("forty-two")# ?
    
    Answers: Yes, Yes (int ignores spaces), No (has decimal), No (words)

Challenge 5: BUILD A BMI CALCULATOR
    - Get height_in_cm (int)
    - Get weight_in_kg (int)
    - Convert height to meters: height_m = height_in_cm / 100
    - Calculate BMI: weight_in_kg / (height_m ** 2)
    - Print health category based on BMI
"""

# =============================================================================
# TYPE REFERENCE CARD
# =============================================================================
"""
PYTHON DATA TYPES:

str (string)   → Text: "Hello", "42", "Virat"
int (integer)  → Whole numbers: 42, -10, 0, 1000
float          → Decimals: 3.14, 52.73, -0.5
bool           → True or False

CONVERTING BETWEEN TYPES:

str(anything)  → Text version    str(42)     → "42"
int(text)      → Integer         int("42")   → 42
float(text)    → Decimal         float("3.14") → 3.14
int(float_val) → Truncated int   int(3.99)   → 3

CHECKING TYPES:

type(value)              → Returns the type
type(42)                 → <class 'int'>
isinstance(42, int)      → True
isinstance("hi", int)    → False

COMMON ERRORS:

TypeError  → Wrong type for operation (can't add str + int)
ValueError → Right type, wrong value (int("abc") fails)
"""
