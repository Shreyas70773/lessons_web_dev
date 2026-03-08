"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 12: Loops on Lists - Filtering IPL Players!
===============================================================================

In this session, you'll learn:
    ✅ for loop to iterate through lists
    ✅ enumerate() - get index AND value
    ✅ Filtering with if inside loops
    ✅ Building new lists from old ones
    ✅ Basic list comprehension (preview!)

===============================================================================
"""

import matplotlib.pyplot as plt

# =============================================================================
# OUR DATA: IPL PLAYERS
# =============================================================================

# 15 IPL players with their stats
players = [
    {"name": "Virat Kohli", "team": "RCB", "role": "Batsman", "avg": 52.3, "matches": 240},
    {"name": "Rohit Sharma", "team": "MI", "role": "Batsman", "avg": 45.2, "matches": 250},
    {"name": "MS Dhoni", "team": "CSK", "role": "Wicketkeeper", "avg": 38.7, "matches": 230},
    {"name": "Jasprit Bumrah", "team": "MI", "role": "Bowler", "avg": 8.5, "matches": 130},
    {"name": "Hardik Pandya", "team": "MI", "role": "Allrounder", "avg": 28.9, "matches": 150},
    {"name": "Ravindra Jadeja", "team": "CSK", "role": "Allrounder", "avg": 32.1, "matches": 210},
    {"name": "KL Rahul", "team": "PBKS", "role": "Batsman", "avg": 48.9, "matches": 130},
    {"name": "Rishabh Pant", "team": "DC", "role": "Wicketkeeper", "avg": 42.8, "matches": 110},
    {"name": "Shikhar Dhawan", "team": "PBKS", "role": "Batsman", "avg": 41.5, "matches": 220},
    {"name": "Suryakumar Yadav", "team": "MI", "role": "Batsman", "avg": 44.2, "matches": 85},
    {"name": "Rashid Khan", "team": "SRH", "role": "Bowler", "avg": 15.2, "matches": 105},
    {"name": "Yuzvendra Chahal", "team": "RR", "role": "Bowler", "avg": 5.6, "matches": 160},
    {"name": "Faf du Plessis", "team": "RCB", "role": "Batsman", "avg": 42.1, "matches": 110},
    {"name": "David Warner", "team": "DC", "role": "Batsman", "avg": 44.8, "matches": 175},
    {"name": "Kane Williamson", "team": "SRH", "role": "Batsman", "avg": 38.5, "matches": 80},
]

print("=" * 60)
print("       🏏 IPL PLAYER ANALYSIS 🏏")
print("=" * 60)
print()
print(f"Total players in database: {len(players)}")
print()

# =============================================================================
# ASCII FLOWCHART: Loop + Filter
# =============================================================================
"""
                    START
                      │
                      ▼
         ┌────────────────────────┐
         │  Create empty lists:  │
         │  filtered_players = []│
         └───────────┬────────────┘
                     │
          ┌──────────▼──────────┐
FOR EACH  │  Get next player    │◄────────────────────┐
PLAYER    │  from players list  │                     │
          └──────────┬──────────┘                     │
                     │                                │
          ┌──────────▼──────────┐                     │
   IF     │ Does player match   │                     │
   CHECK  │ our filter criteria?│                     │
          └──────────┬──────────┘                     │
                     │                                │
           ┌─────────┴─────────┐                      │
           │                   │                      │
         YES                  NO                      │
           │                   │                      │
           ▼                   │                      │
    ┌──────────────┐           │                      │
    │ Add to       │           │                      │
    │ filtered_    │           │                      │
    │ players list │           │                      │
    └──────┬───────┘           │                      │
           │                   │                      │
           └─────────┬─────────┘                      │
                     │                                │
          ┌──────────▼──────────┐                     │
          │ More players left?  │─────────YES─────────┘
          └──────────┬──────────┘
                    NO
                     │
                     ▼
                   END

🔗 FUTURE TOOL: This filter loop is EXACTLY what SQL's WHERE clause does!
    SELECT * FROM players WHERE avg > 40
    This SQL query does the same filtering logic!
"""

# =============================================================================
# BASIC LOOP: Printing All Players
# =============================================================================

print("=" * 60)
print("       📋 ALL PLAYERS 📋")
print("=" * 60)
print()

print(f"{'#':<4} {'Name':<20} {'Team':<6} {'Role':<15} {'Avg':<8}")
print("-" * 55)

for i, player in enumerate(players):
    print(f"{i+1:<4} {player['name']:<20} {player['team']:<6} {player['role']:<15} {player['avg']:<8.1f}")

print()

# 🧠 LOGIC SEED: enumerate() gives you BOTH the index AND the item
# This is super useful when you need to track position!

# =============================================================================
# FILTER 1: Only Batsmen
# =============================================================================

print("=" * 60)
print("       🏏 FILTER: BATSMEN ONLY 🏏")
print("=" * 60)
print()

batsmen = []

for player in players:
    if player["role"] == "Batsman":
        batsmen.append(player)

print(f"Found {len(batsmen)} batsmen:")
for batsman in batsmen:
    print(f"  • {batsman['name']} ({batsman['team']}) - Avg: {batsman['avg']}")

print()

# =============================================================================
# FILTER 2: Players with Average > 40
# =============================================================================

print("=" * 60)
print("       ⭐ FILTER: AVERAGE > 40 ⭐")
print("=" * 60)
print()

high_average = []

for player in players:
    if player["avg"] > 40:
        high_average.append(player)

print(f"Found {len(high_average)} players with avg > 40:")
for player in high_average:
    print(f"  • {player['name']}: {player['avg']}")

print()

# 🔗 FUTURE TOOL: 
# Python: if player["avg"] > 40: high_average.append(player)
# SQL:    SELECT * FROM players WHERE avg > 40
# These do THE EXACT SAME THING!

# =============================================================================
# FILTER 3: Star Players (40+ average AND 150+ matches)
# =============================================================================

print("=" * 60)
print("       🌟 FILTER: STAR PLAYERS 🌟")
print("=" * 60)
print("Criteria: Average > 40 AND Matches > 150")
print()

star_players = []

for player in players:
    # Using AND - both conditions must be true
    if player["avg"] > 40 and player["matches"] > 150:
        star_players.append(player)

print(f"Found {len(star_players)} star players:")
for star in star_players:
    print(f"  🌟 {star['name']}: avg {star['avg']}, {star['matches']} matches")

print()

# =============================================================================
# FILTER 4: Players by Team
# =============================================================================

print("=" * 60)
print("       🏆 FILTER: MUMBAI INDIANS SQUAD 🏆")
print("=" * 60)
print()

mi_squad = []

for player in players:
    if player["team"] == "MI":
        mi_squad.append(player)

print(f"MI has {len(mi_squad)} players in our database:")
for player in mi_squad:
    print(f"  • {player['name']} ({player['role']})")

print()

# =============================================================================
# TRANSFORM: Extract Just Names
# =============================================================================

print("=" * 60)
print("       📝 TRANSFORM: JUST NAMES 📝")
print("=" * 60)
print()

# Create a new list containing only the names
names_only = []
for player in players:
    names_only.append(player["name"])

print("All player names:")
print(names_only)
print()

# =============================================================================
# LIST COMPREHENSION - COMPACT SYNTAX (PREVIEW!)
# =============================================================================

print("=" * 60)
print("       ⚡ LIST COMPREHENSION PREVIEW ⚡")
print("=" * 60)
print()

# The loops above can be written more compactly!

# Long way:
batsmen_names_long = []
for player in players:
    if player["role"] == "Batsman":
        batsmen_names_long.append(player["name"])

# Short way (list comprehension):
batsmen_names = [player["name"] for player in players if player["role"] == "Batsman"]

print("List comprehension syntax:")
print("  [expression for item in list if condition]")
print()
print(f"Batsmen names: {batsmen_names}")
print()

# More examples
averages = [player["avg"] for player in players]
print(f"All averages: {averages}")

high_avg_names = [p["name"] for p in players if p["avg"] > 40]
print(f"Players with avg > 40: {high_avg_names}")

print()

# =============================================================================
# VISUALIZATION: Bar Chart of Filtered Players
# =============================================================================

print("=" * 60)
print("       📊 VISUALIZATION 📊")
print("=" * 60)
print()

# Get star players for chart
chart_players = [p for p in players if p["avg"] > 40]
chart_players.sort(key=lambda x: x["avg"], reverse=True)  # Sort by average

names = [p["name"] for p in chart_players]
averages = [p["avg"] for p in chart_players]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Create bars with team colors
team_colors = {
    "RCB": "#FF0000",
    "MI": "#004BA0",
    "CSK": "#FFCC00",
    "DC": "#0066CC",
    "PBKS": "#DD1F2D",
    "SRH": "#FF6500",
    "RR": "#FF69B4",
    "KKR": "#3A225D"
}

colors = [team_colors.get(p["team"], "#808080") for p in chart_players]

bars = ax.barh(names, averages, color=colors, edgecolor='white', height=0.7)

# Add average values on bars
for bar, avg in zip(bars, averages):
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{avg:.1f}', ha='left', va='center', fontsize=10)

# Add average reference line
ax.axvline(x=40, color='green', linestyle='--', linewidth=2, label='40+ Average Line')

# Customize
ax.set_xlabel('Batting Average', fontsize=12)
ax.set_title('🏏 IPL Players with 40+ Batting Average', fontsize=14, fontweight='bold')
ax.invert_yaxis()  # Highest at top
ax.set_xlim(0, 60)
ax.legend()

plt.tight_layout()
print("📊 Opening visualization...")
plt.show()

print()

# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

print("=" * 60)
print("       📈 SUMMARY STATISTICS 📈")
print("=" * 60)
print()

# Calculate various stats using loops
total_players = len(players)
total_batsmen = len([p for p in players if p["role"] == "Batsman"])
total_bowlers = len([p for p in players if p["role"] == "Bowler"])
total_allrounders = len([p for p in players if p["role"] == "Allrounder"])
total_keepers = len([p for p in players if p["role"] == "Wicketkeeper"])

all_averages = [p["avg"] for p in players]
highest_avg_player = max(players, key=lambda x: x["avg"])
most_experienced = max(players, key=lambda x: x["matches"])

print(f"Total players: {total_players}")
print(f"  • Batsmen: {total_batsmen}")
print(f"  • Bowlers: {total_bowlers}")
print(f"  • Allrounders: {total_allrounders}")
print(f"  • Wicketkeepers: {total_keepers}")
print()
print(f"Highest batting avg: {highest_avg_player['name']} ({highest_avg_player['avg']})")
print(f"Most experienced: {most_experienced['name']} ({most_experienced['matches']} matches)")

print()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: FILTER BY MULTIPLE TEAMS
    Find all players from MI OR CSK.
    Use: if player["team"] == "MI" or player["team"] == "CSK"
    Or:  if player["team"] in ["MI", "CSK"]

Challenge 2: COUNT BY ROLE
    Create a dictionary counting players per role:
    {"Batsman": 8, "Bowler": 3, ...}
    
    Hint: Use a loop and increment counts!

Challenge 3: AVERAGE OF AVERAGES
    Calculate the mean batting average of all batsmen only.
    Steps:
    1. Filter to get only batsmen
    2. Extract their averages
    3. Calculate sum / count

Challenge 4: FIND THE NEWEST TEAM'S PLAYERS
    - Find which team has the fewest players in the database
    - Print all players from that team
    
Challenge 5: CREATE TOP 5 CHART
    - Filter players with avg > 40
    - Sort by average (descending)
    - Take only top 5
    - Create a bar chart
    
    Use slicing: top_5 = sorted_list[:5]

Challenge 6: TRANSFORM TO SUMMARY
    Create a new list of dictionaries with ONLY name and avg:
    summary = [{"name": "Virat Kohli", "avg": 52.3}, ...]
    
    Use list comprehension:
    summary = [{"name": p["name"], "avg": p["avg"]} for p in players]
"""

# =============================================================================
# REFERENCE: Loops on Lists
# =============================================================================
"""
BASIC FOR LOOP:
    for item in list:
        # do something with item

WITH INDEX (enumerate):
    for index, item in enumerate(list):
        # use both index and item

FILTER PATTERN:
    filtered = []
    for item in list:
        if condition:
            filtered.append(item)

LIST COMPREHENSION:
    [expression for item in list]                    # Transform
    [expression for item in list if condition]       # Filter
    
SQL COMPARISONS:
    Python filter loop     →  SQL WHERE clause
    Python sort            →  SQL ORDER BY
    Python [:5]            →  SQL LIMIT 5
    Python list comp       →  SQL SELECT with WHERE
    
    # Python:
    [p["name"] for p in players if p["avg"] > 40]
    
    # SQL:
    SELECT name FROM players WHERE avg > 40
"""
