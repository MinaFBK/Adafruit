import time
import board
import displayio
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.circle import Circle

# Create display group
display = board.DISPLAY
display.auto_refresh = False

# Create default eye shapes
eye_width = 80
eye_height = 100
eye_x_left = 30
eye_x_right = 140
eye_y = 60

# Create a black background fills
bg_bitmap = displayio.Bitmap(display.width, display.height, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x000000  # White background
bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette, x=0, y=0)

# Initialize the display group
splash = displayio.Group()

# Add the white background to the display group
splash.append(bg_sprite)

# Create the initial eye shapes (cyan color)
left_eye = RoundRect(eye_x_left, eye_y, eye_width, eye_height, 5, fill=0x00FFFF)
right_eye = RoundRect(eye_x_right, eye_y, eye_width, eye_height, 5, fill=0x00FFFF)

# Show the normal eyes for 3 seconds
splash.append(left_eye)
splash.append(right_eye)
display.show(splash)
time.sleep(3)  # Display normal eyes for 3 seconds

def transition_to_sad():
    sad_group = displayio.Group()  # Group for the sad circles

    # Create the initial small sad circles
    initial_sad_radius = 0

    # Transition from normal to sad
    for radius in range(initial_sad_radius ,eye_width+5 ,20):
        # Update the radius of the sad circles
        sad_circles = [
        Circle(eye_x_left, eye_y, radius, fill=0x000000),
        Circle(eye_x_right + 79, eye_y, radius, fill=0x000000)
        ]
    
    # Add the initial sad circles
    #  to the sad circles group
        for circle in sad_circles:
            splash.append(circle)
     #   for circle in sad_circles:
     #       circle.r = radius
     #       print(f'radius: {circle.r}')
            #print(splash[-3])
        #display.show(splash)
        display.refresh()
        #time.sleep(0.05)
        splash.pop()
        splash.pop()

    time.sleep(5)

    


    # Clear the sad circles group to remove sad circles
    #for circle in sad_circles:
    #    sad_group.remove(circle)
    #    display.show(splash)  # Display the normal eyes again
    #time.sleep(10)

# Call the transition function
while True:
    transition_to_sad()