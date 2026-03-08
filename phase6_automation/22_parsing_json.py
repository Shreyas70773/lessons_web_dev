"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 22: Parsing JSON - Unpacking Data Treasures!
===============================================================================

In this session, you'll learn:
    ✅ JSON structure and syntax
    ✅ Parsing JSON in Python
    ✅ Working with nested data
    ✅ Converting between JSON and Python objects

===============================================================================
"""

import json
import os

# =============================================================================
# WHAT IS JSON?
# =============================================================================

print("=" * 60)
print("       📦 UNDERSTANDING JSON 📦")
print("=" * 60)
print()

"""
JSON = JavaScript Object Notation

JSON is THE universal data format for exchanging information:
    • All APIs use JSON
    • Configuration files use JSON
    • Databases store JSON
    • n8n passes JSON between nodes

JSON looks almost exactly like Python dictionaries and lists!

Python          JSON
dict { }    →   object { }
list [ ]    →   array [ ]
True/False  →   true/false
None        →   null
"string"    →   "string" (must use double quotes!)
123         →   123
"""

print("JSON vs Python Comparison:")
print()
print("┌─────────────────────────────────────────────────────────┐")
print("│                  PYTHON                                 │")
print("├─────────────────────────────────────────────────────────┤")
print("│ {                                                       │")
print("│     'name': 'Virat Kohli',    # single quotes ok       │")
print("│     'runs': 6624,                                       │")
print("│     'active': True,            # capital T              │")
print("│     'retired': None            # None                   │")
print("│ }                                                       │")
print("└─────────────────────────────────────────────────────────┘")
print()
print("┌─────────────────────────────────────────────────────────┐")
print("│                   JSON                                  │")
print("├─────────────────────────────────────────────────────────┤")
print('│ {                                                       │')
print('│     "name": "Virat Kohli",    // double quotes ONLY    │')
print("│     \"runs\": 6624,                                       │")
print('│     "active": true,            // lowercase t           │')
print('│     "retired": null            // null not None         │')
print("│ }                                                       │")
print("└─────────────────────────────────────────────────────────┘")
print()

# =============================================================================
# PARSING JSON STRINGS
# =============================================================================

print("=" * 60)
print("       🔧 PARSING JSON STRINGS 🔧")
print("=" * 60)
print()

# JSON as a string (like from an API or file)
json_string = '''
{
    "player": "Rohit Sharma",
    "team": "Mumbai Indians",
    "stats": {
        "matches": 243,
        "runs": 5880,
        "centuries": 1
    },
    "roles": ["Batsman", "Captain"],
    "is_captain": true
}
'''

# Parse JSON string to Python dictionary
print("Original JSON string:")
print(json_string)

python_dict = json.loads(json_string)  # loads = load string

print("Converted to Python dictionary:")
print(f"Type: {type(python_dict)}")
print(f"Player: {python_dict['player']}")
print(f"Team: {python_dict['team']}")
print(f"Runs: {python_dict['stats']['runs']}")
print(f"Roles: {python_dict['roles']}")
print(f"Is Captain: {python_dict['is_captain']}")
print()

# =============================================================================
# CONVERTING PYTHON TO JSON
# =============================================================================

print("=" * 60)
print("       🔄 PYTHON → JSON CONVERSION 🔄")
print("=" * 60)
print()

# Create a Python dictionary
player_data = {
    "name": "Jasprit Bumrah",
    "team": "MI",
    "role": "Fast Bowler",
    "stats": {
        "matches": 120,
        "wickets": 145,
        "best_bowling": "5/10"
    },
    "active": True,
    "injury": None
}

# Convert to JSON string
json_output = json.dumps(player_data)  # dumps = dump string
print("Python dict → JSON string (compact):")
print(json_output)
print()

# Pretty print with indentation
json_pretty = json.dumps(player_data, indent=4)
print("Python dict → JSON string (pretty):")
print(json_pretty)
print()

# =============================================================================
# READING JSON FROM FILES
# =============================================================================

print("=" * 60)
print("       📁 READING JSON FILES 📁")
print("=" * 60)
print()

# Load our sample API response file
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "..", "data", "sample_api_response.json")

# Read and parse JSON file
with open(json_path, 'r', encoding='utf-8') as file:
    match_data = json.load(file)  # load (not loads) for files

print(f"Loaded JSON from: sample_api_response.json")
print(f"Data type: {type(match_data)}")
print(f"Top-level keys: {list(match_data.keys())}")
print()

# Navigate the structure
print("Match Information:")
print(f"  Title: {match_data['match_info']['match_title']}")
print(f"  Venue: {match_data['match_info']['venue']}")
print(f"  Winner: {match_data['match_info']['winner']}")
print()

# =============================================================================
# WRITING JSON TO FILES
# =============================================================================

print("=" * 60)
print("       💾 WRITING JSON FILES 💾")
print("=" * 60)
print()

# Create some data to save
team_stats = {
    "tournament": "IPL 2023",
    "teams": [
        {
            "name": "Mumbai Indians",
            "short": "MI",
            "wins": 8,
            "losses": 6,
            "position": 5
        },
        {
            "name": "Chennai Super Kings",
            "short": "CSK",
            "wins": 11,
            "losses": 4,
            "position": 1
        },
        {
            "name": "Gujarat Titans",
            "short": "GT",
            "wins": 10,
            "losses": 5,
            "position": 2
        }
    ],
    "total_matches": 70,
    "season_complete": True
}

# Save to file
output_path = os.path.join(script_dir, "team_stats_output.json")
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(team_stats, file, indent=4)  # dump (not dumps) for files

print(f"✅ Saved team stats to: team_stats_output.json")
print()

# Read it back to verify
with open(output_path, 'r', encoding='utf-8') as file:
    loaded_stats = json.load(file)

print("Verification - loaded data:")
for team in loaded_stats['teams']:
    print(f"  {team['name']}: {team['wins']} wins, Position #{team['position']}")

print()

# =============================================================================
# NAVIGATING COMPLEX NESTED JSON
# =============================================================================

print("=" * 60)
print("       🗺️ NAVIGATING NESTED JSON 🗺️")
print("=" * 60)
print()

# Our match_data has complex nesting - let's navigate it!

print("Getting all batsmen from both innings:")
print("-" * 50)

for i, innings in enumerate(match_data['innings'], 1):
    team = innings['batting_team']
    total = innings['total_runs']
    wickets = innings['wickets']
    
    print(f"\nInnings {i}: {team} - {total}/{wickets}")
    print(f"{'Name':<20} {'Runs':<8} {'Balls':<8} {'4s':<5} {'6s':<5} {'SR'}")
    print("-" * 55)
    
    for batsman in innings['batsmen']:
        print(f"{batsman['name']:<20} {batsman['runs']:<8} {batsman['balls']:<8} "
              f"{batsman['fours']:<5} {batsman['sixes']:<5} {batsman['strike_rate']:.2f}")

print()

# =============================================================================
# SAFE ACCESS WITH .get() METHOD
# =============================================================================

print("=" * 60)
print("       🛡️ SAFE ACCESS WITH .get() 🛡️")
print("=" * 60)
print()

"""
Real-world JSON often has missing fields!
Using dict['key'] will crash if the key doesn't exist.
Using dict.get('key', default) returns the default if missing.
"""

sample_player = {
    "name": "New Player",
    "team": "RCB"
    # Note: 'runs' is missing!
}

# Unsafe - will crash if key missing
# runs = sample_player['runs']  # KeyError!

# Safe - returns default value
runs = sample_player.get('runs', 0)
average = sample_player.get('average', 0.0)
nickname = sample_player.get('nickname', 'No nickname')

print("Safe access demonstration:")
print(f"  Name: {sample_player.get('name', 'Unknown')}")
print(f"  Team: {sample_player.get('team', 'Unknown')}")
print(f"  Runs: {runs} (was missing, used default 0)")
print(f"  Average: {average} (was missing, used default 0.0)")
print(f"  Nickname: {nickname} (was missing, used default)")
print()

# Helper function for nested access
def safe_nested_get(data, *keys, default=None):
    """
    Safely get nested values from dictionaries.
    
    Usage: safe_nested_get(data, 'level1', 'level2', 'level3', default='N/A')
    """
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
            if data is None:
                return default
        else:
            return default
    return data if data is not None else default


# Use the helper
print("Safe nested access:")
venue = safe_nested_get(match_data, 'match_info', 'venue', default='Unknown')
print(f"  Venue: {venue}")

# Missing path - doesn't crash!
missing = safe_nested_get(match_data, 'nonexistent', 'path', default='Not found')
print(f"  Missing path: {missing}")
print()

# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: EXTRACT ALL BOWLERS
    Create a function to get all bowlers from the match data:
    
    def get_all_bowlers(match_data):
        bowlers = []
        for innings in match_data['innings']:
            for bowler in innings['bowlers']:
                bowlers.append({
                    'name': bowler['name'],
                    'wickets': bowler['wickets'],
                    'economy': bowler['economy']
                })
        return bowlers

Challenge 2: CREATE A MATCH SCORECARD JSON
    Create a simplified scorecard structure:
    
    scorecard = {
        "match": match_data['match_info']['match_title'],
        "innings1": {
            "team": innings1_team,
            "score": "runs/wickets",
            "top_scorer": "name (runs)"
        },
        "innings2": {...}
    }
    
    Save it to a new JSON file!

Challenge 3: CALCULATE TEAM TOTALS
    Loop through innings and calculate:
    - Total boundaries (4s + 6s)
    - Boundary percentage of total runs
    - Which team hit more sixes?

Challenge 4: JSON VALIDATION
    Write a function to check if JSON has required fields:
    
    def validate_player_json(data):
        required = ['name', 'team', 'role']
        for field in required:
            if field not in data:
                return False, f"Missing: {field}"
        return True, "Valid"

Challenge 5: MERGE DATA
    Combine player stats from multiple innings:
    - Find players who batted in both innings
    - Sum their total runs across innings
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
JSON MODULE FUNCTIONS:

    PARSING (string → Python):
        json.loads(json_string)     # Parse JSON string to Python
        json.load(file_object)      # Parse JSON file to Python
    
    SERIALIZING (Python → string):
        json.dumps(python_data)     # Python to JSON string
        json.dumps(data, indent=4)  # Pretty printed
        json.dump(data, file)       # Python to JSON file

SAFE ACCESS:
    data.get('key', default)        # Returns default if key missing
    
COMMON ERRORS:
    json.JSONDecodeError - Invalid JSON syntax
    KeyError - Missing key in dictionary
    TypeError - Wrong type (e.g., accessing int like dict)

JSON RULES:
    • Keys must be strings in double quotes
    • Strings must use double quotes
    • No trailing commas
    • true/false (lowercase)
    • null (not None)
    • No comments allowed

🔗 FUTURE TOOL CONNECTION:
    n8n nodes receive and send JSON data.
    Understanding JSON is essential for:
    - Configuring n8n nodes
    - Mapping data between nodes
    - Debugging workflow errors
"""

# Cleanup - remove the test file
try:
    os.remove(output_path)
    print(f"🧹 Cleaned up test file: {output_path}")
except:
    pass
