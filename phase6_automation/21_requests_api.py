"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 21: API Requests - Getting Live Data!
===============================================================================

In this session, you'll learn:
    ✅ What APIs are and why they're essential
    ✅ Making HTTP requests with the requests library
    ✅ Handling API responses
    ✅ Common API patterns and status codes

===============================================================================
"""

import json
import os

# =============================================================================
# WHAT IS AN API?
# =============================================================================

print("=" * 60)
print("       🌐 UNDERSTANDING APIs 🌐")
print("=" * 60)
print()

"""
API = Application Programming Interface

Think of an API like a waiter at a restaurant:
    - You (the customer) want food from the kitchen
    - You can't just walk into the kitchen
    - The waiter takes your ORDER (request)
    - The kitchen prepares your food (processing)
    - The waiter brings back your FOOD (response)

In programming:
    - Your code wants data from another service
    - You send an HTTP REQUEST to their server
    - Their server processes your request
    - They send back a RESPONSE with data

APIs are EVERYWHERE:
    - Weather apps → Weather API
    - Cricket scores → Sports API
    - Maps → Google Maps API  
    - Payments → Stripe/PayPal API
    - Social media → Twitter/Instagram API

🔗 FUTURE TOOL: This is EXACTLY how n8n works!
    n8n connects to APIs to automate workflows.
    Every HTTP Request node in n8n does what you'll learn here!
"""

print("""
How APIs Work:

    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │  Your Code  │ ──────▶ │   Internet  │ ──────▶ │  API Server │
    │             │         │  (HTTP)     │         │  (Cricket)  │
    │  REQUEST:   │         │             │         │  Process    │
    │  "Get MI    │         │             │         │  Request    │
    │   scores"   │         │             │         │             │
    └─────────────┘         └─────────────┘         └──────┬──────┘
                                                           │
    ┌─────────────┐         ┌─────────────┐                │
    │  Your Code  │ ◀────── │   Internet  │ ◀──────────────┘
    │             │         │  (HTTP)     │  RESPONSE:
    │  Use the    │         │             │  JSON data with
    │  data!      │         │             │  scores, stats
    └─────────────┘         └─────────────┘
""")

# =============================================================================
# HTTP METHODS
# =============================================================================

print("=" * 60)
print("       📬 HTTP METHODS - Types of Requests 📬")
print("=" * 60)
print()

print("""
HTTP METHODS - Different ways to interact with APIs:

    GET     → Retrieve data (most common)
              "Give me the match scores"
              
    POST    → Send new data to create something
              "Create a new user account"
              
    PUT     → Update existing data (replace)
              "Update the entire player profile"
              
    PATCH   → Partially update data
              "Just update the player's team"
              
    DELETE  → Remove data
              "Delete this record"

For now, we'll focus on GET - getting data from APIs!
""")

# =============================================================================
# SIMULATING API REQUESTS (No internet needed!)
# =============================================================================

print("=" * 60)
print("       🎮 SIMULATING API REQUESTS 🎮")
print("=" * 60)
print()

"""
The 'requests' library is Python's tool for making HTTP requests.
Install it with: pip install requests

For this lesson, we'll simulate API responses using our 
local JSON file, so you don't need internet access!

The concepts are identical to real API calls.
"""

# Load our mock API response
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "..", "data", "sample_api_response.json")

# Simulate an API call
def mock_api_call(endpoint):
    """
    Simulates an API call by loading local JSON data.
    
    In real code, this would be:
    response = requests.get(endpoint)
    data = response.json()
    """
    print(f"🌐 Calling API: {endpoint}")
    print("   Sending request...")
    
    # Load from our mock file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("   ✅ Response received!")
    return data


# Make a "request"
print("Making an API request for match data...")
print()

response = mock_api_call("https://api.cricket-scores.com/v1/match/ipl-final-2023")
print()

# =============================================================================
# HANDLING THE RESPONSE
# =============================================================================

print("=" * 60)
print("       📦 HANDLING API RESPONSES 📦")
print("=" * 60)
print()

# The response is a Python dictionary (converted from JSON)
print(f"Response type: {type(response)}")
print(f"Top-level keys: {list(response.keys())}")
print()

# Access nested data
match_info = response['match_info']
print("📋 Match Information:")
print(f"   Match: {match_info['match_title']}")
print(f"   Date: {match_info['date']}")
print(f"   Venue: {match_info['venue']}")
print(f"   Status: {match_info['status']}")
print()

# Access the innings data
innings = response['innings']
print("🏏 Innings Summary:")
for inn in innings:
    print(f"   {inn['batting_team']}: {inn['total_runs']}/{inn['wickets']} ({inn['overs']} overs)")
print()

# Access player stats
player_stats = response['player_stats']
print("🏆 Top Performers:")
print(f"   Top Scorer: {player_stats['top_scorer']['name']} - {player_stats['top_scorer']['runs']} runs")
print(f"   Best Bowler: {player_stats['top_bowler']['name']} - {player_stats['top_bowler']['wickets']} wickets")
print()

# =============================================================================
# REAL API REQUEST PATTERN (Reference)
# =============================================================================

print("=" * 60)
print("       📚 REAL API REQUEST PATTERN 📚")
print("=" * 60)
print()

print("""
Here's how you'd make a REAL API request:

import requests

# Step 1: Make the request
url = "https://api.example.com/cricket/scores"
response = requests.get(url)

# Step 2: Check if request was successful
if response.status_code == 200:
    # Success! Parse the JSON data
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# HTTP Status Codes:
# ┌───────┬────────────────────────────────────────────┐
# │ Code  │ Meaning                                    │
# ├───────┼────────────────────────────────────────────┤
# │ 200   │ OK - Request successful                    │
# │ 201   │ Created - New resource created             │
# │ 400   │ Bad Request - Invalid syntax               │
# │ 401   │ Unauthorized - Need to log in              │
# │ 403   │ Forbidden - Not allowed                    │
# │ 404   │ Not Found - Resource doesn't exist         │
# │ 500   │ Server Error - Something broke             │
# └───────┴────────────────────────────────────────────┘
""")

# =============================================================================
# EXTRACTING DATA FROM NESTED JSON
# =============================================================================

print("=" * 60)
print("       🔍 NAVIGATING NESTED DATA 🔍")
print("=" * 60)
print()

# Real API responses are often deeply nested
# Let's navigate the full structure

print("Full response structure:")
print()

def print_structure(data, indent=0):
    """Print the structure of nested data"""
    prefix = "  " * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}📁 {key}:")
                print_structure(value, indent + 1)
            else:
                print(f"{prefix}📄 {key}: {type(value).__name__}")
    elif isinstance(data, list):
        if len(data) > 0:
            print(f"{prefix}📋 List with {len(data)} items:")
            print_structure(data[0], indent + 1)

print_structure(response)

print()
print("Accessing deeply nested data:")
print()

# Get the first bowler from the first innings
first_innings = response['innings'][0]
first_bowler = first_innings['bowlers'][0]
print(f"First bowler: {first_bowler['name']}")
print(f"  Overs: {first_bowler['overs']}")
print(f"  Wickets: {first_bowler['wickets']}")
print(f"  Economy: {first_bowler['economy']}")

print()

# =============================================================================
# BUILDING A DATA EXTRACTION FUNCTION
# =============================================================================

print("=" * 60)
print("       🔧 DATA EXTRACTION FUNCTIONS 🔧")
print("=" * 60)
print()

def extract_match_summary(api_response):
    """
    Extract key match information into a clean format.
    
    This is a common pattern - extract what you need from messy API data
    into a clean structure for your application.
    """
    summary = {
        'title': api_response['match_info']['match_title'],
        'venue': api_response['match_info']['venue'],
        'winner': api_response['match_info']['winner'],
        'innings': []
    }
    
    for inn in api_response['innings']:
        innings_data = {
            'team': inn['batting_team'],
            'score': f"{inn['total_runs']}/{inn['wickets']}",
            'overs': inn['overs'],
            'run_rate': inn['run_rate']
        }
        summary['innings'].append(innings_data)
    
    return summary


# Use the extraction function
summary = extract_match_summary(response)

print("Cleaned Match Summary:")
print(f"  {summary['title']}")
print(f"  Venue: {summary['venue']}")
print(f"  Winner: {summary['winner']}")
print()
for i, inn in enumerate(summary['innings'], 1):
    print(f"  Innings {i}: {inn['team']} - {inn['score']} ({inn['overs']} overs)")
    print(f"             Run Rate: {inn['run_rate']}")

print()

# 🧠 LOGIC SEED: This extraction pattern is used everywhere!
# - n8n "Set" node to reshape data
# - Parsing API responses in web apps
# - ETL (Extract, Transform, Load) pipelines


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: EXTRACT TOP BATSMEN
    Create a function that extracts all batsmen who scored 30+ runs:
    
    def get_high_scorers(api_response, min_runs=30):
        high_scorers = []
        for innings in api_response['innings']:
            for batsman in innings['batsmen']:
                if batsman['runs'] >= min_runs:
                    high_scorers.append({
                        'name': batsman['name'],
                        'runs': batsman['runs'],
                        'team': innings['batting_team']
                    })
        return high_scorers

Challenge 2: CALCULATE ECONOMY RATES
    Find all bowlers with economy rate below 8:
    
    def get_economical_bowlers(api_response, max_economy=8):
        # Loop through innings and bowlers
        # Return list of bowlers with economy < max_economy

Challenge 3: MAKE A REAL API CALL
    Try calling a real free API:
    
    import requests
    
    # Free joke API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        print(f"Setup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}")

Challenge 4: HANDLE MISSING DATA
    Real APIs might have missing fields. Add error handling:
    
    def safe_get(data, key, default="N/A"):
        return data.get(key, default)
    
    # Use it:
    name = safe_get(player, 'name', 'Unknown Player')

Challenge 5: CREATE A CRICINFO-STYLE SCORECARD
    Use the API response to print a formatted scorecard:
    ╔══════════════════════════════════════╗
    ║       MI vs CSK - Final 2023         ║
    ╠══════════════════════════════════════╣
    ║ MI: 180/5 (20 overs)                 ║
    ║ CSK: 175/8 (20 overs)                ║
    ╠══════════════════════════════════════╣
    ║ Winner: Mumbai Indians               ║
    ╚══════════════════════════════════════╝
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
MAKING API REQUESTS:
    import requests
    
    # GET request
    response = requests.get(url)
    
    # GET with parameters
    response = requests.get(url, params={'team': 'MI', 'season': 2023})
    
    # GET with headers (for authentication)
    response = requests.get(url, headers={'Authorization': 'Bearer YOUR_TOKEN'})

HANDLING RESPONSES:
    # Check status
    if response.status_code == 200:
        data = response.json()  # Parse JSON
    
    # Or check with ok property
    if response.ok:
        data = response.json()

COMMON STATUS CODES:
    200 - OK
    201 - Created
    400 - Bad Request
    401 - Unauthorized
    404 - Not Found
    500 - Server Error

NAVIGATING JSON:
    data['key']              # Get value by key
    data['nested']['key']    # Nested access
    data['list'][0]          # First item in list
    data.get('key', default) # Get with default if missing

🔗 FUTURE TOOL: n8n HTTP Request Node
    Everything you learned here is exactly what
    the HTTP Request node does in n8n!
    
    n8n just provides a visual interface for:
    - Setting the URL
    - Choosing GET/POST/etc.
    - Adding headers and parameters
    - Handling the response
"""
