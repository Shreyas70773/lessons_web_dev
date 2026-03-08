"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    FINAL PROJECT: Live Cricket Dashboard
===============================================================================

🎯 PROJECT GOAL:
    Build a complete live cricket dashboard that:
    - Fetches match data (simulated API)
    - Stores data in SQLite database
    - Analyzes statistics
    - Generates visual charts
    - Can be easily extended for n8n integration

🧠 CONCEPTS COMBINED:
    ✅ Variables and data types       ✅ Functions and composition
    ✅ If/else conditions             ✅ Loops and iterations
    ✅ Lists and dictionaries         ✅ CSV and JSON handling  
    ✅ SQLite database operations     ✅ Data visualization
    ✅ API patterns                   ✅ n8n workflow concepts

===============================================================================
"""

import sqlite3
import json
import os
import random
import matplotlib.pyplot as plt
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "live_dashboard.db")
JSON_PATH = os.path.join(SCRIPT_DIR, "..", "data", "sample_api_response.json")

# Teams in IPL
IPL_TEAMS = ["MI", "CSK", "RCB", "KKR", "DC", "PBKS", "RR", "SRH", "GT", "LSG"]

# =============================================================================
# MOCK API SERVICE
# =============================================================================

class CricketAPIService:
    """
    Simulates a cricket API service.
    
    In a real application, this would use requests.get() to call an actual API.
    This mock version generates realistic random data for learning.
    
    🔗 FUTURE TOOL: Replace this with real API calls when ready!
    """
    
    def __init__(self, json_path):
        """Initialize with path to sample data"""
        self.json_path = json_path
        self.last_update = datetime.now()
    
    def get_live_matches(self, num_matches=3):
        """
        Get live match data.
        
        Returns:
            List of match dictionaries with live scores
        """
        matches = []
        
        # Get random unique team pairs
        available_teams = IPL_TEAMS.copy()
        random.shuffle(available_teams)
        
        for i in range(num_matches):
            team1 = available_teams[i * 2]
            team2 = available_teams[i * 2 + 1]
            
            # Generate realistic scores
            team1_runs = random.randint(120, 220)
            team2_runs = random.randint(0, team1_runs + 30)  # Chasing or completed
            
            overs = random.choice([15.3, 16.2, 17.4, 18.1, 19.3, 20.0])
            wickets = random.randint(3, 9)
            
            match = {
                "match_id": f"IPL-2024-{100 + i}",
                "team1": team1,
                "team2": team2,
                "team1_score": team1_runs,
                "team1_wickets": random.randint(4, 10),
                "team2_score": team2_runs,
                "team2_wickets": wickets,
                "overs": overs,
                "required_rate": round((team1_runs - team2_runs) / ((20 - overs) if overs < 20 else 0.1), 2),
                "venue": random.choice(["Wankhede", "Chinnaswamy", "Chepauk", "Eden Gardens", "Narendra Modi"]),
                "status": random.choice(["Live", "In Progress", "Innings Break"]) if team2_runs < team1_runs else "Completed",
                "timestamp": datetime.now().isoformat()
            }
            
            # Determine winner if completed
            if match["status"] == "Completed":
                match["winner"] = team1 if team1_runs > team2_runs else team2
            
            matches.append(match)
        
        return matches
    
    def get_match_details(self, match_id):
        """
        Get detailed information for a specific match.
        Uses our sample JSON file for detailed data.
        """
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return {"error": "Match not found"}
    
    def get_player_stats(self, player_name):
        """Get statistics for a specific player"""
        # Mock player stats
        return {
            "name": player_name,
            "matches": random.randint(80, 200),
            "runs": random.randint(2000, 6000),
            "average": round(random.uniform(25, 50), 2),
            "strike_rate": round(random.uniform(120, 160), 2),
            "centuries": random.randint(0, 6),
            "fifties": random.randint(10, 40)
        }


# =============================================================================
# DATABASE MANAGER
# =============================================================================

class DashboardDatabase:
    """
    Manages the SQLite database for the dashboard.
    
    Provides methods to store and retrieve match data.
    """
    
    def __init__(self, db_path):
        """Initialize with database path"""
        self.db_path = db_path
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish database connection"""
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
    
    def setup_tables(self):
        """Create necessary tables"""
        
        # Match scores table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS match_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id TEXT UNIQUE,
            team1 TEXT,
            team2 TEXT,
            team1_score INTEGER,
            team1_wickets INTEGER,
            team2_score INTEGER,
            team2_wickets INTEGER,
            venue TEXT,
            status TEXT,
            winner TEXT,
            timestamp TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Activity log table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            details TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        self.connection.commit()
    
    def save_match(self, match_data):
        """Save or update match data"""
        self.cursor.execute("""
        INSERT OR REPLACE INTO match_scores 
        (match_id, team1, team2, team1_score, team1_wickets, 
         team2_score, team2_wickets, venue, status, winner, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            match_data['match_id'],
            match_data['team1'],
            match_data['team2'],
            match_data['team1_score'],
            match_data['team1_wickets'],
            match_data['team2_score'],
            match_data['team2_wickets'],
            match_data['venue'],
            match_data['status'],
            match_data.get('winner', ''),
            match_data['timestamp']
        ))
        self.connection.commit()
    
    def log_activity(self, action, details):
        """Log an activity"""
        self.cursor.execute("""
        INSERT INTO activity_log (action, details) VALUES (?, ?);
        """, (action, details))
        self.connection.commit()
    
    def get_all_matches(self):
        """Get all stored matches"""
        self.cursor.execute("SELECT * FROM match_scores ORDER BY timestamp DESC;")
        return self.cursor.fetchall()
    
    def get_team_wins(self):
        """Get win count by team"""
        self.cursor.execute("""
        SELECT winner, COUNT(*) as wins 
        FROM match_scores 
        WHERE winner != '' AND winner IS NOT NULL
        GROUP BY winner 
        ORDER BY wins DESC;
        """)
        return self.cursor.fetchall()
    
    def get_high_scoring_matches(self, min_total=350):
        """Get matches with high total scores"""
        self.cursor.execute("""
        SELECT team1, team2, team1_score, team2_score, (team1_score + team2_score) as total
        FROM match_scores
        WHERE (team1_score + team2_score) > ?
        ORDER BY total DESC;
        """, (min_total,))
        return self.cursor.fetchall()


# =============================================================================
# DASHBOARD ANALYTICS
# =============================================================================

class DashboardAnalytics:
    """
    Provides analytical functions for the dashboard.
    
    Analyzes match data and generates insights.
    """
    
    @staticmethod
    def analyze_match(match_data):
        """
        Analyze a single match and return insights.
        """
        insights = []
        
        total_runs = match_data['team1_score'] + match_data['team2_score']
        run_diff = abs(match_data['team1_score'] - match_data['team2_score'])
        
        # High scoring match
        if total_runs > 380:
            insights.append("🔥 HIGH-SCORING THRILLER!")
        
        # Close match
        if run_diff < 15 and match_data['status'] in ['Completed', 'Live']:
            insights.append("⚡ NAIL-BITING FINISH!")
        
        # One-sided
        if run_diff > 60:
            winner = match_data['team1'] if match_data['team1_score'] > match_data['team2_score'] else match_data['team2']
            insights.append(f"💪 DOMINANT PERFORMANCE by {winner}!")
        
        # Required rate analysis
        if 'required_rate' in match_data and match_data['required_rate'] > 12:
            insights.append(f"📈 High required rate: {match_data['required_rate']} RPO")
        
        return insights
    
    @staticmethod
    def get_match_summary(match_data):
        """Generate a text summary of the match"""
        summary = f"""
╔══════════════════════════════════════════════════════════════╗
║  {match_data['team1']:^10} vs {match_data['team2']:^10}  -  {match_data['venue']:<20}  ║
╠══════════════════════════════════════════════════════════════╣
║  {match_data['team1']}: {match_data['team1_score']}/{match_data['team1_wickets']:<10}                                    ║
║  {match_data['team2']}: {match_data['team2_score']}/{match_data['team2_wickets']:<10}  ({match_data['overs']} overs)                  ║
╠══════════════════════════════════════════════════════════════╣
║  Status: {match_data['status']:<52} ║
╚══════════════════════════════════════════════════════════════╝"""
        return summary


# =============================================================================
# VISUALIZATION
# =============================================================================

class DashboardVisualizer:
    """
    Generates visualizations for the dashboard.
    """
    
    @staticmethod
    def create_dashboard(matches, db):
        """Create a comprehensive dashboard visualization"""
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("🏏 IPL LIVE DASHBOARD 🏏", fontsize=18, fontweight='bold')
        
        # Chart 1: Current match scores
        ax1 = axes[0, 0]
        match_labels = [f"{m['team1']} vs {m['team2']}" for m in matches]
        scores1 = [m['team1_score'] for m in matches]
        scores2 = [m['team2_score'] for m in matches]
        
        x = range(len(matches))
        width = 0.35
        ax1.bar([i - width/2 for i in x], scores1, width, label='Team 1', color='#3498db')
        ax1.bar([i + width/2 for i in x], scores2, width, label='Team 2', color='#e74c3c')
        ax1.set_xlabel('Matches')
        ax1.set_ylabel('Runs')
        ax1.set_title('📊 Current Match Scores')
        ax1.set_xticks(x)
        ax1.set_xticklabels([f"{m['team1']}\nvs\n{m['team2']}" for m in matches])
        ax1.legend()
        
        # Chart 2: Win distribution (if data available)
        ax2 = axes[0, 1]
        wins = db.get_team_wins()
        if wins:
            teams = [w[0] for w in wins]
            win_counts = [w[1] for w in wins]
            colors = plt.cm.Set3(range(len(teams)))
            ax2.pie(win_counts, labels=teams, autopct='%1.0f%%', colors=colors)
            ax2.set_title('🏆 Win Distribution')
        else:
            ax2.text(0.5, 0.5, 'No completed matches yet', ha='center', va='center')
            ax2.set_title('🏆 Win Distribution')
        
        # Chart 3: Runs per over (simulated)
        ax3 = axes[1, 0]
        if matches:
            match = matches[0]
            overs = list(range(1, int(float(match['overs'])) + 1))
            # Simulate run progression
            runs_per_over = [random.randint(4, 15) for _ in overs]
            cumulative = []
            total = 0
            for r in runs_per_over:
                total += r
                cumulative.append(total)
            
            ax3.plot(overs, cumulative, 'b-', marker='o', linewidth=2)
            ax3.fill_between(overs, cumulative, alpha=0.3)
            ax3.set_xlabel('Overs')
            ax3.set_ylabel('Cumulative Runs')
            ax3.set_title(f'📈 Run Progression: {match["team2"]}')
            ax3.grid(True, alpha=0.3)
        
        # Chart 4: Match status
        ax4 = axes[1, 1]
        statuses = [m['status'] for m in matches]
        status_counts = {}
        for s in statuses:
            status_counts[s] = status_counts.get(s, 0) + 1
        
        ax4.bar(status_counts.keys(), status_counts.values(), color=['#2ecc71', '#f39c12', '#9b59b6'])
        ax4.set_ylabel('Count')
        ax4.set_title('🎯 Match Status Distribution')
        
        plt.tight_layout()
        plt.show()


# =============================================================================
# N8N INTEGRATION HELPERS
# =============================================================================

def prepare_for_n8n(matches):
    """
    Prepare match data in a format ready for n8n webhook.
    
    This function shows how you would format data for n8n integration.
    """
    n8n_payload = {
        "workflow": "cricket-dashboard",
        "timestamp": datetime.now().isoformat(),
        "data": {
            "total_matches": len(matches),
            "matches": [],
            "alerts": []
        }
    }
    
    for match in matches:
        # Simplified match data for n8n
        match_simple = {
            "id": match['match_id'],
            "title": f"{match['team1']} vs {match['team2']}",
            "score": f"{match['team1_score']}/{match['team1_wickets']} vs {match['team2_score']}/{match['team2_wickets']}",
            "status": match['status']
        }
        n8n_payload['data']['matches'].append(match_simple)
        
        # Generate alerts for close matches
        if abs(match['team1_score'] - match['team2_score']) < 20:
            n8n_payload['data']['alerts'].append({
                "type": "close_match",
                "match": match['match_id'],
                "message": f"Close match! {match['team1']} vs {match['team2']}"
            })
    
    return n8n_payload


def webhook_endpoint_example():
    """
    Example of how you might expose this as a webhook for n8n.
    
    In a real application, you would use Flask or FastAPI:
    
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/api/matches', methods=['GET'])
    def get_matches():
        api = CricketAPIService(JSON_PATH)
        matches = api.get_live_matches()
        return jsonify(matches)
    
    @app.route('/webhook/n8n', methods=['POST'])
    def n8n_webhook():
        # n8n sends data here
        data = request.json
        # Process the data
        return jsonify({"status": "received"})
    """
    pass


# =============================================================================
# MAIN DASHBOARD APPLICATION
# =============================================================================

def run_dashboard():
    """Main dashboard application entry point"""
    
    print("=" * 70)
    print("       🏏 IPL LIVE CRICKET DASHBOARD 🏏")
    print("=" * 70)
    print()
    
    # Initialize components
    print("⚙️  Initializing dashboard components...")
    
    # Clean start
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    api = CricketAPIService(JSON_PATH)
    db = DashboardDatabase(DB_PATH)
    analytics = DashboardAnalytics()
    
    # Setup database
    db.connect()
    db.setup_tables()
    db.log_activity("startup", "Dashboard initialized")
    print("   ✅ Database ready")
    
    # Fetch live matches
    print("\n🌐 Fetching live matches...")
    matches = api.get_live_matches(3)
    print(f"   ✅ Retrieved {len(matches)} live matches")
    
    # Store matches in database
    print("\n💾 Storing match data...")
    for match in matches:
        db.save_match(match)
    print(f"   ✅ Saved {len(matches)} matches to database")
    
    # Display match summaries
    print("\n" + "=" * 70)
    print("       📋 LIVE MATCH SUMMARIES")
    print("=" * 70)
    
    for match in matches:
        print(analytics.get_match_summary(match))
        
        insights = analytics.analyze_match(match)
        if insights:
            print("   📌 Insights:")
            for insight in insights:
                print(f"      • {insight}")
        print()
    
    # Prepare n8n payload (demonstration)
    print("=" * 70)
    print("       🔗 N8N INTEGRATION PAYLOAD")
    print("=" * 70)
    print()
    
    n8n_data = prepare_for_n8n(matches)
    print("Payload ready for n8n webhook:")
    print(json.dumps(n8n_data, indent=2))
    print()
    
    # Generate visualizations
    print("=" * 70)
    print("       📊 GENERATING VISUALIZATIONS")
    print("=" * 70)
    print()
    
    print("Creating dashboard charts...")
    DashboardVisualizer.create_dashboard(matches, db)
    
    # Cleanup
    db.close()
    
    print("\n" + "=" * 70)
    print("       ✅ DASHBOARD SESSION COMPLETE")
    print("=" * 70)
    print()
    print(f"📁 Database saved: {DB_PATH}")
    print("🎉 Congratulations! You've completed the Python Power User Course!")
    print()


if __name__ == "__main__":
    run_dashboard()


# =============================================================================
# 🔥 EXTENSION CHALLENGES
# =============================================================================
"""
You've completed the course! Here are challenges to keep growing:

CHALLENGE 1: ADD REAL API
    Replace CricketAPIService with actual API calls:
    - Use cricketdata.org API or similar
    - Handle API keys and authentication
    - Add error handling for network issues

CHALLENGE 2: BUILD A WEB INTERFACE  
    Create a Flask web app:
    - Display live scores on a webpage
    - Auto-refresh every 30 seconds
    - Mobile-friendly design

CHALLENGE 3: CREATE N8N WORKFLOWS
    Build these in actual n8n:
    - Score alert to Telegram when MI plays
    - Daily summary email at 10 PM
    - Google Sheets logging of all match results

CHALLENGE 4: ADD HISTORICAL ANALYSIS
    - Track stats over time
    - Win/loss trends by team
    - Best performing players

CHALLENGE 5: NOTIFICATIONS
    - Send alerts via email (smtplib)
    - Telegram bot integration
    - Desktop notifications

CHALLENGE 6: MACHINE LEARNING (Advanced!)
    - Predict match winners
    - Forecast player performance
    - Score predictions
"""

# =============================================================================
# WHAT YOU'VE ACCOMPLISHED
# =============================================================================
"""
🎓 PYTHON POWER USER COURSE - COMPLETE!

You've mastered:

📘 PHASE 1: DRAWING & VARIABLES
   • Variables, data types, print statements
   • Turtle graphics basics
   • For loops and shapes
   • Colors and parameters

📘 PHASE 2: LOGIC & DECISIONS
   • If/else conditions
   • Type casting and comparisons
   • While loops
   • Boolean logic and compound conditions

📘 PHASE 3: DATA STRUCTURES
   • Lists and indexing
   • List methods and sorting
   • Dictionaries (key-value pairs)
   • Loops on collections

📘 PHASE 4: FUNCTIONS
   • Defining and calling functions
   • Parameters and return values
   • Function composition
   • Scope and variable visibility

📘 PHASE 5: DATA MANAGEMENT
   • Reading CSV files
   • SQLite database operations
   • SQL queries (SELECT, WHERE, ORDER BY)
   • Parameterized queries (security!)

📘 PHASE 6: AUTOMATION
   • API requests and HTTP
   • JSON parsing and manipulation
   • n8n workflow thinking
   • Building complete applications

🔗 FUTURE TOOL READINESS:
   • SQL: You understand tables, queries, and relationships
   • n8n: You think in workflows and data transformations
   • APIs: You can fetch, parse, and use web data
   • Automation: You can build end-to-end solutions

🚀 NEXT STEPS:
   1. Install n8n and recreate this dashboard as a workflow
   2. Connect to real APIs
   3. Build your own automation projects
   4. Learn web development (Flask/Django)
   5. Explore data science (Pandas, NumPy)

You're now a Python Power User! 🏏⚡
"""
