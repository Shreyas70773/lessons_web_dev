"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 19: SQL Queries in Python - Finding Data!
===============================================================================

In this session, you'll learn:
    ✅ SELECT statements - retrieving data
    ✅ WHERE clauses - filtering results
    ✅ ORDER BY - sorting results
    ✅ Aggregate functions - COUNT, SUM, AVG, MAX, MIN

===============================================================================
"""

import sqlite3
import os

# =============================================================================
# SETUP: CREATE AND POPULATE DATABASE
# =============================================================================

print("=" * 60)
print("       🏏 SQL QUERIES - FINDING IPL DATA 🏏")
print("=" * 60)
print()

# Create fresh database for this session
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "ipl_query_demo.db")

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
    wickets INTEGER DEFAULT 0,
    bowling_avg REAL DEFAULT 0.0
);
""")

players_data = [
    ('Virat Kohli', 'RCB', 'Batsman', 237, 6624, 37.2, 4, 105.0),
    ('Rohit Sharma', 'MI', 'Batsman', 243, 5880, 30.3, 15, 68.0),
    ('MS Dhoni', 'CSK', 'Wicketkeeper', 250, 4978, 39.5, 0, 0),
    ('Jasprit Bumrah', 'MI', 'Fast Bowler', 120, 56, 7.0, 145, 23.3),
    ('Ravindra Jadeja', 'CSK', 'All-rounder', 210, 2502, 27.8, 132, 29.1),
    ('Hardik Pandya', 'MI', 'All-rounder', 120, 1680, 27.5, 58, 32.5),
    ('KL Rahul', 'PBKS', 'Batsman', 109, 3890, 45.8, 0, 0),
    ('Rishabh Pant', 'DC', 'Wicketkeeper', 98, 2838, 35.1, 0, 0),
    ('Suresh Raina', 'CSK', 'Batsman', 205, 5528, 32.5, 25, 48.2),
    ('Shubman Gill', 'GT', 'Batsman', 65, 2040, 35.8, 0, 0),
    ('Rashid Khan', 'GT', 'Spinner', 92, 245, 9.8, 112, 20.4),
    ('Andre Russell', 'KKR', 'All-rounder', 107, 1950, 29.5, 95, 24.8),
    ('David Warner', 'DC', 'Batsman', 162, 5881, 41.2, 0, 0),
    ('Faf du Plessis', 'RCB', 'Batsman', 116, 3403, 34.7, 0, 0),
    ('Trent Boult', 'MI', 'Fast Bowler', 78, 42, 6.0, 98, 24.2),
]

cursor.executemany("""
INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets, bowling_avg)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
""", players_data)

connection.commit()
print("✅ Database created with 15 players")
print()

# =============================================================================
# HELPER FUNCTION
# =============================================================================

def run_query(sql, description=""):
    """Runs a SQL query and displays results nicely"""
    print(f"📋 {description}")
    print(f"   SQL: {sql}")
    print()
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    if rows:
        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]
        
        # Print header
        header = " | ".join(f"{col:<12}" for col in columns)
        print(f"   {header}")
        print(f"   {'-' * len(header)}")
        
        # Print rows
        for row in rows:
            row_str = " | ".join(f"{str(val):<12}" for val in row)
            print(f"   {row_str}")
    else:
        print("   (No results)")
    print()
    return rows

# =============================================================================
# SELECT - GETTING DATA
# =============================================================================

print("=" * 60)
print("       📊 SELECT - Retrieving Data 📊")
print("=" * 60)
print()

# Basic SELECT - get all columns
run_query(
    "SELECT * FROM players LIMIT 5;",
    "Get first 5 players (all columns)"
)

# SELECT specific columns
run_query(
    "SELECT name, team, runs FROM players LIMIT 5;",
    "Get just name, team, and runs"
)

# =============================================================================
# WHERE - FILTERING DATA
# =============================================================================

print("=" * 60)
print("       🔍 WHERE - Filtering Results 🔍")
print("=" * 60)
print()

# Filter by team
run_query(
    "SELECT name, team, runs FROM players WHERE team = 'MI';",
    "Players from Mumbai Indians"
)

# Filter by runs
run_query(
    "SELECT name, runs FROM players WHERE runs > 3000;",
    "Players with more than 3000 runs"
)

# Multiple conditions with AND
run_query(
    "SELECT name, team, runs FROM players WHERE team = 'CSK' AND runs > 2000;",
    "CSK players with 2000+ runs"
)

# Multiple conditions with OR
run_query(
    "SELECT name, team, role FROM players WHERE role = 'Batsman' OR role = 'Wicketkeeper';",
    "All batsmen and wicketkeepers"
)

# Using IN
run_query(
    "SELECT name, team FROM players WHERE team IN ('MI', 'CSK', 'RCB');",
    "Players from MI, CSK, or RCB"
)

# Using LIKE for pattern matching
run_query(
    "SELECT name, team FROM players WHERE name LIKE '%Sharma%';",
    "Players with 'Sharma' in their name"
)

# 🧠 LOGIC SEED: WHERE = Python's list filtering!
# SQL: WHERE runs > 3000
# Python: [p for p in players if p['runs'] > 3000]

# =============================================================================
# ORDER BY - SORTING RESULTS
# =============================================================================

print("=" * 60)
print("       📈 ORDER BY - Sorting Results 📈")
print("=" * 60)
print()

# Sort by runs (ascending - lowest first)
run_query(
    "SELECT name, runs FROM players ORDER BY runs LIMIT 5;",
    "Bottom 5 run scorers (ascending)"
)

# Sort by runs (descending - highest first)
run_query(
    "SELECT name, runs FROM players ORDER BY runs DESC LIMIT 5;",
    "Top 5 run scorers (descending)"
)

# Sort by multiple columns
run_query(
    "SELECT name, team, runs FROM players ORDER BY team, runs DESC;",
    "Players sorted by team, then by runs within each team"
)

# 🔗 FUTURE TOOL: ORDER BY is universal!
# Same concept in pandas, Excel SORT, n8n sort nodes

# =============================================================================
# AGGREGATE FUNCTIONS - CALCULATIONS
# =============================================================================

print("=" * 60)
print("       🧮 AGGREGATE FUNCTIONS - Calculations 🧮")
print("=" * 60)
print()

# COUNT - how many rows
run_query(
    "SELECT COUNT(*) AS total_players FROM players;",
    "Count all players"
)

# COUNT with condition
run_query(
    "SELECT COUNT(*) AS mi_players FROM players WHERE team = 'MI';",
    "Count MI players"
)

# SUM - total of a column
run_query(
    "SELECT SUM(runs) AS total_runs FROM players;",
    "Total runs by all players"
)

# AVG - average
run_query(
    "SELECT AVG(batting_avg) AS average_batting_avg FROM players WHERE role = 'Batsman';",
    "Average batting average (batsmen only)"
)

# MAX and MIN
run_query(
    "SELECT MAX(runs) AS highest, MIN(runs) AS lowest FROM players;",
    "Highest and lowest run scorers"
)

# Combined with names (subquery concept)
run_query(
    "SELECT name, runs FROM players WHERE runs = (SELECT MAX(runs) FROM players);",
    "Who has the most runs?"
)

# =============================================================================
# GROUP BY - AGGREGATING BY CATEGORY
# =============================================================================

print("=" * 60)
print("       📊 GROUP BY - Category Aggregations 📊")
print("=" * 60)
print()

# Count players per team
run_query(
    "SELECT team, COUNT(*) AS player_count FROM players GROUP BY team;",
    "Players per team"
)

# Total runs per team
run_query(
    "SELECT team, SUM(runs) AS team_runs FROM players GROUP BY team ORDER BY team_runs DESC;",
    "Total runs by team"
)

# Average batting average per role
run_query(
    "SELECT role, AVG(batting_avg) AS avg_batting FROM players GROUP BY role;",
    "Average batting average by role"
)

# Count and filter groups with HAVING
run_query(
    "SELECT team, COUNT(*) AS count FROM players GROUP BY team HAVING count >= 2;",
    "Teams with 2+ players (HAVING filters groups)"
)

# 🧠 LOGIC SEED: GROUP BY in SQL = Python's dictionary aggregation!
# SQL: SELECT team, SUM(runs) FROM players GROUP BY team
# Python: {team: sum of runs for that team}

# =============================================================================
# COMBINING EVERYTHING
# =============================================================================

print("=" * 60)
print("       🎯 PUTTING IT ALL TOGETHER 🎯")
print("=" * 60)
print()

# Complex query
run_query(
    """SELECT team, 
              COUNT(*) AS players, 
              SUM(runs) AS total_runs,
              AVG(batting_avg) AS avg_batting
       FROM players 
       WHERE runs > 500
       GROUP BY team 
       HAVING players >= 2
       ORDER BY total_runs DESC;""",
    "Team stats (players with 500+ runs, teams with 2+ such players)"
)

print()
print("Query Breakdown:")
print("  1. SELECT - what columns to show")
print("  2. FROM - which table")
print("  3. WHERE - filter individual rows")
print("  4. GROUP BY - combine rows by category")
print("  5. HAVING - filter groups (after aggregation)")
print("  6. ORDER BY - sort the results")
print()

# Close connection
connection.close()
print(f"🔒 Connection closed")
print(f"📁 Database saved at: {db_path}")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: FIND ALL ALL-ROUNDERS
    SELECT name, runs, wickets 
    FROM players 
    WHERE role = 'All-rounder'
    ORDER BY runs DESC;

Challenge 2: TOP WICKET TAKERS
    SELECT name, wickets 
    FROM players 
    WHERE wickets > 50 
    ORDER BY wickets DESC;

Challenge 3: PLAYERS BY EXPERIENCE
    Find players with more than 150 matches:
    SELECT name, matches FROM players WHERE matches > 150;

Challenge 4: TEAM ANALYSIS
    For each team, find:
    - Total wickets
    - Average bowling average (for players with wickets > 0)
    
    SELECT team, SUM(wickets), AVG(bowling_avg)
    FROM players
    WHERE wickets > 0
    GROUP BY team;

Challenge 5: BEST ALL-ROUNDERS
    Find players with batting_avg > 25 AND wickets > 50:
    SELECT name, batting_avg, wickets
    FROM players
    WHERE batting_avg > 25 AND wickets > 50;
"""

# =============================================================================
# SQL QUERY REFERENCE
# =============================================================================
"""
SELECT statement structure:

    SELECT column1, column2, ...  -- What to retrieve
    FROM table_name               -- Where to get it
    WHERE condition               -- Filter rows
    GROUP BY column               -- Combine into groups
    HAVING condition              -- Filter groups
    ORDER BY column [ASC|DESC]    -- Sort results
    LIMIT n;                      -- Max rows to return

COMPARISON OPERATORS:
    =    Equal
    <>   Not equal
    >    Greater than
    <    Less than
    >=   Greater or equal
    <=   Less or equal
    
PATTERN MATCHING:
    LIKE '%text%'   Contains 'text'
    LIKE 'text%'    Starts with 'text'
    LIKE '%text'    Ends with 'text'
    
AGGREGATE FUNCTIONS:
    COUNT(*)        Number of rows
    SUM(column)     Total of values
    AVG(column)     Average of values
    MAX(column)     Highest value
    MIN(column)     Lowest value

🔗 PYTHON TO SQL MAPPING:
    Python filter: [x for x in data if x['runs'] > 1000]
    SQL:          SELECT * FROM data WHERE runs > 1000
    
    Python sort:  sorted(data, key=lambda x: x['runs'], reverse=True)
    SQL:          SELECT * FROM data ORDER BY runs DESC
    
    Python group: {team: sum(p['runs'] for p in players if p['team'] == team)}
    SQL:          SELECT team, SUM(runs) FROM players GROUP BY team
"""
