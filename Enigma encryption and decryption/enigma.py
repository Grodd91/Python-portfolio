import random

def generate_enigma_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def generate_rotor():
        rotor = list(alphabet)
        random.shuffle(rotor)
        return ''.join(rotor)

    rotor_1 = generate_rotor()
    rotor_2 = generate_rotor()
    rotor_3 = generate_rotor()

    reflector = list(alphabet)
    random.shuffle(reflector)
    reflector = ''.join(reflector)

    # Przypisanie punktów przełączenia (turnover points) do rotorów
    turnover_1 = random.choice(alphabet)
    turnover_2 = random.choice(alphabet)
    turnover_3 = random.choice(alphabet)

    return {
        'rotor_1': rotor_1 + ": " + turnover_1,
        'rotor_2': rotor_2 + ": " + turnover_2,
        'rotor_3': rotor_3 + ": " + turnover_3,
        'reflector': reflector
    }

def save_enigma_key_to_file(enigma_key):
    try:
        file_name = 'EnigmaKey.txt'
        with open(file_name, 'w') as file:
            file.write("Enigma Key:\n")
            file.write("Rotor 1: " + enigma_key['rotor_1'] + "\n")
            file.write("Rotor 2: " + enigma_key['rotor_2'] + "\n")
            file.write("Rotor 3: " + enigma_key['rotor_3'] + "\n")
            file.write("Reflector: " + enigma_key['reflector'] + "\n")
        print("Enigma key saved to", file_name)
    except Exception as e:
        print(f"Error saving Enigma key: {e}")

# Generowanie i zapis klucza Enigmy
enigma_key = generate_enigma_key()
save_enigma_key_to_file(enigma_key)
