"""
simulator.py
Handles mouse simulation for DesktopBusy.
"""

import threading
import time
import pyautogui

class MouseSimulator:
    """
    Simulates mouse movement at regular intervals to prevent system idle.
    """
    def __init__(self, interval=30):
        """
        Initialize the simulator.
        :param interval: Time in seconds between mouse movements.
        """
        self.interval = interval
        self._running = False
        self._thread = None

    def start(self):
        """
        Start the mouse simulation in a background thread.
        """
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run, daemon=True)
            self._thread.start()

    def stop(self):
        """
        Stop the mouse simulation.
        """
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)
            self._thread = None

    def _run(self):
        """
        Internal method to move the mouse slightly at intervals.
        """
        while self._running:
            x, y = pyautogui.position()
            pyautogui.moveTo(x+1, y)
            print(f"Moving mouse to ({x+1}, {y})")
            time.sleep(0.2)
            pyautogui.moveTo(x, y)
            print(f"Moving mouse back to ({x}, {y})")
            time.sleep(self.interval)
