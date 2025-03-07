#!/bin/bash

# Set environment and script names
VENV_DIR="venv"
REQUIREMENTS="requirements.txt"
PYTHON_SCRIPT="typexgui.py"

# Check if venv exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Check if requirements.txt exists and install dependencies
if [ -f "$REQUIREMENTS" ]; then
    echo "Installing dependencies..."
    pip install -r "$REQUIREMENTS"
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Run the Python script
python "$PYTHON_SCRIPT"

# Deactivate and remove virtual environment after execution
echo "Cleaning up..."
deactivate
rm -rf "$VENV_DIR"

# Exit the script
exit 0
