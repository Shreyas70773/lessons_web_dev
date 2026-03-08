"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 18: SQLite Introduction - Your First Database!
===============================================================================

In this session, you'll learn:
    ✅ What databases are and why they're powerful
    ✅ Creating a SQLite database (lives in a single file!)
    ✅ Creating tables with column definitions
    ✅ Adding data with INSERT statements

===============================================================================
"""

import sqlite3
import os

# =============================================================================
# WHAT IS A DATABASE?
# =============================================================================

print("=" * 60)
print("       🗄️ UNDERSTANDING DATABASES 🗄️")
print("=" * 60)
print()

"""
A DATABASE is an organized collection of data.

Think of it like a super-powered spreadsheet:
    • A DATABASE contains multiple TABLES (like sheets)
    • Each TABLE has COLUMNS (like spreadsheet columns)
    • Each TABLE has ROWS (like spreadsheet rows)

But databases are MUCH more powerful:
    • Can handle millions of rows efficiently
    • Built-in search and filtering (super fast!)
    • Links between tables (relationships)
    • Multiple users can access at once safely
    • Data validation and protection

SQLite is perfect for learning because:
    • The entire database is ONE file
    • No setup or server needed
    • Built into Python!
    • Used by millions of apps (iOS, Android, browsers!)
"""

print("""
Database Structure:

    ┌─────────────────── DATABASE (ipl_stats.db) ──────────────────┐
    │                                                               │
    │   ┌─────────────── TABLE: players ────────────────┐          │
    │   │ id │ name         │ team │ runs  │ wickets   │          │
    │   │────│──────────────│──────│───────│───────────│          │
    │   │ 1  │ Virat Kohli  │ RCB  │ 6624  │ 4         │          │
    │   │ 2  │ Rohit Sharma │ MI   │ 5880  │ 15        │          │
    │   │ 3  │ MS Dhoni     │ CSK  │ 4978  │ 0         │          │
    │   └────────────────────────────────────────────────┘          │
    │                                                               │
    │   ┌─────────────── TABLE: matches ────────────────┐          │
    │   │ id │ team1 │ team2 │ winner │ venue           │          │
    │   │────│───────│───────│────────│─────────────────│          │
    │   │ 1  │ MI    │ CSK   │ MI     │ Wankhede        │          │
    │   │ 2  │ RCB   │ KKR   │ KKR    │ Chinnaswamy     │          │
    │   └────────────────────────────────────────────────┘          │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
""")

# =============================================================================
# CREATING A DATABASE & TABLE
# =============================================================================

print("=" * 60)
print("       🛠️ CREATING YOUR FIRST DATABASE 🛠️")
print("=" * 60)
print()

# Database file path (in current directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "ipl_stats.db")

# Remove old database if it exists (for clean demo)
if os.path.exists(db_path):
    os.remove(db_path)
    print("🗑️ Removed old database")

# Step 1: Connect to database (creates it if doesn't exist!)
print("📁 Creating database: ipl_stats.db")
connection = sqlite3.connect(db_path)

# Step 2: Create a cursor (used to execute SQL commands)
cursor = connection.cursor()
print("✅ Connected to database")
print()

# Step 3: Create a table
print("📋 Creating 'players' table...")

create_table_sql = """
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
"""

# 🧠 LOGIC SEED: SQL Commands Explained:
# CREATE TABLE - makes a new table
# INTEGER - whole numbers
# TEXT - text/strings
# REAL - decimal numbers
# PRIMARY KEY - unique identifier for each row
# AUTOINCREMENT - auto-generates ID numbers
# NOT NULL - this field is required
# DEFAULT - value used if none provided

cursor.execute(create_table_sql)
print("✅ Table 'players' created!")
print()

# Let's see the table structure
print("📊 Table Structure:")
print("-" * 50)
print(f"{'Column':<15} {'Type':<12} {'Constraints'}")
print("-" * 50)
print(f"{'id':<15} {'INTEGER':<12} PRIMARY KEY AUTOINCREMENT")
print(f"{'name':<15} {'TEXT':<12} NOT NULL")
print(f"{'team':<15} {'TEXT':<12} NOT NULL")
print(f"{'role':<15} {'TEXT':<12} ")
print(f"{'matches':<15} {'INTEGER':<12} DEFAULT 0")
print(f"{'runs':<15} {'INTEGER':<12} DEFAULT 0")
print(f"{'batting_avg':<15} {'REAL':<12} DEFAULT 0.0")
print(f"{'wickets':<15} {'INTEGER':<12} DEFAULT 0")
print(f"{'bowling_avg':<15} {'REAL':<12} DEFAULT 0.0")
print()

# =============================================================================
# INSERTING DATA
# =============================================================================

print("=" * 60)
print("       ➕ ADDING DATA TO THE TABLE ➕")
print("=" * 60)
print()

# Method 1: Insert one row
print("Adding single player...")
cursor.execute("""
INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets, bowling_avg)
VALUES ('Virat Kohli', 'RCB', 'Batsman', 237, 6624, 37.2, 4, 105.0);
""")
print("  ✅ Added Virat Kohli")

# Method 2: Insert with placeholders (safer!)
print("Adding more players with placeholders...")

players_data = [
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
]

# Insert using parameterized query (prevents SQL injection!)
for player in players_data:
    cursor.execute("""
    INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets, bowling_avg)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, player)
    print(f"  ✅ Added {player[0]}")

# IMPORTANT: Save (commit) the changes!
connection.commit()
print()
print("💾 All changes saved to database!")
print()

# 🔗 FUTURE TOOL: This is EXACTLY how n8n writes to databases!
# The INSERT statement is universal across all databases.

# =============================================================================
# VERIFYING THE DATA
# =============================================================================

print("=" * 60)
print("       ✅ VERIFYING DATA WAS SAVED ✅")
print("=" * 60)
print()

# Count rows
cursor.execute("SELECT COUNT(*) FROM players;")
count = cursor.fetchone()[0]
print(f"Total players in database: {count}")
print()

# Show all players
cursor.execute("SELECT id, name, team, runs FROM players;")
rows = cursor.fetchall()

print("Players in Database:")
print("-" * 50)
print(f"{'ID':<4} {'Name':<20} {'Team':<8} {'Runs'}")
print("-" * 50)
for row in rows:
    print(f"{row[0]:<4} {row[1]:<20} {row[2]:<8} {row[3]}")

print()

# =============================================================================
# CLOSING THE CONNECTION
# =============================================================================

print("🔒 Closing database connection...")
connection.close()
print("✅ Connection closed!")
print()

print(f"📁 Your database file is at: {db_path}")
print("   You can open it with tools like DB Browser for SQLite!")
print()

# =============================================================================
# SQL STATEMENT REFERENCE
# =============================================================================

print("=" * 60)
print("       📚 SQL STATEMENTS LEARNED TODAY 📚")
print("=" * 60)
print()

print("""
CREATE TABLE - Make a new table
────────────────────────────────
CREATE TABLE table_name (
    column1 TYPE CONSTRAINTS,
    column2 TYPE CONSTRAINTS,
    ...
);

Data Types:
  • INTEGER - Whole numbers (1, 42, -5)
  • REAL - Decimal numbers (3.14, 99.9)
  • TEXT - Text strings ("Hello", "Virat")
  • BLOB - Binary data (images, files)

Constraints:
  • PRIMARY KEY - Unique row identifier
  • NOT NULL - Must have a value
  • UNIQUE - No duplicates allowed
  • DEFAULT value - Use this if none given

INSERT INTO - Add data to a table
────────────────────────────────
INSERT INTO table_name (col1, col2, col3)
VALUES ('value1', 'value2', 'value3');

COMMIT - Save changes
────────────────────────────────
connection.commit()  # In Python
-- Changes aren't saved until you commit!
""")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A NEW PLAYER
    cursor.execute('''
    INSERT INTO players (name, team, role, matches, runs, batting_avg)
    VALUES ('Your Name', 'Your Team', 'Batsman', 10, 500, 50.0);
    ''')
    connection.commit()

Challenge 2: CREATE A TEAMS TABLE
    CREATE TABLE teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        home_city TEXT,
        championships INTEGER DEFAULT 0
    );
    
    Add all IPL teams!

Challenge 3: CREATE A MATCHES TABLE
    CREATE TABLE matches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team1 TEXT NOT NULL,
        team2 TEXT NOT NULL,
        winner TEXT,
        venue TEXT,
        date TEXT
    );
    
    Add a few IPL matches!

Challenge 4: INSERT MULTIPLE AT ONCE
    cursor.executemany('''
    INSERT INTO players (name, team, role) VALUES (?, ?, ?);
    ''', [
        ('Player 1', 'MI', 'Batsman'),
        ('Player 2', 'CSK', 'Bowler'),
        ('Player 3', 'RCB', 'All-rounder'),
    ])
    
Challenge 5: UNDERSTAND THE FLOW
    Draw a flowchart:
    Connect → Create Cursor → Execute SQL → Commit → Close
    
    What happens if you skip commit?
    Answer: Data is lost when you close the connection!
"""

# =============================================================================
# PYTHON + SQL WORKFLOW
# =============================================================================
"""
WORKFLOW FOR DATABASE OPERATIONS:

    ┌─────────────────────────────────────────────────────────┐
    │  1. CONNECT                                             │
    │     connection = sqlite3.connect("database.db")         │
    └────────────────────────┬────────────────────────────────┘
                             ▼
    ┌─────────────────────────────────────────────────────────┐
    │  2. CREATE CURSOR                                       │
    │     cursor = connection.cursor()                        │
    └────────────────────────┬────────────────────────────────┘
                             ▼
    ┌─────────────────────────────────────────────────────────┐
    │  3. EXECUTE SQL                                         │
    │     cursor.execute("SQL STATEMENT HERE")                │
    │     cursor.execute("SELECT ...") / cursor.fetchall()    │
    └────────────────────────┬────────────────────────────────┘
                             ▼
    ┌─────────────────────────────────────────────────────────┐
    │  4. COMMIT CHANGES (for INSERT/UPDATE/DELETE)           │
    │     connection.commit()                                 │
    └────────────────────────┬────────────────────────────────┘
                             ▼
    ┌─────────────────────────────────────────────────────────┐
    │  5. CLOSE CONNECTION                                    │
    │     connection.close()                                  │
    └─────────────────────────────────────────────────────────┘

This is the UNIVERSAL database pattern:
    Python → Connect → Query → Close
    n8n → Database Node → SQL → Output
    Any language → Same concept!
"""
