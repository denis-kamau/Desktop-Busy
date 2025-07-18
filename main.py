"""
main.py
Entry point for the DesktopBusy application.
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.ui import DesktopBusyApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopBusyApp()
    window.show()
    sys.exit(app.exec_())
