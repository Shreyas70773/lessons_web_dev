"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 1: Hello, Variables!
===============================================================================

Welcome to your Python journey! In this first session, you'll learn:
    ✅ How to print messages on screen
    ✅ How to store information in variables
    ✅ How to combine text and numbers with f-strings
    ✅ How to create cool patterns with loops

Let's start with something every cricket fan will love!

===============================================================================
"""

# =============================================================================
# PART 1: YOUR FIRST PRINT STATEMENT
# =============================================================================

# The print() function displays text on your screen
# Whatever you put inside the quotes appears on screen!

print("🏏 Welcome to the Python Power User Course! 🏏")
print("Let's learn to code with cricket!")
print()  # This prints an empty line (makes output easier to read)

# =============================================================================
# PART 2: STORING INFORMATION IN VARIABLES
# =============================================================================

# Variables are like labeled boxes where you store information
# You can put numbers, text, or other data inside them

# Let's store information about a famous cricket player
player_name = "Virat Kohli"           # This is TEXT (called a "string")
team = "Royal Challengers Bangalore"  # Also text
jersey_number = 18                    # This is a WHOLE NUMBER (called an "integer")  
batting_average = 52.73               # This is a DECIMAL NUMBER (called a "float")

# 🔗 FUTURE TOOL: In databases like SQL, these variables become COLUMNS
# A database row would look like: | Virat Kohli | RCB | 18 | 52.73 |
# Each variable = one column of data!

# Let's print what's stored in our variables
print("=== Player Information ===")
print("Name:", player_name)
print("Team:", team)
print("Jersey:", jersey_number)
print("Average:", batting_average)
print()

# =============================================================================
# PART 3: F-STRINGS - THE MAGICAL TEXT COMBINER
# =============================================================================

# F-strings let you mix text and variables together easily
# Put 'f' before the quotes, then use {variable_name} to insert values

# This creates one complete sentence from multiple variables!
player_intro = f"{player_name} plays for {team} wearing jersey #{jersey_number}"
print(player_intro)

# You can even do math inside f-strings!
total_runs = 12000
matches_played = 228
print(f"Career Stats: {total_runs} runs in {matches_played} matches")
print(f"That's about {total_runs // matches_played} runs per match on average!")
print()

# =============================================================================
# PART 4: THE STAIRCASE PATTERN - YOUR FIRST LOOP!
# =============================================================================

# Let's create a cool visual pattern with the player's name
# We'll print increasing parts of the name like stairs:
# V
# Vi
# Vir
# Vira
# Virat

print("=== NAME STAIRCASE PATTERN ===")

# 🧠 LOGIC SEED: This is called "string slicing" - cutting a piece of text
# The pattern name[0:i] means "take characters from position 0 to position i"
# This same logic is used in searching and filtering data!

# range(1, 6) gives us numbers: 1, 2, 3, 4, 5 (stops before 6)
# len() tells us how many characters are in the name
name_length = len(player_name.split()[0])  # Get first name only: "Virat"
first_name = player_name.split()[0]

for i in range(1, name_length + 1):
    # Print characters from position 0 to position i
    print(first_name[0:i])

print()

# Let's do the same for another legend!
dhoni_name = "Dhoni"
print("=== DHONI STAIRCASE ===")
for i in range(1, len(dhoni_name) + 1):
    print(dhoni_name[0:i])

print()

# =============================================================================
# PART 5: MORE CRICKET PLAYER EXAMPLES
# =============================================================================

# Let's create player cards for a few more players
print("=" * 50)
print("        IPL PLAYER CARDS")
print("=" * 50)

# Player 2: MS Dhoni
player2_name = "MS Dhoni"
player2_team = "Chennai Super Kings"
player2_jersey = 7
player2_role = "Wicketkeeper-Batsman"

print(f"""
┌──────────────────────────────────┐
│  🏏 {player2_name:<25} │
│  Team: {player2_team:<22} │
│  Jersey: #{player2_jersey:<22} │
│  Role: {player2_role:<23} │
└──────────────────────────────────┘
""")

# Player 3: Rohit Sharma
player3_name = "Rohit Sharma"
player3_team = "Mumbai Indians"
player3_jersey = 45
player3_role = "Opening Batsman"

print(f"""
┌──────────────────────────────────┐
│  🏏 {player3_name:<25} │
│  Team: {player3_team:<22} │
│  Jersey: #{player3_jersey:<22} │
│  Role: {player3_role:<23} │
└──────────────────────────────────┘
""")

# 🔗 FUTURE TOOL: These player cards are exactly like database RECORDS
# In SQL, you'd query: SELECT * FROM players WHERE jersey_number = 45
# Each card = one row in the database!

# =============================================================================
# PART 6: PLAYING WITH NUMBERS
# =============================================================================

print("=== BATTING STATISTICS ===")

# Let's calculate some cricket stats
rohit_runs = 6500
rohit_matches = 250
rohit_not_outs = 25

# Batting average formula: runs / (matches - not_outs)
rohit_average = rohit_runs / (rohit_matches - rohit_not_outs)

print(f"Rohit Sharma's Statistics:")
print(f"  Total Runs: {rohit_runs}")
print(f"  Matches: {rohit_matches}")
print(f"  Not Outs: {rohit_not_outs}")
print(f"  Batting Average: {rohit_average:.2f}")  # .2f means 2 decimal places

print()

# =============================================================================
# FINAL CELEBRATION MESSAGE
# =============================================================================

print("🎉 CONGRATULATIONS! 🎉")
print("You've learned:")
print("  ✅ print() - to display text")
print("  ✅ Variables - to store information")
print("  ✅ F-strings - to combine text and variables")
print("  ✅ Loops - to create patterns")
print()
print("You're on your way to becoming a Python Power User!")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CREATE YOUR OWN PLAYER CARD
    - Change player_name to your favorite current IPL player
    - Add a new variable called 'specialty' (e.g., "Fast Bowler", "Spinner")
    - Include it in the f-string output
    - Predict: What happens if you forget the 'f' before the string?

Challenge 2: REVERSE STAIRCASE
    - The current code prints: V, Vi, Vir, Virat
    - Can you make it print the REVERSE? Virat, Vira, Vir, Vi, V
    - Hint: Try range(name_length, 0, -1) — the -1 counts backward!

Challenge 3: MATH CHALLENGE
    - Create variables for: total_sixes = 250, total_fours = 680
    - Calculate total boundary runs (sixes = 6 runs, fours = 4 runs)
    - Print: "Total runs from boundaries: X"
    - Calculate what percentage of total_runs come from boundaries
"""

# =============================================================================
# Extra: Here's the answer structure for Challenge 3 (don't peek until you try!)
# =============================================================================
# total_sixes = 250
# total_fours = 680
# boundary_runs = (total_sixes * 6) + (total_fours * 4)
# print(f"Total runs from boundaries: {boundary_runs}")
# percentage = (boundary_runs / rohit_runs) * 100
# print(f"Boundary percentage: {percentage:.1f}%")
