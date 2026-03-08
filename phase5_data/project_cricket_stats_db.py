"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    PROJECT: Cricket Statistics Database
===============================================================================

🎯 WHAT THIS PROJECT DOES:
    Build a complete cricket database application that:
    - Creates a properly structured database
    - Imports data from CSV files  
    - Provides search and analysis features
    - Generates visual reports

🧠 CONCEPTS USED:
    ✅ SQLite database operations
    ✅ Reading CSV files
    ✅ SQL queries (SELECT, INSERT, UPDATE)
    ✅ Parameterized queries (safe!)
    ✅ Data visualization with matplotlib
    ✅ Functions and composition

===============================================================================
"""

import sqlite3
import csv
import os
import matplotlib.pyplot as plt

# =============================================================================
# DATABASE MANAGER CLASS
# =============================================================================

class CricketDatabase:
    """
    A complete cricket statistics database manager.
    
    This class handles all database operations including:
    - Creating and connecting to the database
    - Importing data from CSV files
    - Searching and querying data
    - Generating statistics and reports
    """
    
    def __init__(self, db_path):
        """Initialize with database path"""
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Connect to the database"""
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        print(f"📁 Connected to database: {self.db_path}")
        
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
            print("🔒 Database connection closed")
    
    def create_tables(self):
        """Create all required tables"""
        
        # Players table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
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
        
        # Matches table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1 TEXT NOT NULL,
            team2 TEXT NOT NULL,
            team1_score INTEGER,
            team2_score INTEGER,
            winner TEXT,
            venue TEXT,
            season INTEGER
        );
        """)
        
        # Teams table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_name TEXT NOT NULL UNIQUE,
            full_name TEXT NOT NULL,
            home_city TEXT,
            championships INTEGER DEFAULT 0
        );
        """)
        
        self.connection.commit()
        print("✅ Tables created successfully")
    
    def import_players_from_csv(self, csv_path):
        """Import player data from CSV file"""
        
        # Clear existing data
        self.cursor.execute("DELETE FROM players;")
        
        count = 0
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                self.cursor.execute("""
                INSERT INTO players (name, team, role, matches, runs, batting_avg, wickets, bowling_avg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """, (
                    row['name'],
                    row['team'],
                    row['role'],
                    int(row['matches']),
                    int(row['runs']),
                    float(row['batting_avg']),
                    int(row['wickets']),
                    float(row['bowling_avg'])
                ))
                count += 1
        
        self.connection.commit()
        print(f"✅ Imported {count} players from CSV")
    
    def import_matches_from_csv(self, csv_path):
        """Import match data from CSV file"""
        
        # Clear existing data
        self.cursor.execute("DELETE FROM matches;")
        
        count = 0
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                self.cursor.execute("""
                INSERT INTO matches (team1, team2, team1_score, team2_score, winner, venue, season)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """, (
                    row['team1'],
                    row['team2'],
                    int(row['team1_score']),
                    int(row['team2_score']),
                    row['winner'],
                    row['venue'],
                    int(row['season'])
                ))
                count += 1
        
        self.connection.commit()
        print(f"✅ Imported {count} matches from CSV")
    
    def setup_teams(self):
        """Set up IPL team data"""
        
        teams = [
            ('MI', 'Mumbai Indians', 'Mumbai', 5),
            ('CSK', 'Chennai Super Kings', 'Chennai', 5),
            ('RCB', 'Royal Challengers Bangalore', 'Bangalore', 0),
            ('KKR', 'Kolkata Knight Riders', 'Kolkata', 2),
            ('DC', 'Delhi Capitals', 'Delhi', 0),
            ('PBKS', 'Punjab Kings', 'Mohali', 0),
            ('RR', 'Rajasthan Royals', 'Jaipur', 1),
            ('SRH', 'Sunrisers Hyderabad', 'Hyderabad', 1),
            ('GT', 'Gujarat Titans', 'Ahmedabad', 1),
            ('LSG', 'Lucknow Super Giants', 'Lucknow', 0),
        ]
        
        self.cursor.execute("DELETE FROM teams;")
        
        for team in teams:
            self.cursor.execute("""
            INSERT INTO teams (short_name, full_name, home_city, championships)
            VALUES (?, ?, ?, ?);
            """, team)
        
        self.connection.commit()
        print(f"✅ Added {len(teams)} teams")
    
    # =========================================================================
    # SEARCH METHODS
    # =========================================================================
    
    def search_players(self, name=None, team=None, role=None, min_runs=None):
        """Search players with various filters"""
        
        query = "SELECT * FROM players WHERE 1=1"
        params = []
        
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        
        if team:
            query += " AND team = ?"
            params.append(team)
        
        if role:
            query += " AND role = ?"
            params.append(role)
        
        if min_runs is not None:
            query += " AND runs >= ?"
            params.append(min_runs)
        
        query += " ORDER BY runs DESC"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def get_top_scorers(self, limit=10):
        """Get top run scorers"""
        query = """
        SELECT name, team, runs, batting_avg, matches
        FROM players
        ORDER BY runs DESC
        LIMIT ?;
        """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()
    
    def get_top_wicket_takers(self, limit=10):
        """Get top wicket takers"""
        query = """
        SELECT name, team, wickets, bowling_avg, matches
        FROM players
        WHERE wickets > 0
        ORDER BY wickets DESC
        LIMIT ?;
        """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()
    
    def get_team_stats(self):
        """Get aggregated stats for each team"""
        query = """
        SELECT 
            team,
            COUNT(*) as player_count,
            SUM(runs) as total_runs,
            AVG(batting_avg) as avg_batting,
            SUM(wickets) as total_wickets
        FROM players
        GROUP BY team
        ORDER BY total_runs DESC;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_match_stats(self):
        """Get match statistics by team"""
        query = """
        SELECT 
            winner,
            COUNT(*) as wins
        FROM matches
        WHERE winner IS NOT NULL AND winner != ''
        GROUP BY winner
        ORDER BY wins DESC;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    # =========================================================================
    # REPORT METHODS
    # =========================================================================
    
    def print_top_scorers(self, limit=10):
        """Print formatted top scorers report"""
        print(f"\n{'='*60}")
        print(f"       🏆 TOP {limit} RUN SCORERS 🏆")
        print(f"{'='*60}\n")
        
        scorers = self.get_top_scorers(limit)
        
        print(f"{'Rank':<6} {'Name':<20} {'Team':<6} {'Runs':<8} {'Avg':<8} {'Matches'}")
        print("-" * 60)
        
        for i, (name, team, runs, avg, matches) in enumerate(scorers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"{medal:<6} {name:<20} {team:<6} {runs:<8} {avg:<8.2f} {matches}")
    
    def print_top_bowlers(self, limit=10):
        """Print formatted top bowlers report"""
        print(f"\n{'='*60}")
        print(f"       🎯 TOP {limit} WICKET TAKERS 🎯")
        print(f"{'='*60}\n")
        
        bowlers = self.get_top_wicket_takers(limit)
        
        print(f"{'Rank':<6} {'Name':<20} {'Team':<6} {'Wickets':<10} {'Avg':<8} {'Matches'}")
        print("-" * 60)
        
        for i, (name, team, wickets, avg, matches) in enumerate(bowlers, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"{medal:<6} {name:<20} {team:<6} {wickets:<10} {avg:<8.2f} {matches}")
    
    def print_team_stats(self):
        """Print formatted team statistics"""
        print(f"\n{'='*60}")
        print(f"       📊 TEAM STATISTICS 📊")
        print(f"{'='*60}\n")
        
        stats = self.get_team_stats()
        
        print(f"{'Team':<8} {'Players':<10} {'Total Runs':<12} {'Avg Bat':<10} {'Wickets'}")
        print("-" * 60)
        
        for team, count, runs, avg, wickets in stats:
            print(f"{team:<8} {count:<10} {runs:<12} {avg:<10.2f} {wickets}")
    
    # =========================================================================
    # VISUALIZATION METHODS
    # =========================================================================
    
    def visualize_stats(self):
        """Create comprehensive visualization dashboard"""
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("🏏 IPL Statistics Dashboard", fontsize=16, fontweight='bold')
        
        # Chart 1: Top 5 run scorers
        ax1 = axes[0, 0]
        scorers = self.get_top_scorers(5)
        names = [s[0].split()[-1] for s in scorers]  # Last names
        runs = [s[2] for s in scorers]
        colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#87CEEB', '#87CEEB']
        ax1.bar(names, runs, color=colors, edgecolor='black')
        ax1.set_title("🥇 Top 5 Run Scorers")
        ax1.set_ylabel("Runs")
        for i, v in enumerate(runs):
            ax1.text(i, v + 100, f'{v:,}', ha='center', fontsize=9)
        
        # Chart 2: Team total runs (pie)
        ax2 = axes[0, 1]
        team_stats = self.get_team_stats()
        teams = [t[0] for t in team_stats]
        team_runs = [t[2] for t in team_stats]
        ax2.pie(team_runs, labels=teams, autopct='%1.1f%%', startangle=90)
        ax2.set_title("📊 Team Run Distribution")
        
        # Chart 3: Top 5 wicket takers
        ax3 = axes[1, 0]
        bowlers = self.get_top_wicket_takers(5)
        b_names = [b[0].split()[-1] for b in bowlers]
        wickets = [b[2] for b in bowlers]
        ax3.barh(b_names, wickets, color=['#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#f39c12'])
        ax3.set_title("🎯 Top 5 Wicket Takers")
        ax3.set_xlabel("Wickets")
        ax3.invert_yaxis()
        
        # Chart 4: Match wins by team
        ax4 = axes[1, 1]
        match_stats = self.get_match_stats()
        win_teams = [m[0] for m in match_stats]
        wins = [m[1] for m in match_stats]
        ax4.bar(win_teams, wins, color='#3498db', edgecolor='black')
        ax4.set_title("🏆 Match Wins by Team")
        ax4.set_ylabel("Wins")
        ax4.set_xlabel("Team")
        
        plt.tight_layout()
        plt.show()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Main program entry point"""
    
    print("=" * 60)
    print("       🏏 CRICKET STATISTICS DATABASE 🏏")
    print("=" * 60)
    print()
    
    # Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "cricket_stats.db")
    players_csv = os.path.join(script_dir, "..", "data", "ipl_players.csv")
    matches_csv = os.path.join(script_dir, "..", "data", "cricket_scores.csv")
    
    # Remove old database for fresh start
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Initialize database
    db = CricketDatabase(db_path)
    db.connect()
    db.create_tables()
    
    # Import data
    print()
    print("📥 Importing data...")
    db.import_players_from_csv(players_csv)
    db.import_matches_from_csv(matches_csv)
    db.setup_teams()
    
    # Generate reports
    db.print_top_scorers(5)
    db.print_top_bowlers(5)
    db.print_team_stats()
    
    # Interactive search demo
    print(f"\n{'='*60}")
    print("       🔍 SEARCH DEMO 🔍")
    print(f"{'='*60}\n")
    
    print("Searching for CSK players:")
    csk_players = db.search_players(team="CSK")
    for p in csk_players:
        print(f"  • {p[1]} - {p[5]} runs")
    
    print("\nSearching for players with 3000+ runs:")
    high_scorers = db.search_players(min_runs=3000)
    for p in high_scorers:
        print(f"  • {p[1]} ({p[2]}) - {p[5]} runs")
    
    # Visualize
    print("\n📊 Generating visualization dashboard...")
    db.visualize_stats()
    
    # Cleanup
    db.close()
    print(f"\n📁 Database saved to: {db_path}")
    print("✅ Project complete!")


if __name__ == "__main__":
    main()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD A VENUE ANALYSIS
    Add a method to find which venues have the most high-scoring matches:
    
    def get_venue_stats(self):
        query = '''
        SELECT venue, 
               COUNT(*) as matches,
               AVG(team1_score + team2_score) as avg_total
        FROM matches
        GROUP BY venue
        ORDER BY avg_total DESC;
        '''

Challenge 2: ADD PLAYER COMPARISON
    Create a method to compare two players:
    
    def compare_players(self, player1, player2):
        '''Fetch both players and show side-by-side comparison'''

Challenge 3: ADD DATA EXPORT
    Create a method to export query results back to CSV:
    
    def export_to_csv(self, query, output_file):
        '''Execute query and write results to CSV file'''

Challenge 4: ADD SEASON FILTER
    Modify match queries to filter by season:
    
    def get_season_winners(self, season):
        '''Get all winners for a specific season'''

Challenge 5: CREATE A FULL MENU
    Wrap everything in an interactive menu:
    - View top scorers
    - View top bowlers
    - Search players
    - Team analysis
    - Compare players
    - Generate charts
    - Exit
"""

# =============================================================================
# WHAT YOU'VE BUILT
# =============================================================================
"""
🎉 CONGRATULATIONS! You've built a complete database application!

SKILLS DEMONSTRATED:
    ✅ Database creation and connection
    ✅ Table design with proper data types
    ✅ CSV data import
    ✅ Safe parameterized queries
    ✅ SQL SELECT with WHERE, ORDER BY, GROUP BY
    ✅ Aggregate functions (COUNT, SUM, AVG)
    ✅ Data visualization with matplotlib
    ✅ Object-oriented programming (classes)
    ✅ Code organization and documentation

🔗 FUTURE TOOL CONNECTIONS:
    This project structure maps directly to:
    - n8n database workflows
    - REST API backends
    - Data analysis pipelines
    - Business intelligence dashboards
    
    The patterns you learned here are used in
    professional data applications everywhere!
"""
