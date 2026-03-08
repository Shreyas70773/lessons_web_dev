"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 20: Dynamic Queries & User Input
===============================================================================

In this session, you'll learn:
    ✅ Building SQL queries from user input
    ✅ Parameterized queries (safe!)
    ✅ The danger of SQL injection
    ✅ Working with user data in functions

===============================================================================
"""

import sqlite3
import os

# =============================================================================
# SETUP DATABASE
# =============================================================================

print("=" * 60)
print("       🔧 DYNAMIC SQL QUERIES 🔧")
print("=" * 60)
print()

# Setup
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "ipl_dynamic.db")

if os.path.exists(db_path):
    os.remove(db_path)

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create and populate table
cursor.execute("""
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    role TEXT,
    matches INTEGER DEFAULT 0,
    runs INTEGER DEFAULT 0,
    batting_avg REAL DEFAULT 0.0,
    wickets INTEGER DEFAULT 0
);
""")

players_data = [
    ('Virat Kohli', 'RCB', 'Batsman', 237, 6624, 37.2, 4),
    ('Rohit Sharma', 'MI', 'Batsman', 243, 5880, 30.3, 15),
    ('MS Dhoni', 'CSK', 'Wicketkeeper', 250, 4978, 39.5, 0),
    ('Jasprit Bumrah', 'MI', 'Fast Bowler', 120, 56, 7.0, 145),
    ('Ravindra Jadeja', 'CSK', 'All-rounder', 210, 2502, 27.8, 132),
    ('Hardik Pandya', 'MI', 'All-rounder', 120, 1680, 27.5, 58),
    ('KL Rahul', 'PBKS', 'Batsman', 109, 3890, 45.8, 0),
    ('Rishabh Pant', 'DC', 'Wicketkeeper', 98, 2838, 35.1, 0),
    ('David Warner', 'DC', 'Batsman', 162, 5881, 41.2, 0),
    ('Andre Russell', 'KKR', 'All-rounder', 107, 1950, 29.5, 95),
]

cursor.executemany("""
INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", players_data)

connection.commit()
print("✅ Database ready with 10 players")
print()

# =============================================================================
# THE WRONG WAY - SQL INJECTION DANGER!
# =============================================================================

print("=" * 60)
print("       ⚠️ THE DANGEROUS WAY - SQL INJECTION ⚠️")
print("=" * 60)
print()

"""
SQL INJECTION is when hackers put SQL code in user input
to manipulate your database!

Example: If a user enters as their search term:
    '; DROP TABLE players; --
    
And you build the query like this:
    query = "SELECT * FROM players WHERE name = '" + user_input + "'"
    
The final query becomes:
    SELECT * FROM players WHERE name = ''; DROP TABLE players; --'
    
This DELETES your entire table!
"""

print("❌ THE WRONG WAY (never do this!):")
print()
print("    user_input = input('Enter player name: ')")
print("    query = \"SELECT * FROM players WHERE name = '\" + user_input + \"'\"")
print("    cursor.execute(query)")
print()
print("    If user enters: '; DROP TABLE players; --")
print("    The query becomes:")
print("    SELECT * FROM players WHERE name = ''; DROP TABLE players; --'")
print()
print("    💥 This deletes all your data!")
print()

# =============================================================================
# THE RIGHT WAY - PARAMETERIZED QUERIES
# =============================================================================

print("=" * 60)
print("       ✅ THE SAFE WAY - Parameterized Queries ✅")
print("=" * 60)
print()

"""
PARAMETERIZED QUERIES use placeholders (?) for values.
Python/SQLite handles escaping automatically!

Even if someone enters malicious input, it gets treated
as a plain string value, not SQL code.
"""

print("✅ THE CORRECT WAY (always do this!):")
print()
print("    user_input = input('Enter player name: ')")
print("    query = \"SELECT * FROM players WHERE name = ?\"")
print("    cursor.execute(query, (user_input,))")
print()
print("    The ? is a placeholder. The value is passed separately.")
print("    Python escapes it properly, making injection impossible!")
print()

# =============================================================================
# BUILDING A PLAYER SEARCH FUNCTION
# =============================================================================

print("=" * 60)
print("       🔍 SAFE PLAYER SEARCH FUNCTION 🔍")
print("=" * 60)
print()

def search_players(name_fragment=None, team=None, min_runs=None, role=None):
    """
    Search for players with multiple optional filters.
    All parameters are safely handled to prevent SQL injection.
    
    Parameters:
        name_fragment: Part of player's name (case-insensitive)
        team: Exact team name
        min_runs: Minimum runs scored
        role: Player role
        
    Returns:
        List of matching player dictionaries
    """
    # Start with base query
    query = "SELECT * FROM players WHERE 1=1"
    params = []
    
    # Add conditions based on provided parameters
    if name_fragment:
        query += " AND name LIKE ?"
        params.append(f"%{name_fragment}%")
    
    if team:
        query += " AND team = ?"
        params.append(team)
    
    if min_runs is not None:
        query += " AND runs >= ?"
        params.append(min_runs)
    
    if role:
        query += " AND role = ?"
        params.append(role)
    
    query += " ORDER BY runs DESC"
    
    # Execute with parameters (safe!)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Convert to list of dictionaries
    columns = [desc[0] for desc in cursor.description]
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    
    return results


def display_results(players, title="Search Results"):
    """Display player results in a nice format"""
    print(f"🏏 {title}")
    print("-" * 60)
    
    if not players:
        print("   No players found.")
    else:
        print(f"   {'Name':<20} {'Team':<8} {'Role':<15} {'Runs'}")
        print(f"   {'-'*20} {'-'*8} {'-'*15} {'-'*6}")
        for p in players:
            print(f"   {p['name']:<20} {p['team']:<8} {p['role']:<15} {p['runs']}")
    
    print()

# Demo the search function
print("Example 1: Search by team")
mi_players = search_players(team="MI")
display_results(mi_players, "Mumbai Indians Players")

print("Example 2: Search by name fragment")
sharma_players = search_players(name_fragment="sharma")
display_results(sharma_players, "Players with 'sharma' in name")

print("Example 3: High scorers who are batsmen")
batsmen = search_players(min_runs=3000, role="Batsman")
display_results(batsmen, "Batsmen with 3000+ runs")

print("Example 4: CSK all-rounders")
csk_allrounders = search_players(team="CSK", role="All-rounder")
display_results(csk_allrounders, "CSK All-rounders")

# =============================================================================
# DYNAMIC INSERT FUNCTION
# =============================================================================

print("=" * 60)
print("       ➕ SAFE INSERT FUNCTION ➕")
print("=" * 60)
print()

def add_player(name, team, role, matches=0, runs=0, batting_avg=0.0, wickets=0):
    """
    Safely add a new player to the database.
    
    All values are passed as parameters (not string concatenation).
    """
    query = """
    INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    
    try:
        cursor.execute(query, (name, team, role, matches, runs, batting_avg, wickets))
        connection.commit()
        print(f"✅ Added player: {name}")
        return True
    except sqlite3.Error as e:
        print(f"❌ Error adding player: {e}")
        return False


# Add a new player
add_player("Yashasvi Jaiswal", "RR", "Batsman", 35, 1280, 38.5, 0)

# Verify
print()
print("Updated player list:")
all_players = search_players()
display_results(all_players, "All Players (including new addition)")

# =============================================================================
# DYNAMIC UPDATE FUNCTION
# =============================================================================

print("=" * 60)
print("       ✏️ SAFE UPDATE FUNCTION ✏️")
print("=" * 60)
print()

def update_player_runs(player_name, new_runs):
    """
    Update a player's run count safely.
    """
    query = "UPDATE players SET runs = ? WHERE name = ?;"
    
    cursor.execute(query, (new_runs, player_name))
    connection.commit()
    
    if cursor.rowcount > 0:
        print(f"✅ Updated {player_name}'s runs to {new_runs}")
    else:
        print(f"⚠️ No player found with name: {player_name}")


# Update Virat's runs
update_player_runs("Virat Kohli", 7000)

# Verify
print()
updated = search_players(name_fragment="Kohli")
display_results(updated, "Updated Virat Kohli stats")

# =============================================================================
# INTERACTIVE MENU (Demo)
# =============================================================================

print("=" * 60)
print("       🎮 BUILDING A MENU SYSTEM 🎮")
print("=" * 60)
print()

print("""
Here's how you would build an interactive menu:

def main_menu():
    while True:
        print("\\n🏏 IPL Stats Manager")
        print("1. Search players")
        print("2. Add player")
        print("3. Update player runs")
        print("4. View all players")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            name = input("Enter name fragment (or press Enter to skip): ")
            team = input("Enter team (or press Enter to skip): ")
            
            # Use empty string as None
            results = search_players(
                name_fragment=name if name else None,
                team=team if team else None
            )
            display_results(results)
            
        elif choice == "2":
            name = input("Player name: ")
            team = input("Team: ")
            role = input("Role: ")
            runs = int(input("Runs: "))
            
            add_player(name, team, role, runs=runs)
            
        elif choice == "3":
            name = input("Player name: ")
            new_runs = int(input("New run count: "))
            update_player_runs(name, new_runs)
            
        elif choice == "4":
            all_players = search_players()
            display_results(all_players, "All Players")
            
        elif choice == "5":
            print("Goodbye!")
            break

# Uncomment to run: main_menu()
""")

print("The key is: NEVER concatenate user input into SQL strings!")
print("Always use ? placeholders and pass values as a tuple.")
print()

# Clean up
connection.close()
print(f"🔒 Database closed: {db_path}")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A DELETE FUNCTION
    def delete_player(player_name):
        query = "DELETE FROM players WHERE name = ?;"
        cursor.execute(query, (player_name,))
        connection.commit()
        print(f"Deleted {cursor.rowcount} player(s)")

Challenge 2: ADD SEARCH BY WICKETS
    Modify search_players() to accept min_wickets parameter:
    
    if min_wickets is not None:
        query += " AND wickets >= ?"
        params.append(min_wickets)

Challenge 3: CREATE A TOP SCORERS FUNCTION
    def get_top_scorers(limit=5, team=None):
        query = "SELECT name, runs FROM players"
        params = []
        
        if team:
            query += " WHERE team = ?"
            params.append(team)
        
        query += " ORDER BY runs DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(query, params)
        return cursor.fetchall()

Challenge 4: BATCH UPDATE
    def add_runs_to_team(team, runs_to_add):
        '''Add runs to all players in a team'''
        query = "UPDATE players SET runs = runs + ? WHERE team = ?;"
        cursor.execute(query, (runs_to_add, team))
        connection.commit()

Challenge 5: MAKE THE MENU INTERACTIVE
    Uncomment the main_menu() call and test it!
    Add error handling for invalid inputs.
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
PARAMETERIZED QUERIES:
    ❌ WRONG: f"SELECT * FROM players WHERE name = '{user_input}'"
    ✅ RIGHT: "SELECT * FROM players WHERE name = ?"
              cursor.execute(query, (user_input,))

MULTIPLE PARAMETERS:
    query = "SELECT * FROM players WHERE team = ? AND runs > ?"
    cursor.execute(query, (team_value, runs_value))

BUILDING DYNAMIC QUERIES:
    query = "SELECT * FROM table WHERE 1=1"
    params = []
    
    if condition1:
        query += " AND column1 = ?"
        params.append(value1)
    
    if condition2:
        query += " AND column2 > ?"
        params.append(value2)
    
    cursor.execute(query, params)

WHY WHERE 1=1?
    It's a trick to make adding conditions easier:
    - 1=1 is always true (doesn't filter anything)
    - Every additional condition can start with "AND"
    - No need for special handling of the first condition

🔗 FUTURE TOOL CONNECTION:
    These same patterns apply in:
    - n8n Database nodes (parameterized queries)
    - Web APIs (sanitizing user input)
    - Any system that takes user input!
"""
