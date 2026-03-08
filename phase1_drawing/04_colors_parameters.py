"""
===============================================================================
                    🏏 PYTHON POWER USER COURSE 🏏
                    Session 4: Colors & Parameters - IPL Team Logos!
===============================================================================

In this session, you'll learn:
    ✅ What parameters are (values you pass TO a function)
    ✅ RGB color codes - mixing your own colors
    ✅ Turtle fill colors and backgrounds
    ✅ Creating IPL team logo approximations

===============================================================================
"""

import turtle

# =============================================================================
# UNDERSTANDING PARAMETERS
# =============================================================================

"""
PARAMETERS = SETTINGS YOU HAND TO A FUNCTION

Think of a function like a vending machine:
    - You put money in (input/parameter)
    - The machine does something
    - You get a result

When you call: draw_circle(100, "blue", 0, 50)
    - 100, "blue", 0, 50 are PARAMETERS
    - They tell the function what to do

🔗 FUTURE TOOL: Parameters are EXACTLY like filling in fields in an n8n node!
When you set up an n8n HTTP Request, you "fill in" URL, Method, Headers...
Those are parameters! Same concept, different interface.
"""

# =============================================================================
# SETUP
# =============================================================================

screen = turtle.Screen()
screen.title("🏆 IPL Team Logos - Colors & Parameters!")
screen.bgcolor("#1a1a2e")  # Dark blue background
screen.setup(width=1000, height=700)
screen.colormode(255)  # This lets us use RGB values (0-255)

artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.hideturtle()

# =============================================================================
# RGB COLORS EXPLAINED
# =============================================================================

"""
RGB = Red, Green, Blue

Every color on a computer screen is made by mixing:
    - Red (0 to 255)
    - Green (0 to 255)  
    - Blue (0 to 255)

Examples:
    (255, 0, 0)     = Pure Red
    (0, 255, 0)     = Pure Green
    (0, 0, 255)     = Pure Blue
    (255, 255, 0)   = Yellow (Red + Green)
    (0, 255, 255)   = Cyan (Green + Blue)
    (255, 0, 255)   = Magenta (Red + Blue)
    (255, 255, 255) = White (all colors)
    (0, 0, 0)       = Black (no colors)

🧠 LOGIC SEED: RGB values are stored as 3 numbers. In databases,
this could be 3 columns: color_red, color_green, color_blue
Or stored as a single hex code like "#FF5733"
"""

# =============================================================================
# IPL TEAM COLORS - Real Team Colors!
# =============================================================================

# IPL Team color palette (RGB values)
IPL_COLORS = {
    "MI": {  # Mumbai Indians
        "primary": (0, 102, 178),      # Blue
        "secondary": (212, 175, 55)    # Gold
    },
    "CSK": {  # Chennai Super Kings
        "primary": (255, 204, 0),      # Yellow
        "secondary": (0, 66, 136)      # Blue
    },
    "RCB": {  # Royal Challengers Bangalore
        "primary": (204, 0, 0),        # Red
        "secondary": (30, 30, 30)      # Black
    },
    "KKR": {  # Kolkata Knight Riders
        "primary": (59, 42, 107),      # Purple
        "secondary": (255, 215, 0)     # Gold
    },
    "DC": {  # Delhi Capitals
        "primary": (0, 65, 143),       # Blue
        "secondary": (255, 0, 0)       # Red
    },
    "SRH": {  # Sunrisers Hyderabad
        "primary": (255, 130, 0),      # Orange
        "secondary": (0, 0, 0)         # Black
    },
    "PBKS": {  # Punjab Kings
        "primary": (218, 0, 85),       # Red/Pink
        "secondary": (0, 0, 0)         # Black
    },
    "RR": {  # Rajasthan Royals
        "primary": (255, 55, 148),     # Pink
        "secondary": (37, 74, 165)     # Blue
    }
}

# =============================================================================
# HELPER FUNCTIONS WITH PARAMETERS
# =============================================================================

def draw_filled_circle(x, y, radius, color):
    """
    Draws a filled circle at position (x, y) with given radius and color.
    
    Parameters:
        x      - horizontal position (number)
        y      - vertical position (number)
        radius - size of circle (number)
        color  - RGB tuple like (255, 0, 0) or color name string
    """
    artist.penup()
    artist.goto(x, y - radius)  # Start at bottom of circle
    artist.pendown()
    artist.fillcolor(color)
    artist.pencolor(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()


def draw_rectangle(x, y, width, height, color):
    """
    Draws a filled rectangle starting at (x, y).
    
    Parameters:
        x, y   - bottom-left corner position
        width  - how wide the rectangle is
        height - how tall the rectangle is
        color  - fill color
    """
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.fillcolor(color)
    artist.pencolor(color)
    artist.begin_fill()
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()


def draw_text(x, y, text, color, size=16):
    """
    Writes text at position (x, y).
    
    Parameters:
        x, y  - position
        text  - what to write
        color - text color
        size  - font size (default is 16)
    """
    artist.penup()
    artist.goto(x, y)
    artist.pencolor(color)
    artist.write(text, align="center", font=("Arial", size, "bold"))


# =============================================================================
# LOGO 1: MUMBAI INDIANS (MI) - Blue circle with gold
# =============================================================================

print("Drawing Mumbai Indians logo...")

# Get MI colors from our dictionary
mi_blue = IPL_COLORS["MI"]["primary"]
mi_gold = IPL_COLORS["MI"]["secondary"]

# Position for MI logo
mi_x, mi_y = -350, 200

# Draw outer gold ring (bigger circle behind)
draw_filled_circle(mi_x, mi_y, 70, mi_gold)

# Draw inner blue circle
draw_filled_circle(mi_x, mi_y, 55, mi_blue)

# Add team name
draw_text(mi_x, mi_y - 100, "MUMBAI INDIANS", (255, 255, 255), 12)
draw_text(mi_x, mi_y - 120, "MI", mi_gold, 16)

print("  ✅ MI logo complete!")

# =============================================================================
# LOGO 2: CHENNAI SUPER KINGS (CSK) - Yellow with blue accents
# =============================================================================

print("Drawing Chennai Super Kings logo...")

csk_yellow = IPL_COLORS["CSK"]["primary"]
csk_blue = IPL_COLORS["CSK"]["secondary"]

csk_x, csk_y = -100, 200

# Draw yellow circle (main)
draw_filled_circle(csk_x, csk_y, 65, csk_yellow)

# Draw blue inner circle
draw_filled_circle(csk_x, csk_y, 40, csk_blue)

# Draw yellow center dot
draw_filled_circle(csk_x, csk_y, 15, csk_yellow)

# Add team name
draw_text(csk_x, csk_y - 100, "CHENNAI SUPER KINGS", (255, 255, 255), 12)
draw_text(csk_x, csk_y - 120, "CSK", csk_yellow, 16)

print("  ✅ CSK logo complete!")

# =============================================================================
# LOGO 3: ROYAL CHALLENGERS BANGALORE (RCB) - Red and Black
# =============================================================================

print("Drawing Royal Challengers Bangalore logo...")

rcb_red = IPL_COLORS["RCB"]["primary"]
rcb_black = IPL_COLORS["RCB"]["secondary"]

rcb_x, rcb_y = 150, 200

# Draw red outer circle
draw_filled_circle(rcb_x, rcb_y, 65, rcb_red)

# Draw black inner shape (smaller circle)
draw_filled_circle(rcb_x, rcb_y, 45, rcb_black)

# Draw red center
draw_filled_circle(rcb_x, rcb_y, 20, rcb_red)

# Add team name
draw_text(rcb_x, rcb_y - 100, "ROYAL CHALLENGERS", (255, 255, 255), 12)
draw_text(rcb_x, rcb_y - 120, "RCB", rcb_red, 16)

print("  ✅ RCB logo complete!")

# =============================================================================
# LOGO 4: KOLKATA KNIGHT RIDERS (KKR) - Purple and Gold
# =============================================================================

print("Drawing Kolkata Knight Riders logo...")

kkr_purple = IPL_COLORS["KKR"]["primary"]
kkr_gold = IPL_COLORS["KKR"]["secondary"]

kkr_x, kkr_y = 400, 200

# Draw gold outer ring
draw_filled_circle(kkr_x, kkr_y, 70, kkr_gold)

# Draw purple main circle
draw_filled_circle(kkr_x, kkr_y, 55, kkr_purple)

# Draw gold center
draw_filled_circle(kkr_x, kkr_y, 20, kkr_gold)

# Add team name
draw_text(kkr_x, kkr_y - 100, "KOLKATA KNIGHT RIDERS", (255, 255, 255), 12)
draw_text(kkr_x, kkr_y - 120, "KKR", kkr_gold, 16)

print("  ✅ KKR logo complete!")

# =============================================================================
# ROW 2: MORE TEAMS
# =============================================================================

# DELHI CAPITALS
print("Drawing Delhi Capitals logo...")
dc_blue = IPL_COLORS["DC"]["primary"]
dc_red = IPL_COLORS["DC"]["secondary"]
dc_x, dc_y = -350, -50

draw_filled_circle(dc_x, dc_y, 65, dc_blue)
draw_filled_circle(dc_x, dc_y, 40, dc_red)
draw_filled_circle(dc_x, dc_y, 15, dc_blue)
draw_text(dc_x, dc_y - 100, "DELHI CAPITALS", (255, 255, 255), 12)
draw_text(dc_x, dc_y - 120, "DC", dc_blue, 16)
print("  ✅ DC logo complete!")

# SUNRISERS HYDERABAD
print("Drawing Sunrisers Hyderabad logo...")
srh_orange = IPL_COLORS["SRH"]["primary"]
srh_black = IPL_COLORS["SRH"]["secondary"]
srh_x, srh_y = -100, -50

draw_filled_circle(srh_x, srh_y, 65, srh_orange)
draw_filled_circle(srh_x, srh_y, 40, srh_black)
draw_filled_circle(srh_x, srh_y, 15, srh_orange)
draw_text(srh_x, srh_y - 100, "SUNRISERS HYDERABAD", (255, 255, 255), 12)
draw_text(srh_x, srh_y - 120, "SRH", srh_orange, 16)
print("  ✅ SRH logo complete!")

# PUNJAB KINGS
print("Drawing Punjab Kings logo...")
pbks_red = IPL_COLORS["PBKS"]["primary"]
pbks_black = IPL_COLORS["PBKS"]["secondary"]
pbks_x, pbks_y = 150, -50

draw_filled_circle(pbks_x, pbks_y, 65, pbks_red)
draw_filled_circle(pbks_x, pbks_y, 45, pbks_black)
draw_filled_circle(pbks_x, pbks_y, 25, pbks_red)
draw_text(pbks_x, pbks_y - 100, "PUNJAB KINGS", (255, 255, 255), 12)
draw_text(pbks_x, pbks_y - 120, "PBKS", pbks_red, 16)
print("  ✅ PBKS logo complete!")

# RAJASTHAN ROYALS
print("Drawing Rajasthan Royals logo...")
rr_pink = IPL_COLORS["RR"]["primary"]
rr_blue = IPL_COLORS["RR"]["secondary"]
rr_x, rr_y = 400, -50

draw_filled_circle(rr_x, rr_y, 70, rr_pink)
draw_filled_circle(rr_x, rr_y, 50, rr_blue)
draw_filled_circle(rr_x, rr_y, 25, rr_pink)
draw_text(rr_x, rr_y - 100, "RAJASTHAN ROYALS", (255, 255, 255), 12)
draw_text(rr_x, rr_y - 120, "RR", rr_pink, 16)
print("  ✅ RR logo complete!")

# =============================================================================
# TITLE AND FOOTER
# =============================================================================

draw_text(0, 320, "🏆 IPL TEAM GALLERY 🏆", (255, 215, 0), 24)
draw_text(0, -280, "Created using Python Turtle with RGB Colors & Parameters!", 
          (150, 150, 150), 12)

# =============================================================================
# SUMMARY OUTPUT
# =============================================================================

print("\n" + "=" * 60)
print("         🏆 IPL TEAM LOGO GALLERY COMPLETE! 🏆")
print("=" * 60)
print("\nWhat you learned:")
print("  ✅ Parameters pass values INTO functions")
print("  ✅ RGB colors mix Red, Green, Blue (0-255 each)")
print("  ✅ Functions can have default parameter values")
print("  ✅ Dictionaries store related data together")
print()

# 🔗 FUTURE TOOL: In n8n, every node accepts parameters as inputs.
# The HTTP Request node takes URL, Method, Headers, Body as parameters.
# You just learned the same concept that powers all automation tools!

screen.exitonclick()


# =============================================================================
# 🔥 TRY THIS: Your Challenges!
# =============================================================================
"""
Challenge 1: CREATE YOUR OWN RGB COLOR
    - Use the formula: (R, G, B) where each is 0-255
    - Try making:
        * Brown: (139, 69, 19)
        * Teal: (0, 128, 128)
        * Your school colors?
    - Add a new circle with your custom color

Challenge 2: ADD A NEW IPL TEAM
    - Add "GT" (Gujarat Titans) to the IPL_COLORS dictionary
    - GT colors: Dark Blue (0, 81, 131) and Gold (255, 203, 5)
    - Draw their logo using the same pattern

Challenge 3: CHANGE A PARAMETER'S DEFAULT VALUE
    - In draw_text(), size=16 is a DEFAULT parameter
    - Change it to size=20
    - Notice: you can STILL call draw_text(x, y, "Hi", color, 12)
    - The 12 OVERRIDES the default 20!

Challenge 4: EXPERIMENT WITH TRANSPARENCY
    - What happens if you layer circles of different sizes?
    - Try drawing 10 circles, each slightly smaller, with colors
      that gradually change from one team's primary to secondary
    - This creates a gradient effect!

Challenge 5: COLOR MIXER CALCULATOR
    - Write code that prints all combinations where R, G, B are 
      each either 0, 128, or 255
    - How many unique colors is that? (Answer: 3 × 3 × 3 = 27)
    
    for r in [0, 128, 255]:
        for g in [0, 128, 255]:
            for b in [0, 128, 255]:
                print(f"RGB: ({r}, {g}, {b})")
"""

# =============================================================================
# REFERENCE: Common Color Names Turtle Accepts
# =============================================================================
"""
BASIC COLORS:
    "red", "green", "blue", "yellow", "orange", "purple", "pink"
    "black", "white", "gray", "brown", "cyan", "magenta"

EXTENDED COLORS:
    "gold", "silver", "navy", "teal", "olive", "maroon", "lime"
    "coral", "salmon", "violet", "indigo", "turquoise", "crimson"

HEX CODES (start with #):
    "#FF5733" = Orange-red
    "#3498DB" = Nice blue
    "#2ECC71" = Nice green
    "#9B59B6" = Purple
    "#F1C40F" = Yellow-gold

RGB TUPLES (use screen.colormode(255) first):
    (255, 0, 0)   = Red
    (0, 255, 0)   = Green
    (0, 0, 255)   = Blue
    (255, 165, 0) = Orange
"""
