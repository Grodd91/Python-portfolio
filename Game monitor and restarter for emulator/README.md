
# Game Monitor and Restarter for Emulator

This Python program aims to monitor the operation of a game running on an emulator, such as Bluestacks, and automatically restart the game in case of a crash.

## Requirements

- Python 3.x
- psutil library

## Installation

1. Download the contents of the repository to your computer.

2. Install the required dependencies by running the following command: pip install psutil


## Configuration

1. In the 'MonitorEmulator.py' file, you will find the following lines:

python
'emulator_process_name' = 'HD-Player.exe'
emulator_executable_path = 'path_to_bluestacks_executable'

'emulator_process_name': Change the value to the process name of the emulator you want to monitor (e.g., 'HD-Player.exe' for Bluestacks).

'emulator_executable_path': Change the value to the executable path of the emulator (e.g., 'C:/Program Files/Bluestacks/Bluestacks.exe').

Save the changes.
## Running

Open a terminal or command prompt.

Navigate to the directory containing the MonitorEmulator.py file.

Run the program by executing the following command: python MonitorEmulator.py

The program will monitor the game running on the emulator and automatically restart the game if a crash is detected.

Notes
The program will attempt to close and relaunch the emulator to restart the game. Make sure you have the necessary permissions and access to system files and processes.

Verify that the emulator process name and executable path are correct for your emulator. You may need to adjust these values in the MonitorEmulator.py file.

This program is provided as an example and may require customization to meet specific requirements and configurations of your environment.
