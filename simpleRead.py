import serial
import time
import keyboard  # Import the keyboard module to detect keypress events

# Serial port settings
SERIAL_PORT = 'COM14'  # Replace with the appropriate serial port on your system
BAUD_RATE = 115200

# Function to read EEG data from Arduino
def read_eeg_data():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    try:
        while True:
            # Read a line of data from the serial port
            line = ser.readline().decode().strip()
            if line:
                # Print the received EEG data
                print("EEG Data:", line)
            
            # Check for 'Esc' key press
            if keyboard.is_pressed('esc'):
                print("Stopping EEG data reading...")
                break  # Exit the loop if 'Esc' key is pressed
    except KeyboardInterrupt:
        ser.close()  # Close the serial connection if Ctrl+C is pressed

if __name__ == "__main__":
    read_eeg_data()
