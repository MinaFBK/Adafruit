import time
import board
import displayio
import random
from adafruit_clue import Clue
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.circle import Circle

# Create display group
display = board.DISPLAY
group = displayio.Group()

# Create default eye shapes
eye_width = 80
eye_height = 90
eye_color = 0x000000
left_eye = RoundRect(20, 90, eye_width, eye_height, 15, fill=eye_color)
right_eye = RoundRect(140, 90, eye_width, eye_height, 15, fill=eye_color)
group.append(left_eye)
group.append(right_eye)

# Add group to display
display.show(group)

# Define expressions
expressions = [
    {"shape": "roundrect", "color": 0xFFFFFF},   # Normal (default)
    {"shape": "circle", "color": 0xFF0000},      # Angry
    {"shape": "happy", "color": 0x00FF00},       # Happy
    {"shape": "circle", "color": 0x0000FF},      # Surprised
]

# Duration for each expression in seconds
expression_duration = 2.0

while True:
    for expression in expressions:
        eye_shape = expression["shape"]
        eye_color = expression["color"]

        # Update eye shape and color for expression
        if eye_shape == "roundrect":
            left_eye = RoundRect(20, 90, eye_width, eye_height, 15, fill=eye_color)
            right_eye = RoundRect(140, 90, eye_width, eye_height, 15, fill=eye_color)
        elif eye_shape == "circle":
            left_eye = Circle(100, 115, 20, fill=eye_color)
            right_eye = Circle(160, 115, 20, fill=eye_color)
        elif eye_shape == "happy":
            left_eye = RoundRect(20, 90, eye_width, eye_height + 10, 5, fill=eye_color)
            right_eye = RoundRect(140, 90, eye_width, eye_height + 10, 5, fill=eye_color)

        group[0] = left_eye
        group[1] = right_eye

        # Display the expression
        time.sleep(expression_duration)

    # Reset to default expression
    left_eye = RoundRect(20, 90, eye_width, eye_height, 15, fill=eye_color)
    right_eye = RoundRect(140, 90, eye_width, eye_height, 15, fill=eye_color)
    group[0] = left_eye
    group[1] = right_eye
    time.sleep(expression_duration)