"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 10: List Methods & Sorting - Team Squad Manager!
===============================================================================

In this session, you'll learn:
    ✅ .append() - Adding items to a list
    ✅ .remove() - Removing items from a list
    ✅ .sort() - Sorting a list
    ✅ .reverse() - Reversing order
    ✅ .pop() - Remove and return last item
    ✅ max(), min(), sum() - Quick calculations

===============================================================================
"""

# =============================================================================
# MEET YOUR CRICKET SQUAD
# =============================================================================

print("=" * 60)
print("       🏏 IPL SQUAD MANAGER 🏏")
print("=" * 60)
print()

# Starting squad with player names
squad = ["Rohit Sharma", "Ishan Kishan", "Suryakumar Yadav", 
         "Tilak Varma", "Hardik Pandya"]

# Player scores in a recent match
scores = [45, 32, 78, 15, 55]

print("📋 CURRENT SQUAD:")
for i, player in enumerate(squad):
    print(f"   {i+1}. {player}")
print()

# =============================================================================
# APPEND - ADDING PLAYERS TO THE SQUAD
# =============================================================================

print("=" * 60)
print("       ➕ ADDING PLAYERS (.append) ➕")
print("=" * 60)
print()

print("Adding new players to the squad...")

# .append() adds ONE item to the END of the list
squad.append("Jasprit Bumrah")
print(f"  ✅ Added: Jasprit Bumrah")

squad.append("Arjun Tendulkar")
print(f"  ✅ Added: Arjun Tendulkar")

scores.append(0)   # Bumrah's batting score
scores.append(12)  # Arjun's score

print()
print("📋 UPDATED SQUAD:")
for i, player in enumerate(squad):
    print(f"   {i+1}. {player} - {scores[i]} runs")
print()

# 🧠 LOGIC SEED: .append() is an O(1) operation - it's FAST!
# It just adds to the end without shifting other elements.
# This efficiency matters when dealing with large datasets.

# =============================================================================
# REMOVE - DROPPING PLAYERS FROM THE SQUAD
# =============================================================================

print("=" * 60)
print("       ➖ REMOVING PLAYERS (.remove, .pop) ➖")
print("=" * 60)
print()

# .remove() removes the FIRST occurrence of a value
print("Removing Arjun Tendulkar from squad...")
arjun_index = squad.index("Arjun Tendulkar")
squad.remove("Arjun Tendulkar")
scores.pop(arjun_index)  # Remove corresponding score
print("  ✅ Arjun Tendulkar has been released")
print()

# .pop() removes and RETURNS the last item
print("Using .pop() to remove the last player...")
last_player = squad.pop()
last_score = scores.pop()
print(f"  ✅ Removed: {last_player} (had {last_score} runs)")
print()

# .pop(index) removes at specific position
print("Removing player at position 3 (index 2)...")
removed_player = squad.pop(2)
removed_score = scores.pop(2)
print(f"  ✅ Removed: {removed_player} (had {removed_score} runs)")
print()

print("📋 SQUAD AFTER REMOVALS:")
for i, player in enumerate(squad):
    print(f"   {i+1}. {player} - {scores[i]} runs")
print()

# =============================================================================
# SORTING - ARRANGING IN ORDER
# =============================================================================

print("=" * 60)
print("       📊 SORTING (.sort, sorted) 📊")
print("=" * 60)
print()

# Let's work with a scores list
match_scores = [45, 32, 78, 15, 55, 92, 18, 67]
player_names = ["Player A", "Player B", "Player C", "Player D",
                "Player E", "Player F", "Player G", "Player H"]

print("Scores before sorting:")
print(f"  {match_scores}")
print()

# 🧠 LOGIC SEED: Sorting works by COMPARING and SWAPPING elements
# The most basic sorting (Bubble Sort) compares neighbors repeatedly
# More efficient algorithms exist, but the concept is the same!

# Show conceptually how sorting works (VISUAL)
print("How sorting works (conceptually):")
print("""
  BEFORE: [45, 32, 78, 15, 55, ...]
          
  Step 1: Compare 45 and 32
          32 < 45, so swap! → [32, 45, 78, 15, 55, ...]
          
  Step 2: Compare 45 and 78
          78 > 45, no swap  → [32, 45, 78, 15, 55, ...]
          
  Step 3: Compare 78 and 15
          15 < 78, so swap! → [32, 45, 15, 78, 55, ...]
          
  ... repeat until no more swaps needed ...
  
  AFTER:  [15, 18, 32, 45, 55, 67, 78, 92]
""")

# .sort() modifies the list IN PLACE (changes the original)
demo_scores = match_scores.copy()  # Make a copy first
demo_scores.sort()
print(f"After .sort(): {demo_scores}")
print()

# sorted() returns a NEW list (original unchanged)
print("Using sorted() to keep original intact:")
original = [78, 45, 92, 32]
sorted_version = sorted(original)
print(f"  Original:    {original}")
print(f"  sorted():    {sorted_version}")
print()

# Sort in DESCENDING order (highest first)
print("Sorting in descending order (reverse=True):")
high_to_low = sorted(match_scores, reverse=True)
print(f"  Highest to lowest: {high_to_low}")
print()

# 🔗 FUTURE TOOL: Sorting = SQL's ORDER BY clause!
# SELECT * FROM scores ORDER BY runs ASC   (ascending)
# SELECT * FROM scores ORDER BY runs DESC  (descending)

# =============================================================================
# REVERSE - FLIPPING THE ORDER
# =============================================================================

print("=" * 60)
print("       🔄 REVERSING (.reverse) 🔄")
print("=" * 60)
print()

sample = [1, 2, 3, 4, 5]
print(f"Before reverse: {sample}")

sample.reverse()
print(f"After .reverse(): {sample}")
print()

# You can also use slicing for a reversed copy without modifying original
original = [10, 20, 30, 40, 50]
reversed_copy = original[::-1]
print(f"Original:        {original}")
print(f"[::-1] copy:     {reversed_copy}")
print()

# =============================================================================
# MAX, MIN, SUM - QUICK STATISTICS
# =============================================================================

print("=" * 60)
print("       📈 STATISTICS (max, min, sum) 📈")
print("=" * 60)
print()

ipl_centuries = [973, 732, 689, 615, 600, 585, 571, 546, 500, 488]

print(f"Scores: {ipl_centuries}")
print()

highest = max(ipl_centuries)
lowest = min(ipl_centuries)
total = sum(ipl_centuries)
average = sum(ipl_centuries) / len(ipl_centuries)

print(f"📊 Statistics:")
print(f"   Highest score: {highest}")
print(f"   Lowest score:  {lowest}")
print(f"   Total runs:    {total}")
print(f"   Average:       {average:.2f}")
print(f"   Count:         {len(ipl_centuries)}")

print()

# =============================================================================
# MORE USEFUL LIST METHODS
# =============================================================================

print("=" * 60)
print("       🛠️ MORE LIST METHODS 🛠️")
print("=" * 60)
print()

demo_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"demo_list = {demo_list}")
print()

# .count() - how many times a value appears
count_1 = demo_list.count(1)
count_5 = demo_list.count(5)
print(f".count(1) = {count_1}")
print(f".count(5) = {count_5}")

# .index() - find the position of a value
pos_of_9 = demo_list.index(9)
print(f".index(9) = {pos_of_9}")

# .insert() - insert at a specific position
demo_list.insert(0, 100)  # Insert 100 at position 0
print(f".insert(0, 100) → {demo_list}")

# .extend() - add multiple items at once
demo_list.extend([7, 8, 9])
print(f".extend([7, 8, 9]) → {demo_list}")

# .clear() - remove all items
copy_to_clear = [1, 2, 3]
copy_to_clear.clear()
print(f".clear() → {copy_to_clear}")

print()

# =============================================================================
# LIVE SQUAD MANAGER - INTERACTIVE
# =============================================================================

print("=" * 60)
print("       🎮 LIVE SQUAD MANAGER 🎮")
print("=" * 60)
print()

# Initialize squad
team = ["MS Dhoni", "Ravindra Jadeja", "Devon Conway", "Ruturaj Gaikwad"]
team_scores = [35, 45, 88, 92]

def show_team():
    print("\n📋 Current Team:")
    print("-" * 40)
    for i, player in enumerate(team):
        print(f"   {i+1}. {player}: {team_scores[i]} runs")
    print(f"\n   Total runs: {sum(team_scores)}")
    print(f"   Highest: {max(team_scores)} ({team[team_scores.index(max(team_scores))]})")
    print("-" * 40)

show_team()

print("""
Commands:
  'add'    - Add a player
  'remove' - Remove a player
  'sort'   - Sort by scores
  'quit'   - Exit manager
""")

# Simple interactive loop (you can run this separately to try it)
# while True:
#     command = input("Enter command: ").strip().lower()
#     
#     if command == "quit":
#         break
#     elif command == "add":
#         name = input("Player name: ")
#         score = int(input("Score: "))
#         team.append(name)
#         team_scores.append(score)
#         print(f"✅ Added {name}")
#         show_team()
#     elif command == "sort":
#         # Sort both lists by score (descending)
#         combined = list(zip(team_scores, team))
#         combined.sort(reverse=True)
#         team_scores[:] = [s for s, n in combined]
#         team[:] = [n for s, n in combined]
#         print("✅ Sorted by score (highest first)")
#         show_team()

print("\n(Uncomment the interactive loop above to try the live manager!)")
print()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: COUNT CENTURIES
    Create a list of 10 random scores.
    Count how many are >= 100 (centuries).
    Hint: Use a loop and counter, or list comprehension.

Challenge 2: SECOND HIGHEST
    Given scores = [78, 92, 45, 92, 67, 32]
    Find the SECOND highest score (not 92, but 78).
    Hint: Sort descending, then take index [1]!

Challenge 3: REMOVE ALL ZEROS
    scores = [45, 0, 32, 0, 67, 0, 12]
    Remove all zeros from the list.
    Hint: while 0 in scores: scores.remove(0)

Challenge 4: MERGE TWO TEAMS
    team1 = ["Player A", "Player B"]
    team2 = ["Player C", "Player D"]
    
    Method 1: team1.extend(team2)
    Method 2: combined = team1 + team2
    
    What's the difference? (Method 1 modifies team1, Method 2 creates new list)

Challenge 5: BUILD A SORTED LEADERBOARD
    - Create players and scores lists
    - Use zip() to pair them: combined = list(zip(scores, players))
    - Sort the combined list
    - Print a leaderboard table!

Challenge 6: IN vs NOT IN
    Test: "Virat Kohli" in squad  → True or False?
    Test: "Sachin" not in squad   → True or False?
    
    These are SEARCH operations! Essential for data handling.
"""

# =============================================================================
# LIST METHODS REFERENCE
# =============================================================================
"""
ADDING ITEMS:
    .append(item)       Add item to end
    .insert(index, item) Add item at position
    .extend(items)      Add multiple items

REMOVING ITEMS:
    .remove(value)      Remove first occurrence of value
    .pop()             Remove & return last item
    .pop(index)        Remove & return item at index
    .clear()           Remove all items

SEARCHING:
    .index(value)      Find index of value
    .count(value)      Count occurrences
    value in list      Check if exists (True/False)

ORGANIZING:
    .sort()            Sort in place (ascending)
    .sort(reverse=True) Sort descending
    .reverse()         Reverse in place
    sorted(list)       Return new sorted list

COPYING:
    .copy()            Create shallow copy
    list[:]            Create shallow copy

SQL CONNECTIONS:
    .sort()      →  ORDER BY column ASC
    .reverse()   →  ORDER BY column DESC
    .count()     →  SELECT COUNT(*) WHERE...
    max/min/sum  →  SELECT MAX/MIN/SUM(column)
"""
