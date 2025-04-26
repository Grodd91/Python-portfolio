import os
import subprocess

def open_file(file_name):
    file_path = f"{file_name}.py"
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' does not exist.")
        return
    try:
        subprocess.call(['python', file_path])
    except Exception as e:
        print(f"Error occurred while opening the file: {str(e)}")

def main():
    while True:
        choice = input("Enter 'Enigma' to open enigma.py, 'KeyGenerator' to open KeyGenerator.py, or 'Q' to quit: ").strip().lower()
        
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice == 'enigma':
            open_file('enigma')
        elif choice == 'keygenerator':
            open_file('KeyGenerator')
        else:
            print("Invalid choice. Please enter 'Enigma', 'KeyGenerator', or 'Q'.")

if __name__ == "__main__":
    main()
