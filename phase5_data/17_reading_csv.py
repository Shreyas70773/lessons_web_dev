"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 17: Reading CSV Files - IPL Stats Analysis!
===============================================================================

In this session, you'll learn:
    ✅ What CSV files are and why they're everywhere
    ✅ Reading CSV files with Python's csv module
    ✅ Processing rows and extracting data
    ✅ Creating charts from CSV data

===============================================================================
"""

import csv
import matplotlib.pyplot as plt
import os

# =============================================================================
# WHAT IS A CSV FILE?
# =============================================================================

print("=" * 60)
print("       📊 UNDERSTANDING CSV FILES 📊")
print("=" * 60)
print()

"""
CSV = Comma-Separated Values

It's the simplest way to store table data as plain text.

Example CSV content:
    name,team,runs,average
    Virat Kohli,RCB,6624,37.2
    Rohit Sharma,MI,5880,30.3
    MS Dhoni,CSK,4978,39.5

Each line = one row
Commas separate the columns
First line is usually the header (column names)

🔗 FUTURE TOOL: CSV is universal:
    - Excel can export to CSV
    - Google Sheets can export to CSV
    - Databases can export/import CSV
    - n8n can read/write CSV files
    - Every programming language supports CSV
"""

print("CSV Structure:")
print()
print("    ┌─────────────────────────────────────────────────────┐")
print("    │  name,team,runs,average         ◄── Header row     │")
print("    │  Virat Kohli,RCB,6624,37.2      ◄── Data row 1     │")
print("    │  Rohit Sharma,MI,5880,30.3      ◄── Data row 2     │")
print("    │  MS Dhoni,CSK,4978,39.5         ◄── Data row 3     │")
print("    └─────────────────────────────────────────────────────┘")
print()
print("    Commas (,) separate each column value")
print()

# =============================================================================
# READING OUR IPL PLAYERS CSV
# =============================================================================

print("=" * 60)
print("       🏏 READING IPL PLAYER DATA 🏏")
print("=" * 60)
print()

# Get the path to our data file
# __file__ is a special variable that holds this script's path
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "..", "data", "ipl_players.csv")

# Method 1: Basic CSV reading with csv.reader
print("Method 1: Using csv.reader()")
print("-" * 40)

with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # First row is the header
    header = next(reader)
    print(f"Columns: {header}")
    print()
    
    # Print first 5 rows
    print("First 5 players:")
    for i, row in enumerate(reader):
        if i < 5:
            print(f"  {row}")

print()

# Method 2: Using csv.DictReader (easier to work with!)
print("Method 2: Using csv.DictReader() - RECOMMENDED!")
print("-" * 40)

players = []  # We'll store all players here

with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        players.append(row)

# Now we can access data by column name!
print("First 5 players with their runs:")
for i, player in enumerate(players[:5]):
    print(f"  {player['name']}: {player['runs']} runs")

print()
print(f"Total players loaded: {len(players)}")
print()

# 🧠 LOGIC SEED: csv.DictReader converts each row to a dictionary!
# This is exactly like a SQL row - you access columns by name.

# =============================================================================
# ANALYZING THE DATA
# =============================================================================

print("=" * 60)
print("       📈 ANALYZING IPL PLAYER DATA 📈")
print("=" * 60)
print()

# Convert string data to numbers for calculations
for player in players:
    player['runs'] = int(player['runs'])
    player['matches'] = int(player['matches'])
    player['wickets'] = int(player['wickets'])
    player['batting_avg'] = float(player['batting_avg'])
    player['bowling_avg'] = float(player['bowling_avg'])

# Analysis 1: Top 5 run scorers
print("🏆 Top 5 Run Scorers:")
top_scorers = sorted(players, key=lambda x: x['runs'], reverse=True)[:5]
for i, player in enumerate(top_scorers, 1):
    print(f"  {i}. {player['name']} ({player['team']}): {player['runs']:,} runs")
print()

# Analysis 2: Best batting averages
print("📊 Best Batting Averages (min 10 matches):")
qualified = [p for p in players if p['matches'] >= 10]
best_avg = sorted(qualified, key=lambda x: x['batting_avg'], reverse=True)[:5]
for i, player in enumerate(best_avg, 1):
    print(f"  {i}. {player['name']}: {player['batting_avg']:.2f}")
print()

# Analysis 3: Team-wise run distribution
print("🎯 Total Runs by Team:")
team_runs = {}
for player in players:
    team = player['team']
    if team not in team_runs:
        team_runs[team] = 0
    team_runs[team] += player['runs']

for team, runs in sorted(team_runs.items(), key=lambda x: x[1], reverse=True):
    print(f"  {team}: {runs:,} runs")
print()

# Analysis 4: Role distribution
print("👥 Players by Role:")
role_count = {}
for player in players:
    role = player['role']
    if role not in role_count:
        role_count[role] = 0
    role_count[role] += 1

for role, count in role_count.items():
    print(f"  {role}: {count} players")
print()

# =============================================================================
# VISUALIZING THE DATA
# =============================================================================

print("=" * 60)
print("       📊 CREATING VISUALIZATIONS 📊")
print("=" * 60)
print()

# Create a figure with multiple charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("🏏 IPL Player Statistics Analysis", fontsize=16, fontweight='bold')

# Chart 1: Top 5 run scorers bar chart
ax1 = axes[0, 0]
names = [p['name'].split()[-1] for p in top_scorers]  # Last name only
runs = [p['runs'] for p in top_scorers]
colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#E8E8E8', '#E8E8E8']
ax1.bar(names, runs, color=colors, edgecolor='black')
ax1.set_title("🥇 Top 5 Run Scorers")
ax1.set_ylabel("Runs")
ax1.set_xlabel("Player")

# Add value labels on bars
for i, (name, run) in enumerate(zip(names, runs)):
    ax1.text(i, run + 100, f'{run:,}', ha='center', fontsize=9)

# Chart 2: Team runs pie chart
ax2 = axes[0, 1]
teams = list(team_runs.keys())
team_totals = list(team_runs.values())
team_colors = ['#004BA0', '#FFCB05', '#1C1C6E', '#00B7F1', '#FF9933']
ax2.pie(team_totals, labels=teams, autopct='%1.1f%%', colors=team_colors[:len(teams)],
        startangle=90, explode=[0.05] * len(teams))
ax2.set_title("🏆 Run Distribution by Team")

# Chart 3: Batting average scatter plot
ax3 = axes[1, 0]
matches = [p['matches'] for p in players]
batting_avgs = [p['batting_avg'] for p in players]
ax3.scatter(matches, batting_avgs, c='blue', alpha=0.6, s=100)
ax3.set_title("📈 Matches vs Batting Average")
ax3.set_xlabel("Matches Played")
ax3.set_ylabel("Batting Average")
ax3.grid(True, alpha=0.3)

# Highlight top players
for player in best_avg[:3]:
    ax3.annotate(player['name'].split()[-1], 
                 (player['matches'], player['batting_avg']),
                 textcoords="offset points", xytext=(5,5), fontsize=8)

# Chart 4: Role distribution
ax4 = axes[1, 1]
roles = list(role_count.keys())
counts = list(role_count.values())
ax4.barh(roles, counts, color=['#2ecc71', '#3498db', '#e74c3c', '#9b59b6', '#f39c12'])
ax4.set_title("👥 Players by Role")
ax4.set_xlabel("Number of Players")

plt.tight_layout()
plt.show()

print("✅ Charts displayed!")

# =============================================================================
# FILTERING & SEARCHING DATA
# =============================================================================

print()
print("=" * 60)
print("       🔍 FILTERING & SEARCHING 🔍")
print("=" * 60)
print()

# Find all batsmen
print("All Batsmen:")
batsmen = [p for p in players if p['role'] == 'Batsman']
for bat in batsmen:
    print(f"  • {bat['name']} ({bat['team']})")
print()

# Find players with 1000+ runs
print("Players with 1000+ runs:")
high_scorers = [p for p in players if p['runs'] >= 1000]
for player in high_scorers:
    print(f"  • {player['name']}: {player['runs']:,} runs")
print()

# 🧠 LOGIC SEED: These filters are EXACTLY like SQL WHERE clauses!
# SELECT * FROM players WHERE runs >= 1000
# In Python: [p for p in players if p['runs'] >= 1000]


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: FIND ALL-ROUNDERS
    all_rounders = [p for p in players if p['role'] == 'All-rounder']
    # Print their names and both batting/bowling averages

Challenge 2: CALCULATE TEAM AVERAGES
    For each team, calculate the average batting average of all players.
    team_batting_avg = {
        "MI": average of all MI players' batting averages,
        "CSK": average of all CSK players' batting averages,
        ...
    }

Challenge 3: FIND THE BEST BOWLER
    Find the player with the LOWEST bowling average (better for bowlers!)
    Watch out for players with 0 wickets (might have bowling_avg of 0)

Challenge 4: CREATE A PLAYER SEARCH
    def search_player(players, name_fragment):
        '''Find players whose name contains the fragment'''
        return [p for p in players if name_fragment.lower() in p['name'].lower()]
    
    result = search_player(players, "sharma")
    # Should find Rohit Sharma!

Challenge 5: EXPORT FILTERED DATA
    Write a function that filters players and writes them to a new CSV:
    
    def export_filtered(players, min_runs, output_file):
        filtered = [p for p in players if p['runs'] >= min_runs]
        # Write filtered to output_file using csv.writer or csv.DictWriter
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
READING CSV:
    with open('file.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # row is a list: ['value1', 'value2', 'value3']
    
    with open('file.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # row is a dict: {'column1': 'value1', 'column2': 'value2'}

WRITING CSV:
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'score'])  # Header
        writer.writerow(['Virat', 100])     # Data row

CONVERTING TYPES:
    CSV data is always strings! Convert as needed:
    runs = int(row['runs'])
    average = float(row['average'])

FILTERING (List Comprehension):
    filtered = [row for row in data if condition]
    
    This is the Python equivalent of SQL WHERE:
    SELECT * FROM data WHERE condition

🔗 FUTURE TOOL BRIDGE:
    CSV reading in Python → SQL SELECT
    Filtering lists → SQL WHERE
    Sorting lists → SQL ORDER BY
    Grouping/aggregating → SQL GROUP BY
    
    Learn these patterns now, SQL becomes easy later!
"""
