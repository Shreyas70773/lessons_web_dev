"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 9: Lists & Indexing - IPL Top Scorers!
===============================================================================

In this session, you'll learn:
    ✅ Creating lists to store multiple values
    ✅ Indexing - accessing items by position
    ✅ Negative indexing - counting from the end
    ✅ Slicing - getting a portion of a list
    ✅ len() - counting items in a list

===============================================================================
"""

# =============================================================================
# WHAT IS A LIST?
# =============================================================================

print("=" * 60)
print("       📋 UNDERSTANDING LISTS 📋")
print("=" * 60)
print()

"""
A LIST is a collection of items stored in order.
Think of it like:
    - A playlist of songs
    - A team roster
    - A shopping list
    - High scores in a game

In Python, we use square brackets [] to create a list.
"""

# Example: IPL Top Scorers (runs in a tournament)
ipl_scores = [973, 732, 689, 615, 600, 585, 571, 546, 500, 488]

print("IPL Tournament Top 10 Scores:")
print(ipl_scores)
print()

# Each item has a position (INDEX), starting from 0!
# 
# 🔗 FUTURE TOOL: A list is like a single COLUMN in a database table.
# SQL's LIMIT and OFFSET do what slicing does here!

# =============================================================================
# VISUAL DIAGRAM: HOW INDEXING WORKS
# =============================================================================

print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                         LIST INDEXING DIAGRAM                         ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║   ipl_scores = [973, 732, 689, 615, 600, 585, 571, 546, 500, 488]    ║
║                                                                       ║
║   POSITIVE INDEX (count from start):                                  ║
║                  [ 0    1    2    3    4    5    6    7    8    9 ]   ║
║                    │    │    │    │    │    │    │    │    │    │    ║
║                   973  732  689  615  600  585  571  546  500  488   ║
║                    │    │    │    │    │    │    │    │    │    │    ║
║   NEGATIVE INDEX (count from end):                                    ║
║                 [-10   -9   -8   -7   -6   -5   -4   -3   -2   -1 ]   ║
║                                                                       ║
║   • First item: index 0 (or -10)                                      ║
║   • Last item:  index 9 (or -1)                                       ║
║   • Python counts from 0, not 1!                                      ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
""")

# =============================================================================
# ACCESSING LIST ITEMS (INDEXING)
# =============================================================================

print("=" * 60)
print("       🎯 ACCESSING ITEMS BY INDEX 🎯")
print("=" * 60)
print()

# Player names to match the scores
players = ["Faf du Plessis", "KL Rahul", "Quinton de Kock", 
           "Shikhar Dhawan", "David Warner", "Sanju Samson",
           "Shubman Gill", "Ruturaj Gaikwad", "Jos Buttler", "Devon Conway"]

# Get specific items using [index]
print("Using positive indices:")
print(f"ipl_scores[0] = {ipl_scores[0]}  (1st place: {players[0]})")
print(f"ipl_scores[1] = {ipl_scores[1]}  (2nd place: {players[1]})")
print(f"ipl_scores[2] = {ipl_scores[2]}  (3rd place: {players[2]})")
print()

# Negative indexing (counting from the end)
print("Using negative indices:")
print(f"ipl_scores[-1] = {ipl_scores[-1]}  (Last place: {players[-1]})")
print(f"ipl_scores[-2] = {ipl_scores[-2]}  (2nd last: {players[-2]})")
print(f"ipl_scores[-3] = {ipl_scores[-3]}  (3rd last: {players[-3]})")
print()

# =============================================================================
# SLICING - GETTING A PORTION OF THE LIST
# =============================================================================

print("=" * 60)
print("       ✂️ SLICING - GETTING PORTIONS ✂️")
print("=" * 60)
print()

"""
SLICING SYNTAX: list[start:stop]
    - start: index to begin (included)
    - stop: index to end (NOT included)
    
Examples:
    list[0:3]  → items at index 0, 1, 2 (not 3!)
    list[:3]   → same as [0:3] (start from beginning)
    list[3:]   → from index 3 to the end
    list[:]    → entire list (copy)
"""

# Get top 3 scorers
top_3 = ipl_scores[0:3]
print(f"Top 3 (ipl_scores[0:3]): {top_3}")

# Alternative: [:3] means start from beginning
top_3_short = ipl_scores[:3]
print(f"Top 3 (ipl_scores[:3]):  {top_3_short}")

# Get bottom 3 scorers
bottom_3 = ipl_scores[-3:]
print(f"Bottom 3 (ipl_scores[-3:]): {bottom_3}")

# Get middle players (positions 4-6, indices 3-5)
middle_3 = ipl_scores[3:6]
print(f"Middle (ipl_scores[3:6]): {middle_3}")

# Get the middle player specifically
middle_index = len(ipl_scores) // 2  # // is integer division
middle_player = players[middle_index]
middle_score = ipl_scores[middle_index]
print(f"The middle player is {middle_player} with {middle_score} runs (index {middle_index})")

print()

# =============================================================================
# THE len() FUNCTION
# =============================================================================

print("=" * 60)
print("       📏 len() - COUNTING ITEMS 📏")
print("=" * 60)
print()

num_players = len(ipl_scores)
print(f"len(ipl_scores) = {num_players}")
print(f"There are {num_players} players in our top scorers list!")
print()

# Important relationship: last index = len() - 1
print("Remember: the last valid index = len(list) - 1")
print(f"With {num_players} items, valid indices are 0 to {num_players - 1}")
print()

# =============================================================================
# PUTTING IT ALL TOGETHER: TOP 3, BOTTOM 3, MIDDLE
# =============================================================================

print("=" * 60)
print("       🏆 IPL SCOREBOARD ANALYSIS 🏆")
print("=" * 60)
print()

print("📊 TOP 3 SCORERS:")
print("-" * 40)
for i in range(3):
    print(f"  {i+1}. {players[i]:<20} {ipl_scores[i]} runs")

print()
print("📉 BOTTOM 3 SCORERS (of top 10):")
print("-" * 40)
for i in range(-3, 0):  # -3, -2, -1
    position = len(players) + i + 1  # Convert negative to position
    print(f"  {position}. {players[i]:<20} {ipl_scores[i]} runs")

print()
print(f"🎯 MIDDLE SCORER: {players[middle_index]} with {ipl_scores[middle_index]} runs")

print()

# =============================================================================
# STATISTICS
# =============================================================================

print("=" * 60)
print("       📈 QUICK STATISTICS 📈")
print("=" * 60)
print()

highest = max(ipl_scores)
lowest = min(ipl_scores)
total = sum(ipl_scores)
average = total / len(ipl_scores)

print(f"Highest score: {highest} ({players[ipl_scores.index(highest)]})")
print(f"Lowest score:  {lowest} ({players[ipl_scores.index(lowest)]})")
print(f"Total runs:    {total}")
print(f"Average:       {average:.1f}")

print()

# 🧠 LOGIC SEED: When we do ipl_scores.index(highest), we're SEARCHING
# the list to find where that value is. This is a fundamental algorithm!
# Databases do this same search operation millions of times per second.


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: FIND THE 5TH PLAYER
    - Use indexing to get the 5th player's name and score
    - Remember: 5th position = index 4!
    - Print: "5th place: [name] with [score] runs"

Challenge 2: REVERSE THE LIST
    - Create a reversed version using slicing: ipl_scores[::-1]
    - The ::-1 means "go backwards with step -1"
    - Print the bottom-to-top ranking!

Challenge 3: EVERY OTHER PLAYER
    - Get every 2nd player using: ipl_scores[::2]
    - This is "start to end, stepping by 2"
    - What indices does this give? (0, 2, 4, 6, 8)

Challenge 4: INDEX ERROR
    - What happens if you try: ipl_scores[100]?
    - You get "IndexError: list index out of range"
    - This is Python telling you that index doesn't exist!

Challenge 5: MODIFY THE LIST
    - Lists are MUTABLE (can be changed)
    - Try: ipl_scores[0] = 1000
    - Now print ipl_scores - the first value changed!

Challenge 6: CREATE YOUR OWN LIST
    - Create a list of your 5 favorite cricketers
    - Print their names at index 0, 2, and 4
    - Use negative indexing to print the last name
"""

# =============================================================================
# LIST INDEXING REFERENCE
# =============================================================================
"""
CREATING LISTS:
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "two", 3.0, True]
    nested = [[1, 2], [3, 4]]

INDEXING:
    list[0]     First item
    list[1]     Second item
    list[-1]    Last item
    list[-2]    Second to last

SLICING:
    list[a:b]   Items from index a to b-1
    list[:b]    Items from start to b-1
    list[a:]    Items from a to end
    list[:]     Copy of entire list
    list[::2]   Every 2nd item
    list[::-1]  Reversed list

USEFUL FUNCTIONS:
    len(list)   Number of items
    max(list)   Highest value (for numbers)
    min(list)   Lowest value
    sum(list)   Total of all items
    list.index(value)  Find index of a value

SQL CONNECTION:
    Python: ipl_scores[:5]           
    SQL:    SELECT * FROM scores LIMIT 5
    
    Python: ipl_scores[3:]           
    SQL:    SELECT * FROM scores OFFSET 3
"""
