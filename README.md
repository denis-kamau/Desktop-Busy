# Desktop Busy

## Description
Desktop Busy is a Windows desktop application that mimics user behaviour by simulating mouse movement and scrolling. Its primary purpose is to keep your PC active by preventing the system from going idle.

## Features
- Standalone Windows application
- Simple, modern user interface
- Shows running/stopped status with a colored dot
- Start/stop simulation with a single click
- Simulates random mouse movements and scrolls
- Prevents system from entering idle mode
- Minimal impact on system performance
- Compatible with Windows 10 and later

## Requirements
- Python 3.x
- Windows 10 or later
- All dependencies in `requirements.txt` (install with pip)

## Installation
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage
To run the app:
```powershell
python main.py
```

- Click **Start** to begin simulating activity.
- Click **Stop** to end simulation.
- The status and colored dot indicate if the app is running.

## Building a Standalone .exe
You can package Desktop Busy as a standalone Windows executable using PyInstaller:

1. Ensure all dependencies are installed:
   ```powershell
   pip install -r requirements.txt
   ```
2. Build the executable:
   ```powershell
   pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
   ```
   - If `pyinstaller` is not recognized, try:
     ```powershell
     python -m PyInstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
     ```
3. The `.exe` will be in the `dist` folder. Double-click to run.

## Notes
- The app has been tested on Windows 10 and 11.
- If Teams still goes idle, try running the app as administrator or adjust the simulation interval in the code.
- For best results, keep the app running in the background.
