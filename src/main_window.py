import os
from pathlib import Path
from platform import system

from appdirs import user_data_dir
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.data_dir = Path(user_data_dir("minecraft-location-saver", "C_ffeeStain"))

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(300, 150)
        self.setWindowTitle("Main Menu - Minecraft Location Saver")
        self.center()

        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            os.mkdir(self.data_dir / "locations")
            with open(self.data_dir / "locations" / "Example.xml", "w") as f:
                f.write(
                    '<?xml version="1.0" encoding="UTF-8"?>\n<locations>\n<!-- This is an example location. -->\n<location name="Example_Coords" x="0" y="0" z="0" />\n</locations>'
                )

        system_name = system()
        if system_name == "Windows":
            self.minecraft_dir = os.path.join(os.environ["APPDATA"], ".minecraft")
        elif system_name == "Linux":
            self.minecraft_dir = os.path.join(os.environ["HOME"], ".minecraft")
        elif system_name == "Darwin":
            self.minecraft_dir = os.path.join(
                os.environ["HOME"], "Library", "Application Support", "minecraft"
            )
            QMessageBox.warning(
                self,
                "Warning",
                "This program has not been tested on Mac.\n"
                "Please report any bugs you find.",
            )
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "This program has not been tested on this Operating System.\n"
                "Please report any bugs you find.",
            )
        if not os.path.exists(self.minecraft_dir):
            if (
                QMessageBox.warning(
                    self,
                    "Warning",
                    "Minecraft does not appear to be installed on this computer.\n"
                    "Are you sure you want to continue?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No,
                )
                == QMessageBox.No
            ):
                self.close()

        self.title_label = QLabel("Minecraft Location Saver", self)
        self.title_label.setFont(QFont("Arial", 18))
        self.title_label.adjustSize()
        self.title_label.move(
            (self.width() / 2) - (self.title_label.width() / 2),
            10,
        )

        self.create_new_button = QPushButton("Create New", self)
        self.create_new_button.setFont(QFont("Arial", 12))
        self.create_new_button.adjustSize()
        self.create_new_button.setFixedWidth(200)
        self.create_new_button.move(
            (self.width() / 2) - (self.create_new_button.width() / 2),
            self.title_label.y() + self.title_label.height() + 20,
        )
        self.create_new_button.clicked.connect(self.create_new_button_clicked)

        self.load_button = QPushButton("Load", self)
        self.load_button.setFont(QFont("Arial", 12))
        self.load_button.adjustSize()
        self.load_button.setFixedWidth(200)
        self.load_button.move(
            (self.width() / 2) - (self.load_button.width() / 2),
            self.create_new_button.y() + self.create_new_button.height() + 20,
        )
        self.load_button.clicked.connect(self.load_button_clicked)

    def create_new_button_clicked(self):
        ...

    def load_button_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", str(self.data_dir / "locations"), "XML Files (*.xml)"
        )
        if file_name:
            pass

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication([])
    window = main_window()
    window.show()
    app.exec_()
