This repository contains three Python programs: enigma.py, KeyGenerator.py, and launcher.py. These programs are related to the Enigma machine, a cryptographic device used during World War II.

enigma.py
The enigma.py program implements the functionality of the Enigma machine. It allows you to encrypt and decrypt messages using a simulated Enigma machine.

The program consists of the following components:

EnigmaMachine class: Represents the Enigma machine. It takes the rotor configurations and reflector as inputs and provides methods for encryption and decryption of messages.
Rotor class: Represents a rotor of the Enigma machine. It contains the wiring and turnover point information and provides encryption and decryption operations.
Reflector class: Represents the reflector of the Enigma machine. It provides a method for reflecting a character.
read_key_from_file function: Reads the rotor and reflector configurations from a key file.
main function: Implements the main program logic, allowing the user to encrypt, decrypt, or quit.
To run the enigma.py program, execute the following command: python enigma.py. It will prompt you to choose an option (encrypt, decrypt, or quit) and perform the corresponding operation based on your input.

KeyGenerator.py
The KeyGenerator.py program is used to generate a random Enigma machine key. It creates a key file (EnigmaKey.txt) containing the rotor and reflector configurations.

The program consists of the following components:

generate_enigma_key function: Generates a random Enigma machine key with shuffled rotors and reflector, including additional random characters and values Q, E, and V.
save_enigma_key_to_file function: Saves the generated Enigma machine key to the EnigmaKey.txt file.
open_file function: Opens a Python file using the subprocess module.
main function: Implements the main program logic, allowing the user to open enigma.py, KeyGenerator.py, or quit.
To run the KeyGenerator.py program, execute the following command: python KeyGenerator.py. It will prompt you to enter either "Enigma" to open enigma.py, "KeyGenerator" to open KeyGenerator.py, or "Q" to quit.

launcher.py
The launcher.py program serves as a launcher for the other two programs. It provides a menu-based interface for easy access to enigma.py and KeyGenerator.py.

The program consists of the following components:

open_file function: Opens a Python file using the subprocess module.
main function: Implements the main program logic, allowing the user to open enigma.py, KeyGenerator.py, or quit.
To run the launcher.py program, execute the following command: python launcher.py. It will prompt you to enter either "Enigma" to open enigma.py, "KeyGenerator" to open KeyGenerator.py, or "Q" to quit.

Note: Make sure to have Python installed on your system and execute the commands in the directory where the programs are located.

Feel free to explore and use these programs to understand the functioning of the Enigma machine or experiment with encryption and decryption operations.

Important: These programs provide a basic simulation of the Enigma machine and are not intended for real-world cryptographic purposes.
