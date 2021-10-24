import os
from pathlib import Path

from appdirs import user_data_dir
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QWidget,
    QMessageBox,
    QPushButton,
    QListWidget,
    QLineEdit,
)
from PyQt5.QtCore import QTimer


class editor_window(QWidget):
    def __init__(
        self,
        parent=None,
        main_window=None,
        pos: "list[int]" = [50, 50],
        size: "list[int]" = [375, 300],
    ):
        super().__init__(parent)

        self.main_window = main_window
        if main_window is None:
            QMessageBox.warning(self, "Error", "Main window not found.")
            self.close()

        self.setGeometry(pos[0], pos[1], size[0], size[1])
        self.setFixedSize(size[0], size[1])
        self.setWindowTitle("Editor - Minecraft Location Saver")

        self.all_locations = {}

        self.title = QLabel("Minecraft Location Saver", self)
        self.title.setFont(QFont("Arial", 20))
        self.title.adjustSize()
        self.title.move((self.width() / 2) - (self.title.width() / 2), 10)

        self.locations_list = QListWidget(self)
        self.locations_list.setFont(QFont("Arial", 12))
        self.locations_list.setFixedSize(100, 175)
        self.locations_list.move(15, 75)

        self.locations_label = QLabel("Locations", self)
        self.locations_label.setFont(QFont("Arial", 12))
        self.locations_label.adjustSize()
        self.locations_label.move(
            (self.locations_list.x() + self.locations_list.width() / 2)
            - (self.locations_label.width() / 2),
            self.locations_list.y() - self.locations_label.height() - 5,
        )

        self.save_button = QPushButton("Save", self)
        self.save_button.setFont(QFont("Arial", 12))
        self.save_button.adjustSize()
        self.save_button.move(
            (self.locations_list.x() + self.locations_list.width() / 2)
            - (self.save_button.width() / 2),
            self.locations_list.y() + self.locations_list.height() + 10,
        )
        self.save_button.clicked.connect(self.save_file)

        self.new_location_name = QLabel("Name:", self)
        self.new_location_name.setFont(QFont("Arial", 12))
        self.new_location_name.adjustSize()
        self.new_location_name.move(
            self.locations_list.x() + self.locations_list.width() + 10,
            self.locations_list.y() + 10,
        )

        self.new_location_name_input = QLineEdit(self)
        self.new_location_name_input.setFont(QFont("Arial", 12))
        self.new_location_name_input.setFixedSize(
            self.width() / 2 - 15, self.save_button.height()
        )
        self.new_location_name_input.move(
            self.new_location_name.x() + self.new_location_name.width() + 10,
            self.new_location_name.y() - 2,
        )

        self.new_location_coords = QLabel("Coordinates:", self)
        self.new_location_coords.setFont(QFont("Arial", 12))
        self.new_location_coords.adjustSize()
        self.new_location_coords.move(
            self.new_location_name.x(),
            self.new_location_name.y() + self.new_location_name_input.height() + 10,
        )

        self.new_location_x = QLineEdit(self)
        self.new_location_x.setFont(QFont("Arial", 12))
        self.new_location_x.setFixedSize(
            35,
            self.new_location_name_input.height(),
        )
        self.new_location_x.move(
            self.new_location_coords.x() + self.new_location_coords.width() + 10,
            self.new_location_coords.y() - 2,
        )
        self.new_location_x.setValidator(QIntValidator())
        self.new_location_x.setPlaceholderText("X")

        self.new_location_y = QLineEdit(self)
        self.new_location_y.setFont(QFont("Arial", 12))
        self.new_location_y.setFixedSize(
            35,
            self.new_location_name_input.height(),
        )
        self.new_location_y.move(
            self.new_location_x.x() + self.new_location_x.width() + 10,
            self.new_location_x.y(),
        )
        self.new_location_y.setValidator(QIntValidator())
        self.new_location_y.setPlaceholderText("Y")

        self.new_location_z = QLineEdit(self)
        self.new_location_z.setFont(QFont("Arial", 12))
        self.new_location_z.setFixedSize(
            35,
            self.new_location_name_input.height(),
        )
        self.new_location_z.move(
            self.new_location_y.x() + self.new_location_y.width() + 10,
            self.new_location_x.y(),
        )
        self.new_location_z.setValidator(QIntValidator())
        self.new_location_z.setPlaceholderText("Z")

        self.create_button = QPushButton("Create", self)
        self.create_button.setFont(QFont("Arial", 12))
        self.create_button.adjustSize()
        self.create_button.move(
            245 - (self.create_button.width() / 2) - 50,
            self.locations_list.height() / 2 + self.new_location_coords.y() + 5,
        )
        self.create_button.clicked.connect(self.create_location)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setFont(QFont("Arial", 12))
        self.delete_button.adjustSize()
        self.delete_button.move(
            245 - (self.delete_button.width() / 2) + 50,
            self.locations_list.height() / 2 + self.new_location_coords.y() + 5,
        )
        self.delete_button.clicked.connect(self.delete_location)

        self.clear_text_button = QPushButton("Clear All Input", self)
        self.clear_text_button.setFont(QFont("Arial", 12))
        self.clear_text_button.adjustSize()
        self.clear_text_button.move(
            245 - (self.clear_text_button.width() / 2),
            160,
        )
        self.clear_text_button.clicked.connect(self.clear_text)

        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 12))
        self.back_button.adjustSize()
        self.back_button.move(
            245 - (self.back_button.width() / 2),
            self.height() - self.back_button.height() - 10,
        )
        self.back_button.clicked.connect(self.back)

    def save_file(self):
        pass

    def back(self):
        if (
            QMessageBox.question(
                self,
                "Return to Main Menu",
                "Are you sure you want to return to the main menu?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            == QMessageBox.Yes
        ):
            self.main_window.show()
            self.close()

    def create_location(self):
        if self.new_location_name_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Please enter a name for the location.",
            )
        elif (
            self.new_location_x.text() == ""
            or self.new_location_y.text() == ""
            or self.new_location_z.text() == ""
        ):
            QMessageBox.warning(
                self,
                "Error",
                "Please enter all three coordinates for the location.",
            )
        elif self.new_location_name in self.locations_list.selectedItems():
            QMessageBox.warning(
                self,
                "Error",
                "A location with that name already exists.",
            )
        else:
            self.all_locations[self.new_location_name_input.text()] = [
                int(self.new_location_x.text()),
                int(self.new_location_y.text()),
                int(self.new_location_z.text()),
            ]
            self.locations_list.addItem(self.new_location_name_input.text())
            self.new_location_name_input.clear()
            self.new_location_x.clear()
            self.new_location_y.clear()
            self.new_location_z.clear()

    def delete_location(self):
        if self.locations_list.currentItem():
            del self.all_locations[self.locations_list.currentItem().text()]
            self.locations_list.takeItem(self.locations_list.currentRow())

    def clear_text(self):
        self.new_location_name_input.clear()
        self.new_location_x.clear()
        self.new_location_y.clear()
        self.new_location_z.clear()
