import time
import array
import board
from adafruit_clue import clue
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Initialize BLE
ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)
ble.start_advertising(advertisement)

# Function to initialize the microphone
def initialize_microphone():
    import audiobusio
    try:
        mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)
        print("Microphone initialized successfully")
        return mic
    except Exception as e:
        print(f"Error initializing microphone: {e}")
        return None

# Function to handle microphone recording
def handle_microphone():
    import audiobusio
    mic = initialize_microphone()
    if mic:
        samples = array.array('H', [0] * 160)
        try:
            mic.record(samples, len(samples))
            print("Audio samples:", samples)
        except Exception as e:
            print(f"Error recording samples: {e}")
        finally:
            mic.deinit()  # Properly deinitialize the microphone
    else:
        print("Microphone initialization failed")

# Function to handle CLUE display and inputs
def handle_clue():
    clue.sea_level_pressure = 1015
    clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2)

    while True:
        # Update the display with sensor data
        text_updates = [
            (0, "Accel: {:.2f} {:.2f} {:.2f}".format(*clue.acceleration)),
            (1, "Gyro: {:.2f} {:.2f} {:.2f}".format(*clue.gyro)),
            (2, "Alt: {:.1f}m".format(clue.altitude)),
            (3, "Prox: {}".format(clue.proximity)),
            (4, f"Btn A: {clue.button_a}"),
            (5, f"Btn B: {clue.button_b}"),
            (6, f"Touch 0: {clue.touch_0}"),
            (7, f"Touch 1: {clue.touch_1}"),
            (8, f"Touch 2: {clue.touch_2}"),
            (9, f"Color: R:{clue.color[0]} G:{clue.color[1]} B:{clue.color[2]} C:{clue.color[3]}"),
            (10, f"Humidity: {clue.humidity:.1f}%"),
            (11, f"Pressure: {clue.pressure:.3f} hPa"),
            (12, f"Temp: {clue.temperature:.1f}C"),
            (13, f"BLE: {'Connected' if ble.connected else 'Disconnected'}")
        ]

        for idx, new_text in text_updates:
            if clue_data[idx].text != new_text:
                clue_data[idx].text = new_text

        clue_data.show()

        # Handle button A
        if clue.button_a:
            handle_microphone()
    
        time.sleep(0.5)

# Handle CLUE functionalities
handle_clue()
