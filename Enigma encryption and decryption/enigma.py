class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                encrypted_char = self.process_character(char.upper())
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                decrypted_char = self.process_character(char.upper())
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message

    def process_character(self, char):
        self.rotate_rotors()
        encrypted_char = char
        for rotor in self.rotors:
            encrypted_char = rotor.encrypt(encrypted_char)
        encrypted_char = self.reflector.reflect(encrypted_char)
        for rotor in reversed(self.rotors):
            encrypted_char = rotor.decrypt(encrypted_char)
        return encrypted_char

    def rotate_rotors(self):
        self.rotors[0].rotate()
        for i in range(len(self.rotors) - 1):
            if self.rotors[i].has_reached_turnover_point():
                self.rotors[i + 1].rotate()

class Rotor:
    def __init__(self, wiring, turnover_point):
        self.wiring = wiring
        self.turnover_point = turnover_point
        self.position = 0

    def encrypt(self, char):
        offset = ord(char) - ord('A')
        shifted_char = self.wiring[(offset + self.position) % 26]
        encrypted_char = chr((ord(shifted_char) - ord('A') - self.position) % 26 + ord('A'))
        return encrypted_char

    def decrypt(self, char):
        offset = ord(char) - ord('A')
        shifted_char = chr((offset + self.position) % 26 + ord('A'))
        decrypted_char = chr((self.wiring.index(shifted_char) - self.position) % 26 + ord('A'))
        return decrypted_char

    def rotate(self):
        self.position = (self.position + 1) % 26

    def has_reached_turnover_point(self):
        return self.position == ord(self.turnover_point) - ord('A')

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        offset = ord(char) - ord('A')
        reflected_char = self.wiring[offset]
        return reflected_char

def read_key_from_file(filename):
    rotors = []
    reflector = None
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Rotor"):
                rotor_wiring = line.split(":")[1].strip()
                rotor_turnover = line.split(":")[2].strip()
                rotor = Rotor(rotor_wiring, rotor_turnover)
                rotors.append(rotor)
            elif line.startswith("Reflector"):
                reflector_wiring = line.split(":")[1].strip()
                reflector = Reflector(reflector_wiring)
    return rotors, reflector

def main():
    key_filename = "EnigmaKey.txt"
    rotors, reflector = read_key_from_file(key_filename)

    enigma = EnigmaMachine(rotors, reflector)

    while True:
        choice = input("Choose an option: (E)ncrypt, (D)ecrypt, or (Q)uit: ")
        if choice.upper() == 'E':
            message = input("Enter the message to encrypt: ")
            encrypted_message = enigma.encrypt(message)
            print("Encrypted message:", encrypted_message)
        elif choice.upper() == 'D':
            message = input("Enter the message to decrypt: ")
            decrypted_message = enigma.decrypt(message)
            print("Decrypted message:", decrypted_message)
        elif choice.upper() == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
