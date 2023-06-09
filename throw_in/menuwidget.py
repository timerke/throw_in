import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class MenuWidget(QWidget):

    exit_signal: pyqtSignal = pyqtSignal()
    start_signal: pyqtSignal = pyqtSignal()

    def __init__(self, dir_media: str, version: str) -> None:
        super().__init__()
        self._dir_media: str = dir_media
        self._version: str = version
        self._init_ui()

    def _init_ui(self) -> None:
        loadUi(os.path.join(self._dir_media, "menu.ui"), self)
        self.button_exit.clicked.connect(lambda: self.exit_signal.emit())
        self.button_start.clicked.connect(lambda: self.start_signal.emit())
        self.label_version.setText(f"v{self._version}")
