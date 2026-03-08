"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 14: Parameters & Return Values
===============================================================================

In this session, you'll learn:
    ✅ Parameters - passing data INTO a function
    ✅ Default parameters - optional values with fallbacks
    ✅ Return values - getting data OUT of a function
    ✅ Using returned values in your code

===============================================================================
"""

# =============================================================================
# THE UNIVERSAL PATTERN
# =============================================================================

print("=" * 60)
print("       🔄 THE UNIVERSAL PATTERN 🔄")
print("=" * 60)
print()

"""
Every function follows this pattern:

    INPUT  →  PROCESS  →  OUTPUT
    
    • INPUT (Parameters): Data you give TO the function
    • PROCESS (Function Body): What the function DOES with the data
    • OUTPUT (Return Value): Data you get BACK from the function

🧠 LOGIC SEED: This INPUT → PROCESS → OUTPUT pattern is the structure of:
    - Every Python function
    - Every SQL query
    - Every n8n node
    - Every API endpoint
    
It's THE universal pattern in all of computing!
"""

print("The Universal Pattern:")
print()
print("    ╔════════════╗     ╔═══════════════╗     ╔════════════╗")
print("    ║   INPUT    ║ ──▶ ║   PROCESS     ║ ──▶ ║   OUTPUT   ║")
print("    ║ (params)   ║     ║ (function)    ║     ║ (return)   ║")
print("    ╚════════════╝     ╚═══════════════╝     ╚════════════╝")
print()
print("    runs=100       calculate_strike      result=125.0")
print("    balls=80       _rate(runs, balls)    ")
print()

# =============================================================================
# PARAMETERS - PASSING DATA IN
# =============================================================================

print("=" * 60)
print("       📥 PARAMETERS - INPUT TO FUNCTIONS 📥")
print("=" * 60)
print()

# Function WITHOUT parameters (limited usefulness)
def greet_generic():
    print("Hello, Player!")

# Function WITH parameters (flexible and reusable)
def greet_player(player_name):
    print(f"Hello, {player_name}!")

# Function with MULTIPLE parameters
def greet_full(player_name, team, role):
    print(f"Hello, {player_name}!")
    print(f"Team: {team}")
    print(f"Role: {role}")

# Calling these functions
print("Function without parameters:")
greet_generic()
greet_generic()  # Always says the same thing

print()
print("Function WITH parameter:")
greet_player("Virat Kohli")
greet_player("Rohit Sharma")
greet_player("MS Dhoni")

print()
print("Function with MULTIPLE parameters:")
greet_full("Jasprit Bumrah", "Mumbai Indians", "Fast Bowler")

print()

# =============================================================================
# DEFAULT PARAMETERS - OPTIONAL VALUES
# =============================================================================

print("=" * 60)
print("       🔧 DEFAULT PARAMETERS - OPTIONAL VALUES 🔧")
print("=" * 60)
print()

# Default parameters have a fallback value if not provided
def create_player_card(name, team="Unknown Team", jersey=0):
    """Creates a player card with optional team and jersey"""
    print(f"┌{'─' * 30}┐")
    print(f"│ {name:<28} │")
    print(f"│ Team: {team:<22} │")
    print(f"│ Jersey: #{jersey:<21} │")
    print(f"└{'─' * 30}┘")

# Call with all parameters
print("With all parameters:")
create_player_card("Virat Kohli", "RCB", 18)

# Call with some parameters (jersey uses default)
print("\nWith team only (jersey defaults to 0):")
create_player_card("New Player", "CSK")

# Call with just name (team and jersey use defaults)
print("\nWith just name (team and jersey use defaults):")
create_player_card("Mystery Player")

print()

# =============================================================================
# RETURN VALUES - GETTING DATA BACK
# =============================================================================

print("=" * 60)
print("       📤 RETURN VALUES - OUTPUT FROM FUNCTIONS 📤")
print("=" * 60)
print()

# Function that RETURNS a value
def calculate_strike_rate(runs, balls_faced):
    """
    Calculate batting strike rate.
    
    Parameters:
        runs: Total runs scored
        balls_faced: Total balls faced
        
    Returns:
        Strike rate as a float
    """
    if balls_faced == 0:
        return 0.0
    
    strike_rate = (runs / balls_faced) * 100
    return strike_rate  # This sends the value BACK to the caller

# Using the returned value
print("Calculating strike rates:")
print()

# The returned value can be stored in a variable
virat_sr = calculate_strike_rate(55, 40)
print(f"Virat: 55 runs off 40 balls → Strike Rate: {virat_sr:.2f}")

rohit_sr = calculate_strike_rate(78, 50)
print(f"Rohit: 78 runs off 50 balls → Strike Rate: {rohit_sr:.2f}")

dhoni_sr = calculate_strike_rate(25, 15)
print(f"Dhoni: 25 runs off 15 balls → Strike Rate: {dhoni_sr:.2f}")

print()

# You can use the returned value directly in expressions
print("Using return values in expressions:")
average_sr = (virat_sr + rohit_sr + dhoni_sr) / 3
print(f"Average team strike rate: {average_sr:.2f}")

print()

# =============================================================================
# MORE EXAMPLES: CRICKET STATISTICS FUNCTIONS
# =============================================================================

print("=" * 60)
print("       🏏 CRICKET STATISTICS FUNCTIONS 🏏")
print("=" * 60)
print()

def calculate_batting_average(runs, innings, not_outs):
    """
    Calculate batting average.
    Returns: Average as float, or 0 if never dismissed
    """
    dismissals = innings - not_outs
    if dismissals == 0:
        return 0.0
    return runs / dismissals


def get_performance_grade(average):
    """
    Assign a grade based on batting average.
    Returns: Grade string (A+, A, B, C, D)
    """
    if average >= 50:
        return "A+ (World Class)"
    elif average >= 40:
        return "A (Excellent)"
    elif average >= 30:
        return "B (Good)"
    elif average >= 20:
        return "C (Average)"
    else:
        return "D (Needs Improvement)"


def is_allrounder(batting_avg, bowling_avg):
    """
    Check if a player qualifies as an allrounder.
    Returns: True if allrounder, False otherwise
    """
    # Good allrounder: batting avg >= 25 AND bowling avg <= 30
    is_decent_batsman = batting_avg >= 25
    is_decent_bowler = bowling_avg <= 30
    
    return is_decent_batsman and is_decent_bowler


# Using these functions together
print("Player Analysis: Hardik Pandya")
print("-" * 40)

runs = 2400
innings = 90
not_outs = 12
bowling_avg = 28.5

# Calculate batting average
bat_avg = calculate_batting_average(runs, innings, not_outs)
print(f"Batting Average: {bat_avg:.2f}")

# Get grade
grade = get_performance_grade(bat_avg)
print(f"Grade: {grade}")

# Check allrounder status
allrounder = is_allrounder(bat_avg, bowling_avg)
print(f"Allrounder Status: {'✅ Yes!' if allrounder else '❌ No'}")

print()

# =============================================================================
# RETURN vs PRINT - IMPORTANT DIFFERENCE!
# =============================================================================

print("=" * 60)
print("       ⚠️ RETURN vs PRINT - KEY DIFFERENCE! ⚠️")
print("=" * 60)
print()

# This function PRINTS (shows on screen, but returns nothing)
def show_runs(runs):
    print(f"Runs scored: {runs}")
    # No return statement - returns None by default

# This function RETURNS (gives back a value you can use)
def double_runs(runs):
    return runs * 2  # Returns the doubled value

# Demonstrating the difference
print("Using show_runs(50):")
result1 = show_runs(50)  # Prints "Runs scored: 50"
print(f"Returned value: {result1}")  # None!
print()

print("Using double_runs(50):")
result2 = double_runs(50)  # Returns 100
print(f"Returned value: {result2}")  # 100!
print()

print("Key insight:")
print("  • print() shows on screen but doesn't give you a value")
print("  • return gives you a value you can use in your code")
print("  • Use print() for displaying, return for calculations!")

print()

# =============================================================================
# CHAINING FUNCTION CALLS
# =============================================================================

print("=" * 60)
print("       🔗 CHAINING FUNCTION CALLS 🔗")
print("=" * 60)
print()

# You can use the output of one function as input to another!
def add_bonus(runs, bonus_percent=10):
    """Add bonus percentage to runs"""
    bonus = runs * (bonus_percent / 100)
    return runs + bonus

def format_score(score):
    """Format score with commas and text"""
    return f"{score:,.0f} runs"

# Chain the functions
base_runs = 1000
final_score = format_score(add_bonus(base_runs, 15))
print(f"Base runs: {base_runs}")
print(f"With 15% bonus, formatted: {final_score}")

print()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CREATE A BOWLING AVERAGE FUNCTION
    def calculate_bowling_average(runs_conceded, wickets):
        # Return runs_conceded / wickets
        # Handle division by zero!
        
    Test: calculate_bowling_average(500, 20) → 25.0

Challenge 2: ECONOMY RATE FUNCTION
    def calculate_economy(runs_conceded, overs_bowled):
        # Economy = runs / overs
        # Return the economy rate
        
    Test: calculate_economy(36, 4) → 9.0

Challenge 3: PREDICT THE OUTPUT
    def mystery(a, b=10):
        return a * b
    
    print(mystery(5))       # What prints?
    print(mystery(5, 3))    # What prints?
    print(mystery(b=2, a=8))  # What prints? (keyword arguments!)

Challenge 4: RETURN MULTIPLE VALUES
    Python can return multiple values!
    
    def analyze_innings(runs, balls, fours, sixes):
        strike_rate = (runs / balls) * 100
        boundary_runs = (fours * 4) + (sixes * 6)
        boundary_percent = (boundary_runs / runs) * 100
        return strike_rate, boundary_runs, boundary_percent
    
    sr, br, bp = analyze_innings(75, 50, 8, 3)
    # sr = 150.0, br = 50, bp = 66.67

Challenge 5: CREATE A PLAYER SUMMARY FUNCTION
    def get_player_summary(name, runs, innings, not_outs, wickets, runs_conceded):
        # Calculate batting average
        # Calculate bowling average
        # Check if allrounder
        # Return a dictionary with all stats!
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
PARAMETERS:
    def func(required_param, optional_param="default"):
        # required_param MUST be provided
        # optional_param has a default value

RETURN VALUES:
    def func():
        return value  # Send value back to caller
    
    result = func()   # Capture the returned value

MULTIPLE RETURN VALUES:
    def func():
        return a, b, c
    
    x, y, z = func()

KEYWORD ARGUMENTS:
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}")
    
    greet("Virat")                     # Uses default greeting
    greet("Virat", "Welcome")          # Positional argument
    greet(name="Virat", greeting="Hi") # Keyword arguments
    greet(greeting="Hey", name="Virat") # Order doesn't matter with keywords!

THE UNIVERSAL PATTERN:
    INPUT (parameters) → PROCESS (function body) → OUTPUT (return value)
    
    This applies to:
    - Python functions
    - SQL queries (SELECT input → process → result rows)
    - n8n nodes (trigger → action → output)
    - API endpoints (request → process → response)
"""
