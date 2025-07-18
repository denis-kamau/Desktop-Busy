"""
simulator.py
Handles mouse simulation for DesktopBusy.
"""

import threading
import time
import pyautogui
import random

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
        Internal method to move the mouse slightly and scroll at random intervals.
        """
        while self._running:
            movement_range = [i for i in range(-20, 21) if i != 0]
            
            x, y = pyautogui.position()
            dx = random.choice(movement_range)
            dy = random.choice(movement_range)
            
            pyautogui.moveTo(x + dx, y + dy)
            print(f"Moving mouse to ({x + dx}, {y + dy})")
            time.sleep(0.5)
            pyautogui.moveTo(x, y)
            print(f"Moving mouse back to ({x}, {y})")
            scroll_amount = random.choice([-2, -1, 1, 2])
            pyautogui.scroll(scroll_amount)
            print(f"Scrolling {'up' if scroll_amount > 0 else 'down'} by {abs(scroll_amount)}")
            interval = random.randint(45, 75)
            print(f"Waiting for {interval} seconds before next action.")
            time.sleep(interval)
