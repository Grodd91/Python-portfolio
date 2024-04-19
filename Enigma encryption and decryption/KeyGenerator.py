import random

def generate_enigma_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor_1 = list(alphabet)
    rotor_2 = list(alphabet)
    rotor_3 = list(alphabet)

    random.shuffle(rotor_1)
    random.shuffle(rotor_2)
    random.shuffle(rotor_3)

    reflector = list(alphabet)
    random.shuffle(reflector)

    q_index = random.randint(0, 25)
    e_index = random.randint(0, 25)
    v_index = random.randint(0, 25)

    rotor_1[q_index], rotor_1[e_index], rotor_1[v_index] = 'Q', 'E', 'V'

    random_alphabet_sign_1 = random.choice(alphabet)
    random_alphabet_sign_2 = random.choice(alphabet)
    random_alphabet_sign_3 = random.choice(alphabet)

    rotor_1 = ''.join(rotor_1) + ": " + random_alphabet_sign_1
    rotor_2 = ''.join(rotor_2) + ": " + random_alphabet_sign_2
    rotor_3 = ''.join(rotor_3) + ": " + random_alphabet_sign_3

    return {
        'rotor_1': rotor_1,
        'rotor_2': rotor_2,
        'rotor_3': rotor_3,
        'reflector': ''.join(reflector)
    }

def save_enigma_key_to_file(enigma_key):
    file_name = 'EnigmaKey.txt'
    with open(file_name, 'w') as file:
        file.write("Enigma Key:\n")
        file.write("Rotor 1: " + enigma_key['rotor_1'] + "\n")
        file.write("Rotor 2: " + enigma_key['rotor_2'] + "\n")
        file.write("Rotor 3: " + enigma_key['rotor_3'] + "\n")
        file.write("Reflector: " + enigma_key['reflector'] + "\n")
    print("Enigma key saved to", file_name)

enigma_key = generate_enigma_key()
save_enigma_key_to_file(enigma_key)
