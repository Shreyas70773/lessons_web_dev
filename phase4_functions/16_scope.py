"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 16: Scope - Find and Fix the Bug!
===============================================================================

In this session, you'll learn:
    ✅ What "scope" means in programming
    ✅ Local vs global variables
    ✅ Why scope bugs are so tricky
    ✅ How to fix common scope errors

===============================================================================
"""

# =============================================================================
# WHAT IS SCOPE?
# =============================================================================

print("=" * 60)
print("       🔭 UNDERSTANDING SCOPE 🔭")
print("=" * 60)
print()

"""
SCOPE = Where a variable can be seen and used

Think of it like rooms in a house:
    • A variable created INSIDE a function is like a note in one room
    • People in OTHER rooms can't see that note
    • But a note on the HOUSE bulletin board (global) can be seen by everyone

LOCAL SCOPE:
    • Variables created INSIDE a function
    • Only exist while the function is running
    • Can't be accessed from outside the function

GLOBAL SCOPE:
    • Variables created OUTSIDE all functions
    • Can be accessed from anywhere in the code
"""

# =============================================================================
# VISUAL EXPLANATION
# =============================================================================

print("""
╔═══════════════════════════════════════════════════════════════════╗
║                         SCOPE DIAGRAM                             ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║     GLOBAL SCOPE (outside all functions)                          ║
║     ┌────────────────────────────────────────────────────────┐    ║
║     │  team_name = "Mumbai Indians"  ← Everyone can see this │    ║
║     │                                                        │    ║
║     │   ┌─────────────────────────────────┐                  │    ║
║     │   │ def calculate_score():          │ ← LOCAL SCOPE    │    ║
║     │   │     local_runs = 50  ← Only     │                  │    ║
║     │   │     # visible inside here!      │                  │    ║
║     │   │                                 │                  │    ║
║     │   │     # CAN access team_name     │                  │    ║
║     │   │     # (it's global)             │                  │    ║
║     │   └─────────────────────────────────┘                  │    ║
║     │                                                        │    ║
║     │   # Can NOT access local_runs here!                    │    ║
║     │   # It doesn't exist outside the function              │    ║
║     │                                                        │    ║
║     └────────────────────────────────────────────────────────┘    ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
""")

# =============================================================================
# THE BUGGY PROGRAM - CAN YOU SPOT THE ERRORS?
# =============================================================================

print("=" * 60)
print("       🐛 THE BUGGY SCORE TRACKER 🐛")
print("=" * 60)
print()

print("Below is a BUGGY program. Read it and try to spot the errors!")
print("The bugs are marked with ❌ BUG comments.")
print()

# ============== BUGGY VERSION ==============

"""
# ❌ BUG VERSION - DO NOT RUN AS-IS (will crash!)
# This code has scope errors. Can you find them?

def add_runs(runs_scored):
    '''Adds runs to the total'''
    # ❌ BUG: Trying to modify 'total_runs' without declaring it
    # Python thinks we're creating a NEW local variable!
    total_runs = total_runs + runs_scored
    print(f"Added {runs_scored} runs!")

def add_wicket():
    '''Adds a wicket'''
    # ❌ BUG: Same problem - can't modify global without 'global' keyword
    wickets = wickets + 1
    print("Wicket! ⚡")

def show_score():
    '''Shows current score'''
    # This works fine - we're only READING, not modifying
    print(f"Score: {total_runs}/{wickets}")

# Initialize game state
total_runs = 0
wickets = 0

# Try to use the functions
add_runs(4)     # ❌ CRASH! UnboundLocalError
add_wicket()    # ❌ CRASH! UnboundLocalError
show_score()
"""

print("The bugs are:")
print("  1. add_runs() tries to modify total_runs without 'global' keyword")
print("  2. add_wicket() tries to modify wickets without 'global' keyword")
print()

# =============================================================================
# THE FIXED PROGRAM - SOLUTION 1: Global Keyword
# =============================================================================

print("=" * 60)
print("       ✅ FIX #1: Using 'global' Keyword ✅")
print("=" * 60)
print()

# ============== FIXED VERSION 1: Global Keyword ==============

# Initialize game state (global variables)
total_runs = 0
wickets = 0

def add_runs_v1(runs_scored):
    """Adds runs to the total - FIXED with global"""
    global total_runs  # ✅ FIX: Tell Python to use the global variable
    total_runs = total_runs + runs_scored
    print(f"  Added {runs_scored} runs!")

def add_wicket_v1():
    """Adds a wicket - FIXED with global"""
    global wickets  # ✅ FIX: Tell Python to use the global variable
    wickets = wickets + 1
    print("  Wicket! ⚡")

def show_score_v1():
    """Shows current score"""
    # Reading globals is fine without the global keyword
    print(f"  Score: {total_runs}/{wickets}")

# Test the fixed version
print("Testing Fix #1 (global keyword):")
print("-" * 40)
total_runs = 0  # Reset
wickets = 0     # Reset

add_runs_v1(4)
add_runs_v1(6)
add_wicket_v1()
add_runs_v1(2)
show_score_v1()
print()

# =============================================================================
# THE BETTER FIX - SOLUTION 2: Return Values (Recommended!)
# =============================================================================

print("=" * 60)
print("       ✅ FIX #2: Using Return Values (Better!) ✅")
print("=" * 60)
print()

# ============== FIXED VERSION 2: Return Values ==============

def add_runs_v2(current_total, runs_scored):
    """Adds runs and returns new total - NO GLOBALS!"""
    new_total = current_total + runs_scored
    print(f"  Added {runs_scored} runs!")
    return new_total

def add_wicket_v2(current_wickets):
    """Adds wicket and returns new count - NO GLOBALS!"""
    new_wickets = current_wickets + 1
    print("  Wicket! ⚡")
    return new_wickets

def show_score_v2(runs, wkts):
    """Shows score - takes values as parameters"""
    print(f"  Score: {runs}/{wkts}")

# Test with return values
print("Testing Fix #2 (return values - BETTER!):")
print("-" * 40)

score = 0
wkts = 0

score = add_runs_v2(score, 4)
score = add_runs_v2(score, 6)
wkts = add_wicket_v2(wkts)
score = add_runs_v2(score, 2)
show_score_v2(score, wkts)
print()

print("Why is Fix #2 better?")
print("  • No hidden dependencies on global variables")
print("  • Functions are self-contained and testable")
print("  • Easier to understand what data flows where")
print()

# =============================================================================
# THE BEST FIX - SOLUTION 3: Using a Class/Dictionary (Preview!)
# =============================================================================

print("=" * 60)
print("       ✅ FIX #3: Using a Dictionary (Best!) ✅")
print("=" * 60)
print()

# ============== FIXED VERSION 3: Dictionary State ==============

def create_game():
    """Create a new game state"""
    return {"runs": 0, "wickets": 0, "balls": 0}

def add_runs_v3(game, runs_scored):
    """Add runs to game state"""
    game["runs"] += runs_scored
    game["balls"] += 1
    print(f"  Added {runs_scored} runs!")
    return game

def add_wicket_v3(game):
    """Add wicket to game state"""
    game["wickets"] += 1
    game["balls"] += 1
    print("  Wicket! ⚡")
    return game

def show_score_v3(game):
    """Show game score"""
    print(f"  Score: {game['runs']}/{game['wickets']} ({game['balls']} balls)")

# Test with dictionary
print("Testing Fix #3 (dictionary state - BEST!):")
print("-" * 40)

match = create_game()
match = add_runs_v3(match, 4)
match = add_runs_v3(match, 6)
match = add_wicket_v3(match)
match = add_runs_v3(match, 2)
show_score_v3(match)
print()

print("Why is Fix #3 best?")
print("  • All game data in one place")
print("  • Easy to have multiple games at once")
print("  • Functions clearly show what they need and return")
print()

# 🧠 LOGIC SEED: Scope bugs are one of the most common errors in programming!
# Understanding scope saves HOURS of debugging - in Python, n8n, SQL, everywhere!

# =============================================================================
# SCOPE RULES SUMMARY
# =============================================================================

print("=" * 60)
print("       📜 SCOPE RULES SUMMARY 📜")
print("=" * 60)
print()

print("""
RULE 1: Local variables are created when you assign inside a function
    def my_func():
        x = 10  # x is LOCAL to my_func
    
    print(x)  # ❌ ERROR! x doesn't exist here

RULE 2: You CAN read global variables from inside functions
    name = "Virat"  # Global
    
    def greet():
        print(f"Hello {name}")  # ✅ OK - reading global
    
    greet()  # Prints "Hello Virat"

RULE 3: You CANNOT modify globals without 'global' keyword
    count = 0  # Global
    
    def increment():
        count = count + 1  # ❌ ERROR! Python thinks count is local
    
    def increment_fixed():
        global count       # ✅ Tell Python we mean the global
        count = count + 1

RULE 4: Variables created in functions disappear when function ends
    def my_func():
        temporary = "I exist briefly"
        return temporary
    
    result = my_func()
    print(temporary)  # ❌ ERROR! temporary is gone
    print(result)     # ✅ OK - we saved the value
""")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: PREDICT THE OUTPUT
    x = 10
    
    def change_x():
        x = 20
        print(f"Inside: {x}")
    
    change_x()
    print(f"Outside: {x}")
    
    What prints? (Answer: Inside: 20, Outside: 10)
    The function created a LOCAL x, didn't touch the global!

Challenge 2: FIX THIS BUG
    player_score = 0
    
    def add_points(pts):
        player_score = player_score + pts  # ❌ BUG!
    
    add_points(100)
    
    Fix it using either:
    a) The global keyword
    b) Return value approach (better!)

Challenge 3: VARIABLE SHADOWING
    name = "Global Name"
    
    def show_name():
        name = "Local Name"  # This "shadows" the global
        print(name)
    
    show_name()    # What prints?
    print(name)    # What prints?

Challenge 4: THE LEAKY LOOP BUG
    # This is a scope quirk in Python!
    for i in range(5):
        pass
    
    print(i)  # What prints? (Answer: 4 - loop variable leaks out!)
    
    # In many other languages, this would be an error.
    # Python lets loop variables escape their loop.

Challenge 5: DESIGN A BETTER SCORER
    Create a cricket scorer using the dictionary approach:
    - create_innings() returns a new innings dict
    - add_delivery(innings, runs, is_wicket) updates and returns innings
    - get_run_rate(innings) calculates and returns run rate
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
SCOPE KEYWORDS:
    global x       # Use the global variable x (not create local)
    nonlocal x     # Use variable from enclosing function (advanced)

DEBUGGING SCOPE ISSUES:
    1. UnboundLocalError: local variable 'x' referenced before assignment
       → You're trying to modify a global without 'global' keyword
    
    2. NameError: name 'x' is not defined
       → Variable doesn't exist in this scope
    
    3. Variable has wrong value
       → Check if you're using local instead of global (or vice versa)

BEST PRACTICES:
    1. Minimize global variables
    2. Pass data through parameters and return values
    3. Use dictionaries or classes to group related state
    4. If you must use global, document it clearly

WHY THIS MATTERS:
    Scope bugs are sneaky because the code LOOKS correct.
    Understanding scope prevents hours of frustrating debugging!
    
    This same concept applies to:
    - JavaScript (var vs let vs const)
    - SQL (table aliases)
    - n8n (workflow variables vs node data)
"""
