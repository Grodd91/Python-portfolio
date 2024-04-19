import os
import random

def ins_error(minimum_operation_number, maximum_operation_number, instruction):
    while True:
        try:
            instruction = int(instruction)
            if instruction < minimum_operation_number or instruction > maximum_operation_number:
                print("Invalid instruction, please enter a number within the specified range.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a number.")
        instruction = input("Your action: ")
    return instruction

def main():
    day = 0
    cotb = 500
    food = 10
    water = 5
    medkit = 2
    resources = 5
    hunger = 3000
    thirst = 150
    hp = 100
    instruction = 6
    note = ""
    
    print("Nuclear Bunker Simulator")
    print("Remake")
    input("Press Enter, to continue...")
    os.system("cls")
    print("Game started...")

    while instruction != 7:
        if hp <= 0 or cotb <= 0:
            break
        else:
            os.system("cls")

            if hunger > 0:
                hunger -= 100
            if thirst > 0:
                thirst -= 50
            if hunger == 0:
                hp -= 50
                hunger = 0
            if thirst <= 0:
                hp -= 50
                thirst = 0

            day += 1
            cotb -= 20
            event = 0
            if instruction == 1:
                ex = random.randint(1, 10)
                if ex == 1:
                    note = "I have found an abandoned car. I found a first aid kit in the trunk!"
                    medkit += 1
                    water += 1
                elif ex == 2:
                    note = "I have visited local shop, i found some food."
                    food += random.randint(1, 5)
                    water += random.randint(1, 4)
                elif ex == 3:
                    note = "I met wild dogs, fortunately the noise scared them. I'm so tired That's Enough for today."
                    thirst -= 10
                    hp -= 10
                    hunger -= 20
                elif ex == 4:
                    note = "I have visited local shop, i found some resources need to keep my shelter on."
                    resources += random.randint(1, 3)
                elif ex == 5:
                    note = "I have found abandoned military resources! WoW!"
                    resources += random.randint(1, 3)
                    food += random.randint(1, 5)
                    water += random.randint(1, 4)
                    medkit += 1
                elif ex == 6:
                    note = "I have found abandoned ambulance."
                    resources += random.randint(1, 3)
                    food += random.randint(1, 2)
                    water += random.randint(1, 3)
                    medkit += 1
                    if hp != 100 or local_hp > 0:
                        local_hp = 100 - hp
                        hp += local_hp
                elif ex == 7:
                    note = "I met wild dogs, unfortunately the noise didn't scare them. They attacked me!"
                    thirst -= 20
                    hp -= 50
                    hunger -= 30
                elif ex == 8:
                    note = "I met raiders! They attacked me!"
                    thirst -= 20
                    hp -= 60
                    hunger -= 30
                elif ex == 9:
                    note = "Building collapsed on me"
                    thirst -= 50
                    hp -= 80
                    hunger -= 50
                elif ex == 10:
                    note = "I tripped and hurt myself"
                    thirst -= 10
                    hp -= 10
                    hunger -= 200
            elif instruction == 2:
                local_bunker = 0
                if resources > 0:
                    if cotb < 450:
                        rr_event = random.randint(1, 3)
                        cotb += 100
                        resources -= 1
                        if rr_event == 1:
                            note = "Work, work, work!"
                        elif rr_event == 2:
                            note = "My shelter looks like new one!"
                        elif rr_event == 3:
                            note = "Home, sweet home!"
                    else:
                        note = "Why should I repair my shelter? Everything is fine!"
                else:
                    note = "I have no resources unnecessary for repairs!"
            elif instruction == 3:
                local_hp = 0
                if medkit > 0:
                    if hp < 80:
                        rr_event = random.randint(1, 3)
                        hp += 40
                        medkit -= 1
                        if rr_event == 1:
                            note = "I feel much better!"
                        elif rr_event == 2:
                            note = "My wound doesn't look good, but I'm hopeful!"
                        elif rr_event == 3:
                            note = "It hurts less"
                    else:
                        note = "So much better!"
                else:
                    note = "I have no medkits!"
            elif instruction == 4:
                if water > 0:
                    if thirst < 80:
                        rr_event = random.randint(1, 3)
                        thirst += 150
                        water -= 1
                        if rr_event == 1:
                            note = "I feel much better!"
                        elif rr_event == 2:
                            note = "It's better than water from the nearest river!"
                        elif rr_event == 3:
                            note = "Finally water!"
                    else:
                        note = "I'm fine!"
                else:
                    note = "I have no water!"
            elif instruction == 5:
                local_hunger = 0
                if food > 0:
                    if hunger < 2500:
                        rr_event = random.randint(1, 3)
                        hunger += 500
                        food -= 1
                        if rr_event == 1:
                            note = "I feel much better!"
                        elif rr_event == 2:
                            note = "This food is only 10 years old! It's tasty!"
                        elif rr_event == 3:
                            note = "I like this ham!"
                    else:
                        note = "I'm not hungry!"
                else:
                    note = "I have no food!"
            elif instruction == 6:
                stay_e = random.randint(1, 5)
                if stay_e == 1:
                    note = "It was quiet here, but I'm safe here."
                elif stay_e == 2:
                    note = "Raiders attacked my shelter!"
                    cotb -= 200
                elif stay_e == 3:
                    note = "I'm ready to go!"
                elif stay_e == 4:
                    note = "I have played chess - with myself..."
                elif stay_e == 5:
                    note = "I'm wondering, why the world ended"

            print("     Personal termianl (r) 1989     ")
            print("      ____________     ")
            print("Day:", day)
            print("__Bunker status:__")
            print("Bunker condition:", cotb)
            print("__Bunker resources:__")
            print("Gear:", resources)
            print("Medkits:", medkit)
            print("Water:", water)
            print("Food:", food)
            print("__Player status:__")
            print("Health:", hp)
            print("Hunger:", hunger)
            print("Thirst:", thirst)
            print("--------------------------------------------------------------------")
            if day == 1:
                note = "This is my first day!"
            print("Note:", note)
            print("Instructions:")
            print("1 - Expedition")
            print("2 - Repair bunker")
            print("3 - Use med kit")
            print("4 - Drink water")
            print("5 - Eat food")
            print("6 - Stay in shelter")
            print("7 - Exit")
            print("____________________________________________________________________")
            instruction = input("Your action: ")
            instruction = ins_error(1, 7, instruction)

    print("Game Over!")
    if hp <= 0:
        print("You died!")
    elif cotb <= 0:
        print("Your bunker has been destroyed!")
    print("You have survived", day, "days!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
