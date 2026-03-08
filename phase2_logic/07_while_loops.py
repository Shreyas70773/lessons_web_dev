"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 7: While Loops - Cricket Innings Simulator!
===============================================================================

In this session, you'll learn:
    ✅ while loops - Repeat until a condition becomes false
    ✅ break - Exit a loop immediately  
    ✅ continue - Skip to the next iteration
    ✅ The danger of infinite loops!
    ✅ Simulating a cricket innings ball by ball

===============================================================================
"""

# =============================================================================
# ASCII FLOWCHART: How a WHILE LOOP Works
# =============================================================================
"""
                        START
                          │
                          ▼
         ┌────────────────────────────────┐
         │  Initialize: wickets = 0      │
         │              total_runs = 0   │
         └────────────────┬───────────────┘
                          │
                          │
            ┌─────────────▼────────────┐
            │  Is wickets < 10?        │◄────────────────────┐
            │  (condition check)       │                     │
            └─────────────┬────────────┘                     │
                          │                                  │
               ┌──────────┴──────────┐                       │
               │                     │                       │
             YES                    NO                       │
               │                     │                       │
               ▼                     ▼                       │
    ┌──────────────────┐    ┌──────────────────┐             │
    │  Ask for runs    │    │  Exit the loop   │             │
    │  (one ball)      │    │  (ALL OUT!)      │             │
    └────────┬─────────┘    └──────────────────┘             │
             │                                               │
             ▼                                               │
    ┌──────────────────┐                                     │
    │  Add to total    │                                     │
    │  Check if 'out'  │                                     │
    │  if out: wickets+│                                     │
    └────────┬─────────┘                                     │
             │                                               │
             └───────────────────────────────────────────────┘
             
🧠 LOGIC SEED: While loops = "Keep doing this UNTIL a condition is met"
This is EXACTLY how n8n Wait nodes and retry logic works!
"Wait UNTIL response received" or "Retry UNTIL success or 5 attempts"
"""

# =============================================================================
# WHILE LOOP VS FOR LOOP - WHEN TO USE EACH
# =============================================================================

"""
FOR LOOP:  Use when you KNOW exactly how many times to repeat
    for i in range(10):     # Exactly 10 times
    for player in team:     # Once per player

WHILE LOOP: Use when you DON'T KNOW how many times to repeat
    while wickets < 10:     # Until we're all out
    while not finished:     # Until user says stop
    while guesses_left > 0: # Until out of guesses

In cricket:
    - FOR: "Let's play exactly 20 overs" (T20 format)
    - WHILE: "Keep playing until all out" (Test cricket innings)
"""

# =============================================================================
# THE CRICKET INNINGS SIMULATOR
# =============================================================================

print("=" * 60)
print("       🏏 CRICKET INNINGS SIMULATOR 🏏")
print("=" * 60)
print()
print("Welcome! You're now the batsman.")
print("Enter runs scored each ball (0-6)")
print("Type 'out' if you got dismissed")
print("Type 'retire' to retire hurt")
print()
print("Your innings ends when 10 wickets fall!")
print("-" * 60)
print()

# Initialize the game state
wickets = 0           # How many batsmen are out
total_runs = 0        # Team's total score
balls_faced = 0       # Total balls in the innings
current_batsman = 1   # Who's batting (1-11)

# For tracking individual scores
batsmen_scores = []   # Will store each batsman's score

current_batsman_runs = 0  # Current batsman's score

# =============================================================================
# THE MAIN GAME LOOP
# =============================================================================

# While we still have wickets left (not all out)
while wickets < 10:
    
    # Show current status
    overs = balls_faced // 6
    balls_in_over = balls_faced % 6
    
    print(f"📊 Score: {total_runs}/{wickets} | Over: {overs}.{balls_in_over}")
    print(f"   Batsman #{current_batsman}: {current_batsman_runs} runs")
    
    # Get input for this ball
    ball_result = input("Enter runs (0-6) or 'out'/'retire': ").strip().lower()
    
    # Check if it's a special command
    if ball_result == 'out':
        # Batsman is dismissed!
        wickets += 1
        print(f"   ❌ OUT! Batsman #{current_batsman} dismissed for {current_batsman_runs}")
        
        # Save this batsman's score
        batsmen_scores.append((current_batsman, current_batsman_runs))
        
        # New batsman comes in
        current_batsman += 1
        current_batsman_runs = 0
        balls_faced += 1
        
        print()
        continue  # Skip to next loop iteration
        
    elif ball_result == 'retire':
        # Batsman retires (doesn't count as wicket)
        print(f"   🏥 Batsman #{current_batsman} retires hurt with {current_batsman_runs}")
        batsmen_scores.append((current_batsman, current_batsman_runs))
        current_batsman += 1
        current_batsman_runs = 0
        print()
        continue
        
    elif ball_result == 'quit':
        # User wants to end early
        print("   👋 Ending innings early...")
        break  # Exit the loop immediately!
        
    # Try to convert to runs
    try:
        runs = int(ball_result)
        
        # Validate the runs (must be 0-6)
        if runs < 0 or runs > 6:
            print("   ⚠️ Invalid! Runs must be 0-6. Try again.")
            continue  # Ask again without counting the ball
            
        # Valid runs scored!
        total_runs += runs
        current_batsman_runs += runs
        balls_faced += 1
        
        # Fun commentary based on runs
        if runs == 0:
            print("   • Dot ball")
        elif runs == 1:
            print("   • Single taken")
        elif runs == 2:
            print("   • Good running, two!")
        elif runs == 3:
            print("   • Three runs")
        elif runs == 4:
            print("   ⭐ FOUR! Boundary!")
        elif runs == 5:
            print("   • Five runs (overthrow?)")
        elif runs == 6:
            print("   🔥 SIX! Out of the park!")
            
    except ValueError:
        print("   ⚠️ Please enter a number (0-6) or 'out'")
        continue
    
    print()

# =============================================================================
# INNINGS COMPLETE - SHOW FINAL SCORECARD
# =============================================================================

print()
print("=" * 60)
print("       🏏 INNINGS COMPLETE! ALL OUT! 🏏" if wickets == 10 else "       🏏 INNINGS ENDED 🏏")
print("=" * 60)
print()

# Calculate statistics
overs = balls_faced // 6
balls = balls_faced % 6
if balls_faced > 0:
    run_rate = (total_runs / balls_faced) * 6
else:
    run_rate = 0

print(f"📊 FINAL SCORE: {total_runs}/{wickets}")
print(f"📊 OVERS: {overs}.{balls}")
print(f"📊 RUN RATE: {run_rate:.2f}")
print()

# Show individual scores
print("🏏 BATTING SCORECARD:")
print("-" * 40)
for batsman_num, score in batsmen_scores:
    print(f"   Batsman #{batsman_num}: {score} runs")
    
# Current batsman (not out)
if wickets < 10:
    print(f"   Batsman #{current_batsman}: {current_batsman_runs}* (not out)")
    batsmen_scores.append((current_batsman, current_batsman_runs))

print("-" * 40)

# Find top scorer
if batsmen_scores:
    top_scorer = max(batsmen_scores, key=lambda x: x[1])
    print(f"🏆 TOP SCORER: Batsman #{top_scorer[0]} with {top_scorer[1]} runs")

# Performance message
if total_runs >= 200:
    print("🔥 AMAZING! A score above 200!")
elif total_runs >= 150:
    print("⭐ Great score! Above 150!")
elif total_runs >= 100:
    print("👍 Decent total. Above 100.")
else:
    print("📉 Low score. Team needs to improve!")

print()


# =============================================================================
# UNDERSTANDING BREAK AND CONTINUE
# =============================================================================

"""
BREAK vs CONTINUE:

BREAK - Exit the loop completely
    while True:
        if should_stop:
            break  # Exits the while loop entirely
        # This code runs if no break
    # Code continues here after break

CONTINUE - Skip to the next iteration
    while condition:
        if should_skip:
            continue  # Goes back to "while condition"
        # This code only runs if no continue
        
Example with numbers:
    for i in range(10):
        if i == 3:
            continue  # Skip 3, go to 4
        if i == 7:
            break     # Stop at 7, exit loop
        print(i)
    
    Output: 0, 1, 2, 4, 5, 6 (no 3 because continue, no 7+ because break)
"""

# 🔗 FUTURE TOOL: While loops are used in:
# - Retry logic: "Keep trying until success or max attempts"
# - Waiting: "Wait until file exists"  
# - Processing: "Process items until queue is empty"
# In n8n, the "Wait" node pauses UNTIL a condition is met - same concept!


# =============================================================================
# ⚠️ INFINITE LOOP WARNING
# =============================================================================

"""
DANGER: INFINITE LOOPS!

This loop NEVER ends:
    while True:
        print("Forever...")
        
This loop NEVER ends (condition never becomes False):
    x = 1
    while x > 0:
        x = x + 1  # x keeps growing, always > 0!

ALWAYS make sure your loop's condition will eventually become False!

If you're stuck in an infinite loop, press Ctrl+C to stop the program.
"""


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD AN OVER LIMIT
    - Modify the loop so it also ends after 20 overs (T20 format)
    - Change the condition to:
        while wickets < 10 and balls_faced < 120:  # 20 overs × 6 balls
    - Print a different message if innings ended due to over limit

Challenge 2: EXTRAS
    - Add handling for 'wide' and 'noball'
    - Wide: +1 run, ball doesn't count (don't increment balls_faced)
    - No ball: +1 run + whatever runs scored, ball doesn't count

Challenge 3: COUNT THE BOUNDARIES
    - Create variables: total_fours = 0, total_sixes = 0
    - Increment them when 4 or 6 is scored
    - Print boundary count in the final scorecard

Challenge 4: MAKE IT A LOOP
    - After one innings, ask "Play another innings? (yes/no)"
    - If yes, reset everything and play again
    - This is a LOOP INSIDE A LOOP! (nested loops)

Challenge 5: PREDICT THE OUTPUT
    count = 0
    while count < 5:
        if count == 2:
            count += 1
            continue
        print(count)
        count += 1
    
    What numbers print? Why?
    (Answer: 0, 1, 3, 4 - because 2 is skipped by continue)

Challenge 6: DANGER ZONE
    Can you spot why this is an infinite loop?
    
    wickets = 0
    while wickets < 10:
        print("Still batting...")
        # Oops! We never update wickets!
    
    ALWAYS make sure something inside the loop can change the condition!
"""
