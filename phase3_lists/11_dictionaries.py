"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 11: Dictionaries - IPL Player Profile Cards!
===============================================================================

In this session, you'll learn:
    ✅ What dictionaries are and why they're powerful
    ✅ Keys and values - the building blocks
    ✅ Creating and accessing dictionary data
    ✅ .get(), .keys(), .values(), .items()
    ✅ Nested dictionaries - data inside data

===============================================================================
"""

# =============================================================================
# WHAT IS A DICTIONARY?
# =============================================================================

print("=" * 60)
print("       📖 UNDERSTANDING DICTIONARIES 📖")
print("=" * 60)
print()

"""
A DICTIONARY stores data as KEY-VALUE pairs.

Think of it like:
    - A real dictionary: word → definition
    - A contact list: name → phone number
    - An ID card: field → value

Instead of accessing by index [0], [1], [2]...
You access by NAME (key): ["name"], ["age"], ["team"]

🔗 FUTURE TOOL: A dictionary = ONE ROW in a database table!
    Keys = column names
    Values = the actual data in that row
    
JSON (used everywhere in APIs and n8n) is built on this EXACT structure!
"""

# =============================================================================
# CREATING A DICTIONARY
# =============================================================================

print("=" * 60)
print("       🏏 CREATING PLAYER PROFILE 🏏")
print("=" * 60)
print()

# A dictionary uses curly braces {} with key: value pairs
virat = {
    "name": "Virat Kohli",
    "team": "Royal Challengers Bangalore",
    "jersey": 18,
    "role": "Batsman",
    "batting_avg": 52.73,
    "centuries": 71,
    "catches": 125,
    "is_captain": False
}

print("Created player profile:")
print(virat)
print()

# The structure is clearer when formatted
print("Formatted view:")
for key, value in virat.items():
    print(f"  {key}: {value}")
print()

# =============================================================================
# ACCESSING VALUES
# =============================================================================

print("=" * 60)
print("       🎯 ACCESSING DATA 🎯")
print("=" * 60)
print()

# Method 1: Using square brackets [key]
player_name = virat["name"]
player_team = virat["team"]
player_average = virat["batting_avg"]

print("Using [key] access:")
print(f"  virat['name'] = {player_name}")
print(f"  virat['team'] = {player_team}")
print(f"  virat['batting_avg'] = {player_average}")
print()

# ⚠️ WARNING: Using [key] for a key that doesn't exist causes KeyError!
# virat["height"]  ← This would crash the program!

# Method 2: Using .get(key) - SAFER!
height = virat.get("height")  # Returns None if key doesn't exist
height_default = virat.get("height", "Unknown")  # Returns "Unknown" if not found

print("Using .get(key) for safety:")
print(f"  virat.get('height') = {height}")
print(f"  virat.get('height', 'Unknown') = {height_default}")
print()

# =============================================================================
# DICTIONARY METHODS
# =============================================================================

print("=" * 60)
print("       🛠️ DICTIONARY METHODS 🛠️")
print("=" * 60)
print()

# .keys() - get all keys
print("All keys:")
print(f"  {list(virat.keys())}")
print()

# .values() - get all values
print("All values:")
print(f"  {list(virat.values())}")
print()

# .items() - get all key-value pairs
print("All items (key, value tuples):")
for item in virat.items():
    print(f"  {item}")
print()

# =============================================================================
# MODIFYING DICTIONARIES
# =============================================================================

print("=" * 60)
print("       ✏️ MODIFYING DATA ✏️")
print("=" * 60)
print()

# Create a copy to modify
player = virat.copy()

# Adding a new key
print("Adding new field 'ipl_team':")
player["ipl_team"] = "RCB"
print(f"  player['ipl_team'] = {player['ipl_team']}")

# Modifying an existing value
print("\nUpdating centuries from 71 to 75:")
player["centuries"] = 75
print(f"  player['centuries'] = {player['centuries']}")

# Removing a key
print("\nRemoving 'is_captain' field:")
del player["is_captain"]
print(f"  'is_captain' in player? {('is_captain' in player)}")

# Using .pop() to remove and get value
print("\nUsing .pop('catches'):")
catches = player.pop("catches")
print(f"  Removed and got: {catches}")

print()

# =============================================================================
# NESTED DICTIONARIES
# =============================================================================

print("=" * 60)
print("       📦 NESTED DICTIONARIES 📦")
print("=" * 60)
print()

# Dictionaries can contain other dictionaries!
# This is how complex data is structured - like JSON from APIs

ipl_teams = {
    "MI": {
        "full_name": "Mumbai Indians",
        "captain": "Hardik Pandya",
        "home_ground": "Wankhede Stadium",
        "titles": 5,
        "players": ["Rohit Sharma", "Suryakumar Yadav", "Jasprit Bumrah"],
        "colors": {"primary": "Blue", "secondary": "Gold"}
    },
    "CSK": {
        "full_name": "Chennai Super Kings",
        "captain": "MS Dhoni",
        "home_ground": "MA Chidambaram Stadium",
        "titles": 5,
        "players": ["MS Dhoni", "Ravindra Jadeja", "Devon Conway"],
        "colors": {"primary": "Yellow", "secondary": "Blue"}
    },
    "RCB": {
        "full_name": "Royal Challengers Bangalore",
        "captain": "Faf du Plessis",
        "home_ground": "M. Chinnaswamy Stadium",
        "titles": 0,
        "players": ["Virat Kohli", "Glenn Maxwell", "Mohammed Siraj"],
        "colors": {"primary": "Red", "secondary": "Black"}
    }
}

print("IPL Teams Database (nested dictionary):")
print()

# Accessing nested data
print("Accessing nested values:")
print(f"  ipl_teams['MI']['full_name'] = {ipl_teams['MI']['full_name']}")
print(f"  ipl_teams['CSK']['captain'] = {ipl_teams['CSK']['captain']}")
print(f"  ipl_teams['RCB']['titles'] = {ipl_teams['RCB']['titles']}")
print()

# Going deeper - accessing list inside dict inside dict
print("Deep nesting:")
print(f"  ipl_teams['MI']['players'][0] = {ipl_teams['MI']['players'][0]}")
print(f"  ipl_teams['CSK']['colors']['primary'] = {ipl_teams['CSK']['colors']['primary']}")
print()

# 🔗 FUTURE TOOL: This nested structure IS JSON!
# Every API response you get from the internet looks like this.
# n8n passes data between nodes in this exact format!

# =============================================================================
# PRINTING PLAYER CARDS
# =============================================================================

print("=" * 60)
print("       🎴 PLAYER PROFILE CARDS 🎴")
print("=" * 60)
print()

def print_player_card(player_dict):
    """Prints a nicely formatted player card"""
    print("╔" + "═" * 40 + "╗")
    print(f"║{'🏏 PLAYER CARD':^40}║")
    print("╠" + "═" * 40 + "╣")
    print(f"║ Name:    {player_dict.get('name', 'N/A'):<29}║")
    print(f"║ Team:    {player_dict.get('team', 'N/A'):<29}║")
    print(f"║ Jersey:  #{str(player_dict.get('jersey', 'N/A')):<28}║")
    print(f"║ Role:    {player_dict.get('role', 'N/A'):<29}║")
    print("╠" + "═" * 40 + "╣")
    print(f"║ Batting Avg: {player_dict.get('batting_avg', 0):<25}║")
    print(f"║ Centuries:   {player_dict.get('centuries', 0):<25}║")
    print("╚" + "═" * 40 + "╝")

# Print Virat's card
print_player_card(virat)
print()

# Create and print another player
rohit = {
    "name": "Rohit Sharma",
    "team": "Mumbai Indians",
    "jersey": 45,
    "role": "Opening Batsman",
    "batting_avg": 45.50,
    "centuries": 40
}

print_player_card(rohit)
print()

# =============================================================================
# LOOPING THROUGH TEAMS
# =============================================================================

print("=" * 60)
print("       🏆 ALL IPL TEAMS 🏆")
print("=" * 60)
print()

for team_code, team_data in ipl_teams.items():
    titles_text = f"🏆 × {team_data['titles']}" if team_data['titles'] > 0 else "0 titles"
    print(f"{team_code}: {team_data['full_name']}")
    print(f"    Captain: {team_data['captain']}")
    print(f"    Titles: {titles_text}")
    print()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CREATE YOUR OWN PLAYER
    - Create a dictionary for your favorite cricketer
    - Include at least 6 fields
    - Print it using the print_player_card() function

Challenge 2: ADD A NEW TEAM
    - Add "RR" (Rajasthan Royals) to the ipl_teams dictionary
    - Include all the same fields as other teams
    - Print the new team's captain

Challenge 3: COMPARE TWO PLAYERS
    - Create dictionaries for two players
    - Write code that compares their batting averages
    - Print who has the higher average

Challenge 4: UPDATE NESTED DATA
    - Change MI's captain to "Rohit Sharma"
    - Add a new player to CSK's players list
    - Change RCB's primary color to "Gold"
    
    Remember: ipl_teams["MI"]["captain"] = "Rohit Sharma"

Challenge 5: COUNT TOTAL TITLES
    - Loop through all teams
    - Sum up all their titles
    - Print: "Total IPL titles won: X"

Challenge 6: DICTIONARY COMPREHENSION (PREVIEW!)
    This is advanced, but try it:
    
    # Create a dict of just team codes and titles
    titles_only = {code: data["titles"] for code, data in ipl_teams.items()}
    print(titles_only)
    # Output: {'MI': 5, 'CSK': 5, 'RCB': 0}
"""

# =============================================================================
# DICTIONARY REFERENCE
# =============================================================================
"""
CREATING DICTIONARIES:
    empty = {}
    player = {"name": "Virat", "runs": 100}
    player = dict(name="Virat", runs=100)

ACCESSING VALUES:
    player["name"]           Get value (KeyError if missing)
    player.get("name")       Get value (None if missing)
    player.get("x", default) Get value (default if missing)

MODIFYING:
    player["age"] = 35       Add or update
    del player["age"]        Delete key
    player.pop("age")        Delete and return value
    player.update({"a": 1})  Merge another dict

USEFUL METHODS:
    .keys()    All keys
    .values()  All values
    .items()   All (key, value) tuples
    .copy()    Shallow copy
    .clear()   Remove all

CHECKING:
    "name" in player         True if key exists
    len(player)              Number of key-value pairs

JSON CONNECTION:
    Dictionaries and JSON are nearly identical!
    
    Python dict:  {"name": "Virat", "runs": 100}
    JSON:         {"name": "Virat", "runs": 100}
    
    This is why Python is great for working with APIs!
"""
