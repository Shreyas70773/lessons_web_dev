"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    PROJECT: Smart Report Card System
===============================================================================

🎓 WHAT THIS PROJECT DOES:
    Enter marks for 5 CBSE subjects → Python calculates total, percentage,
    grade, pass/fail for each subject → Displays a color-coded bar chart!

🧠 CONCEPTS YOU'LL USE:
    ✅ input() and type casting
    ✅ while loops for validation
    ✅ if/elif/else for grading
    ✅ Lists to store subjects and marks
    ✅ matplotlib for visualization

===============================================================================
"""

# We need matplotlib for the bar chart
# If you don't have it, run: pip install matplotlib
import matplotlib.pyplot as plt

# =============================================================================
# SETUP - SUBJECTS AND DATA
# =============================================================================

print("=" * 60)
print("       🎓 SMART REPORT CARD SYSTEM 🎓")
print("=" * 60)
print()
print("Enter marks (0-100) for each subject.")
print("The system will calculate grades and show a visual report!")
print()

# CBSE subjects for Class 7
subjects = ["Mathematics", "Science", "English", "Hindi", "Social Studies"]

# We'll store marks, grades, and pass/fail status
marks = []
grades = []
pass_fail = []

# =============================================================================
# GET MARKS WITH VALIDATION
# =============================================================================

for subject in subjects:
    valid = False
    
    while not valid:
        try:
            mark = int(input(f"Enter marks for {subject}: "))
            
            # Validate range
            if mark < 0 or mark > 100:
                print("   ⚠️ Marks must be between 0 and 100!")
            else:
                valid = True
                marks.append(mark)
                
        except ValueError:
            print("   ⚠️ Please enter a valid number!")

print()
print("✅ All marks entered successfully!")
print()

# =============================================================================
# CALCULATE GRADES (if/elif/else Chain)
# =============================================================================

"""
CBSE Grading System:
    A1: 91-100 (Excellent)
    A2: 81-90  (Very Good)
    B1: 71-80  (Good)
    B2: 61-70  (Above Average)
    C1: 51-60  (Average)
    C2: 41-50  (Below Average)
    D:  33-40  (Pass)
    E:  Below 33 (Fail)
    
Pass marks: 33
"""

def get_grade(mark):
    """Returns grade based on marks using CBSE grading"""
    if mark >= 91:
        return "A1"
    elif mark >= 81:
        return "A2"
    elif mark >= 71:
        return "B1"
    elif mark >= 61:
        return "B2"
    elif mark >= 51:
        return "C1"
    elif mark >= 41:
        return "C2"
    elif mark >= 33:
        return "D"
    else:
        return "E"


def is_pass(mark):
    """Returns True if passed (>= 33), False if failed"""
    return mark >= 33


# Calculate grades and pass/fail for each subject
for mark in marks:
    grades.append(get_grade(mark))
    pass_fail.append("PASS" if is_pass(mark) else "FAIL")

# =============================================================================
# CALCULATE TOTALS AND PERCENTAGES
# =============================================================================

total_marks = sum(marks)
max_marks = len(subjects) * 100
percentage = (total_marks / max_marks) * 100

# Count passes and fails
num_pass = pass_fail.count("PASS")
num_fail = pass_fail.count("FAIL")

# Overall result
overall_grade = get_grade(percentage)
overall_result = "PASS" if num_fail == 0 else "FAIL"

# =============================================================================
# DISPLAY TEXT REPORT CARD
# =============================================================================

print("=" * 65)
print(f"{'📋 REPORT CARD':^65}")
print("=" * 65)
print()

# Header
print(f"{'Subject':<20} {'Marks':<10} {'Grade':<10} {'Status':<10}")
print("-" * 50)

# Each subject
for i in range(len(subjects)):
    status_symbol = "✅" if pass_fail[i] == "PASS" else "❌"
    print(f"{subjects[i]:<20} {marks[i]:<10} {grades[i]:<10} {status_symbol} {pass_fail[i]}")

print("-" * 50)

# Totals
print(f"{'TOTAL':<20} {total_marks}/{max_marks}")
print(f"{'PERCENTAGE':<20} {percentage:.1f}%")
print(f"{'OVERALL GRADE':<20} {overall_grade}")
print(f"{'RESULT':<20} {'✅ ' + overall_result if overall_result == 'PASS' else '❌ ' + overall_result}")

print()
print("=" * 65)

# Performance message based on percentage
if percentage >= 90:
    print("🏆 OUTSTANDING! You're among the top performers!")
elif percentage >= 75:
    print("⭐ EXCELLENT! Keep up the great work!")
elif percentage >= 60:
    print("👍 GOOD! You're doing well, aim higher!")
elif percentage >= 45:
    print("📚 AVERAGE. More effort needed in some subjects.")
else:
    print("⚠️ NEEDS IMPROVEMENT. Focus on studies!")

print()

# =============================================================================
# MATPLOTLIB BAR CHART
# =============================================================================

# 🔗 FUTURE TOOL: This visualization is what happens after n8n collects data
# In a real workflow: Trigger → Collect Data → Process → Visualize

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set colors based on pass/fail
colors = []
for status in pass_fail:
    if status == "PASS":
        colors.append('#2ecc71')  # Green for pass
    else:
        colors.append('#e74c3c')  # Red for fail

# Create bar chart
bars = ax.bar(subjects, marks, color=colors, edgecolor='white', linewidth=1.5)

# Add value labels on bars
for bar, mark in zip(bars, marks):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{mark}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add pass line
ax.axhline(y=33, color='orange', linestyle='--', linewidth=2, label='Pass Line (33)')

# Customize the chart
ax.set_ylim(0, 110)
ax.set_xlabel('Subjects', fontsize=12)
ax.set_ylabel('Marks', fontsize=12)
ax.set_title(f'📊 Report Card Visualization\nTotal: {total_marks}/{max_marks} | Percentage: {percentage:.1f}% | Grade: {overall_grade}',
             fontsize=14, fontweight='bold')

# Add grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend
legend_elements = [
    plt.Rectangle((0,0), 1, 1, facecolor='#2ecc71', label='Pass'),
    plt.Rectangle((0,0), 1, 1, facecolor='#e74c3c', label='Fail'),
]
ax.legend(handles=legend_elements, loc='upper right')

# Rotate x-axis labels for better fit
plt.xticks(rotation=15, ha='right')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the chart
print("📊 Opening visualization...")
plt.show()

print()
print("=" * 60)
print("       🎓 Thank you for using Smart Report Card! 🎓")
print("=" * 60)

# 🔗 FUTURE TOOL: This entire program is an n8n workflow!
# INPUT (Form/Webhook) → PROCESS (Code Node) → DECISION (IF Node) → OUTPUT (Report/Dashboard)


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: ADD MORE SUBJECTS
    - Add "Computer Science" and "Physical Education" to the subjects list
    - The program should automatically handle them!
    - Why? Because we use len(subjects) instead of hardcoded numbers

Challenge 2: CLASS AVERAGE
    - Calculate the class average (like if you had marks from multiple students)
    - You could prompt: "How many students?" and loop to get each student's marks
    - Display a comparison chart

Challenge 3: IMPROVEMENT TRACKER
    - Ask for last semester's marks too
    - Show which subjects improved and which declined
    - Add improvement arrows (↑ or ↓) in the report

Challenge 4: PIE CHART
    - Below the bar chart, add a pie chart showing:
        - How many subjects passed vs failed
    - Use: ax2.pie([num_pass, num_fail], labels=['Pass', 'Fail'], ...)

Challenge 5: SAVE TO FILE
    - Save the report card to a text file
    - Use:
        with open("report_card.txt", "w") as f:
            f.write(f"Student Report Card\\n")
            # ... write all the report content

Challenge 6: GRADE POINT AVERAGE (GPA)
    Use this mapping:
        A1: 10  A2: 9  B1: 8  B2: 7  C1: 6  C2: 5  D: 4  E: 0
    
    Calculate: GPA = sum of grade points / number of subjects
    Add GPA to the report!
"""

# =============================================================================
# HOW THIS CONNECTS TO REAL TOOLS
# =============================================================================
"""
🔗 FUTURE TOOL CONNECTIONS:

This program is a complete DATA PIPELINE:

1. INPUT (Getting marks)
   → n8n: Webhook node, Form node
   → SQL: INSERT INTO marks VALUES (...)

2. VALIDATION (Checking 0-100)
   → n8n: IF node to filter invalid data
   → SQL: CHECK constraint (marks >= 0 AND marks <= 100)

3. PROCESSING (Calculate grades)
   → n8n: Code node with JavaScript
   → SQL: CASE WHEN marks >= 91 THEN 'A1' ...

4. AGGREGATION (Total, average, count)
   → n8n: Aggregate node
   → SQL: SELECT SUM(marks), AVG(marks), COUNT(*) ...

5. OUTPUT (Display and visualize)
   → n8n: Send to dashboard, email, or Slack
   → SQL: SELECT for reporting tools like Metabase

You just built what professionals call an "ETL Pipeline"!
    E = Extract (get data)
    T = Transform (process and calculate)
    L = Load (output and visualize)
"""
