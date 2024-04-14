import pyautogui
import time
import keyboard

def main():
    try:
        print("The program has started spamming. Press the Escape (Esc) key to exit.")

        time.sleep(10)

        file_path = r"D:\\spam.txt"
        with open(file_path, 'r') as f:
            lines = f.readlines()

            while True:
                for line in lines:
                    pyautogui.typewrite(line.strip())
                    pyautogui.press("enter")
                    time.sleep(1.5)

                    if keyboard.is_pressed('esc'):
                        print("Escape key pressed. Exiting the program.")
                        return  # Exiting the main function and the program when the Escape key is pressed

    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred while spamming:", e)
    finally:
        try:
            f.close()
        except NameError:
            pass

if __name__ == "__main__":
    main()
