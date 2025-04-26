# Ulepszona wersja twojego kodu Enigmy

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, message):
        return self._process(message)

    def decrypt(self, message):
        return self._process(message)

    def _process(self, message):
        result = ""
        for char in message:
            if char.isalpha():
                processed_char = self.process_character(char.upper())
                result += processed_char
            else:
                result += char
        return result

    def process_character(self, char):
        self.rotate_rotors()

        # Przechodzimy przez rotory w przód
        for rotor in self.rotors:
            char = rotor.encrypt(char)

        # Odbicie w reflektorze
        char = self.reflector.reflect(char)

        # Przechodzimy przez rotory wstecz
        for rotor in reversed(self.rotors):
            char = rotor.decrypt(char)

        return char

    def rotate_rotors(self):
        rotate_next = True
        for rotor in self.rotors:
            if rotate_next:
                rotor.rotate()
                rotate_next = rotor.has_reached_turnover_point()
            else:
                break

class Rotor:
    def __init__(self, wiring, turnover_point):
        self.wiring = wiring
        self.turnover_point = turnover_point
        self.position = 0

    def encrypt(self, char):
        offset = (ord(char) - ord('A') + self.position) % 26
        encrypted_char = self.wiring[offset]
        return encrypted_char

    def decrypt(self, char):
        index_in_wiring = self.wiring.index(char)
        offset = (index_in_wiring - self.position + 26) % 26
        decrypted_char = chr(offset + ord('A'))
        return decrypted_char

    def rotate(self):
        self.position = (self.position + 1) % 26

    def has_reached_turnover_point(self):
        return self.position == (ord(self.turnover_point) - ord('A'))

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        offset = ord(char) - ord('A')
        return self.wiring[offset]

def read_key_from_file(filename):
    rotors = []
    reflector = None
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Rotor"):
                parts = line.split(":")
                rotor_wiring = parts[1].strip()
                rotor_turnover = parts[2].strip()
                rotors.append(Rotor(rotor_wiring, rotor_turnover))
            elif line.startswith("Reflector"):
                reflector_wiring = line.split(":")[1].strip()
                reflector = Reflector(reflector_wiring)
    return rotors, reflector

def main():
    key_filename = "EnigmaKey.txt"
    try:
        rotors, reflector = read_key_from_file(key_filename)
    except Exception as e:
        print(f"Error reading key file: {e}")
        return

    enigma = EnigmaMachine(rotors, reflector)

    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, or (Q)uit: ").strip().upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            print("Encrypted message:", enigma.encrypt(message))
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            print("Decrypted message:", enigma.decrypt(message))
        elif choice == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
