import random
import time
import os

class Character:
    def __init__(self, name, health, armor_class, attack):
        self.name = name
        self.health = health
        self.armor_class = armor_class
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name, character_class):
        if character_class in ["Wojownik", "Warrior"]:
            super().__init__(name, health=100, armor_class=16, attack=10)
            self.damage_dice = 1
            self.damage_sides = 8
        elif character_class in ["Mag", "Mage"]:
            super().__init__(name, health=60, armor_class=12, attack=18)
            self.damage_dice = 1
            self.damage_sides = 4
        elif character_class in ["Łucznik", "Archer"]:
            super().__init__(name, health=80, armor_class=14, attack=14)
            self.damage_dice = 1
            self.damage_sides = 6
        elif character_class in ["Łotrzyk", "Rogue"]:
            super().__init__(name, health=70, armor_class=15, attack=16)
            self.damage_dice = 1
            self.damage_sides = 6
        else:
            super().__init__(name, health=100, armor_class=16, attack=10)
            self.damage_dice = 1
            self.damage_sides = 8
        self.character_class = character_class
        self.experience = 0
        self.level = 1
        self.max_health = self.health

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        if self.character_class in ["Wojownik", "Warrior"]:
            self.attack += 2
        elif self.character_class in ["Mag", "Mage"]:
            self.attack += 1
        elif self.character_class in ["Łucznik", "Archer"]:
            self.attack += 1
        elif self.character_class in ["Łotrzyk", "Rogue"]:
            self.attack += 2

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= self.level * 10:
            self.level_up()
            if self.character_class in ["Wojownik", "Warrior"]:
                print(f"Congratulations! {self.name} reached level {self.level} as a Warrior!")
            elif self.character_class in ["Mag", "Mage"]:
                print(f"Congratulations! {self.name} reached level {self.level} as a Mage!")
            elif self.character_class in ["Łucznik", "Archer"]:
                print(f"Congratulations! {self.name} reached level {self.level} as an Archer!")
            elif self.character_class in ["Łotrzyk", "Rogue"]:
                print(f"Congratulations! {self.name} reached level {self.level} as a Rogue!")
            else:
                print(f"Congratulations! {self.name} reached level {self.level}!")

    def calculate_damage(self):
        return roll_dice(self.damage_dice, self.damage_sides) + self.attack

class Potwór(Character):
    def __init__(self, name, health, armor_class, attack):
        super().__init__(name, health, armor_class, attack)
        self.damage_dice = 1
        self.damage_sides = 6

    def calculate_damage(self):
        return roll_dice(self.damage_dice, self.damage_sides) + self.attack

class Boss(Character):
    def __init__(self, name, health, armor_class, attack):
        super().__init__(name, health, armor_class, attack)
        self.damage_dice = 2
        self.damage_sides = 8

    def calculate_damage(self):
        return roll_dice(self.damage_dice, self.damage_sides) + self.attack

def roll_dice(num_dice, sides):
    return sum(random.randint(1, sides) for _ in range(num_dice))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_difficulty():
    while True:
        print("Choose difficulty level (Wybierz poziom trudności):")
        print("1. Easy (Łatwy)")
        print("2. Medium (Średni)")
        print("3. Hard (Trudny)")
        choice = input("Enter the number of your choice (Wpisz numer wybranego poziomu): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please choose 1, 2, or 3. (Nieprawidłowy wybór. Proszę wybrać 1, 2 lub 3.)")

def set_difficulty(difficulty, enemies):
    if difficulty == 1:
        for enemy in enemies:
            enemy.health -= 10
            enemy.attack -= 2
    elif difficulty == 3:
        for enemy in enemies:
            enemy.health += 10
            enemy.attack += 2

def after_battle(player, enemy, language):
    if enemy.is_alive():
        if language == "pl":
            print(f"{enemy.name} pokonał {player.name}!\n")
        else:
            print(f"{enemy.name} has defeated {player.name}!\n")
    else:
        experience_gain = random.randint(5, 10)
        player.gain_experience(experience_gain)
        if language == "pl":
            print(f"{player.name} pokonał {enemy.name} i zdobył {experience_gain} punktów doświadczenia!\n")
        else:
            print(f"{player.name} has defeated {enemy.name} and gained {experience_gain} experience points!\n")

def battle(player, enemy, language):
    while player.is_alive() and enemy.is_alive():
        clear_console()
        if language == "pl":
            print(f"{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}\n")
        else:
            print(f"{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}\n")
        input("Press Enter to attack... (Wciśnij Enter, aby zaatakować...)")

        player_roll = roll_dice(1, 20)
        enemy_roll = roll_dice(1, 20)

        if language == "pl":
            print(f"{player.name} atakuje {enemy.name}!")
            print(f"{player.name} wyrzuca: {player_roll}")
            print(f"{enemy.name} wyrzuca: {enemy_roll}\n")
        else:
            print(f"{player.name} attacks {enemy.name}!")
            print(f"{player.name} rolls: {player_roll}")
            print(f"{enemy.name} rolls: {enemy_roll}\n")

        if player_roll >= enemy.armor_class:
            player_damage = player.calculate_damage()
            enemy.take_damage(player_damage)
            if language == "pl":
                print(f"{player.name} trafia {enemy.name} i zadaje {player_damage} obrażeń!")
            else:
                print(f"{player.name} hits {enemy.name} and deals {player_damage} damage!")
        else:
            if language == "pl":
                print(f"{player.name} nie trafia {enemy.name}!")
            else:
                print(f"{player.name} misses {enemy.name}!")

        input("\nPress Enter to continue... (Wciśnij Enter, aby kontynuować...)")

        if enemy.is_alive():
            if enemy_roll >= player.armor_class:
                enemy_damage = enemy.calculate_damage()
                player.take_damage(enemy_damage)
                if language == "pl":
                    print(f"{enemy.name} trafia {player.name} i zadaje {enemy_damage} obrażeń!")
                else:
                    print(f"{enemy.name} hits {player.name} and deals {enemy_damage} damage!")
            else:
                if language == "pl":
                    print(f"{enemy.name} nie trafia {player.name}!")
                else:
                    print(f"{enemy.name} misses {player.name}!")
        else:
            after_battle(player, enemy, language)
            return

        input("\nPress Enter to continue... (Wciśnij Enter, aby kontynuować...)")
        clear_console()

def main():
    language = input("Choose language (en/pl): ")
    name = input("Enter your character's name: ")
    character_class = input("Choose character class (Wojownik/Warrior, Mag/Mage, Łucznik/Archer, Łotrzyk/Rogue): ")
    player = Player(name, character_class)

    if language == "pl":
        print(f"Witaj, {player.name} - {player.character_class}!")
        print("Przygotuj się na epicką przygodę!\n")
    else:
        print(f"Welcome, {player.name} the {player.character_class}!")
        print("Get ready for an epic adventure!\n")

    difficulty = choose_difficulty()

    maps = {
        1: [Potwór("Goblin 1", 30, 14, 8), Potwór("Goblin 2", 28, 13, 7), Potwór("Goblin 3", 25, 12, 6), Potwór("Goblin 4", 27, 13, 7)],
        2: [Potwór("Orc 1", 40, 16, 9), Potwór("Orc 2", 38, 15, 8), Potwór("Orc 3", 35, 14, 7), Potwór("Orc 4", 37, 15, 8)],
        3: [Potwór("Szkielet 1", 35, 14, 8), Potwór("Szkielet 2", 32, 13, 7), Potwór("Szkielet 3", 30, 12, 6), Potwór("Szkielet 4", 33, 13, 7)],
        4: [Boss("Smok", 150, 20, 12)]
    }

    set_difficulty(difficulty, maps[1])
    set_difficulty(difficulty, maps[2])
    set_difficulty(difficulty, maps[3])
    set_difficulty(difficulty, maps[4])

    current_map = 1

    while current_map <= 4 and player.is_alive():
        clear_console()
        if language == "pl":
            print(f"Mapa {current_map}")
        else:
            print(f"Map {current_map}")
        enemies = maps[current_map]
        for enemy in enemies:
            battle(player, enemy, language)
            if not player.is_alive():
                break

        if player.is_alive():
            choice = input("Do you want to rest (R) or continue (C)? (Wybierz O - Odpoczynek / K - Kontynuacja): ")
            if choice.lower() == 'o':
                if difficulty == 1:
                    player.health = player.max_health
                elif difficulty == 2:
                    player.health += int((player.max_health - player.health) * 0.75)
                elif difficulty == 3:
                    player.health += int((player.max_health - player.health) * 0.5)
                if language == "pl":
                    print(f"{player.name} odpoczął i odnowił zdrowie!")
                else:
                    print(f"{player.name} rested and restored health!")

        input("Press Enter to continue... (Wciśnij Enter, aby kontynuować...)")
        current_map += 1

    clear_console()

    if player.is_alive():
        if language == "pl":
            print("Gratulacje! Wygrałeś grę!")
        else:
            print("Congratulations! You won the game!")
    else:
        if language == "pl":
            print("Niestety, przegrałeś grę. Może następnym razem pójdzie Ci lepiej.")
        else:
            print("Unfortunately, you lost the game. Maybe next time you'll do better.")

if __name__ == "__main__":
    main()
