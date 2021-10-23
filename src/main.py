from PyQt5.QtWidgets import QApplication
from main_window import main_window


def main():
    app = QApplication([])
    win = main_window()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()
