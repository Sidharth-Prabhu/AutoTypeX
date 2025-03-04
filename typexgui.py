import tkinter as tk
from tkinter import messagebox
import pyautogui
import random
import time
import keyboard
import threading


class AutoTypeXGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoTypeX")
        self.root.attributes('-topmost', True)  # Always on top
        self.root.geometry("400x350")
        self.is_typing = False

        # Instructions label
        self.label = tk.Label(
            root, text="Paste text below. Ctrl+Q to emergency stop.")
        self.label.pack(pady=5)

        # Text area (initially editable)
        self.text_area = tk.Text(root, height=10, width=50, state="normal")
        self.text_area.pack(pady=5)
        # Enable on click
        self.text_area.bind("<Button-1>", self.enable_text_area)

        # Buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Start button
        self.start_button = tk.Button(
            self.button_frame, text="Start", command=self.start_typing)
        self.start_button.grid(row=0, column=0, padx=5)

        # Stop button
        self.stop_button = tk.Button(
            self.button_frame, text="Stop", command=self.stop_typing, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)

        # Status label
        self.status_label = tk.Label(root, text="Status: Idle")
        self.status_label.pack(pady=5)

    def simulate_typing_with_typos(self, text, typing_speed=0.1, typo_rate=0.05):
        """
        Simulates typing with typos and corrections.
        """
        for char in text:
            if not self.is_typing or keyboard.is_pressed('ctrl+q'):
                self.is_typing = False
                return False

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

            time.sleep(random.uniform(
                typing_speed - 0.02, typing_speed + 0.02))
        return True

    def typing_thread(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("AutoTypeX", "Text area is empty!")
            self.reset_ui()
            return

        # Disable text area during typing
        self.text_area.config(state="disabled")
        self.status_label.config(text="Status: Giving 5s to focus cursor...")
        self.root.update()
        time.sleep(5)

        self.status_label.config(text="Status: Typing... (Ctrl+Q to stop)")
        self.root.update()

        completed = self.simulate_typing_with_typos(
            text,
            typing_speed=0.02,
            typo_rate=0.1
        )

        if completed:
            messagebox.showinfo("AutoTypeX", "Typing Completed!")
            self.status_label.config(text="Status: Idle")
        else:
            messagebox.showinfo("AutoTypeX", "Typing Stopped!")
            self.status_label.config(text="Status: Stopped")

        self.reset_ui()

    def start_typing(self):
        if not self.is_typing:
            self.is_typing = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            threading.Thread(target=self.typing_thread, daemon=True).start()

    def stop_typing(self):
        if self.is_typing:
            self.is_typing = False
            self.status_label.config(text="Status: Stopping...")
            # Text area remains disabled until clicked

    def reset_ui(self):
        self.is_typing = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        # Do not enable text_area here; wait for user click

    def enable_text_area(self, event):
        """Enable the text area for editing when clicked."""
        if self.text_area["state"] == "disabled" and not self.is_typing:
            self.text_area.config(state="normal")
            self.status_label.config(text="Status: Idle (Editing Enabled)")


def main():
    root = tk.Tk()
    app = AutoTypeXGUI(root)
    root.mainloop()


if __name__ == "__main__":
    try:
        pyautogui.FAILSAFE = True  # Enable PyAutoGUI failsafe
        main()
    except Exception as e:
        messagebox.showerror("AutoTypeX Error", f"An error occurred: {e}")
