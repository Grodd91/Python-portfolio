
import psutil
import subprocess
import time

def is_game_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'HD-Player.exe':  # Replace with the process name of the emulator
            return True
    return False

def restart_game():
    subprocess.run(['taskkill', '/IM', 'HD-Player.exe', '/F'])  # Replace with the process name of the emulator
    time.sleep(5)  # Wait for the emulator to close
    subprocess.Popen('path_to_bluestacks_executable')  # Replace with the actual path to Bluestacks executable

def main():
    while True:
        if not is_game_running():
            print("Game has crashed. Restarting...")
            restart_game()
        time.sleep(10)  # Adjust the interval as per your requirement

if __name__ == '__main__':
    main()

