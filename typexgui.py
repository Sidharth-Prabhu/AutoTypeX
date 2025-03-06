import tkinter as tk
from tkinter import messagebox, Menu
import pyautogui
import random
import time
import keyboard
import threading
import webbrowser
import subprocess
import requests  # Added for GitHub API calls
from packaging import version  # Added for version comparison

class AutoTypeXGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoTypeX")
        self.root.attributes('-topmost', True)
        self.root.geometry("400x350")
        self.is_typing = False
        self.current_version = "1.1"  # Define current version
        try:
            # Replace with your GitHub repository details
            repo_owner = "Sidharth-Prabhu"  # Replace with your GitHub username
            repo_name = "AutoTypeX"      # Replace with your repository name
            api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
            
            # Fetch latest release from GitHub
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            latest_release = response.json()
            latest_version = latest_release["tag_name"].lstrip('v')  # Remove 'v' prefix if present
            
            # Compare versions
            if version.parse(latest_version) > version.parse(self.current_version):
                update_msg = (f"A new version ({latest_version}) is available!\n"
                            f"Current version: {self.current_version}\n"
                            f"Visit the GitHub releases page to download the update?")
                if messagebox.askyesno("Update Available", update_msg):
                    release_url = latest_release["html_url"]
                    webbrowser.open(release_url)
            else:
                messagebox.showinfo("No Updates", f"You are using the latest version ({self.current_version})")
                
        except requests.RequestException as e:
            messagebox.showerror("Update Check Failed", f"Failed to check for updates: {str(e)}")
        except Exception as e:
            messagebox.showerror("Update Check Error", f"An unexpected error occurred: {str(e)}")


        # Menu Bar
        self.menu_bar = Menu(root)
        root.config(menu=self.menu_bar)

        # Help Menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="How to use?", command=self.show_help)
        self.help_menu.add_command(label="Enable Copying in Skillrack", command=self.enable_copying_in_skillrack)
        self.help_menu.add_command(label="Download Firefox", command=self.download_firefox)
        self.help_menu.add_command(label="Check for Updates", command=self.check_for_updates)  # New command
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Instructions label
        self.label = tk.Label(root, text="Paste text below. Ctrl+Q to emergency stop.")
        self.label.pack(pady=5)

        # Text area (initially editable)
        self.text_area = tk.Text(root, height=10, width=50, state="normal")
        self.text_area.pack(pady=5)
        self.text_area.bind("<Button-1>", self.enable_text_area)

        # Buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Start button
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_typing)
        self.start_button.grid(row=0, column=0, padx=5)

        # Stop button
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_typing, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)

        # Status label
        self.status_label = tk.Label(root, text="Status: Idle")
        self.status_label.pack(pady=5)

    def check_for_updates(self):
        try:
            # Replace with your GitHub repository details
            repo_owner = "Sidharth-Prabhu"  # Replace with your GitHub username
            repo_name = "AutoTypeX"      # Replace with your repository name
            api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
            
            # Fetch latest release from GitHub
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            latest_release = response.json()
            latest_version = latest_release["tag_name"].lstrip('v')  # Remove 'v' prefix if present
            
            # Compare versions
            if version.parse(latest_version) > version.parse(self.current_version):
                update_msg = (f"A new version ({latest_version}) is available!\n"
                            f"Current version: {self.current_version}\n"
                            f"Visit the GitHub releases page to download the update?")
                if messagebox.askyesno("Update Available", update_msg):
                    release_url = latest_release["html_url"]
                    webbrowser.open(release_url)
            else:
                messagebox.showinfo("No Updates", f"You are using the latest version ({self.current_version})")
                
        except requests.RequestException as e:
            messagebox.showerror("Update Check Failed", f"Failed to check for updates: {str(e)}")
        except Exception as e:
            messagebox.showerror("Update Check Error", f"An unexpected error occurred: {str(e)}")

    def show_help(self):
        messagebox.showinfo("How to use?", "1. Paste your text in the text box.\n2. Click Start to begin typing.\n3. Ctrl+Q to emergency stop.\n4. Click Stop to halt typing manually.")

    def download_firefox(self):
        firefox_url = "https://www.mozilla.org/en-US/firefox/new/"
        webbrowser.open(firefox_url)
        messagebox.showinfo("Download Firefox", "The latest version of Firefox is being downloaded from the official site.")

    def show_about(self):
        messagebox.showinfo("About AutoTypeX", f"AutoTypeX v{self.current_version}\nA simple auto-typing tool with typo simulation for SkillRack.")

    def enable_copying_in_skillrack(self):
        messagebox.showinfo("Enable Copying", "1.Download FireFox from the web or help menu of the program\n2.Search for 'about:config' in the search and go to the page.\n3.Search for 'dom.event.clipboardevents.enabled' and turn the value to False.\nNow you should be able to copy from SkillRack.")

    def simulate_typing_with_typos(self, text, typing_speed=0.1, typo_rate=0.05):
        for char in text:
            if not self.is_typing or keyboard.is_pressed('ctrl+q'):
                self.is_typing = False
                return False

            if random.random() < typo_rate:
                wrong_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                pyautogui.typewrite(wrong_char, interval=typing_speed)
                time.sleep(random.uniform(0.05, 0.2))
                pyautogui.press('backspace')
                time.sleep(random.uniform(0.05, 0.15))
                pyautogui.typewrite(char, interval=typing_speed)
            else:
                pyautogui.typewrite(char, interval=typing_speed)

            time.sleep(random.uniform(typing_speed - 0.02, typing_speed + 0.02))
        return True

    def typing_thread(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("AutoTypeX", "Text area is empty!")
            self.reset_ui()
            return

        self.text_area.config(state="disabled")
        self.status_label.config(text="Status: Giving 5s to focus cursor...")
        self.root.update()
        time.sleep(5)

        self.status_label.config(text="Status: Typing... (Ctrl+Q to stop)")
        self.root.update()

        completed = self.simulate_typing_with_typos(text, typing_speed=0.02, typo_rate=0.1)

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

    def reset_ui(self):
        self.is_typing = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def enable_text_area(self, event):
        if self.text_area["state"] == "disabled" and not self.is_typing:
            self.text_area.config(state="normal")
            self.status_label.config(text="Status: Idle (Editing Enabled)")

def main():
    root = tk.Tk()
    app = AutoTypeXGUI(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        pyautogui.FAILSAFE = True
        main()
    except Exception as e:
        messagebox.showerror("AutoTypeX Error", f"An error occurred: {e}")