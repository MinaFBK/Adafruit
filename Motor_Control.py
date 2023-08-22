import board
import pwmio
from adafruit_clue import clue

# Set up the left motor
left_motor = pwmio.PWMOut(board.D7)
left_motor.frequency = 50


# Set up the right motor
right_motor = pwmio.PWMOut(board.D8)
right_motor.frequency = 50

# Define some constants for the motor speeds
FORWARD = 100
BACKWARD = 0
LEFT = 50
RIGHT = 50

# Create a function to move the robot forward
def forward():
  left_motor.duty_cycle = FORWARD
  right_motor.duty_cycle = FORWARD

# Create a function to move the robot backward
def backward():
  left_motor.duty_cycle = BACKWARD
  right_motor.duty_cycle = BACKWARD

# Create a function to turn the robot left
def left():
  left_motor.duty_cycle = LEFT
  right_motor.duty_cycle = FORWARD

# Create a function to turn the robot right
def right():
  left_motor.duty_cycle = FORWARD
  right_motor.duty_cycle = LEFT

# Create a function to stop the robot
def stop():
  left_motor.duty_cycle = 0
  right_motor.duty_cycle = 0

# Main loop
while True:
  # Get input from the user
  command = input("Enter a command (w, s, a, d, x): ")

  # Act on the input
  if command == "w":
    forward()
  elif command == "s":
    backward()
  elif command == "a":
    left()
  elif command == "d":
    right()
  elif command == "x":
    stop()