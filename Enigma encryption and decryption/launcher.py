import os
import subprocess

def open_file(file_name):
    file_path = f"{file_name}.py"
    try:
        if os.path.exists(file_path):
            subprocess.call(['python', file_path])
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error occurred while opening the file: {str(e)}")

def main():
    while True:
        choice = input("Enter 'Enigma' to open enigma.py, 'KeyGenerator' to open KeyGenerator.py, or 'Q' to quit: ")
        if choice.upper() == 'Q':
            print("Exiting the program.")
            break
        elif choice.lower() == 'enigma':
            open_file('enigma')
        elif choice.lower() == 'keygenerator':
            open_file('KeyGenerator')
        else:
            print("Invalid choice. Please enter 'Enigma', 'KeyGenerator', or 'Q'.")

if __name__ == "__main__":
    main()
