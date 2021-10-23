import os
from pathlib import Path

from appdirs import user_data_dir
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QWidget,
    QMessageBox,
    QPushButton,
)


class editor_window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
