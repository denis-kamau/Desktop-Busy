"""
ui.py
Defines the main application window for DesktopBusy.
"""

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from src.simulator import MouseSimulator

class DesktopBusyApp(QMainWindow):
    """
    Main window for the DesktopBusy application.
    Provides UI to start/stop mouse simulation and display status.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Busy")
        self.setWindowIcon(QIcon("icon.png")) 
        self.setFixedSize(750, 350)
        self.simulator = MouseSimulator()
        self.is_running = False
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface with enhanced visual styling and a status dot.
        """
        self.setStyleSheet("""
            QMainWindow {
                background-color: #23272f;
                color: #f5f6fa;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 18px;
            }
            QLabel {
                color: #f5f6fa;
                font-size: 21px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border-radius: 8px;
                padding: 10px 24px;
                font-size: 18px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
        """)

        title_label = QLabel("\U0001F5A5  Desktop Busy", self)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #009688; margin-bottom: 10px;")
        title_label.setAlignment(Qt.AlignCenter)

        # Status layout with dot and label
        status_layout = QVBoxLayout()
        status_dot = QLabel(self)
        status_dot.setFixedSize(16, 16)
        status_dot.setPixmap(self._status_pixmap(QColor("#fd2a2a")))  # Red for stopped
        self.status_dot = status_dot
        self.status_label = QLabel("Status: Stopped", self)
        self.status_label.setStyleSheet("font-weight: bold; margin-bottom: 10px;")
        self.status_label.setAlignment(Qt.AlignCenter)
        status_row = QHBoxLayout()
        status_row.addStretch()
        status_row.addWidget(self.status_dot)
        status_row.addSpacing(8)
        status_row.addWidget(self.status_label)
        status_row.addStretch()
        status_layout.addLayout(status_row)

        self.toggle_button = QPushButton("Start", self)
        self.toggle_button.setMinimumWidth(120)
        self.toggle_button.clicked.connect(self.toggle_simulation)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addSpacing(10)
        layout.addLayout(status_layout)
        layout.addSpacing(10)
        layout.addWidget(self.toggle_button, alignment=Qt.AlignCenter)
        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _status_pixmap(self, color):
        """
        Create a colored dot pixmap for status indication.
        :param color: QColor for the dot.
        :return: QPixmap with a colored dot.
        """
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 16, 16)
        painter.end()
        return pixmap

    def toggle_simulation(self):
        if self.is_running:
            self.simulator.stop()
            self.status_label.setText("Status: Stopped")
            self.status_dot.setPixmap(self._status_pixmap(QColor('#fd2a2a')))
            self.toggle_button.setText("Start")
            self.is_running = False
        else:
            self.simulator.start()
            self.status_label.setText("Status: Running")
            self.status_dot.setPixmap(self._status_pixmap(QColor('#22c55e')))
            self.toggle_button.setText("Stop")
            self.is_running = True
