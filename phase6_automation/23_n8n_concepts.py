"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 23: n8n Concepts - Thinking in Workflows!
===============================================================================

In this session, you'll learn:
    ✅ What n8n is and why it's powerful
    ✅ Workflow thinking - breaking tasks into steps
    ✅ How Python skills transfer to n8n
    ✅ Designing automation workflows

===============================================================================
"""

import json
import os

# =============================================================================
# WHAT IS N8N?
# =============================================================================

print("=" * 60)
print("       ⚡ UNDERSTANDING N8N ⚡")
print("=" * 60)
print()

"""
n8n (pronounced "n-eight-n") is a WORKFLOW AUTOMATION tool.

Think of it like connecting LEGO blocks:
    • Each block (node) does ONE thing
    • Blocks connect together in a chain
    • Data flows from one block to the next
    • You build complex automations visually!

Real-world examples:
    📧 Email received → Save attachment to Google Drive → Notify on Slack
    🏏 Cricket API → Filter exciting matches → Send SMS alert
    📊 CSV file → Transform data → Insert into database → Send report
    
n8n has 400+ pre-built nodes for:
    • Email (Gmail, Outlook)
    • Databases (MySQL, Postgres, SQLite)
    • APIs and Webhooks
    • Google services (Sheets, Drive, Calendar)
    • Social media (Twitter, Instagram, Telegram)
    • And much more!

The BEST PART: Everything you learned in Python maps to n8n!
"""

print("""
n8n Visual Workflow:

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │ Trigger  │ ──▶ │   HTTP   │ ──▶ │   Code   │ ──▶ │  Slack   │
    │ (Manual) │     │ Request  │     │ (Filter) │     │ Message  │
    └──────────┘     └──────────┘     └──────────┘     └──────────┘
         │                │                │                │
         │                │                │                │
    "Start!"      "Get cricket      "Find close      "Alert: 
                   scores"          matches"        Close match!"

Each box is a NODE. Data flows left to right.
""")

# =============================================================================
# PYTHON → N8N CONCEPT MAPPING
# =============================================================================

print("=" * 60)
print("       🔄 PYTHON TO N8N MAPPING 🔄")
print("=" * 60)
print()

print("""
Everything you learned in Python has an n8n equivalent!

┌─────────────────────────────────────────────────────────────────┐
│           PYTHON CONCEPT          →    N8N EQUIVALENT          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Variables                        →    Workflow Variables       │
│  player_name = "Virat"                 {{$vars.player_name}}    │
│                                                                 │
│  requests.get(url)                →    HTTP Request Node        │
│  response = requests.get(api)          Configure URL, Method    │
│                                                                 │
│  json.loads() / json.dumps()      →    Automatic! n8n uses JSON │
│                                                                 │
│  if/else conditions               →    IF Node                  │
│  if score > 300:                       Condition: score > 300   │
│                                                                 │
│  for loop                         →    Split In Batches Node    │
│  for player in players:                Or: Loop over each item  │
│                                                                 │
│  Functions                        →    Sub-workflows            │
│  def process(data):                    Create, reuse anywhere   │
│                                                                 │
│  List filtering                   →    Filter Node / IF Node    │
│  [p for p in players if ok]            Filter items by condition│
│                                                                 │
│  Dictionary access                →    Expression: {{$json.key}}│
│  player['name']                         Access with dot notation│
│                                                                 │
│  SQL queries                      →    Database Nodes           │
│  cursor.execute("SELECT...")           Configure SQL visually   │
│                                                                 │
│  try/except                       →    Error Handling Branch    │
│  Handle errors gracefully              Continue On Fail option  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
""")

# =============================================================================
# WORKFLOW THINKING
# =============================================================================

print("=" * 60)
print("       🧠 THINKING IN WORKFLOWS 🧠")
print("=" * 60)
print()

"""
WORKFLOW THINKING = Breaking a task into sequential steps

This is EXACTLY what we've been doing in Python!
Each function/block of code = one node in n8n

Let's design a workflow: "IPL Match Alert System"
"""

print("""
TASK: Alert me when a close match is happening

Step 1: THINK about what needs to happen
    "I want to get cricket scores, check if any match is close,
     and send me a message if so."

Step 2: BREAK into individual steps
    1. Get live scores (HTTP Request)
    2. Parse the JSON response (automatic in n8n)
    3. Check each match (Loop)
    4. Is the score close? (IF condition)
    5. If yes, send alert (Slack/Email/SMS)
    6. If no, do nothing

Step 3: VISUALIZE the workflow
    
    ┌──────────────┐
    │   Schedule   │  ← "Every 5 minutes"
    │   Trigger    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │     HTTP     │  ← "GET api.cricket.com/live"
    │   Request    │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │   Loop Over  │  ← "For each match in response"
    │    Items     │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │      IF      │  ← "Is score difference < 20?"
    │   Condition  │
    └───┬─────┬────┘
        │     │
    TRUE│     │FALSE
        ▼     ▼
    ┌───────┐ ┌───────┐
    │ Send  │ │ No    │
    │ Alert │ │ Op    │
    └───────┘ └───────┘
""")

# =============================================================================
# SIMULATING A WORKFLOW IN PYTHON
# =============================================================================

print("=" * 60)
print("       🎮 SIMULATING AN N8N WORKFLOW 🎮")
print("=" * 60)
print()

# Let's build the same workflow logic in Python
# This shows how our Python skills transfer!

def simulate_n8n_workflow():
    """
    Simulates an n8n workflow for cricket match alerts.
    
    Each function represents a node in the workflow.
    """
    
    # NODE 1: Trigger (we'll just start it)
    print("⚡ NODE 1: Trigger - Starting workflow...")
    
    # NODE 2: HTTP Request (we'll use mock data)
    print("🌐 NODE 2: HTTP Request - Getting live scores...")
    
    # Mock live match data (simulating API response)
    live_matches = [
        {
            "match_id": "ipl-2024-01",
            "team1": "MI",
            "team2": "CSK",
            "team1_score": 185,
            "team2_score": 178,
            "status": "In Progress",
            "overs_remaining": 2
        },
        {
            "match_id": "ipl-2024-02",
            "team1": "RCB",
            "team2": "KKR",
            "team1_score": 210,
            "team2_score": 145,
            "status": "In Progress",
            "overs_remaining": 4
        },
        {
            "match_id": "ipl-2024-03",
            "team1": "DC",
            "team2": "PBKS",
            "team1_score": 165,
            "team2_score": 160,
            "status": "In Progress",
            "overs_remaining": 1
        }
    ]
    
    print(f"   Received {len(live_matches)} matches")
    print()
    
    # NODE 3: Loop Over Items
    print("🔄 NODE 3: Loop Over Items - Processing each match...")
    
    alerts = []
    
    for match in live_matches:
        # NODE 4: IF Condition - Is it a close match?
        score_diff = abs(match['team1_score'] - match['team2_score'])
        is_close = score_diff < 20 and match['overs_remaining'] <= 3
        
        print(f"   📊 {match['team1']} vs {match['team2']}: "
              f"Diff={score_diff}, Close={is_close}")
        
        if is_close:
            # NODE 5: Send Alert (we'll just collect them)
            alert = {
                "message": f"🏏 CLOSE MATCH! {match['team1']} vs {match['team2']}",
                "details": f"Score: {match['team1_score']}-{match['team2_score']} "
                          f"({match['overs_remaining']} overs left!)",
                "match_id": match['match_id']
            }
            alerts.append(alert)
    
    print()
    
    # NODE 6: Output
    print("📤 NODE 6: Output - Sending alerts...")
    
    if alerts:
        for alert in alerts:
            print()
            print("   ┌" + "─" * 50 + "┐")
            print(f"   │ {alert['message']:<48} │")
            print(f"   │ {alert['details']:<48} │")
            print("   └" + "─" * 50 + "┘")
    else:
        print("   No close matches right now.")
    
    return alerts


# Run the simulated workflow
print("Running simulated n8n workflow...")
print("=" * 50)
results = simulate_n8n_workflow()
print()
print(f"✅ Workflow complete! Generated {len(results)} alerts.")
print()

# =============================================================================
# DATA TRANSFORMATION IN N8N
# =============================================================================

print("=" * 60)
print("       🔧 DATA TRANSFORMATION 🔧")
print("=" * 60)
print()

"""
n8n uses EXPRESSIONS to transform data (similar to Python!).

In n8n, you access data using:
    {{$json.key}}          - Access a field
    {{$json.player.name}}  - Nested access
    {{$json.runs > 100}}   - Condition
"""

# Example: Transform API response for downstream use
raw_data = {
    "match_info": {
        "id": "ipl-2024-final",
        "team1": "Mumbai Indians",
        "team2": "Chennai Super Kings",
        "venue": "Wankhede Stadium"
    },
    "scores": {
        "team1_runs": 180,
        "team1_wickets": 5,
        "team2_runs": 175,
        "team2_wickets": 8
    }
}

def transform_for_alert(data):
    """
    Transform raw API data into alert format.
    
    This is what a "Set" node or "Code" node does in n8n!
    """
    return {
        "title": f"{data['match_info']['team1']} vs {data['match_info']['team2']}",
        "venue": data['match_info']['venue'],
        "score_summary": f"{data['scores']['team1_runs']}/{data['scores']['team1_wickets']} vs "
                         f"{data['scores']['team2_runs']}/{data['scores']['team2_wickets']}",
        "winner": data['match_info']['team1'] 
                  if data['scores']['team1_runs'] > data['scores']['team2_runs'] 
                  else data['match_info']['team2'],
        "margin": abs(data['scores']['team1_runs'] - data['scores']['team2_runs'])
    }


transformed = transform_for_alert(raw_data)
print("Transformed data (for sending as alert):")
print(json.dumps(transformed, indent=2))
print()

# =============================================================================
# N8N WORKFLOW DESIGN EXERCISE
# =============================================================================

print("=" * 60)
print("       📝 DESIGN YOUR OWN WORKFLOWS 📝")
print("=" * 60)
print()

print("""
Practice designing workflows WITHOUT n8n - just on paper!

WORKFLOW 1: Gaming Score Reporter
─────────────────────────────────
"Every day at 6pm, get my gaming stats and email me a summary"

Design it:
    1. Schedule Trigger (5 PM daily)
    2. HTTP Request (get gaming API)
    3. Code/Set Node (format message)
    4. Email Node (send summary)

WORKFLOW 2: IPL Score Checker
─────────────────────────────────
"When RCB plays, if they're winning, tweet about it!"

Design it:
    1. Schedule Trigger (every 10 minutes during match hours)
    2. HTTP Request (get live scores)
    3. IF Node (is RCB playing?)
    4. IF Node (is RCB winning?)
    5. Twitter Node (post tweet)

WORKFLOW 3: Homework Reminder
─────────────────────────────────
"Every day check Google Calendar, if homework is due tomorrow, 
send me a WhatsApp message"

Design it:
    1. Schedule Trigger (7 PM daily)
    2. Google Calendar Node (get tomorrow's events)
    3. Filter Node (find "homework" events)
    4. IF Node (any homework found?)
    5. WhatsApp Node (send reminder)

YOUR TURN: Design a workflow for:
"Monitor product prices and alert when something goes on sale"
""")


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: DESIGN A WEATHER ALERT WORKFLOW
    Design nodes for: "If rain is predicted, remind me to take umbrella"
    
    Hint: What trigger? What API? What conditions? What alert?

Challenge 2: DESIGN A BIRTHDAY REMINDER
    Design: "Every morning, check if any friend's birthday is today,
            send them a WhatsApp message"
    
    What do you need?
    - Where is the birthday data stored?
    - How do you check today's date?
    - How do you send the message?

Challenge 3: BUILD A WORKFLOW SIMULATOR
    Create a Python class that can:
    - Add nodes
    - Connect nodes
    - Run the workflow step by step
    
    class Workflow:
        def add_node(self, name, action):
            ...
        def connect(self, from_node, to_node):
            ...
        def run(self):
            ...

Challenge 4: PRACTICE EXPRESSIONS
    Write the n8n expression for:
    a) Get player name from: {"player": {"name": "Virat"}}
       Answer: {{$json.player.name}}
    
    b) Check if runs > 100
       Answer: {{$json.runs > 100}}
    
    c) Get first match from array
       Answer: {{$json.matches[0]}}

Challenge 5: DRAW YOUR DREAM AUTOMATION
    Think of something you do repeatedly.
    Design an n8n workflow to automate it!
    Draw boxes and arrows on paper.
"""

# =============================================================================
# REFERENCE
# =============================================================================
"""
N8N CORE CONCEPTS:

TRIGGERS - Start a workflow
    • Manual Trigger (click to run)
    • Schedule Trigger (time-based)
    • Webhook (external events)
    • App triggers (email received, etc.)

ACTIONS - Do something
    • HTTP Request (call APIs)
    • Code (write JavaScript/Python)
    • Set (transform data)
    • Database operations
    • Send messages (Slack, Email, etc.)

LOGIC - Control flow
    • IF (branch based on condition)
    • Switch (multiple branches)
    • Loop (process items one by one)
    • Merge (combine branches)

EXPRESSIONS - Access data
    {{$json.field}}          - Current item's field
    {{$node["Name"].json}}   - Another node's data
    {{$vars.myVar}}          - Workflow variable

KEY INSIGHT:
    If you can write it in Python, you can build it in n8n!
    n8n just gives you a visual way to connect the pieces.
    
GETTING STARTED:
    1. Go to https://n8n.io
    2. Install locally or use cloud version
    3. Start with simple workflows
    4. Build up complexity gradually
"""
