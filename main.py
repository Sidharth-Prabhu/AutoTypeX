import pyautogui
import random
import time
from tkinter import messagebox

def simulate_typing_with_typos(text, typing_speed=0.1, typo_rate=0.05):
    for char in text:
        if random.random() < typo_rate:
            wrong_char = random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            pyautogui.typewrite(wrong_char, interval=typing_speed)
            time.sleep(random.uniform(0.05, 0.2))
            pyautogui.press('backspace') 
            time.sleep(random.uniform(0.05, 0.15))
            pyautogui.typewrite(char, interval=typing_speed)
        else:
            pyautogui.typewrite(char, interval=typing_speed)

        time.sleep(random.uniform(typing_speed - 0.02, typing_speed + 0.02))

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Main function
if __name__ == "__main__":
    file_path = 'content.txt'
    text_to_type = read_file(file_path)
    print("You have 5 seconds to focus the cursor on the target application...")
    time.sleep(6)
    simulate_typing_with_typos(text_to_type, typing_speed=0.02, typo_rate=0.1)
    messagebox.showinfo("AutoTypeX", "Typing Completed!")
