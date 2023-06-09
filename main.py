import sys
from PyQt5.QtWidgets import QApplication
from throw_in import MainWindow


def run() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    run()
