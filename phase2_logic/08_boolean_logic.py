"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 8: Boolean Logic - IPL Playoff Qualifier!
===============================================================================

In this session, you'll learn:
    ✅ Boolean values: True and False
    ✅ and - Both conditions must be True
    ✅ or - At least one condition must be True  
    ✅ not - Reverses True to False (and vice versa)
    ✅ Truth tables - All possible combinations

===============================================================================
"""

# =============================================================================
# WHAT ARE BOOLEANS?
# =============================================================================

print("=" * 60)
print("       🔘 UNDERSTANDING BOOLEANS 🔘")
print("=" * 60)
print()

# Boolean means only TWO possible values: True or False
# Named after mathematician George Boole!

is_match_live = True
has_rain_delay = False

print(f"is_match_live = {is_match_live}")
print(f"has_rain_delay = {has_rain_delay}")
print()

# Comparison operators RETURN booleans
runs = 85
print(f"runs = {runs}")
print(f"runs > 50 → {runs > 50}")      # True (85 is greater than 50)
print(f"runs == 100 → {runs == 100}")  # False (85 is not 100)
print(f"runs < 100 → {runs < 100}")    # True (85 is less than 100)
print()

# =============================================================================
# THE AND OPERATOR - Both Must Be True
# =============================================================================

print("=" * 60)
print("       🔗 THE 'AND' OPERATOR 🔗")
print("=" * 60)
print()

print("AND rule: BOTH conditions must be True to get True")
print()

# IPL Example: To be a good all-rounder, a player needs BOTH:
# - Batting average >= 25 AND
# - Bowling average <= 30

batting_avg = 32
bowling_avg = 25

is_good_batsman = batting_avg >= 25
is_good_bowler = bowling_avg <= 30

print(f"Batting average: {batting_avg} (>= 25? {is_good_batsman})")
print(f"Bowling average: {bowling_avg} (<= 30? {is_good_bowler})")
print()

is_allrounder = is_good_batsman and is_good_bowler
print(f"Is all-rounder? ({is_good_batsman} AND {is_good_bowler}) → {is_allrounder}")
print()

# AND Truth Table
print("AND TRUTH TABLE:")
print("┌───────┬───────┬───────────┐")
print("│   A   │   B   │  A AND B  │")
print("├───────┼───────┼───────────┤")
print(f"│ True  │ True  │   {True and True}    │")
print(f"│ True  │ False │   {True and False}   │")
print(f"│ False │ True  │   {False and True}   │")
print(f"│ False │ False │   {False and False}   │")
print("└───────┴───────┴───────────┘")
print()

# =============================================================================
# THE OR OPERATOR - At Least One Must Be True
# =============================================================================

print("=" * 60)
print("       🔀 THE 'OR' OPERATOR 🔀")
print("=" * 60)
print()

print("OR rule: At least ONE condition must be True to get True")
print()

# IPL Example: A team can qualify if:
# - They're in top 2 OR
# - They win the eliminator

is_top_two = False
won_eliminator = True

print(f"In top 2? {is_top_two}")
print(f"Won eliminator? {won_eliminator}")
print()

qualifies = is_top_two or won_eliminator
print(f"Qualifies for final? ({is_top_two} OR {won_eliminator}) → {qualifies}")
print()

# OR Truth Table
print("OR TRUTH TABLE:")
print("┌───────┬───────┬──────────┐")
print("│   A   │   B   │  A OR B  │")
print("├───────┼───────┼──────────┤")
print(f"│ True  │ True  │   {True or True}   │")
print(f"│ True  │ False │   {True or False}   │")
print(f"│ False │ True  │   {False or True}   │")
print(f"│ False │ False │   {False or False}  │")
print("└───────┴───────┴──────────┘")
print()

# =============================================================================
# THE NOT OPERATOR - Reverses the Value
# =============================================================================

print("=" * 60)
print("       ❗ THE 'NOT' OPERATOR ❗")
print("=" * 60)
print()

print("NOT rule: Flips True to False, and False to True")
print()

is_raining = True
match_can_continue = not is_raining

print(f"Is it raining? {is_raining}")
print(f"Can match continue? (not {is_raining}) → {match_can_continue}")
print()

# NOT Truth Table
print("NOT TRUTH TABLE:")
print("┌───────┬─────────┐")
print("│   A   │  NOT A  │")
print("├───────┼─────────┤")
print(f"│ True  │  {not True}  │")
print(f"│ False │  {not False}   │")
print("└───────┴─────────┘")
print()

# =============================================================================
# COMBINING OPERATORS
# =============================================================================

print("=" * 60)
print("       🔄 COMBINING OPERATORS 🔄")
print("=" * 60)
print()

# You can combine and, or, not in complex conditions!
# Order of operations: not first, then and, then or

# Example: Player of the match criteria
# Must be: (scored 50+ OR took 3+ wickets) AND on winning team

runs_scored = 75
wickets_taken = 1
team_won = True

condition1 = runs_scored >= 50  # True (75 >= 50)
condition2 = wickets_taken >= 3  # False (1 < 3)
condition3 = team_won  # True

# (True OR False) AND True → True AND True → True
is_player_of_match = (condition1 or condition2) and condition3

print(f"Runs: {runs_scored} (>= 50? {condition1})")
print(f"Wickets: {wickets_taken} (>= 3? {condition2})")
print(f"Team won: {condition3}")
print()
print(f"({condition1} OR {condition2}) AND {condition3}")
print(f"= {condition1 or condition2} AND {condition3}")
print(f"= {is_player_of_match}")
print()

# 🔗 FUTURE TOOL: AND / OR in Python = AND / OR in SQL WHERE clauses.
# Exact same syntax in many databases!
#   SELECT * FROM players WHERE batting_avg > 40 AND team = 'MI'
#   SELECT * FROM matches WHERE venue = 'Mumbai' OR venue = 'Chennai'

# =============================================================================
# IPL PLAYOFF QUALIFIER CHECKER
# =============================================================================

print("=" * 60)
print("       🏆 IPL PLAYOFF QUALIFICATION CHECKER 🏆")
print("=" * 60)
print()

# Get team data from user
team_name = input("Enter team name: ")
wins = int(input("Number of wins: "))
losses = int(input("Number of losses: "))
nrr_input = input("Net Run Rate (e.g., 0.5 or -0.3): ")
nrr = float(nrr_input)

print()

# Calculate points (2 points per win)
points = wins * 2
total_matches = wins + losses

print(f"📊 {team_name} Statistics:")
print(f"   Record: {wins}W - {losses}L")
print(f"   Points: {points}")
print(f"   NRR: {nrr:+.3f}")  # +.3f shows + sign for positive
print()

# =============================================================================
# QUALIFICATION RULES (Complex Boolean Logic!)
# =============================================================================

"""
IPL Playoff Rules (simplified):
- Top 4 teams qualify for playoffs
- To guarantee qualification: 16+ points
- With 14 points: Need positive NRR
- With 12 points: Need NRR > 0.5
- Below 12 points: Very unlikely
"""

# Define conditions
has_16_plus = points >= 16
has_14_with_good_nrr = points == 14 and nrr > 0
has_12_with_great_nrr = points == 12 and nrr > 0.5
has_at_least_12 = points >= 12

# Check qualification
guaranteed = has_16_plus
likely = has_14_with_good_nrr
possible = has_12_with_great_nrr

# Overall qualification chance
qualifies = guaranteed or likely or possible

print("🤔 QUALIFICATION ANALYSIS:")
print()

if guaranteed:
    print("✅ GUARANTEED QUALIFICATION!")
    print(f"   16+ points ({points}) = definitely in playoffs!")
elif likely:
    print("👍 LIKELY TO QUALIFY!")
    print(f"   14 points with positive NRR ({nrr:+.3f}) = good chance!")
elif possible:
    print("🤞 POSSIBLE QUALIFICATION")
    print(f"   12 points but needs NRR > 0.5 (yours: {nrr:+.3f})")
elif has_at_least_12:
    print("😰 UNLIKELY - Needs other results to favor")
    print(f"   12+ points but NRR not favorable ({nrr:+.3f})")
else:
    print("❌ ELIMINATED")
    print(f"   Less than 12 points ({points}) = mathematically very difficult")

print()

# Show the boolean logic breakdown
print("📝 BOOLEAN BREAKDOWN:")
print(f"   points >= 16? {has_16_plus}")
print(f"   points == 14 AND nrr > 0? {has_14_with_good_nrr}")
print(f"   points == 12 AND nrr > 0.5? {has_12_with_great_nrr}")
print(f"   Overall: {has_16_plus} OR {has_14_with_good_nrr} OR {has_12_with_great_nrr}")
print(f"   Qualifies: {qualifies}")

print()
print("=" * 60)

# =============================================================================
# TRUTH TABLE GENERATOR (NESTED LOOPS!)
# =============================================================================

print()
print("🧮 GENERATING COMPLETE TRUTH TABLE:")
print()

print("┌───────┬───────┬───────────┬──────────┬──────────────────────────┐")
print("│   A   │   B   │  A AND B  │  A OR B  │  NOT A  │  NOT (A OR B)  │")
print("├───────┼───────┼───────────┼──────────┼─────────┼────────────────┤")

# 🧠 LOGIC SEED: Nested loops generate ALL combinations!
# This is fundamental to algorithms and database operations

for a in [True, False]:
    for b in [True, False]:
        and_result = a and b
        or_result = a or b
        not_a = not a
        not_or = not (a or b)
        
        # Format True/False as strings with padding
        a_str = str(a).ljust(5)
        b_str = str(b).ljust(5)
        and_str = str(and_result).ljust(5)
        or_str = str(or_result).ljust(5)
        not_a_str = str(not_a).ljust(5)
        not_or_str = str(not_or).ljust(5)
        
        print(f"│ {a_str} │ {b_str} │   {and_str}   │  {or_str}  │  {not_a_str}  │     {not_or_str}      │")

print("└───────┴───────┴───────────┴──────────┴─────────┴────────────────┘")
print()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: DE MORGAN'S LAWS
    There are famous rules in logic called De Morgan's Laws:
    - not (A and B) = (not A) or (not B)
    - not (A or B) = (not A) and (not B)
    
    Test this! For all combinations of A and B, verify:
        not (A and B) equals (not A) or (not B)
    They should ALWAYS be the same!

Challenge 2: XOR (Exclusive OR)
    XOR means "one or the other, but NOT BOTH"
    In Python: (A or B) and not (A and B)
    
    Create a truth table for XOR. When is it True?
    (Answer: only when A and B are DIFFERENT)

Challenge 3: MORE QUALIFICATION RULES
    Add these rules:
    - If team has 10+ points AND NRR > 1.0, they might still qualify
    - If team has exactly 14 points but NRR < -0.5, qualification is risky
    
    Add more elif branches to handle these cases!

Challenge 4: THREE CONDITIONS
    With 3 conditions A, B, C, how many rows in the truth table?
    (Hint: 2 × 2 × 2 = ?)
    
    Generate a truth table for: A AND B AND C
    Use THREE nested for loops!

Challenge 5: SHORT-CIRCUIT EVALUATION
    Python is "lazy" - it stops evaluating as soon as it knows the answer:
    
    False and (something)  → Python returns False without checking "something"
    True or (something)    → Python returns True without checking "something"
    
    Try this:
        False and print("This won't print")
        True or print("This won't print either")
    
    Why? Because Python already knows the answer!

Challenge 6: COMPLEX CONDITION
    Write a condition for: "Player is eligible for awards"
    Rules:
    - Must have played at least 10 matches
    - Must have either: scored 400+ runs OR taken 15+ wickets
    - Must NOT have any suspensions
    
    is_eligible = (matches >= 10) and (runs >= 400 or wickets >= 15) and (not suspended)
"""

# =============================================================================
# BOOLEAN REFERENCE
# =============================================================================
"""
OPERATORS:
    and     Both must be True
    or      At least one True
    not     Reverses the value

ORDER OF OPERATIONS:
    1. not (highest priority)
    2. and 
    3. or (lowest priority)
    
    not True and False  → (not True) and False → False and False → False
    True or False and False → True or (False and False) → True or False → True

COMPARISON OPERATORS (return booleans):
    ==   Equal to
    !=   Not equal to
    <    Less than
    >    Greater than
    <=   Less than or equal
    >=   Greater than or equal

TRUTHY AND FALSY:
    These are "falsy" (treated as False):
        False, None, 0, 0.0, "", [], {}
    
    Everything else is "truthy" (treated as True):
        True, 1, -1, "hello", [1,2,3], {a:1}
"""
