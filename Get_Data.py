# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Adafruit Service demo for Adafruit CLUE board.
# Accessible via Adafruit Bluefruit Playground app and Web Bluetooth Dashboard.

import time
import board
from digitalio import DigitalInOut
from adafruit_clue import clue


"""View All Data"""
clue.sea_level_pressure = 1015
clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2)
while True:
    # Space
    clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f}".format(*clue.acceleration)
    clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f}".format(*clue.gyro)
    clue_data[2].text = "Altitude: {:.1f}m".format(clue.altitude)
    clue_data[3].text = "Proximity: {}".format(clue.proximity)

    # Buttons
    if clue.button_a:
        clue_data[4].text = "Button A: True"
        clue.start_tone(523)
    else:
        clue_data[4].text = "Button A: False"
        clue.stop_tone()

    if clue.button_b:
        clue_data[5].text = "Button B: True"
        clue.start_tone(587)
    else:
        clue_data[5].text = "Button B: False"
        clue.stop_tone()

    if clue.touch_0:
        clue_data[6].text = "Touch 0: True"
    else:
        clue_data[6].text = "Touch 0: False"

    if clue.touch_1:
        clue_data[7].text = "Touch 1: True"
    else:
        clue_data[7].text = "Touch 1: False"

    if clue.touch_2:
        clue_data[8].text = "Touch 1: True"
    else:
        clue_data[8].text = "Touch 1: False"

    # Mic Triggers LED & Speaker
    if clue.loud_sound(sound_threshold=300):
        clue.pixel.fill((0, 50, 0))
        clue.red_led = True
        clue.play_tone(880, 1)
    else:
        clue.pixel.fill(0)

    clue_data[9].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
    clue_data[10].text = "Humidity: {:.1f}%".format(clue.humidity)
    clue_data[11].text = "Pressure: {:.3f} hPa".format(clue.pressure)
    clue_data[12].text = "Temperature: {:.1f}C".format(clue.temperature)
    clue_data.show()

    # Stops the Program ?
    '''
    #Sensors
    value = clue.gesture
    if value:
        clue_data[13].text = "Gesture: {}".format(value)

    else:
        clue_data[13].text = "Gesture: :)"
    clue_data.show()
    '''
