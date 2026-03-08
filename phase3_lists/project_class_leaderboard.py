"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    PROJECT: Class Gaming Leaderboard
===============================================================================

🎮 WHAT THIS PROJECT DOES:
    - Store 8 friends' scores across 3 games
    - Calculate total scores for each person
    - Sort and rank by total score
    - Display a formatted leaderboard table
    - Create a podium-style bar chart (gold/silver/bronze!)

🧠 CONCEPTS YOU'LL USE:
    ✅ Dictionaries with nested data
    ✅ Loops to calculate totals
    ✅ Sorting dictionaries by value
    ✅ F-string formatting for aligned tables
    ✅ Matplotlib for visualization

===============================================================================
"""

import matplotlib.pyplot as plt

# =============================================================================
# THE GAMING DATA
# =============================================================================

print("=" * 60)
print("       🎮 CLASS GAMING LEADERBOARD 🎮")
print("=" * 60)
print()

# 8 friends with scores in 3 different games
# Each person is a dictionary with game scores

gamers = [
    {
        "name": "Arjun",
        "games": {
            "BGMI": 2850,
            "Minecraft": 1200,
            "FreeFire": 3100
        }
    },
    {
        "name": "Priya",
        "games": {
            "BGMI": 3200,
            "Minecraft": 2500,
            "FreeFire": 2800
        }
    },
    {
        "name": "Rohan",
        "games": {
            "BGMI": 1800,
            "Minecraft": 3500,
            "FreeFire": 1500
        }
    },
    {
        "name": "Ananya",
        "games": {
            "BGMI": 4100,
            "Minecraft": 1800,
            "FreeFire": 3800
        }
    },
    {
        "name": "Vikram",
        "games": {
            "BGMI": 2200,
            "Minecraft": 2900,
            "FreeFire": 2400
        }
    },
    {
        "name": "Sneha",
        "games": {
            "BGMI": 3600,
            "Minecraft": 3100,
            "FreeFire": 4200
        }
    },
    {
        "name": "Karthik",
        "games": {
            "BGMI": 1500,
            "Minecraft": 4200,
            "FreeFire": 1200
        }
    },
    {
        "name": "Meera",
        "games": {
            "BGMI": 2700,
            "Minecraft": 2100,
            "FreeFire": 3500
        }
    }
]

print(f"📊 {len(gamers)} gamers registered")
print(f"🎮 Games tracked: BGMI, Minecraft, FreeFire")
print()

# =============================================================================
# CALCULATE TOTALS
# =============================================================================

print("=" * 60)
print("       🧮 CALCULATING TOTAL SCORES 🧮")
print("=" * 60)
print()

# Loop through each gamer and add their total
for gamer in gamers:
    # Sum all game scores
    game_scores = gamer["games"]
    total = sum(game_scores.values())
    
    # Add total to the dictionary
    gamer["total"] = total
    
    print(f"  {gamer['name']}: {total:,} total points")

print()

# =============================================================================
# SORT BY TOTAL SCORE
# =============================================================================

print("=" * 60)
print("       📊 SORTING BY TOTAL SCORE 📊")
print("=" * 60)
print()

# Sort the list by the 'total' key in each dictionary
# reverse=True means highest first
sorted_gamers = sorted(gamers, key=lambda x: x["total"], reverse=True)

print("✅ Gamers sorted from highest to lowest total score!")
print()

# 🧠 LOGIC SEED: Sorting by a key in dictionaries is a fundamental operation!
# lambda x: x["total"] tells Python "use the 'total' value for comparison"

# =============================================================================
# ADD RANKS
# =============================================================================

# Add rank to each gamer
for i, gamer in enumerate(sorted_gamers):
    gamer["rank"] = i + 1

# =============================================================================
# DISPLAY FORMATTED LEADERBOARD
# =============================================================================

print("=" * 70)
print(f"{'🏆 GAMING LEADERBOARD 🏆':^70}")
print("=" * 70)
print()

# Header
print(f"{'Rank':<6} {'Name':<12} {'BGMI':>10} {'Minecraft':>12} {'FreeFire':>12} {'TOTAL':>12}")
print("-" * 70)

# Rows
for gamer in sorted_gamers:
    rank = gamer["rank"]
    name = gamer["name"]
    bgmi = gamer["games"]["BGMI"]
    mc = gamer["games"]["Minecraft"]
    ff = gamer["games"]["FreeFire"]
    total = gamer["total"]
    
    # Add medal emoji for top 3
    if rank == 1:
        rank_display = "🥇 1"
    elif rank == 2:
        rank_display = "🥈 2"
    elif rank == 3:
        rank_display = "🥉 3"
    else:
        rank_display = f"   {rank}"
    
    print(f"{rank_display:<6} {name:<12} {bgmi:>10,} {mc:>12,} {ff:>12,} {total:>12,}")

print("-" * 70)
print()

# =============================================================================
# STATISTICS
# =============================================================================

print("=" * 60)
print("       📈 STATISTICS 📈")
print("=" * 60)
print()

# Total scores list
all_totals = [g["total"] for g in sorted_gamers]

print(f"🏆 Winner: {sorted_gamers[0]['name']} with {sorted_gamers[0]['total']:,} points!")
print(f"📊 Average score: {sum(all_totals) / len(all_totals):,.0f}")
print(f"⬆️ Highest total: {max(all_totals):,}")
print(f"⬇️ Lowest total: {min(all_totals):,}")
print()

# Best in each game
bgmi_scores = [(g["name"], g["games"]["BGMI"]) for g in gamers]
mc_scores = [(g["name"], g["games"]["Minecraft"]) for g in gamers]
ff_scores = [(g["name"], g["games"]["FreeFire"]) for g in gamers]

bgmi_winner = max(bgmi_scores, key=lambda x: x[1])
mc_winner = max(mc_scores, key=lambda x: x[1])
ff_winner = max(ff_scores, key=lambda x: x[1])

print("🎯 Best in each game:")
print(f"   BGMI:      {bgmi_winner[0]} ({bgmi_winner[1]:,})")
print(f"   Minecraft: {mc_winner[0]} ({mc_winner[1]:,})")
print(f"   FreeFire:  {ff_winner[0]} ({ff_winner[1]:,})")
print()

# =============================================================================
# PODIUM BAR CHART
# =============================================================================

print("=" * 60)
print("       📊 CREATING PODIUM CHART 📊")
print("=" * 60)
print()

# Get all names and totals (sorted order)
names = [g["name"] for g in sorted_gamers]
totals = [g["total"] for g in sorted_gamers]

# Color scheme: Gold, Silver, Bronze for top 3, grey for others
colors = []
for i in range(len(sorted_gamers)):
    if i == 0:
        colors.append('#FFD700')  # Gold
    elif i == 1:
        colors.append('#C0C0C0')  # Silver
    elif i == 2:
        colors.append('#CD7F32')  # Bronze
    else:
        colors.append('#4A90D9')  # Blue for others

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# === Subplot 1: Total Scores Bar Chart ===
bars = ax1.bar(names, totals, color=colors, edgecolor='white', linewidth=2)

# Add value labels on bars
for bar, total in zip(bars, totals):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 100,
             f'{total:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_ylabel('Total Score', fontsize=12)
ax1.set_title('🏆 Gaming Leaderboard - Total Scores', fontsize=14, fontweight='bold')
ax1.set_ylim(0, max(totals) * 1.15)
plt.sca(ax1)
plt.xticks(rotation=45, ha='right')

# === Subplot 2: Stacked Bar by Game ===
bgmi = [g["games"]["BGMI"] for g in sorted_gamers]
minecraft = [g["games"]["Minecraft"] for g in sorted_gamers]
freefire = [g["games"]["FreeFire"] for g in sorted_gamers]

x = range(len(names))
width = 0.6

ax2.bar(x, bgmi, width, label='BGMI', color='#FF6B6B')
ax2.bar(x, minecraft, width, bottom=bgmi, label='Minecraft', color='#4ECDC4')
ax2.bar(x, freefire, width, bottom=[b+m for b,m in zip(bgmi, minecraft)], 
        label='FreeFire', color='#45B7D1')

ax2.set_ylabel('Score', fontsize=12)
ax2.set_title('🎮 Score Breakdown by Game', fontsize=14, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(names, rotation=45, ha='right')
ax2.legend(loc='upper right')

plt.tight_layout()
print("📊 Opening charts...")
plt.show()

# =============================================================================
# FINAL ANNOUNCEMENTS
# =============================================================================

print()
print("=" * 60)
print("       🎉 FINAL RESULTS 🎉")
print("=" * 60)
print()
print(f"🥇 CHAMPION: {sorted_gamers[0]['name']} - {sorted_gamers[0]['total']:,} points")
print(f"🥈 2nd Place: {sorted_gamers[1]['name']} - {sorted_gamers[1]['total']:,} points")
print(f"🥉 3rd Place: {sorted_gamers[2]['name']} - {sorted_gamers[2]['total']:,} points")
print()

# Gap analysis
gap_1_2 = sorted_gamers[0]["total"] - sorted_gamers[1]["total"]
gap_2_3 = sorted_gamers[1]["total"] - sorted_gamers[2]["total"]

print(f"📊 Gap between 1st and 2nd: {gap_1_2:,} points")
print(f"📊 Gap between 2nd and 3rd: {gap_2_3:,} points")
print()

# 🔗 FUTURE TOOL: This is exactly what data analysis tools do!
# In n8n, you'd collect this data from different sources (APIs, databases)
# Then process it (calculate totals, sort), and output (charts, reports)


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A NEW GAMER
    - Add yourself to the gamers list!
    - Include scores for all 3 games
    - Re-run to see your ranking

Challenge 2: ADD A NEW GAME
    - Add a 4th game like "Valorant" to everyone's scores
    - Update the total calculation to include it
    - Add it to the leaderboard display

Challenge 3: FIND THE MOST COMPETITIVE GAME
    - Calculate the range (max - min) for each game
    - The game with the smallest range is most competitive
    - Print which game is most balanced

Challenge 4: IMPROVEMENT TRACKER
    - Add a "previous_total" field to each gamer
    - Calculate who improved the most
    - Add ↑ or ↓ arrows in the display

Challenge 5: INTERACTIVE VERSION
    - Ask user to input scores for a new gamer
    - Add them to the leaderboard
    - Show updated rankings

Challenge 6: EXPORT TO FILE
    - Write the leaderboard to a CSV file
    - Use:
        with open("leaderboard.csv", "w") as f:
            f.write("Rank,Name,BGMI,Minecraft,FreeFire,Total\\n")
            for g in sorted_gamers:
                f.write(f"{g['rank']},{g['name']},{g['games']['BGMI']}...")

Challenge 7: PIE CHART OF GAMES
    - For the winner, create a pie chart showing
      what percentage of their score came from each game
"""

# =============================================================================
# CODE PATTERNS LEARNED
# =============================================================================
"""
SORTING DICTIONARIES:
    sorted_list = sorted(dict_list, key=lambda x: x["field"], reverse=True)

CALCULATING TOTALS:
    total = sum(dict.values())
    
F-STRING FORMATTING:
    f"{number:,}"      # Comma separator: 1,234,567
    f"{number:>10}"    # Right-align, width 10
    f"{number:<10}"    # Left-align, width 10
    f"{number:^10}"    # Center, width 10
    f"{number:,.2f}"   # Commas + 2 decimal places

FINDING MAX/MIN IN DICT LIST:
    winner = max(list, key=lambda x: x["score"])
    
LIST COMPREHENSION WITH DICTS:
    names = [person["name"] for person in people]
    filtered = [p for p in people if p["score"] > 100]

This leaderboard system is EXACTLY what you'd build for:
    - School competition trackers
    - Sports league standings
    - Sales performance dashboards
    - Game analytics
"""
