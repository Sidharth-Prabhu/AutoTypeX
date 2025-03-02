# AutoTypeX - Auto-Typing tool for SkillRack.

AutoTypeX is a Python-based script that simulates human-like typing from a text file. It introduces **random typos** and **backspace corrections** to mimic natural typing behavior. The script is useful for automation, testing, or creating realistic typing simulations.

## Features
- Reads text from a `.txt` file and types it automatically.
- Introduces **random typos** and corrects them using backspace.
- Simulates **human-like typing speed** with slight variations.
- Uses `pyautogui` to send keystrokes to any focused application.

## Installation

### 1. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Required Dependencies
```bash
pip install pyautogui
```

## Usage

### 1. Prepare a Text File
Create a text file (e.g., `content.txt`) and write the content you want AutoTypeX to type.

### 2. Run the Script
Ensure your cursor is focused on the target text field (e.g., a document, browser, or text editor), then run:
```bash
python autotypex.py
```

### 3. Script Behavior
- The script waits **5 seconds** before typing (so you can switch to the target application).
- It types the content with **random typos and corrections**.
- It includes **slight speed variations** to appear more natural.

## Notes
- Ensure `pyautogui` is installed before running the script.
- Modify `typing_speed` and `typo_rate` to adjust typing behavior.
- To stop the script while it's running, **move the mouse to a corner of the screen** (a safety feature of `pyautogui`).

## License
This project is open-source and available under the GPL License.

---
Happy Typing! 🚀

